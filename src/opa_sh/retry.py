"""httpx transports that retry `5xx`/`429` responses with exponential backoff.

Wraps whatever transport `httpx.Client`/`httpx.AsyncClient` would otherwise
use (its own default `HTTPTransport`/`AsyncHTTPTransport`, or a caller-supplied
one), following the pattern documented in the httpx docs for custom
transports. `Retry-After` (seconds or HTTP-date) is honored when present,
taking priority over the computed backoff. Never retries other 4xx status
codes, so idempotent semantics are preserved for POST.
"""

import asyncio
import random
import time
from email.utils import parsedate_to_datetime
from types import TracebackType
from typing import Optional

import httpx

from .errors import NetworkError

DEFAULT_RETRIES = 3
DEFAULT_RETRY_DELAY = 1.0
DEFAULT_MAX_DELAY = 20.0


def _is_retryable_status(status_code: int) -> bool:
    return status_code == 429 or status_code >= 500


def compute_backoff_seconds(attempt: int, base_delay: float, max_delay: float) -> float:
    """Exponential backoff with +/-20% jitter, capped at `max_delay`."""
    exponential = min(max_delay, base_delay * (2**attempt))
    jitter = exponential * 0.2 * (random.random() * 2 - 1)
    return float(max(0.0, min(max_delay, exponential + jitter)))


def parse_retry_after_seconds(header: Optional[str]) -> Optional[float]:
    """Parses `Retry-After` (seconds or HTTP-date) into a delay in seconds."""
    if not header:
        return None
    try:
        return max(0.0, float(header))
    except ValueError:
        pass
    try:
        target = parsedate_to_datetime(header)
    except (TypeError, ValueError):
        return None
    if target is None:
        return None
    delay = target.timestamp() - time.time()
    return max(0.0, delay)


class RetryTransport(httpx.BaseTransport):
    """Sync retrying transport. Used internally by :class:`opa_sh.OpaClient`."""

    def __init__(
        self,
        transport: Optional[httpx.BaseTransport] = None,
        *,
        retries: int = DEFAULT_RETRIES,
        retry_delay: float = DEFAULT_RETRY_DELAY,
        max_delay: float = DEFAULT_MAX_DELAY,
    ) -> None:
        self._transport = transport or httpx.HTTPTransport()
        self._retries = retries
        self._retry_delay = retry_delay
        self._max_delay = max_delay

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        attempt = 0
        while True:
            try:
                response = self._transport.handle_request(request)
            except httpx.TransportError as exc:
                if attempt >= self._retries:
                    raise NetworkError(str(exc) or exc.__class__.__name__, cause=exc) from exc
                time.sleep(compute_backoff_seconds(attempt, self._retry_delay, self._max_delay))
                attempt += 1
                continue

            if _is_retryable_status(response.status_code) and attempt < self._retries:
                response.close()
                retry_after = parse_retry_after_seconds(response.headers.get("retry-after"))
                delay = (
                    retry_after
                    if retry_after is not None
                    else compute_backoff_seconds(attempt, self._retry_delay, self._max_delay)
                )
                time.sleep(delay)
                attempt += 1
                continue

            return response

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> "RetryTransport":
        self._transport.__enter__()
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]] = None,
        exc: Optional[BaseException] = None,
        tb: Optional[TracebackType] = None,
    ) -> None:
        self._transport.__exit__(exc_type, exc, tb)


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async retrying transport. Used internally by :class:`opa_sh.AsyncOpaClient`."""

    def __init__(
        self,
        transport: Optional[httpx.AsyncBaseTransport] = None,
        *,
        retries: int = DEFAULT_RETRIES,
        retry_delay: float = DEFAULT_RETRY_DELAY,
        max_delay: float = DEFAULT_MAX_DELAY,
    ) -> None:
        self._transport = transport or httpx.AsyncHTTPTransport()
        self._retries = retries
        self._retry_delay = retry_delay
        self._max_delay = max_delay

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        attempt = 0
        while True:
            try:
                response = await self._transport.handle_async_request(request)
            except httpx.TransportError as exc:
                if attempt >= self._retries:
                    raise NetworkError(str(exc) or exc.__class__.__name__, cause=exc) from exc
                await asyncio.sleep(
                    compute_backoff_seconds(attempt, self._retry_delay, self._max_delay)
                )
                attempt += 1
                continue

            if _is_retryable_status(response.status_code) and attempt < self._retries:
                await response.aclose()
                retry_after = parse_retry_after_seconds(response.headers.get("retry-after"))
                delay = (
                    retry_after
                    if retry_after is not None
                    else compute_backoff_seconds(attempt, self._retry_delay, self._max_delay)
                )
                await asyncio.sleep(delay)
                attempt += 1
                continue

            return response

    async def aclose(self) -> None:
        await self._transport.aclose()

    async def __aenter__(self) -> "AsyncRetryTransport":
        await self._transport.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]] = None,
        exc: Optional[BaseException] = None,
        tb: Optional[TracebackType] = None,
    ) -> None:
        await self._transport.__aexit__(exc_type, exc, tb)
