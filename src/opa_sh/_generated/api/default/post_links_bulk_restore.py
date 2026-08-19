from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_links_bulk_restore_body import PostLinksBulkRestoreBody
from ...models.post_links_bulk_restore_response_200 import PostLinksBulkRestoreResponse200
from ...models.post_links_bulk_restore_response_401 import PostLinksBulkRestoreResponse401
from ...models.post_links_bulk_restore_response_403 import PostLinksBulkRestoreResponse403
from ...models.post_links_bulk_restore_response_422 import PostLinksBulkRestoreResponse422
from ...models.post_links_bulk_restore_response_429 import PostLinksBulkRestoreResponse429
from ...types import Response


def _get_kwargs(
    *,
    body: PostLinksBulkRestoreBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/links/bulk-restore",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostLinksBulkRestoreResponse200
    | PostLinksBulkRestoreResponse401
    | PostLinksBulkRestoreResponse403
    | PostLinksBulkRestoreResponse422
    | PostLinksBulkRestoreResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PostLinksBulkRestoreResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostLinksBulkRestoreResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostLinksBulkRestoreResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostLinksBulkRestoreResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostLinksBulkRestoreResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostLinksBulkRestoreResponse200
    | PostLinksBulkRestoreResponse401
    | PostLinksBulkRestoreResponse403
    | PostLinksBulkRestoreResponse422
    | PostLinksBulkRestoreResponse429
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostLinksBulkRestoreBody,
) -> Response[
    PostLinksBulkRestoreResponse200
    | PostLinksBulkRestoreResponse401
    | PostLinksBulkRestoreResponse403
    | PostLinksBulkRestoreResponse422
    | PostLinksBulkRestoreResponse429
]:
    """Bulk restore archived links

     Un-archives every link in `linkIds` in one call, the counterpart to `POST /links/bulk-archive`. Same
    all-or-nothing membership check: any id outside the organization fails the whole request with
    `not_found`. Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkRestoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksBulkRestoreResponse200 | PostLinksBulkRestoreResponse401 | PostLinksBulkRestoreResponse403 | PostLinksBulkRestoreResponse422 | PostLinksBulkRestoreResponse429]
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
    client: AuthenticatedClient | Client,
    body: PostLinksBulkRestoreBody,
) -> (
    PostLinksBulkRestoreResponse200
    | PostLinksBulkRestoreResponse401
    | PostLinksBulkRestoreResponse403
    | PostLinksBulkRestoreResponse422
    | PostLinksBulkRestoreResponse429
    | None
):
    """Bulk restore archived links

     Un-archives every link in `linkIds` in one call, the counterpart to `POST /links/bulk-archive`. Same
    all-or-nothing membership check: any id outside the organization fails the whole request with
    `not_found`. Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkRestoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksBulkRestoreResponse200 | PostLinksBulkRestoreResponse401 | PostLinksBulkRestoreResponse403 | PostLinksBulkRestoreResponse422 | PostLinksBulkRestoreResponse429
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostLinksBulkRestoreBody,
) -> Response[
    PostLinksBulkRestoreResponse200
    | PostLinksBulkRestoreResponse401
    | PostLinksBulkRestoreResponse403
    | PostLinksBulkRestoreResponse422
    | PostLinksBulkRestoreResponse429
]:
    """Bulk restore archived links

     Un-archives every link in `linkIds` in one call, the counterpart to `POST /links/bulk-archive`. Same
    all-or-nothing membership check: any id outside the organization fails the whole request with
    `not_found`. Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkRestoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksBulkRestoreResponse200 | PostLinksBulkRestoreResponse401 | PostLinksBulkRestoreResponse403 | PostLinksBulkRestoreResponse422 | PostLinksBulkRestoreResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostLinksBulkRestoreBody,
) -> (
    PostLinksBulkRestoreResponse200
    | PostLinksBulkRestoreResponse401
    | PostLinksBulkRestoreResponse403
    | PostLinksBulkRestoreResponse422
    | PostLinksBulkRestoreResponse429
    | None
):
    """Bulk restore archived links

     Un-archives every link in `linkIds` in one call, the counterpart to `POST /links/bulk-archive`. Same
    all-or-nothing membership check: any id outside the organization fails the whole request with
    `not_found`. Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkRestoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksBulkRestoreResponse200 | PostLinksBulkRestoreResponse401 | PostLinksBulkRestoreResponse403 | PostLinksBulkRestoreResponse422 | PostLinksBulkRestoreResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
