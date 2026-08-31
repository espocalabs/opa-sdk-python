from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_track_event_body_type_0 import PostTrackEventBodyType0
from ...models.post_track_event_body_type_1 import PostTrackEventBodyType1
from ...models.post_track_event_response_200 import PostTrackEventResponse200
from ...models.post_track_event_response_401 import PostTrackEventResponse401
from ...models.post_track_event_response_403 import PostTrackEventResponse403
from ...models.post_track_event_response_409 import PostTrackEventResponse409
from ...models.post_track_event_response_422 import PostTrackEventResponse422
from ...models.post_track_event_response_429 import PostTrackEventResponse429
from ...types import Response


def _get_kwargs(
    *,
    body: PostTrackEventBodyType0 | PostTrackEventBodyType1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/track/event",
    }

    if isinstance(body, PostTrackEventBodyType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostTrackEventResponse200
    | PostTrackEventResponse401
    | PostTrackEventResponse403
    | PostTrackEventResponse409
    | PostTrackEventResponse422
    | PostTrackEventResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PostTrackEventResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostTrackEventResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostTrackEventResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = PostTrackEventResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = PostTrackEventResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostTrackEventResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostTrackEventResponse200
    | PostTrackEventResponse401
    | PostTrackEventResponse403
    | PostTrackEventResponse409
    | PostTrackEventResponse422
    | PostTrackEventResponse429
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostTrackEventBodyType0 | PostTrackEventBodyType1,
) -> Response[
    PostTrackEventResponse200
    | PostTrackEventResponse401
    | PostTrackEventResponse403
    | PostTrackEventResponse409
    | PostTrackEventResponse422
    | PostTrackEventResponse429
]:
    """Track an event

     Records an idempotent generic event for an anonymous or identified customer. Accepts either a secret
    `x-api-key` with `conversions:write` or a public, origin-bound `x-opa-site-key` for browser SDK
    calls.

    Args:
        body (PostTrackEventBodyType0 | PostTrackEventBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTrackEventResponse200 | PostTrackEventResponse401 | PostTrackEventResponse403 | PostTrackEventResponse409 | PostTrackEventResponse422 | PostTrackEventResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostTrackEventBodyType0 | PostTrackEventBodyType1,
) -> (
    PostTrackEventResponse200
    | PostTrackEventResponse401
    | PostTrackEventResponse403
    | PostTrackEventResponse409
    | PostTrackEventResponse422
    | PostTrackEventResponse429
    | None
):
    """Track an event

     Records an idempotent generic event for an anonymous or identified customer. Accepts either a secret
    `x-api-key` with `conversions:write` or a public, origin-bound `x-opa-site-key` for browser SDK
    calls.

    Args:
        body (PostTrackEventBodyType0 | PostTrackEventBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTrackEventResponse200 | PostTrackEventResponse401 | PostTrackEventResponse403 | PostTrackEventResponse409 | PostTrackEventResponse422 | PostTrackEventResponse429
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostTrackEventBodyType0 | PostTrackEventBodyType1,
) -> Response[
    PostTrackEventResponse200
    | PostTrackEventResponse401
    | PostTrackEventResponse403
    | PostTrackEventResponse409
    | PostTrackEventResponse422
    | PostTrackEventResponse429
]:
    """Track an event

     Records an idempotent generic event for an anonymous or identified customer. Accepts either a secret
    `x-api-key` with `conversions:write` or a public, origin-bound `x-opa-site-key` for browser SDK
    calls.

    Args:
        body (PostTrackEventBodyType0 | PostTrackEventBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTrackEventResponse200 | PostTrackEventResponse401 | PostTrackEventResponse403 | PostTrackEventResponse409 | PostTrackEventResponse422 | PostTrackEventResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostTrackEventBodyType0 | PostTrackEventBodyType1,
) -> (
    PostTrackEventResponse200
    | PostTrackEventResponse401
    | PostTrackEventResponse403
    | PostTrackEventResponse409
    | PostTrackEventResponse422
    | PostTrackEventResponse429
    | None
):
    """Track an event

     Records an idempotent generic event for an anonymous or identified customer. Accepts either a secret
    `x-api-key` with `conversions:write` or a public, origin-bound `x-opa-site-key` for browser SDK
    calls.

    Args:
        body (PostTrackEventBodyType0 | PostTrackEventBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTrackEventResponse200 | PostTrackEventResponse401 | PostTrackEventResponse403 | PostTrackEventResponse409 | PostTrackEventResponse422 | PostTrackEventResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
