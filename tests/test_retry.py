import httpx
import pytest

from opa_sh.errors import NetworkError
from opa_sh.retry import (
    AsyncRetryTransport,
    RetryTransport,
    compute_backoff_seconds,
    parse_retry_after_seconds,
)


def make_handler(statuses: list[int]):
    calls = {"count": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        status = statuses[min(calls["count"], len(statuses) - 1)]
        calls["count"] += 1
        return httpx.Response(status, json={"data": {}})

    handler.calls = calls  # type: ignore[attr-defined]
    return handler


def test_compute_backoff_seconds_stays_within_bounds() -> None:
    for attempt in range(6):
        delay = compute_backoff_seconds(attempt, base_delay=1.0, max_delay=8.0)
        assert 0.0 <= delay <= 8.0 * 1.2


def test_parse_retry_after_seconds_numeric() -> None:
    assert parse_retry_after_seconds("5") == 5.0


def test_parse_retry_after_seconds_invalid() -> None:
    assert parse_retry_after_seconds("not-a-date") is None


def test_parse_retry_after_seconds_none() -> None:
    assert parse_retry_after_seconds(None) is None


def test_retries_on_5xx_then_succeeds() -> None:
    handler = make_handler([503, 503, 200])
    inner = httpx.MockTransport(handler)
    transport = RetryTransport(inner, retries=3, retry_delay=0.001, max_delay=0.01)

    with httpx.Client(transport=transport, base_url="https://api.opa.sh/v1") as client:
        response = client.get("/links")

    assert response.status_code == 200
    assert handler.calls["count"] == 3  # type: ignore[attr-defined]


def test_retries_on_429_then_succeeds() -> None:
    handler = make_handler([429, 200])
    inner = httpx.MockTransport(handler)
    transport = RetryTransport(inner, retries=3, retry_delay=0.001, max_delay=0.01)

    with httpx.Client(transport=transport, base_url="https://api.opa.sh/v1") as client:
        response = client.get("/links")

    assert response.status_code == 200
    assert handler.calls["count"] == 2  # type: ignore[attr-defined]


def test_gives_up_after_max_retries_and_returns_last_response() -> None:
    handler = make_handler([503, 503, 503, 503, 503])
    inner = httpx.MockTransport(handler)
    transport = RetryTransport(inner, retries=2, retry_delay=0.001, max_delay=0.01)

    with httpx.Client(transport=transport, base_url="https://api.opa.sh/v1") as client:
        response = client.get("/links")

    assert response.status_code == 503
    assert handler.calls["count"] == 3  # 1 initial + 2 retries  # type: ignore[attr-defined]


def test_does_not_retry_other_4xx() -> None:
    handler = make_handler([404, 200])
    inner = httpx.MockTransport(handler)
    transport = RetryTransport(inner, retries=3, retry_delay=0.001, max_delay=0.01)

    with httpx.Client(transport=transport, base_url="https://api.opa.sh/v1") as client:
        response = client.get("/links")

    assert response.status_code == 404
    assert handler.calls["count"] == 1  # type: ignore[attr-defined]


def test_transport_error_raises_network_error_after_exhausting_retries() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection refused", request=request)

    inner = httpx.MockTransport(handler)
    transport = RetryTransport(inner, retries=1, retry_delay=0.001, max_delay=0.01)

    # Nested (not parenthesized-combined) `with` on purpose: parenthesized
    # multi-context managers are Python 3.10+ syntax, and this test suite
    # follows the package's Python 3.9 floor.
    with httpx.Client(transport=transport, base_url="https://api.opa.sh/v1") as client:  # noqa: SIM117
        with pytest.raises(NetworkError):
            client.get("/links")


@pytest.mark.asyncio
async def test_async_retries_on_5xx_then_succeeds() -> None:
    handler = make_handler([503, 200])
    inner = httpx.MockTransport(handler)
    transport = AsyncRetryTransport(inner, retries=3, retry_delay=0.001, max_delay=0.01)

    async with httpx.AsyncClient(transport=transport, base_url="https://api.opa.sh/v1") as client:
        response = await client.get("/links")

    assert response.status_code == 200
    assert handler.calls["count"] == 2  # type: ignore[attr-defined]


@pytest.mark.asyncio
async def test_async_transport_error_raises_network_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection refused", request=request)

    inner = httpx.MockTransport(handler)
    transport = AsyncRetryTransport(inner, retries=1, retry_delay=0.001, max_delay=0.01)

    async with httpx.AsyncClient(transport=transport, base_url="https://api.opa.sh/v1") as client:
        with pytest.raises(NetworkError):
            await client.get("/links")
