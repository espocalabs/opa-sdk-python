"""Per-call options accepted by every resource method."""

from dataclasses import dataclass
from typing import Any, Optional

import httpx


@dataclass(frozen=True)
class RequestOptions:
    """Options accepted by every resource method.

    Attributes:
        timeout: Per-request timeout override, in seconds. Falls back to
            the client's default timeout when omitted.
    """

    timeout: Optional[float] = None


def request_timeout(options: Optional[RequestOptions]) -> Any:
    """Returns a per-request timeout override, or httpx's "use the client
    default" sentinel when none was given. Typed ``Any`` because httpx's own
    sentinel type (`httpx._client.UseClientDefault`) is private.
    """
    if options and options.timeout is not None:
        return options.timeout
    return httpx.USE_CLIENT_DEFAULT
