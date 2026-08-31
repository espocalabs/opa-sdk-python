from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_track_sale_body import PostTrackSaleBody
from ...models.post_track_sale_response_200 import PostTrackSaleResponse200
from ...models.post_track_sale_response_401 import PostTrackSaleResponse401
from ...models.post_track_sale_response_403 import PostTrackSaleResponse403
from ...models.post_track_sale_response_422 import PostTrackSaleResponse422
from ...models.post_track_sale_response_429 import PostTrackSaleResponse429
from ...types import Response


def _get_kwargs(
    *,
    body: PostTrackSaleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/track/sale",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostTrackSaleResponse200
    | PostTrackSaleResponse401
    | PostTrackSaleResponse403
    | PostTrackSaleResponse422
    | PostTrackSaleResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PostTrackSaleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostTrackSaleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostTrackSaleResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostTrackSaleResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostTrackSaleResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostTrackSaleResponse200
    | PostTrackSaleResponse401
    | PostTrackSaleResponse403
    | PostTrackSaleResponse422
    | PostTrackSaleResponse429
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
    body: PostTrackSaleBody,
) -> Response[
    PostTrackSaleResponse200
    | PostTrackSaleResponse401
    | PostTrackSaleResponse403
    | PostTrackSaleResponse422
    | PostTrackSaleResponse429
]:
    """Track a sale

     Records a monetary `sale` conversion event for a customer. `amount` is an integer number of minor
    units (cents), `>= 0` — a float or negative value is rejected. The customer must already be known
    via a prior lead, unless a `clickId` is supplied to bind one on the fly (otherwise
    `customer_not_found`). Idempotent on `invoiceId`: a replayed invoice records the sale exactly once
    and responds `200` with `deduped: true`, so retries never double-count revenue. Requires the
    `conversions:write` scope and full (read/write) API access (Pro plan).

    Args:
        body (PostTrackSaleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTrackSaleResponse200 | PostTrackSaleResponse401 | PostTrackSaleResponse403 | PostTrackSaleResponse422 | PostTrackSaleResponse429]
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
    body: PostTrackSaleBody,
) -> (
    PostTrackSaleResponse200
    | PostTrackSaleResponse401
    | PostTrackSaleResponse403
    | PostTrackSaleResponse422
    | PostTrackSaleResponse429
    | None
):
    """Track a sale

     Records a monetary `sale` conversion event for a customer. `amount` is an integer number of minor
    units (cents), `>= 0` — a float or negative value is rejected. The customer must already be known
    via a prior lead, unless a `clickId` is supplied to bind one on the fly (otherwise
    `customer_not_found`). Idempotent on `invoiceId`: a replayed invoice records the sale exactly once
    and responds `200` with `deduped: true`, so retries never double-count revenue. Requires the
    `conversions:write` scope and full (read/write) API access (Pro plan).

    Args:
        body (PostTrackSaleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTrackSaleResponse200 | PostTrackSaleResponse401 | PostTrackSaleResponse403 | PostTrackSaleResponse422 | PostTrackSaleResponse429
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostTrackSaleBody,
) -> Response[
    PostTrackSaleResponse200
    | PostTrackSaleResponse401
    | PostTrackSaleResponse403
    | PostTrackSaleResponse422
    | PostTrackSaleResponse429
]:
    """Track a sale

     Records a monetary `sale` conversion event for a customer. `amount` is an integer number of minor
    units (cents), `>= 0` — a float or negative value is rejected. The customer must already be known
    via a prior lead, unless a `clickId` is supplied to bind one on the fly (otherwise
    `customer_not_found`). Idempotent on `invoiceId`: a replayed invoice records the sale exactly once
    and responds `200` with `deduped: true`, so retries never double-count revenue. Requires the
    `conversions:write` scope and full (read/write) API access (Pro plan).

    Args:
        body (PostTrackSaleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTrackSaleResponse200 | PostTrackSaleResponse401 | PostTrackSaleResponse403 | PostTrackSaleResponse422 | PostTrackSaleResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostTrackSaleBody,
) -> (
    PostTrackSaleResponse200
    | PostTrackSaleResponse401
    | PostTrackSaleResponse403
    | PostTrackSaleResponse422
    | PostTrackSaleResponse429
    | None
):
    """Track a sale

     Records a monetary `sale` conversion event for a customer. `amount` is an integer number of minor
    units (cents), `>= 0` — a float or negative value is rejected. The customer must already be known
    via a prior lead, unless a `clickId` is supplied to bind one on the fly (otherwise
    `customer_not_found`). Idempotent on `invoiceId`: a replayed invoice records the sale exactly once
    and responds `200` with `deduped: true`, so retries never double-count revenue. Requires the
    `conversions:write` scope and full (read/write) API access (Pro plan).

    Args:
        body (PostTrackSaleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTrackSaleResponse200 | PostTrackSaleResponse401 | PostTrackSaleResponse403 | PostTrackSaleResponse422 | PostTrackSaleResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
