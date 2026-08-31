from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_track_lead_body import PostTrackLeadBody
from ...models.post_track_lead_response_200 import PostTrackLeadResponse200
from ...models.post_track_lead_response_401 import PostTrackLeadResponse401
from ...models.post_track_lead_response_403 import PostTrackLeadResponse403
from ...models.post_track_lead_response_422 import PostTrackLeadResponse422
from ...models.post_track_lead_response_429 import PostTrackLeadResponse429
from ...types import Response


def _get_kwargs(
    *,
    body: PostTrackLeadBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/track/lead",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostTrackLeadResponse200
    | PostTrackLeadResponse401
    | PostTrackLeadResponse403
    | PostTrackLeadResponse422
    | PostTrackLeadResponse429
    | None
):
    if response.status_code == 200:
        response_200 = PostTrackLeadResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostTrackLeadResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostTrackLeadResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostTrackLeadResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostTrackLeadResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostTrackLeadResponse200
    | PostTrackLeadResponse401
    | PostTrackLeadResponse403
    | PostTrackLeadResponse422
    | PostTrackLeadResponse429
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
    body: PostTrackLeadBody,
) -> Response[
    PostTrackLeadResponse200
    | PostTrackLeadResponse401
    | PostTrackLeadResponse403
    | PostTrackLeadResponse422
    | PostTrackLeadResponse429
]:
    """Track a lead

     Binds a click to a customer and records a `lead` conversion event — the anchor that ties a `clickId`
    to your own `customerExternalId` so later sales only need the external id. Upserts the customer
    (stamping their first click). Deduped by `(customerExternalId, eventName)`: reporting the same lead
    twice records ONE event and responds `200` both times — `deduped` in the response says whether this
    call recorded a new event. Requires the `conversions:write` scope and full (read/write) API access
    (Pro plan).

    Args:
        body (PostTrackLeadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTrackLeadResponse200 | PostTrackLeadResponse401 | PostTrackLeadResponse403 | PostTrackLeadResponse422 | PostTrackLeadResponse429]
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
    body: PostTrackLeadBody,
) -> (
    PostTrackLeadResponse200
    | PostTrackLeadResponse401
    | PostTrackLeadResponse403
    | PostTrackLeadResponse422
    | PostTrackLeadResponse429
    | None
):
    """Track a lead

     Binds a click to a customer and records a `lead` conversion event — the anchor that ties a `clickId`
    to your own `customerExternalId` so later sales only need the external id. Upserts the customer
    (stamping their first click). Deduped by `(customerExternalId, eventName)`: reporting the same lead
    twice records ONE event and responds `200` both times — `deduped` in the response says whether this
    call recorded a new event. Requires the `conversions:write` scope and full (read/write) API access
    (Pro plan).

    Args:
        body (PostTrackLeadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTrackLeadResponse200 | PostTrackLeadResponse401 | PostTrackLeadResponse403 | PostTrackLeadResponse422 | PostTrackLeadResponse429
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostTrackLeadBody,
) -> Response[
    PostTrackLeadResponse200
    | PostTrackLeadResponse401
    | PostTrackLeadResponse403
    | PostTrackLeadResponse422
    | PostTrackLeadResponse429
]:
    """Track a lead

     Binds a click to a customer and records a `lead` conversion event — the anchor that ties a `clickId`
    to your own `customerExternalId` so later sales only need the external id. Upserts the customer
    (stamping their first click). Deduped by `(customerExternalId, eventName)`: reporting the same lead
    twice records ONE event and responds `200` both times — `deduped` in the response says whether this
    call recorded a new event. Requires the `conversions:write` scope and full (read/write) API access
    (Pro plan).

    Args:
        body (PostTrackLeadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTrackLeadResponse200 | PostTrackLeadResponse401 | PostTrackLeadResponse403 | PostTrackLeadResponse422 | PostTrackLeadResponse429]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostTrackLeadBody,
) -> (
    PostTrackLeadResponse200
    | PostTrackLeadResponse401
    | PostTrackLeadResponse403
    | PostTrackLeadResponse422
    | PostTrackLeadResponse429
    | None
):
    """Track a lead

     Binds a click to a customer and records a `lead` conversion event — the anchor that ties a `clickId`
    to your own `customerExternalId` so later sales only need the external id. Upserts the customer
    (stamping their first click). Deduped by `(customerExternalId, eventName)`: reporting the same lead
    twice records ONE event and responds `200` both times — `deduped` in the response says whether this
    call recorded a new event. Requires the `conversions:write` scope and full (read/write) API access
    (Pro plan).

    Args:
        body (PostTrackLeadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTrackLeadResponse200 | PostTrackLeadResponse401 | PostTrackLeadResponse403 | PostTrackLeadResponse422 | PostTrackLeadResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
