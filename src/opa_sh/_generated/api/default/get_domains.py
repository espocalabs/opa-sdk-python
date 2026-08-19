from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_domains_response_200 import GetDomainsResponse200
from ...models.get_domains_response_401 import GetDomainsResponse401
from ...models.get_domains_response_403 import GetDomainsResponse403
from ...models.get_domains_response_422 import GetDomainsResponse422
from ...models.get_domains_response_429 import GetDomainsResponse429
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domains",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetDomainsResponse200
    | GetDomainsResponse401
    | GetDomainsResponse403
    | GetDomainsResponse422
    | GetDomainsResponse429
    | None
):
    if response.status_code == 200:
        response_200 = GetDomainsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetDomainsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetDomainsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetDomainsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetDomainsResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetDomainsResponse200
    | GetDomainsResponse401
    | GetDomainsResponse403
    | GetDomainsResponse422
    | GetDomainsResponse429
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
) -> Response[
    GetDomainsResponse200
    | GetDomainsResponse401
    | GetDomainsResponse403
    | GetDomainsResponse422
    | GetDomainsResponse429
]:
    """List usable domains

     Domains this organization can use as a link's `domain`: its own custom (USER_DOMAIN) domains plus
    every verified shared (APP_DOMAIN) domain.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDomainsResponse200 | GetDomainsResponse401 | GetDomainsResponse403 | GetDomainsResponse422 | GetDomainsResponse429]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetDomainsResponse200
    | GetDomainsResponse401
    | GetDomainsResponse403
    | GetDomainsResponse422
    | GetDomainsResponse429
    | None
):
    """List usable domains

     Domains this organization can use as a link's `domain`: its own custom (USER_DOMAIN) domains plus
    every verified shared (APP_DOMAIN) domain.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDomainsResponse200 | GetDomainsResponse401 | GetDomainsResponse403 | GetDomainsResponse422 | GetDomainsResponse429
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetDomainsResponse200
    | GetDomainsResponse401
    | GetDomainsResponse403
    | GetDomainsResponse422
    | GetDomainsResponse429
]:
    """List usable domains

     Domains this organization can use as a link's `domain`: its own custom (USER_DOMAIN) domains plus
    every verified shared (APP_DOMAIN) domain.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDomainsResponse200 | GetDomainsResponse401 | GetDomainsResponse403 | GetDomainsResponse422 | GetDomainsResponse429]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetDomainsResponse200
    | GetDomainsResponse401
    | GetDomainsResponse403
    | GetDomainsResponse422
    | GetDomainsResponse429
    | None
):
    """List usable domains

     Domains this organization can use as a link's `domain`: its own custom (USER_DOMAIN) domains plus
    every verified shared (APP_DOMAIN) domain.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDomainsResponse200 | GetDomainsResponse401 | GetDomainsResponse403 | GetDomainsResponse422 | GetDomainsResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
