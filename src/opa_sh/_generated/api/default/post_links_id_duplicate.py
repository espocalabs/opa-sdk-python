from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_links_id_duplicate_response_201 import PostLinksIdDuplicateResponse201
from ...models.post_links_id_duplicate_response_401 import PostLinksIdDuplicateResponse401
from ...models.post_links_id_duplicate_response_403 import PostLinksIdDuplicateResponse403
from ...models.post_links_id_duplicate_response_422 import PostLinksIdDuplicateResponse422
from ...models.post_links_id_duplicate_response_429 import PostLinksIdDuplicateResponse429
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/links/{id}/duplicate".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostLinksIdDuplicateResponse201
    | PostLinksIdDuplicateResponse401
    | PostLinksIdDuplicateResponse403
    | PostLinksIdDuplicateResponse422
    | PostLinksIdDuplicateResponse429
    | None
):
    if response.status_code == 201:
        response_201 = PostLinksIdDuplicateResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = PostLinksIdDuplicateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostLinksIdDuplicateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostLinksIdDuplicateResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostLinksIdDuplicateResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostLinksIdDuplicateResponse201
    | PostLinksIdDuplicateResponse401
    | PostLinksIdDuplicateResponse403
    | PostLinksIdDuplicateResponse422
    | PostLinksIdDuplicateResponse429
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
    PostLinksIdDuplicateResponse201
    | PostLinksIdDuplicateResponse401
    | PostLinksIdDuplicateResponse403
    | PostLinksIdDuplicateResponse422
    | PostLinksIdDuplicateResponse429
]:
    """Duplicate a link

     Creates a copy of the link. Not copied: password, an in-flight A/B test, `disabledAt`. Responds with
    the detail shape of the NEW link.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksIdDuplicateResponse201 | PostLinksIdDuplicateResponse401 | PostLinksIdDuplicateResponse403 | PostLinksIdDuplicateResponse422 | PostLinksIdDuplicateResponse429]
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
    PostLinksIdDuplicateResponse201
    | PostLinksIdDuplicateResponse401
    | PostLinksIdDuplicateResponse403
    | PostLinksIdDuplicateResponse422
    | PostLinksIdDuplicateResponse429
    | None
):
    """Duplicate a link

     Creates a copy of the link. Not copied: password, an in-flight A/B test, `disabledAt`. Responds with
    the detail shape of the NEW link.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksIdDuplicateResponse201 | PostLinksIdDuplicateResponse401 | PostLinksIdDuplicateResponse403 | PostLinksIdDuplicateResponse422 | PostLinksIdDuplicateResponse429
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
    PostLinksIdDuplicateResponse201
    | PostLinksIdDuplicateResponse401
    | PostLinksIdDuplicateResponse403
    | PostLinksIdDuplicateResponse422
    | PostLinksIdDuplicateResponse429
]:
    """Duplicate a link

     Creates a copy of the link. Not copied: password, an in-flight A/B test, `disabledAt`. Responds with
    the detail shape of the NEW link.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksIdDuplicateResponse201 | PostLinksIdDuplicateResponse401 | PostLinksIdDuplicateResponse403 | PostLinksIdDuplicateResponse422 | PostLinksIdDuplicateResponse429]
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
    PostLinksIdDuplicateResponse201
    | PostLinksIdDuplicateResponse401
    | PostLinksIdDuplicateResponse403
    | PostLinksIdDuplicateResponse422
    | PostLinksIdDuplicateResponse429
    | None
):
    """Duplicate a link

     Creates a copy of the link. Not copied: password, an in-flight A/B test, `disabledAt`. Responds with
    the detail shape of the NEW link.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksIdDuplicateResponse201 | PostLinksIdDuplicateResponse401 | PostLinksIdDuplicateResponse403 | PostLinksIdDuplicateResponse422 | PostLinksIdDuplicateResponse429
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
