from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_analytics_events_response_200 import GetAnalyticsEventsResponse200
from ...models.get_analytics_events_response_401 import GetAnalyticsEventsResponse401
from ...models.get_analytics_events_response_403 import GetAnalyticsEventsResponse403
from ...models.get_analytics_events_response_422 import GetAnalyticsEventsResponse422
from ...models.get_analytics_events_response_429 import GetAnalyticsEventsResponse429
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    before: str | Unset = UNSET,
    link_id: str | Unset = UNSET,
    country: str | Unset = UNSET,
    device: str | Unset = UNSET,
    os: str | Unset = UNSET,
    browser: str | Unset = UNSET,
    referer_domain: str | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_medium: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    variant_url: str | Unset = UNSET,
    domain: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["before"] = before

    params["linkId"] = link_id

    params["country"] = country

    params["device"] = device

    params["os"] = os

    params["browser"] = browser

    params["refererDomain"] = referer_domain

    params["utmSource"] = utm_source

    params["utmMedium"] = utm_medium

    params["utmCampaign"] = utm_campaign

    params["variantUrl"] = variant_url

    params["domain"] = domain

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAnalyticsEventsResponse200
    | GetAnalyticsEventsResponse401
    | GetAnalyticsEventsResponse403
    | GetAnalyticsEventsResponse422
    | GetAnalyticsEventsResponse429
    | None
):
    if response.status_code == 200:
        response_200 = GetAnalyticsEventsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetAnalyticsEventsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetAnalyticsEventsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetAnalyticsEventsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetAnalyticsEventsResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAnalyticsEventsResponse200
    | GetAnalyticsEventsResponse401
    | GetAnalyticsEventsResponse403
    | GetAnalyticsEventsResponse422
    | GetAnalyticsEventsResponse429
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
    limit: int | Unset = 100,
    before: str | Unset = UNSET,
    link_id: str | Unset = UNSET,
    country: str | Unset = UNSET,
    device: str | Unset = UNSET,
    os: str | Unset = UNSET,
    browser: str | Unset = UNSET,
    referer_domain: str | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_medium: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    variant_url: str | Unset = UNSET,
    domain: str | Unset = UNSET,
) -> Response[
    GetAnalyticsEventsResponse200
    | GetAnalyticsEventsResponse401
    | GetAnalyticsEventsResponse403
    | GetAnalyticsEventsResponse422
    | GetAnalyticsEventsResponse429
]:
    """Analytics events

     The raw per-click event stream, cursor-paginated (`limit`/`before`) and optionally filtered by
    dimension — same filters as `analytics/summary`/`analytics/timeseries`. Pulled directly from
    Tinybird's raw event pipe, never the aggregated pipes those two endpoints use, so results reflect
    clicks within seconds. Same field set as the dashboard's events table, no reduction.

    Args:
        limit (int | Unset): Items per page. 1-500, default 100. Default: 100.
        before (str | Unset): Cursor. ISO-8601 UTC timestamp — returns events strictly older than
            it. Omit for the first (most recent) page; pass the previous page's `pagination.next` to
            fetch the next one. Chosen over an epoch cursor for readability and because every other
            timestamp this API returns (`range.from`/`range.to`, and this same endpoint's own
            `pagination.next`) is already ISO-8601.
        link_id (str | Unset):
        country (str | Unset):
        device (str | Unset):
        os (str | Unset):
        browser (str | Unset):
        referer_domain (str | Unset):
        utm_source (str | Unset):
        utm_medium (str | Unset):
        utm_campaign (str | Unset):
        variant_url (str | Unset):
        domain (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnalyticsEventsResponse200 | GetAnalyticsEventsResponse401 | GetAnalyticsEventsResponse403 | GetAnalyticsEventsResponse422 | GetAnalyticsEventsResponse429]
    """

    kwargs = _get_kwargs(
        limit=limit,
        before=before,
        link_id=link_id,
        country=country,
        device=device,
        os=os,
        browser=browser,
        referer_domain=referer_domain,
        utm_source=utm_source,
        utm_medium=utm_medium,
        utm_campaign=utm_campaign,
        variant_url=variant_url,
        domain=domain,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    before: str | Unset = UNSET,
    link_id: str | Unset = UNSET,
    country: str | Unset = UNSET,
    device: str | Unset = UNSET,
    os: str | Unset = UNSET,
    browser: str | Unset = UNSET,
    referer_domain: str | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_medium: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    variant_url: str | Unset = UNSET,
    domain: str | Unset = UNSET,
) -> (
    GetAnalyticsEventsResponse200
    | GetAnalyticsEventsResponse401
    | GetAnalyticsEventsResponse403
    | GetAnalyticsEventsResponse422
    | GetAnalyticsEventsResponse429
    | None
):
    """Analytics events

     The raw per-click event stream, cursor-paginated (`limit`/`before`) and optionally filtered by
    dimension — same filters as `analytics/summary`/`analytics/timeseries`. Pulled directly from
    Tinybird's raw event pipe, never the aggregated pipes those two endpoints use, so results reflect
    clicks within seconds. Same field set as the dashboard's events table, no reduction.

    Args:
        limit (int | Unset): Items per page. 1-500, default 100. Default: 100.
        before (str | Unset): Cursor. ISO-8601 UTC timestamp — returns events strictly older than
            it. Omit for the first (most recent) page; pass the previous page's `pagination.next` to
            fetch the next one. Chosen over an epoch cursor for readability and because every other
            timestamp this API returns (`range.from`/`range.to`, and this same endpoint's own
            `pagination.next`) is already ISO-8601.
        link_id (str | Unset):
        country (str | Unset):
        device (str | Unset):
        os (str | Unset):
        browser (str | Unset):
        referer_domain (str | Unset):
        utm_source (str | Unset):
        utm_medium (str | Unset):
        utm_campaign (str | Unset):
        variant_url (str | Unset):
        domain (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnalyticsEventsResponse200 | GetAnalyticsEventsResponse401 | GetAnalyticsEventsResponse403 | GetAnalyticsEventsResponse422 | GetAnalyticsEventsResponse429
    """

    return sync_detailed(
        client=client,
        limit=limit,
        before=before,
        link_id=link_id,
        country=country,
        device=device,
        os=os,
        browser=browser,
        referer_domain=referer_domain,
        utm_source=utm_source,
        utm_medium=utm_medium,
        utm_campaign=utm_campaign,
        variant_url=variant_url,
        domain=domain,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    before: str | Unset = UNSET,
    link_id: str | Unset = UNSET,
    country: str | Unset = UNSET,
    device: str | Unset = UNSET,
    os: str | Unset = UNSET,
    browser: str | Unset = UNSET,
    referer_domain: str | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_medium: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    variant_url: str | Unset = UNSET,
    domain: str | Unset = UNSET,
) -> Response[
    GetAnalyticsEventsResponse200
    | GetAnalyticsEventsResponse401
    | GetAnalyticsEventsResponse403
    | GetAnalyticsEventsResponse422
    | GetAnalyticsEventsResponse429
]:
    """Analytics events

     The raw per-click event stream, cursor-paginated (`limit`/`before`) and optionally filtered by
    dimension — same filters as `analytics/summary`/`analytics/timeseries`. Pulled directly from
    Tinybird's raw event pipe, never the aggregated pipes those two endpoints use, so results reflect
    clicks within seconds. Same field set as the dashboard's events table, no reduction.

    Args:
        limit (int | Unset): Items per page. 1-500, default 100. Default: 100.
        before (str | Unset): Cursor. ISO-8601 UTC timestamp — returns events strictly older than
            it. Omit for the first (most recent) page; pass the previous page's `pagination.next` to
            fetch the next one. Chosen over an epoch cursor for readability and because every other
            timestamp this API returns (`range.from`/`range.to`, and this same endpoint's own
            `pagination.next`) is already ISO-8601.
        link_id (str | Unset):
        country (str | Unset):
        device (str | Unset):
        os (str | Unset):
        browser (str | Unset):
        referer_domain (str | Unset):
        utm_source (str | Unset):
        utm_medium (str | Unset):
        utm_campaign (str | Unset):
        variant_url (str | Unset):
        domain (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnalyticsEventsResponse200 | GetAnalyticsEventsResponse401 | GetAnalyticsEventsResponse403 | GetAnalyticsEventsResponse422 | GetAnalyticsEventsResponse429]
    """

    kwargs = _get_kwargs(
        limit=limit,
        before=before,
        link_id=link_id,
        country=country,
        device=device,
        os=os,
        browser=browser,
        referer_domain=referer_domain,
        utm_source=utm_source,
        utm_medium=utm_medium,
        utm_campaign=utm_campaign,
        variant_url=variant_url,
        domain=domain,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
    before: str | Unset = UNSET,
    link_id: str | Unset = UNSET,
    country: str | Unset = UNSET,
    device: str | Unset = UNSET,
    os: str | Unset = UNSET,
    browser: str | Unset = UNSET,
    referer_domain: str | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_medium: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    variant_url: str | Unset = UNSET,
    domain: str | Unset = UNSET,
) -> (
    GetAnalyticsEventsResponse200
    | GetAnalyticsEventsResponse401
    | GetAnalyticsEventsResponse403
    | GetAnalyticsEventsResponse422
    | GetAnalyticsEventsResponse429
    | None
):
    """Analytics events

     The raw per-click event stream, cursor-paginated (`limit`/`before`) and optionally filtered by
    dimension — same filters as `analytics/summary`/`analytics/timeseries`. Pulled directly from
    Tinybird's raw event pipe, never the aggregated pipes those two endpoints use, so results reflect
    clicks within seconds. Same field set as the dashboard's events table, no reduction.

    Args:
        limit (int | Unset): Items per page. 1-500, default 100. Default: 100.
        before (str | Unset): Cursor. ISO-8601 UTC timestamp — returns events strictly older than
            it. Omit for the first (most recent) page; pass the previous page's `pagination.next` to
            fetch the next one. Chosen over an epoch cursor for readability and because every other
            timestamp this API returns (`range.from`/`range.to`, and this same endpoint's own
            `pagination.next`) is already ISO-8601.
        link_id (str | Unset):
        country (str | Unset):
        device (str | Unset):
        os (str | Unset):
        browser (str | Unset):
        referer_domain (str | Unset):
        utm_source (str | Unset):
        utm_medium (str | Unset):
        utm_campaign (str | Unset):
        variant_url (str | Unset):
        domain (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnalyticsEventsResponse200 | GetAnalyticsEventsResponse401 | GetAnalyticsEventsResponse403 | GetAnalyticsEventsResponse422 | GetAnalyticsEventsResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            before=before,
            link_id=link_id,
            country=country,
            device=device,
            os=os,
            browser=browser,
            referer_domain=referer_domain,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            variant_url=variant_url,
            domain=domain,
        )
    ).parsed
