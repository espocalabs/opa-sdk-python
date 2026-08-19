import httpx
import pytest
import respx

from opa_sh import AsyncOpaClient, OpaClient

DOMAINS_JSON = [
    {
        "id": "dom_1",
        "domain": "opa.sh",
        "type": "APP_DOMAIN",
        "verified": True,
        "primary": False,
        "allowedHosts": ["opa.sh"],
    },
    {
        "id": "dom_2",
        "domain": "go.example.com",
        "type": "USER_DOMAIN",
        "verified": True,
        "primary": True,
        "allowedHosts": ["go.example.com", "www.go.example.com"],
    },
]


def test_list_domains(mock_api: respx.MockRouter) -> None:
    mock_api.get("/domains").mock(return_value=httpx.Response(200, json={"data": DOMAINS_JSON}))
    with OpaClient(api_key="test_key") as opa:
        domains = opa.domains.list()
    assert len(domains) == 2
    assert domains[0].domain == "opa.sh"
    assert domains[1].primary is True
    assert domains[1].allowed_hosts == ["go.example.com", "www.go.example.com"]


def test_list_domains_empty(mock_api: respx.MockRouter) -> None:
    mock_api.get("/domains").mock(return_value=httpx.Response(200, json={"data": []}))
    with OpaClient(api_key="test_key") as opa:
        domains = opa.domains.list()
    assert domains == []


@pytest.mark.asyncio
async def test_list_domains_async(mock_api: respx.MockRouter) -> None:
    mock_api.get("/domains").mock(return_value=httpx.Response(200, json={"data": DOMAINS_JSON}))
    async with AsyncOpaClient(api_key="test_key") as opa:
        domains = await opa.domains.list()
    assert len(domains) == 2
