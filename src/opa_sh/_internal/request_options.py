"""Per-call options accepted by every resource method."""

from dataclasses import dataclass
from typing import Any, Optional

import httpx


@dataclass(frozen=True)
class RequestOptions:
    """Options accepted by every resource method.

    Attributes:
        idempotency_key: A client-generated key that makes a mutating
            request safe to retry. Sent as the ``Idempotency-Key`` header.
            The API deduplicates requests with the same key for 24 hours.
            Generate one per business operation with ``uuid.uuid4()``.
        timeout: Per-request timeout override, in seconds. Falls back to
            the client's default timeout when omitted.
    """

    idempotency_key: Optional[str] = None
    timeout: Optional[float] = None


def request_headers(options: Optional[RequestOptions]) -> dict[str, str]:
    if options and options.idempotency_key:
        return {"Idempotency-Key": options.idempotency_key}
    return {}


def request_timeout(options: Optional[RequestOptions]) -> Any:
    """Returns a per-request timeout override, or httpx's "use the client
    default" sentinel when none was given. Typed ``Any`` because httpx's own
    sentinel type (`httpx._client.UseClientDefault`) is private.
    """
    if options and options.timeout is not None:
        return options.timeout
    return httpx.USE_CLIENT_DEFAULT
