from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_links_id_body import PatchLinksIdBody
from ...models.patch_links_id_response_200 import PatchLinksIdResponse200
from ...models.patch_links_id_response_401 import PatchLinksIdResponse401
from ...models.patch_links_id_response_403 import PatchLinksIdResponse403
from ...models.patch_links_id_response_422 import PatchLinksIdResponse422
from ...models.patch_links_id_response_429 import PatchLinksIdResponse429
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PatchLinksIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/links/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchLinksIdResponse200
    | PatchLinksIdResponse401
    | PatchLinksIdResponse403
    | PatchLinksIdResponse422
    | PatchLinksIdResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PatchLinksIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PatchLinksIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchLinksIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PatchLinksIdResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PatchLinksIdResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchLinksIdResponse200
    | PatchLinksIdResponse401
    | PatchLinksIdResponse403
    | PatchLinksIdResponse422
    | PatchLinksIdResponse429
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
    body: PatchLinksIdBody,
) -> Response[
    PatchLinksIdResponse200
    | PatchLinksIdResponse401
    | PatchLinksIdResponse403
    | PatchLinksIdResponse422
    | PatchLinksIdResponse429
]:
    """Update a link

     Full-payload update — same schema as create, minus `linkId` (supplied by the path). Responds with
    the detail shape.

    Args:
        id (str):
        body (PatchLinksIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchLinksIdResponse200 | PatchLinksIdResponse401 | PatchLinksIdResponse403 | PatchLinksIdResponse422 | PatchLinksIdResponse429]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchLinksIdBody,
) -> (
    PatchLinksIdResponse200
    | PatchLinksIdResponse401
    | PatchLinksIdResponse403
    | PatchLinksIdResponse422
    | PatchLinksIdResponse429
    | None
):
    """Update a link

     Full-payload update — same schema as create, minus `linkId` (supplied by the path). Responds with
    the detail shape.

    Args:
        id (str):
        body (PatchLinksIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchLinksIdResponse200 | PatchLinksIdResponse401 | PatchLinksIdResponse403 | PatchLinksIdResponse422 | PatchLinksIdResponse429
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchLinksIdBody,
) -> Response[
    PatchLinksIdResponse200
    | PatchLinksIdResponse401
    | PatchLinksIdResponse403
    | PatchLinksIdResponse422
    | PatchLinksIdResponse429
]:
    """Update a link

     Full-payload update — same schema as create, minus `linkId` (supplied by the path). Responds with
    the detail shape.

    Args:
        id (str):
        body (PatchLinksIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchLinksIdResponse200 | PatchLinksIdResponse401 | PatchLinksIdResponse403 | PatchLinksIdResponse422 | PatchLinksIdResponse429]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchLinksIdBody,
) -> (
    PatchLinksIdResponse200
    | PatchLinksIdResponse401
    | PatchLinksIdResponse403
    | PatchLinksIdResponse422
    | PatchLinksIdResponse429
    | None
):
    """Update a link

     Full-payload update — same schema as create, minus `linkId` (supplied by the path). Responds with
    the detail shape.

    Args:
        id (str):
        body (PatchLinksIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchLinksIdResponse200 | PatchLinksIdResponse401 | PatchLinksIdResponse403 | PatchLinksIdResponse422 | PatchLinksIdResponse429
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
