from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_links_body import PostLinksBody
from ...models.post_links_response_201 import PostLinksResponse201
from ...models.post_links_response_401 import PostLinksResponse401
from ...models.post_links_response_403 import PostLinksResponse403
from ...models.post_links_response_422 import PostLinksResponse422
from ...models.post_links_response_429 import PostLinksResponse429
from ...types import Response


def _get_kwargs(
    *,
    body: PostLinksBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/links",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostLinksResponse201
    | PostLinksResponse401
    | PostLinksResponse403
    | PostLinksResponse422
    | PostLinksResponse429
    | None
):
    if response.status_code == 201:
        response_201 = PostLinksResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = PostLinksResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostLinksResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostLinksResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostLinksResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostLinksResponse201
    | PostLinksResponse401
    | PostLinksResponse403
    | PostLinksResponse422
    | PostLinksResponse429
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
    body: PostLinksBody,
) -> Response[
    PostLinksResponse201
    | PostLinksResponse401
    | PostLinksResponse403
    | PostLinksResponse422
    | PostLinksResponse429
]:
    """Create a link

     Creates a link with the same contract as the dashboard's create form. Only `destinationUrl` is
    required — every other field has a default, including `domain`: omit it to fall back to the team's
    default domain (primary custom domain, else the app's default short domain). Responds with the
    detail shape (same as `GET /links/{id}`).

    Args:
        body (PostLinksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksResponse201 | PostLinksResponse401 | PostLinksResponse403 | PostLinksResponse422 | PostLinksResponse429]
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
    body: PostLinksBody,
) -> (
    PostLinksResponse201
    | PostLinksResponse401
    | PostLinksResponse403
    | PostLinksResponse422
    | PostLinksResponse429
    | None
):
    """Create a link

     Creates a link with the same contract as the dashboard's create form. Only `destinationUrl` is
    required — every other field has a default, including `domain`: omit it to fall back to the team's
    default domain (primary custom domain, else the app's default short domain). Responds with the
    detail shape (same as `GET /links/{id}`).

    Args:
        body (PostLinksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksResponse201 | PostLinksResponse401 | PostLinksResponse403 | PostLinksResponse422 | PostLinksResponse429
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostLinksBody,
) -> Response[
    PostLinksResponse201
    | PostLinksResponse401
    | PostLinksResponse403
    | PostLinksResponse422
    | PostLinksResponse429
]:
    """Create a link

     Creates a link with the same contract as the dashboard's create form. Only `destinationUrl` is
    required — every other field has a default, including `domain`: omit it to fall back to the team's
    default domain (primary custom domain, else the app's default short domain). Responds with the
    detail shape (same as `GET /links/{id}`).

    Args:
        body (PostLinksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinksResponse201 | PostLinksResponse401 | PostLinksResponse403 | PostLinksResponse422 | PostLinksResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostLinksBody,
) -> (
    PostLinksResponse201
    | PostLinksResponse401
    | PostLinksResponse403
    | PostLinksResponse422
    | PostLinksResponse429
    | None
):
    """Create a link

     Creates a link with the same contract as the dashboard's create form. Only `destinationUrl` is
    required — every other field has a default, including `domain`: omit it to fall back to the team's
    default domain (primary custom domain, else the app's default short domain). Responds with the
    detail shape (same as `GET /links/{id}`).

    Args:
        body (PostLinksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinksResponse201 | PostLinksResponse401 | PostLinksResponse403 | PostLinksResponse422 | PostLinksResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
