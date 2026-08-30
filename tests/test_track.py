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
