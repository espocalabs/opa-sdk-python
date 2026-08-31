from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_links_bulk_archive_body import PostLinksBulkArchiveBody
from ...models.post_links_bulk_archive_response_200 import PostLinksBulkArchiveResponse200
from ...models.post_links_bulk_archive_response_401 import PostLinksBulkArchiveResponse401
from ...models.post_links_bulk_archive_response_403 import PostLinksBulkArchiveResponse403
from ...models.post_links_bulk_archive_response_422 import PostLinksBulkArchiveResponse422
from ...models.post_links_bulk_archive_response_429 import PostLinksBulkArchiveResponse429
from ...types import Response


def _get_kwargs(
    *,
    body: PostLinksBulkArchiveBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/links/bulk/archive",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostLinksBulkArchiveResponse200
    | PostLinksBulkArchiveResponse401
    | PostLinksBulkArchiveResponse403
    | PostLinksBulkArchiveResponse422
    | PostLinksBulkArchiveResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PostLinksBulkArchiveResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostLinksBulkArchiveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostLinksBulkArchiveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostLinksBulkArchiveResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostLinksBulkArchiveResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostLinksBulkArchiveResponse200
    | PostLinksBulkArchiveResponse401
    | PostLinksBulkArchiveResponse403
    | PostLinksBulkArchiveResponse422
    | PostLinksBulkArchiveResponse429
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
    body: PostLinksBulkArchiveBody,
) -> Response[
    PostLinksBulkArchiveResponse200
    | PostLinksBulkArchiveResponse401
    | PostLinksBulkArchiveResponse403
    | PostLinksBulkArchiveResponse422
    | PostLinksBulkArchiveResponse429
]:
    """Bulk archive links

     Archives every link in `linkIds` in one call — same effect as `DELETE /links/{id}`, batched. All-or-
    nothing on membership: if any id does not belong to the organization (or does not exist), the whole
    request fails `not_found` — there is no partial/best-effort success. Reversible with `POST
    /links/bulk/restore`. Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkArchiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksBulkArchiveResponse200 | PostLinksBulkArchiveResponse401 | PostLinksBulkArchiveResponse403 | PostLinksBulkArchiveResponse422 | PostLinksBulkArchiveResponse429]
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
    body: PostLinksBulkArchiveBody,
) -> (
    PostLinksBulkArchiveResponse200
    | PostLinksBulkArchiveResponse401
    | PostLinksBulkArchiveResponse403
    | PostLinksBulkArchiveResponse422
    | PostLinksBulkArchiveResponse429
    | None
):
    """Bulk archive links

     Archives every link in `linkIds` in one call — same effect as `DELETE /links/{id}`, batched. All-or-
    nothing on membership: if any id does not belong to the organization (or does not exist), the whole
    request fails `not_found` — there is no partial/best-effort success. Reversible with `POST
    /links/bulk/restore`. Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkArchiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksBulkArchiveResponse200 | PostLinksBulkArchiveResponse401 | PostLinksBulkArchiveResponse403 | PostLinksBulkArchiveResponse422 | PostLinksBulkArchiveResponse429
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostLinksBulkArchiveBody,
) -> Response[
    PostLinksBulkArchiveResponse200
    | PostLinksBulkArchiveResponse401
    | PostLinksBulkArchiveResponse403
    | PostLinksBulkArchiveResponse422
    | PostLinksBulkArchiveResponse429
]:
    """Bulk archive links

     Archives every link in `linkIds` in one call — same effect as `DELETE /links/{id}`, batched. All-or-
    nothing on membership: if any id does not belong to the organization (or does not exist), the whole
    request fails `not_found` — there is no partial/best-effort success. Reversible with `POST
    /links/bulk/restore`. Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkArchiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksBulkArchiveResponse200 | PostLinksBulkArchiveResponse401 | PostLinksBulkArchiveResponse403 | PostLinksBulkArchiveResponse422 | PostLinksBulkArchiveResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostLinksBulkArchiveBody,
) -> (
    PostLinksBulkArchiveResponse200
    | PostLinksBulkArchiveResponse401
    | PostLinksBulkArchiveResponse403
    | PostLinksBulkArchiveResponse422
    | PostLinksBulkArchiveResponse429
    | None
):
    """Bulk archive links

     Archives every link in `linkIds` in one call — same effect as `DELETE /links/{id}`, batched. All-or-
    nothing on membership: if any id does not belong to the organization (or does not exist), the whole
    request fails `not_found` — there is no partial/best-effort success. Reversible with `POST
    /links/bulk/restore`. Requires the `bulk` plan capability (Start plan or above) — otherwise fails
    `bulk_capability_required`.

    Args:
        body (PostLinksBulkArchiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksBulkArchiveResponse200 | PostLinksBulkArchiveResponse401 | PostLinksBulkArchiveResponse403 | PostLinksBulkArchiveResponse422 | PostLinksBulkArchiveResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
