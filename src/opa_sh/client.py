"""``OpaClient`` / ``AsyncOpaClient`` — the SDK's top-level entry points."""

from types import TracebackType
from typing import Optional

import httpx

from ._internal.version import __version__
from .resources.analytics import AnalyticsResource, AsyncAnalyticsResource
from .resources.domains import AsyncDomainsResource, DomainsResource
from .resources.links import AsyncLinksResource, LinksResource
from .retry import AsyncRetryTransport, RetryTransport

__all__ = ["OpaClient", "AsyncOpaClient", "DEFAULT_BASE_URL"]

DEFAULT_BASE_URL = "https://api.opa.sh/v1"
DEFAULT_TIMEOUT = 30.0
DEFAULT_RETRIES = 3
DEFAULT_RETRY_DELAY = 1.0


def _auth_headers(api_key: Optional[str], bearer_token: Optional[str]) -> dict[str, str]:
    if not api_key and not bearer_token:
        raise ValueError("Either `api_key` or `bearer_token` is required.")
    headers = {"User-Agent": f"opa-sh/{__version__}"}
    if api_key:
        headers["x-api-key"] = api_key
    elif bearer_token:
        headers["Authorization"] = f"Bearer {bearer_token}"
    return headers


class OpaClient:
    """Synchronous SDK client for the Opa link shortener API.

    Requires exactly one of ``api_key`` or ``bearer_token``. Get an API key
    at https://app.opa.sh/settings/api-keys.

    Example:
        >>> from opa_sh import OpaClient
        >>> opa = OpaClient(api_key="opa_live_...")
        >>> link = opa.links.create(destination_url="https://example.com", domain="opa.sh")
        >>> link.short_link

    Use as a context manager to close the underlying connection pool
    automatically::

        with OpaClient(api_key="...") as opa:
            ...
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        bearer_token: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        retries: int = DEFAULT_RETRIES,
        retry_delay: float = DEFAULT_RETRY_DELAY,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        headers = _auth_headers(api_key, bearer_token)

        if http_client is not None:
            self._client = http_client
            self._client.headers.update(headers)
        else:
            transport = RetryTransport(retries=retries, retry_delay=retry_delay)
            self._client = httpx.Client(
                base_url=base_url,
                headers=headers,
                timeout=timeout,
                transport=transport,
            )

        self.links = LinksResource(self._client)
        self.analytics = AnalyticsResource(self._client)
        self.domains = DomainsResource(self._client)

    def close(self) -> None:
        """Closes the underlying HTTP connection pool."""
        self._client.close()

    def __enter__(self) -> "OpaClient":
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        self.close()


class AsyncOpaClient:
    """Async equivalent of :class:`OpaClient`, backed by ``httpx.AsyncClient``.

    Example:
        >>> from opa_sh import AsyncOpaClient
        >>> async with AsyncOpaClient(api_key="opa_live_...") as opa:
        ...     link = await opa.links.create(destination_url="https://example.com")
        ...     print(link.short_link)
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        bearer_token: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        retries: int = DEFAULT_RETRIES,
        retry_delay: float = DEFAULT_RETRY_DELAY,
        http_client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        headers = _auth_headers(api_key, bearer_token)

        if http_client is not None:
            self._client = http_client
            self._client.headers.update(headers)
        else:
            transport = AsyncRetryTransport(retries=retries, retry_delay=retry_delay)
            self._client = httpx.AsyncClient(
                base_url=base_url,
                headers=headers,
                timeout=timeout,
                transport=transport,
            )

        self.links = AsyncLinksResource(self._client)
        self.analytics = AsyncAnalyticsResource(self._client)
        self.domains = AsyncDomainsResource(self._client)

    async def close(self) -> None:
        """Closes the underlying HTTP connection pool."""
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncOpaClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        await self.close()
