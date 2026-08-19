from typing import Optional

import httpx
import pytest

from opa_sh.errors import (
    AuthenticationError,
    ConflictError,
    NotFoundError,
    OpaError,
    PermissionDeniedError,
    RateLimitError,
    ServerError,
    ValidationError,
    raise_for_response,
)


def _response(status: int, error_body: dict, headers: Optional[dict] = None) -> httpx.Response:
    return httpx.Response(
        status,
        json={"error": error_body},
        headers=headers or {},
        request=httpx.Request("GET", "https://api.opa.sh/v1/links"),
    )


def test_success_response_is_noop() -> None:
    response = httpx.Response(200, json={"data": {}}, request=httpx.Request("GET", "https://x"))
    raise_for_response(response)  # should not raise


@pytest.mark.parametrize(
    "status,error_cls",
    [
        (401, AuthenticationError),
        (403, PermissionDeniedError),
        (404, NotFoundError),
        (409, ConflictError),
        (422, ValidationError),
        (500, ServerError),
        (502, ServerError),
        (503, ServerError),
    ],
)
def test_status_maps_to_error_class(status: int, error_cls: type) -> None:
    response = _response(status, {"code": "some_code", "message": "boom"})
    with pytest.raises(error_cls) as exc_info:
        raise_for_response(response)
    err = exc_info.value
    assert isinstance(err, OpaError)
    assert err.status == status
    assert err.code == "some_code"
    assert err.message == "boom"


def test_unrecognized_4xx_status_falls_back_to_base_error() -> None:
    response = _response(418, {"code": "teapot", "message": "I'm a teapot"})
    with pytest.raises(OpaError) as exc_info:
        raise_for_response(response)
    assert type(exc_info.value) is OpaError
    assert exc_info.value.status == 418


def test_400_is_not_validation_error() -> None:
    """The `/api/v1` `CODE_TO_STATUS` map has no path that ever produces a
    400 — `validation_error` is fixed at 422. A stray 400 (e.g. from a
    proxy in front of the API) should not be misreported as a
    :class:`ValidationError`; it falls through to the generic
    :class:`OpaError`, same as any other unmapped 4xx."""
    response = _response(400, {"code": "some_code", "message": "boom"})
    with pytest.raises(OpaError) as exc_info:
        raise_for_response(response)
    assert type(exc_info.value) is OpaError
    assert not isinstance(exc_info.value, ValidationError)
    assert exc_info.value.status == 400


def test_rate_limit_error_parses_retry_after_seconds() -> None:
    response = _response(
        429,
        {"code": "rate_limited", "message": "slow down"},
        headers={"retry-after": "42"},
    )
    with pytest.raises(RateLimitError) as exc_info:
        raise_for_response(response)
    assert exc_info.value.retry_after == 42


def test_rate_limit_error_without_retry_after_header() -> None:
    response = _response(429, {"code": "rate_limited", "message": "slow down"})
    with pytest.raises(RateLimitError) as exc_info:
        raise_for_response(response)
    assert exc_info.value.retry_after is None


def test_validation_error_carries_issues_in_details() -> None:
    response = _response(
        422,
        {
            "code": "validation_error",
            "message": "The request did not pass validation.",
            "issues": [{"path": "destinationUrl", "message": "Required"}],
        },
    )
    with pytest.raises(ValidationError) as exc_info:
        raise_for_response(response)
    assert exc_info.value.details is not None
    assert exc_info.value.details["issues"] == [{"path": "destinationUrl", "message": "Required"}]


def test_non_json_error_body_falls_back_gracefully() -> None:
    response = httpx.Response(
        502,
        content=b"<html>Bad Gateway</html>",
        request=httpx.Request("GET", "https://api.opa.sh/v1/links"),
    )
    with pytest.raises(ServerError) as exc_info:
        raise_for_response(response)
    assert exc_info.value.code == "unknown_error"
    assert exc_info.value.status == 502


def test_opa_error_repr() -> None:
    err = OpaError("boom", code="not_found", status=404)
    assert "not_found" in repr(err)
    assert "404" in repr(err)
