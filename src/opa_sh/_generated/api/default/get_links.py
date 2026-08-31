from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_links_response_200 import GetLinksResponse200
from ...models.get_links_response_401 import GetLinksResponse401
from ...models.get_links_response_403 import GetLinksResponse403
from ...models.get_links_response_422 import GetLinksResponse422
from ...models.get_links_response_429 import GetLinksResponse429
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 20,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    search: str | Unset = UNSET,
    archived: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    params["before"] = before

    params["search"] = search

    params["archived"] = archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/links",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetLinksResponse200
    | GetLinksResponse401
    | GetLinksResponse403
    | GetLinksResponse422
    | GetLinksResponse429
    | None
):
    if response.status_code == 200:
        response_200 = GetLinksResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetLinksResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetLinksResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetLinksResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetLinksResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetLinksResponse200
    | GetLinksResponse401
    | GetLinksResponse403
    | GetLinksResponse422
    | GetLinksResponse429
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
    limit: int | Unset = 20,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    search: str | Unset = UNSET,
    archived: str | Unset = UNSET,
) -> Response[
    GetLinksResponse200
    | GetLinksResponse401
    | GetLinksResponse403
    | GetLinksResponse422
    | GetLinksResponse429
]:
    """List links

     Paginated list of the organization's links, in the same summary shape the dashboard's links table
    uses. `archived` (default `false`) mirrors the dashboard's tab: non-archived by default, or `true`
    for the archived list. An archived link still resolves — see `POST /links/{id}/restore`.

    Args:
        limit (int | Unset): Items per page. 1-100, default 20. Default: 20.
        after (str | Unset): Cursor. The `id` of the last link on the previous page — returns
            links older than it. Mutually exclusive with `before`.
        before (str | Unset): Cursor. The `id` of the first link on the next page — returns links
            newer than it. Mutually exclusive with `after`.
        search (str | Unset): Case-insensitive substring match against the short link, destination
            URL, folder name, or tag name.
        archived (str | Unset): `false` (default) lists active links; `true` lists archived ones.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLinksResponse200 | GetLinksResponse401 | GetLinksResponse403 | GetLinksResponse422 | GetLinksResponse429]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        before=before,
        search=search,
        archived=archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    search: str | Unset = UNSET,
    archived: str | Unset = UNSET,
) -> (
    GetLinksResponse200
    | GetLinksResponse401
    | GetLinksResponse403
    | GetLinksResponse422
    | GetLinksResponse429
    | None
):
    """List links

     Paginated list of the organization's links, in the same summary shape the dashboard's links table
    uses. `archived` (default `false`) mirrors the dashboard's tab: non-archived by default, or `true`
    for the archived list. An archived link still resolves — see `POST /links/{id}/restore`.

    Args:
        limit (int | Unset): Items per page. 1-100, default 20. Default: 20.
        after (str | Unset): Cursor. The `id` of the last link on the previous page — returns
            links older than it. Mutually exclusive with `before`.
        before (str | Unset): Cursor. The `id` of the first link on the next page — returns links
            newer than it. Mutually exclusive with `after`.
        search (str | Unset): Case-insensitive substring match against the short link, destination
            URL, folder name, or tag name.
        archived (str | Unset): `false` (default) lists active links; `true` lists archived ones.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLinksResponse200 | GetLinksResponse401 | GetLinksResponse403 | GetLinksResponse422 | GetLinksResponse429
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        before=before,
        search=search,
        archived=archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    search: str | Unset = UNSET,
    archived: str | Unset = UNSET,
) -> Response[
    GetLinksResponse200
    | GetLinksResponse401
    | GetLinksResponse403
    | GetLinksResponse422
    | GetLinksResponse429
]:
    """List links

     Paginated list of the organization's links, in the same summary shape the dashboard's links table
    uses. `archived` (default `false`) mirrors the dashboard's tab: non-archived by default, or `true`
    for the archived list. An archived link still resolves — see `POST /links/{id}/restore`.

    Args:
        limit (int | Unset): Items per page. 1-100, default 20. Default: 20.
        after (str | Unset): Cursor. The `id` of the last link on the previous page — returns
            links older than it. Mutually exclusive with `before`.
        before (str | Unset): Cursor. The `id` of the first link on the next page — returns links
            newer than it. Mutually exclusive with `after`.
        search (str | Unset): Case-insensitive substring match against the short link, destination
            URL, folder name, or tag name.
        archived (str | Unset): `false` (default) lists active links; `true` lists archived ones.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLinksResponse200 | GetLinksResponse401 | GetLinksResponse403 | GetLinksResponse422 | GetLinksResponse429]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        before=before,
        search=search,
        archived=archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    search: str | Unset = UNSET,
    archived: str | Unset = UNSET,
) -> (
    GetLinksResponse200
    | GetLinksResponse401
    | GetLinksResponse403
    | GetLinksResponse422
    | GetLinksResponse429
    | None
):
    """List links

     Paginated list of the organization's links, in the same summary shape the dashboard's links table
    uses. `archived` (default `false`) mirrors the dashboard's tab: non-archived by default, or `true`
    for the archived list. An archived link still resolves — see `POST /links/{id}/restore`.

    Args:
        limit (int | Unset): Items per page. 1-100, default 20. Default: 20.
        after (str | Unset): Cursor. The `id` of the last link on the previous page — returns
            links older than it. Mutually exclusive with `before`.
        before (str | Unset): Cursor. The `id` of the first link on the next page — returns links
            newer than it. Mutually exclusive with `after`.
        search (str | Unset): Case-insensitive substring match against the short link, destination
            URL, folder name, or tag name.
        archived (str | Unset): `false` (default) lists active links; `true` lists archived ones.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLinksResponse200 | GetLinksResponse401 | GetLinksResponse403 | GetLinksResponse422 | GetLinksResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            before=before,
            search=search,
            archived=archived,
        )
    ).parsed
