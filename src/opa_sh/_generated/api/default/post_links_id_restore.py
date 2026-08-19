from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_links_id_restore_response_200 import PostLinksIdRestoreResponse200
from ...models.post_links_id_restore_response_401 import PostLinksIdRestoreResponse401
from ...models.post_links_id_restore_response_403 import PostLinksIdRestoreResponse403
from ...models.post_links_id_restore_response_422 import PostLinksIdRestoreResponse422
from ...models.post_links_id_restore_response_429 import PostLinksIdRestoreResponse429
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/links/{id}/restore".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostLinksIdRestoreResponse200
    | PostLinksIdRestoreResponse401
    | PostLinksIdRestoreResponse403
    | PostLinksIdRestoreResponse422
    | PostLinksIdRestoreResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PostLinksIdRestoreResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostLinksIdRestoreResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostLinksIdRestoreResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostLinksIdRestoreResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostLinksIdRestoreResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostLinksIdRestoreResponse200
    | PostLinksIdRestoreResponse401
    | PostLinksIdRestoreResponse403
    | PostLinksIdRestoreResponse422
    | PostLinksIdRestoreResponse429
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
    PostLinksIdRestoreResponse200
    | PostLinksIdRestoreResponse401
    | PostLinksIdRestoreResponse403
    | PostLinksIdRestoreResponse422
    | PostLinksIdRestoreResponse429
]:
    """Restore an archived link

     Un-archives the link (`archived = false`), the counterpart to `DELETE /links/{id}`. Brings it back
    onto `GET /links`' default list — it never stopped resolving while archived.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksIdRestoreResponse200 | PostLinksIdRestoreResponse401 | PostLinksIdRestoreResponse403 | PostLinksIdRestoreResponse422 | PostLinksIdRestoreResponse429]
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
    PostLinksIdRestoreResponse200
    | PostLinksIdRestoreResponse401
    | PostLinksIdRestoreResponse403
    | PostLinksIdRestoreResponse422
    | PostLinksIdRestoreResponse429
    | None
):
    """Restore an archived link

     Un-archives the link (`archived = false`), the counterpart to `DELETE /links/{id}`. Brings it back
    onto `GET /links`' default list — it never stopped resolving while archived.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksIdRestoreResponse200 | PostLinksIdRestoreResponse401 | PostLinksIdRestoreResponse403 | PostLinksIdRestoreResponse422 | PostLinksIdRestoreResponse429
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
    PostLinksIdRestoreResponse200
    | PostLinksIdRestoreResponse401
    | PostLinksIdRestoreResponse403
    | PostLinksIdRestoreResponse422
    | PostLinksIdRestoreResponse429
]:
    """Restore an archived link

     Un-archives the link (`archived = false`), the counterpart to `DELETE /links/{id}`. Brings it back
    onto `GET /links`' default list — it never stopped resolving while archived.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksIdRestoreResponse200 | PostLinksIdRestoreResponse401 | PostLinksIdRestoreResponse403 | PostLinksIdRestoreResponse422 | PostLinksIdRestoreResponse429]
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
    PostLinksIdRestoreResponse200
    | PostLinksIdRestoreResponse401
    | PostLinksIdRestoreResponse403
    | PostLinksIdRestoreResponse422
    | PostLinksIdRestoreResponse429
    | None
):
    """Restore an archived link

     Un-archives the link (`archived = false`), the counterpart to `DELETE /links/{id}`. Brings it back
    onto `GET /links`' default list — it never stopped resolving while archived.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksIdRestoreResponse200 | PostLinksIdRestoreResponse401 | PostLinksIdRestoreResponse403 | PostLinksIdRestoreResponse422 | PostLinksIdRestoreResponse429
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
