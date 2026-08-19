from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_analytics_timeseries_response_200 import GetAnalyticsTimeseriesResponse200
from ...models.get_analytics_timeseries_response_401 import GetAnalyticsTimeseriesResponse401
from ...models.get_analytics_timeseries_response_403 import GetAnalyticsTimeseriesResponse403
from ...models.get_analytics_timeseries_response_422 import GetAnalyticsTimeseriesResponse422
from ...models.get_analytics_timeseries_response_429 import GetAnalyticsTimeseriesResponse429
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str,
    to: str,
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

    params["from"] = from_

    params["to"] = to

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
        "url": "/analytics/timeseries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAnalyticsTimeseriesResponse200
    | GetAnalyticsTimeseriesResponse401
    | GetAnalyticsTimeseriesResponse403
    | GetAnalyticsTimeseriesResponse422
    | GetAnalyticsTimeseriesResponse429
    | None
):
    if response.status_code == 200:
        response_200 = GetAnalyticsTimeseriesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetAnalyticsTimeseriesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetAnalyticsTimeseriesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetAnalyticsTimeseriesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetAnalyticsTimeseriesResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAnalyticsTimeseriesResponse200
    | GetAnalyticsTimeseriesResponse401
    | GetAnalyticsTimeseriesResponse403
    | GetAnalyticsTimeseriesResponse422
    | GetAnalyticsTimeseriesResponse429
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
    from_: str,
    to: str,
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
    GetAnalyticsTimeseriesResponse200
    | GetAnalyticsTimeseriesResponse401
    | GetAnalyticsTimeseriesResponse403
    | GetAnalyticsTimeseriesResponse422
    | GetAnalyticsTimeseriesResponse429
]:
    """Analytics timeseries

     Daily click counts for a date range, optionally filtered by dimension. Same source and filters as
    the summary endpoint, including the same plan-retention range clamp — see that endpoint's
    description.

    Args:
        from_ (str): ISO date, inclusive. Must be on or before `to`; the range between them cannot
            exceed 366 days. May be pushed forward server-side, independent of this cap, if it reaches
            further back than the organization's current plan retains analytics for — see the
            response's `clamped`/effective `range`.
        to (str): ISO date, inclusive. Must be on or after `from`; the range between them cannot
            exceed 366 days.
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
        Response[GetAnalyticsTimeseriesResponse200 | GetAnalyticsTimeseriesResponse401 | GetAnalyticsTimeseriesResponse403 | GetAnalyticsTimeseriesResponse422 | GetAnalyticsTimeseriesResponse429]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
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
    client: AuthenticatedClient | Client,
    from_: str,
    to: str,
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
    GetAnalyticsTimeseriesResponse200
    | GetAnalyticsTimeseriesResponse401
    | GetAnalyticsTimeseriesResponse403
    | GetAnalyticsTimeseriesResponse422
    | GetAnalyticsTimeseriesResponse429
    | None
):
    """Analytics timeseries

     Daily click counts for a date range, optionally filtered by dimension. Same source and filters as
    the summary endpoint, including the same plan-retention range clamp — see that endpoint's
    description.

    Args:
        from_ (str): ISO date, inclusive. Must be on or before `to`; the range between them cannot
            exceed 366 days. May be pushed forward server-side, independent of this cap, if it reaches
            further back than the organization's current plan retains analytics for — see the
            response's `clamped`/effective `range`.
        to (str): ISO date, inclusive. Must be on or after `from`; the range between them cannot
            exceed 366 days.
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
        GetAnalyticsTimeseriesResponse200 | GetAnalyticsTimeseriesResponse401 | GetAnalyticsTimeseriesResponse403 | GetAnalyticsTimeseriesResponse422 | GetAnalyticsTimeseriesResponse429
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
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
    client: AuthenticatedClient | Client,
    from_: str,
    to: str,
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
    GetAnalyticsTimeseriesResponse200
    | GetAnalyticsTimeseriesResponse401
    | GetAnalyticsTimeseriesResponse403
    | GetAnalyticsTimeseriesResponse422
    | GetAnalyticsTimeseriesResponse429
]:
    """Analytics timeseries

     Daily click counts for a date range, optionally filtered by dimension. Same source and filters as
    the summary endpoint, including the same plan-retention range clamp — see that endpoint's
    description.

    Args:
        from_ (str): ISO date, inclusive. Must be on or before `to`; the range between them cannot
            exceed 366 days. May be pushed forward server-side, independent of this cap, if it reaches
            further back than the organization's current plan retains analytics for — see the
            response's `clamped`/effective `range`.
        to (str): ISO date, inclusive. Must be on or after `from`; the range between them cannot
            exceed 366 days.
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
        Response[GetAnalyticsTimeseriesResponse200 | GetAnalyticsTimeseriesResponse401 | GetAnalyticsTimeseriesResponse403 | GetAnalyticsTimeseriesResponse422 | GetAnalyticsTimeseriesResponse429]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
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
    client: AuthenticatedClient | Client,
    from_: str,
    to: str,
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
    GetAnalyticsTimeseriesResponse200
    | GetAnalyticsTimeseriesResponse401
    | GetAnalyticsTimeseriesResponse403
    | GetAnalyticsTimeseriesResponse422
    | GetAnalyticsTimeseriesResponse429
    | None
):
    """Analytics timeseries

     Daily click counts for a date range, optionally filtered by dimension. Same source and filters as
    the summary endpoint, including the same plan-retention range clamp — see that endpoint's
    description.

    Args:
        from_ (str): ISO date, inclusive. Must be on or before `to`; the range between them cannot
            exceed 366 days. May be pushed forward server-side, independent of this cap, if it reaches
            further back than the organization's current plan retains analytics for — see the
            response's `clamped`/effective `range`.
        to (str): ISO date, inclusive. Must be on or after `from`; the range between them cannot
            exceed 366 days.
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
        GetAnalyticsTimeseriesResponse200 | GetAnalyticsTimeseriesResponse401 | GetAnalyticsTimeseriesResponse403 | GetAnalyticsTimeseriesResponse422 | GetAnalyticsTimeseriesResponse429
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
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
