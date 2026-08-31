from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_links_id_response_200 import DeleteLinksIdResponse200
from ...models.delete_links_id_response_401 import DeleteLinksIdResponse401
from ...models.delete_links_id_response_403 import DeleteLinksIdResponse403
from ...models.delete_links_id_response_422 import DeleteLinksIdResponse422
from ...models.delete_links_id_response_429 import DeleteLinksIdResponse429
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/links/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteLinksIdResponse200
    | DeleteLinksIdResponse401
    | DeleteLinksIdResponse403
    | DeleteLinksIdResponse422
    | DeleteLinksIdResponse429
    | None
):
    if response.status_code == 200:
        response_200 = DeleteLinksIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DeleteLinksIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteLinksIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = DeleteLinksIdResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = DeleteLinksIdResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteLinksIdResponse200
    | DeleteLinksIdResponse401
    | DeleteLinksIdResponse403
    | DeleteLinksIdResponse422
    | DeleteLinksIdResponse429
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteLinksIdResponse200
    | DeleteLinksIdResponse401
    | DeleteLinksIdResponse403
    | DeleteLinksIdResponse422
    | DeleteLinksIdResponse429
]:
    """Archive a link

     Archives the link (same as the dashboard's delete action). The row is not physically removed and the
    link keeps resolving normally — archiving only removes it from `GET /links`' default list.
    Reversible with `POST /links/{id}/restore`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteLinksIdResponse200 | DeleteLinksIdResponse401 | DeleteLinksIdResponse403 | DeleteLinksIdResponse422 | DeleteLinksIdResponse429]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteLinksIdResponse200
    | DeleteLinksIdResponse401
    | DeleteLinksIdResponse403
    | DeleteLinksIdResponse422
    | DeleteLinksIdResponse429
    | None
):
    """Archive a link

     Archives the link (same as the dashboard's delete action). The row is not physically removed and the
    link keeps resolving normally — archiving only removes it from `GET /links`' default list.
    Reversible with `POST /links/{id}/restore`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteLinksIdResponse200 | DeleteLinksIdResponse401 | DeleteLinksIdResponse403 | DeleteLinksIdResponse422 | DeleteLinksIdResponse429
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteLinksIdResponse200
    | DeleteLinksIdResponse401
    | DeleteLinksIdResponse403
    | DeleteLinksIdResponse422
    | DeleteLinksIdResponse429
]:
    """Archive a link

     Archives the link (same as the dashboard's delete action). The row is not physically removed and the
    link keeps resolving normally — archiving only removes it from `GET /links`' default list.
    Reversible with `POST /links/{id}/restore`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteLinksIdResponse200 | DeleteLinksIdResponse401 | DeleteLinksIdResponse403 | DeleteLinksIdResponse422 | DeleteLinksIdResponse429]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteLinksIdResponse200
    | DeleteLinksIdResponse401
    | DeleteLinksIdResponse403
    | DeleteLinksIdResponse422
    | DeleteLinksIdResponse429
    | None
):
    """Archive a link

     Archives the link (same as the dashboard's delete action). The row is not physically removed and the
    link keeps resolving normally — archiving only removes it from `GET /links`' default list.
    Reversible with `POST /links/{id}/restore`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteLinksIdResponse200 | DeleteLinksIdResponse401 | DeleteLinksIdResponse403 | DeleteLinksIdResponse422 | DeleteLinksIdResponse429
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
