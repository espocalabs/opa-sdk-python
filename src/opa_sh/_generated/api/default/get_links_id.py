from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_links_id_response_200 import GetLinksIdResponse200
from ...models.get_links_id_response_401 import GetLinksIdResponse401
from ...models.get_links_id_response_403 import GetLinksIdResponse403
from ...models.get_links_id_response_422 import GetLinksIdResponse422
from ...models.get_links_id_response_429 import GetLinksIdResponse429
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/links/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetLinksIdResponse200
    | GetLinksIdResponse401
    | GetLinksIdResponse403
    | GetLinksIdResponse422
    | GetLinksIdResponse429
    | None
):
    if response.status_code == 200:
        response_200 = GetLinksIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetLinksIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetLinksIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetLinksIdResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetLinksIdResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetLinksIdResponse200
    | GetLinksIdResponse401
    | GetLinksIdResponse403
    | GetLinksIdResponse422
    | GetLinksIdResponse429
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
    client: AuthenticatedClient | Client,
) -> Response[
    GetLinksIdResponse200
    | GetLinksIdResponse401
    | GetLinksIdResponse403
    | GetLinksIdResponse422
    | GetLinksIdResponse429
]:
    """Get a link

     Fetches a single link in the detail shape.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLinksIdResponse200 | GetLinksIdResponse401 | GetLinksIdResponse403 | GetLinksIdResponse422 | GetLinksIdResponse429]
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
    client: AuthenticatedClient | Client,
) -> (
    GetLinksIdResponse200
    | GetLinksIdResponse401
    | GetLinksIdResponse403
    | GetLinksIdResponse422
    | GetLinksIdResponse429
    | None
):
    """Get a link

     Fetches a single link in the detail shape.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLinksIdResponse200 | GetLinksIdResponse401 | GetLinksIdResponse403 | GetLinksIdResponse422 | GetLinksIdResponse429
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetLinksIdResponse200
    | GetLinksIdResponse401
    | GetLinksIdResponse403
    | GetLinksIdResponse422
    | GetLinksIdResponse429
]:
    """Get a link

     Fetches a single link in the detail shape.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLinksIdResponse200 | GetLinksIdResponse401 | GetLinksIdResponse403 | GetLinksIdResponse422 | GetLinksIdResponse429]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetLinksIdResponse200
    | GetLinksIdResponse401
    | GetLinksIdResponse403
    | GetLinksIdResponse422
    | GetLinksIdResponse429
    | None
):
    """Get a link

     Fetches a single link in the detail shape.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLinksIdResponse200 | GetLinksIdResponse401 | GetLinksIdResponse403 | GetLinksIdResponse422 | GetLinksIdResponse429
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
