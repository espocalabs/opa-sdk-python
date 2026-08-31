from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_track_identify_body import PostTrackIdentifyBody
from ...models.post_track_identify_response_200 import PostTrackIdentifyResponse200
from ...models.post_track_identify_response_401 import PostTrackIdentifyResponse401
from ...models.post_track_identify_response_403 import PostTrackIdentifyResponse403
from ...models.post_track_identify_response_409 import PostTrackIdentifyResponse409
from ...models.post_track_identify_response_422 import PostTrackIdentifyResponse422
from ...models.post_track_identify_response_429 import PostTrackIdentifyResponse429
from ...types import Response


def _get_kwargs(
    *,
    body: PostTrackIdentifyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/track/identify",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostTrackIdentifyResponse200
    | PostTrackIdentifyResponse401
    | PostTrackIdentifyResponse403
    | PostTrackIdentifyResponse409
    | PostTrackIdentifyResponse422
    | PostTrackIdentifyResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PostTrackIdentifyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostTrackIdentifyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostTrackIdentifyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = PostTrackIdentifyResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = PostTrackIdentifyResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostTrackIdentifyResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostTrackIdentifyResponse200
    | PostTrackIdentifyResponse401
    | PostTrackIdentifyResponse403
    | PostTrackIdentifyResponse409
    | PostTrackIdentifyResponse422
    | PostTrackIdentifyResponse429
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
    body: PostTrackIdentifyBody,
) -> Response[
    PostTrackIdentifyResponse200
    | PostTrackIdentifyResponse401
    | PostTrackIdentifyResponse403
    | PostTrackIdentifyResponse409
    | PostTrackIdentifyResponse422
    | PostTrackIdentifyResponse429
]:
    """Identify a customer

     Binds the browser's anonymous visitor id to your stable external customer id without recording a
    lead. Accepts either a secret `x-api-key` with `conversions:write` or a public, origin-bound `x-opa-
    site-key` for browser SDK calls.

    Args:
        body (PostTrackIdentifyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTrackIdentifyResponse200 | PostTrackIdentifyResponse401 | PostTrackIdentifyResponse403 | PostTrackIdentifyResponse409 | PostTrackIdentifyResponse422 | PostTrackIdentifyResponse429]
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
    body: PostTrackIdentifyBody,
) -> (
    PostTrackIdentifyResponse200
    | PostTrackIdentifyResponse401
    | PostTrackIdentifyResponse403
    | PostTrackIdentifyResponse409
    | PostTrackIdentifyResponse422
    | PostTrackIdentifyResponse429
    | None
):
    """Identify a customer

     Binds the browser's anonymous visitor id to your stable external customer id without recording a
    lead. Accepts either a secret `x-api-key` with `conversions:write` or a public, origin-bound `x-opa-
    site-key` for browser SDK calls.

    Args:
        body (PostTrackIdentifyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTrackIdentifyResponse200 | PostTrackIdentifyResponse401 | PostTrackIdentifyResponse403 | PostTrackIdentifyResponse409 | PostTrackIdentifyResponse422 | PostTrackIdentifyResponse429
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostTrackIdentifyBody,
) -> Response[
    PostTrackIdentifyResponse200
    | PostTrackIdentifyResponse401
    | PostTrackIdentifyResponse403
    | PostTrackIdentifyResponse409
    | PostTrackIdentifyResponse422
    | PostTrackIdentifyResponse429
]:
    """Identify a customer

     Binds the browser's anonymous visitor id to your stable external customer id without recording a
    lead. Accepts either a secret `x-api-key` with `conversions:write` or a public, origin-bound `x-opa-
    site-key` for browser SDK calls.

    Args:
        body (PostTrackIdentifyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTrackIdentifyResponse200 | PostTrackIdentifyResponse401 | PostTrackIdentifyResponse403 | PostTrackIdentifyResponse409 | PostTrackIdentifyResponse422 | PostTrackIdentifyResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostTrackIdentifyBody,
) -> (
    PostTrackIdentifyResponse200
    | PostTrackIdentifyResponse401
    | PostTrackIdentifyResponse403
    | PostTrackIdentifyResponse409
    | PostTrackIdentifyResponse422
    | PostTrackIdentifyResponse429
    | None
):
    """Identify a customer

     Binds the browser's anonymous visitor id to your stable external customer id without recording a
    lead. Accepts either a secret `x-api-key` with `conversions:write` or a public, origin-bound `x-opa-
    site-key` for browser SDK calls.

    Args:
        body (PostTrackIdentifyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTrackIdentifyResponse200 | PostTrackIdentifyResponse401 | PostTrackIdentifyResponse403 | PostTrackIdentifyResponse409 | PostTrackIdentifyResponse422 | PostTrackIdentifyResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
