from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_links_bulk_tag_body import PostLinksBulkTagBody
from ...models.post_links_bulk_tag_response_200 import PostLinksBulkTagResponse200
from ...models.post_links_bulk_tag_response_401 import PostLinksBulkTagResponse401
from ...models.post_links_bulk_tag_response_403 import PostLinksBulkTagResponse403
from ...models.post_links_bulk_tag_response_422 import PostLinksBulkTagResponse422
from ...models.post_links_bulk_tag_response_429 import PostLinksBulkTagResponse429
from ...types import Response


def _get_kwargs(
    *,
    body: PostLinksBulkTagBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/links/bulk-tag",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostLinksBulkTagResponse200
    | PostLinksBulkTagResponse401
    | PostLinksBulkTagResponse403
    | PostLinksBulkTagResponse422
    | PostLinksBulkTagResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PostLinksBulkTagResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostLinksBulkTagResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostLinksBulkTagResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostLinksBulkTagResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostLinksBulkTagResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostLinksBulkTagResponse200
    | PostLinksBulkTagResponse401
    | PostLinksBulkTagResponse403
    | PostLinksBulkTagResponse422
    | PostLinksBulkTagResponse429
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
    body: PostLinksBulkTagBody,
) -> Response[
    PostLinksBulkTagResponse200
    | PostLinksBulkTagResponse401
    | PostLinksBulkTagResponse403
    | PostLinksBulkTagResponse422
    | PostLinksBulkTagResponse429
]:
    """Bulk add tags to links

     Adds (never replaces) every tag in `tagIds` to every link in `linkIds`. Every id in `tagIds` must
    belong to the organization (`tags_not_found` otherwise). Re-tagging a link that already carries one
    of the tags is a no-op, not an error. Same all-or-nothing membership check on `linkIds` as `POST
    /links/bulk-archive`: any id outside the organization fails the whole request with `not_found`.
    Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkTagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksBulkTagResponse200 | PostLinksBulkTagResponse401 | PostLinksBulkTagResponse403 | PostLinksBulkTagResponse422 | PostLinksBulkTagResponse429]
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
    body: PostLinksBulkTagBody,
) -> (
    PostLinksBulkTagResponse200
    | PostLinksBulkTagResponse401
    | PostLinksBulkTagResponse403
    | PostLinksBulkTagResponse422
    | PostLinksBulkTagResponse429
    | None
):
    """Bulk add tags to links

     Adds (never replaces) every tag in `tagIds` to every link in `linkIds`. Every id in `tagIds` must
    belong to the organization (`tags_not_found` otherwise). Re-tagging a link that already carries one
    of the tags is a no-op, not an error. Same all-or-nothing membership check on `linkIds` as `POST
    /links/bulk-archive`: any id outside the organization fails the whole request with `not_found`.
    Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkTagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksBulkTagResponse200 | PostLinksBulkTagResponse401 | PostLinksBulkTagResponse403 | PostLinksBulkTagResponse422 | PostLinksBulkTagResponse429
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostLinksBulkTagBody,
) -> Response[
    PostLinksBulkTagResponse200
    | PostLinksBulkTagResponse401
    | PostLinksBulkTagResponse403
    | PostLinksBulkTagResponse422
    | PostLinksBulkTagResponse429
]:
    """Bulk add tags to links

     Adds (never replaces) every tag in `tagIds` to every link in `linkIds`. Every id in `tagIds` must
    belong to the organization (`tags_not_found` otherwise). Re-tagging a link that already carries one
    of the tags is a no-op, not an error. Same all-or-nothing membership check on `linkIds` as `POST
    /links/bulk-archive`: any id outside the organization fails the whole request with `not_found`.
    Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkTagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksBulkTagResponse200 | PostLinksBulkTagResponse401 | PostLinksBulkTagResponse403 | PostLinksBulkTagResponse422 | PostLinksBulkTagResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostLinksBulkTagBody,
) -> (
    PostLinksBulkTagResponse200
    | PostLinksBulkTagResponse401
    | PostLinksBulkTagResponse403
    | PostLinksBulkTagResponse422
    | PostLinksBulkTagResponse429
    | None
):
    """Bulk add tags to links

     Adds (never replaces) every tag in `tagIds` to every link in `linkIds`. Every id in `tagIds` must
    belong to the organization (`tags_not_found` otherwise). Re-tagging a link that already carries one
    of the tags is a no-op, not an error. Same all-or-nothing membership check on `linkIds` as `POST
    /links/bulk-archive`: any id outside the organization fails the whole request with `not_found`.
    Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkTagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksBulkTagResponse200 | PostLinksBulkTagResponse401 | PostLinksBulkTagResponse403 | PostLinksBulkTagResponse422 | PostLinksBulkTagResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
