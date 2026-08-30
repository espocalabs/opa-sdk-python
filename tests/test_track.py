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
