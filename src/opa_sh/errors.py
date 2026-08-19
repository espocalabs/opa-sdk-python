"""Exception hierarchy for the Opa SDK.

Every failed API call raises a subclass of :class:`OpaError` — this is a
Python-idiomatic ``raise``-based SDK (mirrors Stripe, OpenAI, Anthropic,
boto3), not a ``Result``/``Either`` pattern. Catch :class:`OpaError` to
handle any SDK failure, or a specific subclass to handle one case:

.. code-block:: python

    from opa_sh import OpaClient
    from opa_sh.errors import NotFoundError, RateLimitError, OpaError

    opa = OpaClient(api_key="...")

    try:
        link = opa.links.get("lnk_xxx")
    except NotFoundError:
        ...
    except RateLimitError as e:
        print("retry after", e.retry_after)
    except OpaError as e:
        print(e.code, e.status, e.message)
"""

from typing import Any, Optional

import httpx

__all__ = [
    "OpaError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "ValidationError",
    "RateLimitError",
    "ServerError",
    "NetworkError",
    "raise_for_response",
]


class OpaError(Exception):
    """Base class for all Opa SDK errors.

    Attributes:
        message: Human-readable error message from the API (or generated
            locally for transport-level failures).
        code: Machine-readable error code from the API's ``error.code``
            field (e.g. ``"not_found"``, ``"validation_error"``). Left as a
            plain ``str`` (not an enum) so a code the SDK doesn't know
            about yet still surfaces instead of raising on parse.
        status: The HTTP status code, when the error came from a response.
            ``0`` for transport-level failures (see :class:`NetworkError`).
        details: The raw ``error`` object from the API response body, when
            available. May include a ``"issues"`` list of
            ``{"path": ..., "message": ...}`` field-level validation errors
            for :class:`ValidationError`.
    """

    def __init__(
        self,
        message: str,
        *,
        code: str,
        status: int,
        details: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.status = status
        self.details = details

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message={self.message!r}, code={self.code!r}, status={self.status!r})"


class AuthenticationError(OpaError):
    """401 — the API key is missing or invalid."""


class PermissionDeniedError(OpaError):
    """403 — the credential is valid but lacks permission for this operation.

    Also raised when the organization's plan doesn't include the requested
    capability (e.g. the API access add-on).
    """


class NotFoundError(OpaError):
    """404 — the requested resource doesn't exist."""


class ConflictError(OpaError):
    """409 — the request conflicts with existing state.

    Examples: a custom ``key`` that's already taken on the domain, or
    ``no_domain_available`` when no domain was specified and the team has
    none configured.
    """


class ValidationError(OpaError):
    """400/422 — the request body or query parameters failed validation.

    ``details`` typically includes an ``"issues"`` list of
    ``{"path": str, "message": str}`` entries pinpointing the offending
    field(s).
    """


class RateLimitError(OpaError):
    """429 — the API key has exceeded its rate limit.

    Attributes:
        retry_after: Seconds to wait before retrying, parsed from the
            ``Retry-After`` response header, when present.
    """

    def __init__(
        self,
        message: str,
        *,
        code: str,
        status: int,
        details: Optional[dict[str, Any]] = None,
        retry_after: Optional[int] = None,
    ) -> None:
        super().__init__(message, code=code, status=status, details=details)
        self.retry_after = retry_after


class ServerError(OpaError):
    """5xx — the Opa API had an internal error. Safe to retry."""


class NetworkError(OpaError):
    """Connection failure, timeout, or DNS error — never reached the API."""

    def __init__(self, message: str, *, cause: Optional[BaseException] = None) -> None:
        super().__init__(message, code="network_error", status=0)
        self.__cause__ = cause


_STATUS_TO_ERROR: "dict[int, type[OpaError]]" = {
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    400: ValidationError,
    422: ValidationError,
    429: RateLimitError,
}


def _parse_retry_after(response: httpx.Response) -> Optional[int]:
    header = response.headers.get("retry-after")
    if not header:
        return None
    try:
        return int(float(header))
    except ValueError:
        return None


def _error_body(response: httpx.Response) -> "tuple[str, str, Optional[dict[str, Any]]]":
    """Extracts ``(code, message, details)`` from an ``{"error": {...}}`` body.

    Falls back to a generic message when the body isn't JSON or doesn't
    match the documented error envelope — a non-JSON 502 from a proxy in
    front of the API is the main case this guards against.
    """
    try:
        payload: Any = response.json()
    except ValueError:
        return "unknown_error", f"Request failed with status {response.status_code}.", None

    error = payload.get("error") if isinstance(payload, dict) else None
    if not isinstance(error, dict):
        return "unknown_error", f"Request failed with status {response.status_code}.", None

    code = error.get("code") or "unknown_error"
    message = error.get("message") or f"Request failed with status {response.status_code}."
    return code, message, error


def raise_for_response(response: httpx.Response) -> None:
    """Raises the appropriate :class:`OpaError` subclass for a non-2xx response.

    No-op when ``response`` is a success (2xx). Call this immediately after
    every request, before parsing the body as a success payload.
    """
    if response.is_success:
        return

    code, message, details = _error_body(response)
    status = response.status_code

    if status == 429:
        raise RateLimitError(
            message,
            code=code,
            status=status,
            details=details,
            retry_after=_parse_retry_after(response),
        )

    error_cls = _STATUS_TO_ERROR.get(status)
    if error_cls is None:
        error_cls = ServerError if status >= 500 else OpaError
    raise error_cls(message, code=code, status=status, details=details)
