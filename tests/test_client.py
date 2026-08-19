import httpx
import pytest
import respx

from opa_sh import AsyncOpaClient, OpaClient
from opa_sh.client import DEFAULT_BASE_URL


def test_requires_api_key() -> None:
    with pytest.raises(ValueError, match=r"api_key"):
        OpaClient()


def test_requires_api_key_async() -> None:
    with pytest.raises(ValueError, match=r"api_key"):
        AsyncOpaClient()


def test_api_key_sent_as_header(mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/domains").mock(return_value=httpx.Response(200, json={"data": []}))
    with OpaClient(api_key="opa_test") as opa:
        opa.domains.list()
    assert route.calls.last.request.headers["x-api-key"] == "opa_test"
    assert "authorization" not in route.calls.last.request.headers


def test_api_key_constructs_working_client(mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/domains").mock(return_value=httpx.Response(200, json={"data": []}))
    with OpaClient(api_key="opa_test") as opa:
        opa.domains.list()
    assert route.called


def test_user_agent_header(mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/domains").mock(return_value=httpx.Response(200, json={"data": []}))
    with OpaClient(api_key="key") as opa:
        opa.domains.list()
    assert route.calls.last.request.headers["user-agent"].startswith("opa-sh/")


def test_default_base_url() -> None:
    assert DEFAULT_BASE_URL == "https://api.opa.sh/v1"


def test_custom_base_url_used(mock_api: respx.MockRouter) -> None:
    with respx.mock(base_url="https://staging.example.com") as router:
        route = router.get("/domains").mock(return_value=httpx.Response(200, json={"data": []}))
        with OpaClient(api_key="key", base_url="https://staging.example.com") as opa:
            opa.domains.list()
        assert route.called


def test_context_manager_closes_client() -> None:
    with OpaClient(api_key="key") as opa:
        assert not opa._client.is_closed
    assert opa._client.is_closed


def test_close_is_idempotent_safe() -> None:
    opa = OpaClient(api_key="key")
    opa.close()
    assert opa._client.is_closed


def test_custom_http_client_gets_auth_header_merged() -> None:
    custom = httpx.Client(base_url="https://api.opa.sh/v1")
    opa = OpaClient(api_key="key", http_client=custom)
    assert opa._client is custom
    assert custom.headers["x-api-key"] == "key"
    opa.close()


@pytest.mark.asyncio
async def test_async_client_requires_auth() -> None:
    with pytest.raises(ValueError):
        AsyncOpaClient()


@pytest.mark.asyncio
async def test_async_client_api_key_header(mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/domains").mock(return_value=httpx.Response(200, json={"data": []}))
    async with AsyncOpaClient(api_key="opa_test") as opa:
        await opa.domains.list()
    assert route.calls.last.request.headers["x-api-key"] == "opa_test"


@pytest.mark.asyncio
async def test_async_context_manager_closes_client() -> None:
    async with AsyncOpaClient(api_key="key") as opa:
        assert not opa._client.is_closed
    assert opa._client.is_closed
