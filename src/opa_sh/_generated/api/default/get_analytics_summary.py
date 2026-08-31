from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_analytics_summary_response_200 import GetAnalyticsSummaryResponse200
from ...models.get_analytics_summary_response_401 import GetAnalyticsSummaryResponse401
from ...models.get_analytics_summary_response_403 import GetAnalyticsSummaryResponse403
from ...models.get_analytics_summary_response_422 import GetAnalyticsSummaryResponse422
from ...models.get_analytics_summary_response_429 import GetAnalyticsSummaryResponse429
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
        "url": "/analytics/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAnalyticsSummaryResponse200
    | GetAnalyticsSummaryResponse401
    | GetAnalyticsSummaryResponse403
    | GetAnalyticsSummaryResponse422
    | GetAnalyticsSummaryResponse429
    | None
):
    if response.status_code == 200:
        response_200 = GetAnalyticsSummaryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetAnalyticsSummaryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetAnalyticsSummaryResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = GetAnalyticsSummaryResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetAnalyticsSummaryResponse429.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAnalyticsSummaryResponse200
    | GetAnalyticsSummaryResponse401
    | GetAnalyticsSummaryResponse403
    | GetAnalyticsSummaryResponse422
    | GetAnalyticsSummaryResponse429
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
    GetAnalyticsSummaryResponse200
    | GetAnalyticsSummaryResponse401
    | GetAnalyticsSummaryResponse403
    | GetAnalyticsSummaryResponse422
    | GetAnalyticsSummaryResponse429
]:
    """Analytics summary

     Aggregated totals (clicks, unique clicks) for a date range, optionally filtered by dimension.
    Aggregated straight from Postgres, never the raw event stream. The effective range is clamped to the
    organization's current plan's analytics retention window when the requested `from` reaches further
    back than the plan allows — see the response's `clamped`/`range`.

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
        Response[GetAnalyticsSummaryResponse200 | GetAnalyticsSummaryResponse401 | GetAnalyticsSummaryResponse403 | GetAnalyticsSummaryResponse422 | GetAnalyticsSummaryResponse429]
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
    client: AuthenticatedClient,
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
    GetAnalyticsSummaryResponse200
    | GetAnalyticsSummaryResponse401
    | GetAnalyticsSummaryResponse403
    | GetAnalyticsSummaryResponse422
    | GetAnalyticsSummaryResponse429
    | None
):
    """Analytics summary

     Aggregated totals (clicks, unique clicks) for a date range, optionally filtered by dimension.
    Aggregated straight from Postgres, never the raw event stream. The effective range is clamped to the
    organization's current plan's analytics retention window when the requested `from` reaches further
    back than the plan allows — see the response's `clamped`/`range`.

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
        GetAnalyticsSummaryResponse200 | GetAnalyticsSummaryResponse401 | GetAnalyticsSummaryResponse403 | GetAnalyticsSummaryResponse422 | GetAnalyticsSummaryResponse429
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
    client: AuthenticatedClient,
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
    GetAnalyticsSummaryResponse200
    | GetAnalyticsSummaryResponse401
    | GetAnalyticsSummaryResponse403
    | GetAnalyticsSummaryResponse422
    | GetAnalyticsSummaryResponse429
]:
    """Analytics summary

     Aggregated totals (clicks, unique clicks) for a date range, optionally filtered by dimension.
    Aggregated straight from Postgres, never the raw event stream. The effective range is clamped to the
    organization's current plan's analytics retention window when the requested `from` reaches further
    back than the plan allows — see the response's `clamped`/`range`.

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
        Response[GetAnalyticsSummaryResponse200 | GetAnalyticsSummaryResponse401 | GetAnalyticsSummaryResponse403 | GetAnalyticsSummaryResponse422 | GetAnalyticsSummaryResponse429]
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
    client: AuthenticatedClient,
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
    GetAnalyticsSummaryResponse200
    | GetAnalyticsSummaryResponse401
    | GetAnalyticsSummaryResponse403
    | GetAnalyticsSummaryResponse422
    | GetAnalyticsSummaryResponse429
    | None
):
    """Analytics summary

     Aggregated totals (clicks, unique clicks) for a date range, optionally filtered by dimension.
    Aggregated straight from Postgres, never the raw event stream. The effective range is clamped to the
    organization's current plan's analytics retention window when the requested `from` reaches further
    back than the plan allows — see the response's `clamped`/`range`.

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
        GetAnalyticsSummaryResponse200 | GetAnalyticsSummaryResponse401 | GetAnalyticsSummaryResponse403 | GetAnalyticsSummaryResponse422 | GetAnalyticsSummaryResponse429
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
