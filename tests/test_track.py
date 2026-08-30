import json

import httpx
import pytest
import respx

from opa_sh import AsyncOpaClient, OpaClient

IDENTIFY_JSON = {
    "customerId": "cus_1",
    "anonymousId": "anon_1",
    "externalId": "user_1",
    "merged": False,
    "futureField": "ignored",
}

EVENT_JSON = {
    "eventId": "evt_1",
    "customerId": "cus_1",
    "deduped": False,
    "futureField": "ignored",
}

CONVERSION_JSON = {
    "event": {
        "id": "cnv_1",
        "eventType": "lead",
        "eventName": "Signup",
        "clickId": "clk_1",
        "customerId": "cus_1",
        "valueCents": None,
        "currency": None,
        "invoiceId": None,
        "paymentProcessor": None,
        "metadata": {"source": "form"},
        "occurredAt": "2026-08-30T12:00:00.000Z",
        "createdAt": "2026-08-30T12:00:00.000Z",
    },
    "customer": {
        "id": "cus_1",
        "externalId": "user_1",
        "email": "person@example.com",
        "name": "Person",
        "avatar": None,
        "createdAt": "2026-08-30T12:00:00.000Z",
    },
    "deduped": False,
    "futureField": "ignored",
}


def test_identify_sync_uses_reserved_wire_contract(mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/track/identify").mock(
        return_value=httpx.Response(200, json={"data": IDENTIFY_JSON})
    )

    with OpaClient(api_key="test_key") as opa:
        result = opa.track.identify(
            anonymous_id="anon_1",
            external_id="user_1",
            traits={"email": "person@example.com", "plan": "pro"},
            click_id="clk_1",
        )

    assert json.loads(route.calls.last.request.content) == {
        "anonymousId": "anon_1",
        "externalId": "user_1",
        "traits": {"email": "person@example.com", "plan": "pro"},
        "clickId": "clk_1",
    }
    assert result.customer_id == "cus_1"
    assert result.anonymous_id == "anon_1"
    assert result.external_id == "user_1"
    assert result.merged is False


@pytest.mark.asyncio
async def test_identify_async_omits_absent_optional_fields(mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/track/identify").mock(
        return_value=httpx.Response(200, json={"data": IDENTIFY_JSON})
    )

    async with AsyncOpaClient(api_key="test_key") as opa:
        result = await opa.track.identify(anonymous_id="anon_1", external_id="user_1")

    assert json.loads(route.calls.last.request.content) == {
        "anonymousId": "anon_1",
        "externalId": "user_1",
    }
    assert result.customer_id == "cus_1"


def test_event_sync_tracks_anonymous_identity_and_omits_none(mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/track/event").mock(
        return_value=httpx.Response(200, json={"data": EVENT_JSON})
    )

    with OpaClient(api_key="test_key") as opa:
        result = opa.track.event(
            event_id="evt_1",
            event_name="checkout_started",
            anonymous_id="anon_1",
        )

    assert json.loads(route.calls.last.request.content) == {
        "eventId": "evt_1",
        "eventName": "checkout_started",
        "anonymousId": "anon_1",
    }
    assert result.event_id == "evt_1"
    assert result.customer_id == "cus_1"
    assert result.deduped is False


@pytest.mark.asyncio
async def test_event_async_is_external_only_and_does_not_reuse_identify(
    mock_api: respx.MockRouter,
) -> None:
    identify_route = mock_api.post("/track/identify").mock(
        return_value=httpx.Response(200, json={"data": IDENTIFY_JSON})
    )
    event_route = mock_api.post("/track/event").mock(
        return_value=httpx.Response(200, json={"data": EVENT_JSON})
    )

    async with AsyncOpaClient(api_key="test_key") as opa:
        await opa.track.identify(anonymous_id="anon_previous", external_id="user_previous")
        result = await opa.track.event(
            event_id="evt_1",
            event_name="purchase_completed",
            external_id="user_1",
            click_id="clk_1",
            properties={"total": 14990},
            occurred_at="2026-08-30T12:00:00.000Z",
        )

    assert identify_route.called
    assert json.loads(event_route.calls.last.request.content) == {
        "eventId": "evt_1",
        "eventName": "purchase_completed",
        "externalId": "user_1",
        "clickId": "clk_1",
        "properties": {"total": 14990},
        "occurredAt": "2026-08-30T12:00:00.000Z",
    }
    assert result.event_id == "evt_1"


def test_lead_sync_uses_legacy_wire_contract(mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/track/lead").mock(
        return_value=httpx.Response(200, json={"data": CONVERSION_JSON})
    )

    with OpaClient(api_key="test_key") as opa:
        result = opa.track.lead(
            click_id="clk_1",
            event_name="Signup",
            customer_external_id="user_1",
            customer_email="person@example.com",
            customer_name="Person",
            customer_avatar="https://example.com/avatar.png",
            metadata={"source": "form"},
        )

    assert json.loads(route.calls.last.request.content) == {
        "clickId": "clk_1",
        "eventName": "Signup",
        "customerExternalId": "user_1",
        "customerEmail": "person@example.com",
        "customerName": "Person",
        "customerAvatar": "https://example.com/avatar.png",
        "metadata": {"source": "form"},
    }
    assert result.event.event_type == "lead"
    assert result.customer.external_id == "user_1"
    assert result.deduped is False


@pytest.mark.asyncio
async def test_lead_async_omits_absent_optional_fields(mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/track/lead").mock(
        return_value=httpx.Response(200, json={"data": CONVERSION_JSON})
    )

    async with AsyncOpaClient(api_key="test_key") as opa:
        result = await opa.track.lead(
            click_id="clk_1",
            event_name="Signup",
            customer_external_id="user_1",
        )

    assert json.loads(route.calls.last.request.content) == {
        "clickId": "clk_1",
        "eventName": "Signup",
        "customerExternalId": "user_1",
    }
    assert result.customer.id == "cus_1"
