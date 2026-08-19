"""``opa.domains`` — the domains available to shorten links under."""

from typing import Optional

import httpx

from .._internal.request_options import RequestOptions, request_timeout
from ..errors import raise_for_response
from ..models import Domain


class DomainsResource:
    """Synchronous ``opa.domains`` resource."""

    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def list(self, *, options: Optional[RequestOptions] = None) -> list[Domain]:
        """Lists every domain the organization can shorten links under —
        verified custom domains plus the shared app domain. Not paginated:
        this list is small by nature."""
        response = self._client.get("/domains", timeout=request_timeout(options))
        raise_for_response(response)
        return [Domain.model_validate(item) for item in response.json()["data"]]


class AsyncDomainsResource:
    """Async equivalent of :class:`DomainsResource`."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client

    async def list(self, *, options: Optional[RequestOptions] = None) -> list[Domain]:
        response = await self._client.get("/domains", timeout=request_timeout(options))
        raise_for_response(response)
        return [Domain.model_validate(item) for item in response.json()["data"]]
