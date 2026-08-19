"""``opa.analytics`` — aggregate and raw-event click analytics."""

from collections.abc import AsyncIterator, Iterator
from typing import Any, Optional

import httpx

from .._internal.request_options import RequestOptions, request_headers, request_timeout
from .._internal.serialize import build_query
from ..errors import raise_for_response
from ..models import AnalyticsEvent, AnalyticsSummary, AnalyticsTimeseries, Page
from ..pagination import apaginate, paginate


def _query_params(
    *,
    from_: Optional[str] = None,
    to: Optional[str] = None,
    link_id: Optional[str] = None,
    country: Optional[str] = None,
    device: Optional[str] = None,
    os: Optional[str] = None,
    browser: Optional[str] = None,
    referer_domain: Optional[str] = None,
    utm_source: Optional[str] = None,
    utm_medium: Optional[str] = None,
    utm_campaign: Optional[str] = None,
    variant_url: Optional[str] = None,
    domain: Optional[str] = None,
) -> dict[str, Any]:
    params = build_query(
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
    # `from`/`to` are Python-keyword-adjacent, kept out of build_query's kwargs.
    if from_ is not None:
        params["from"] = from_
    if to is not None:
        params["to"] = to
    return params


class AnalyticsResource:
    """Synchronous ``opa.analytics`` resource."""

    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def query(
        self,
        *,
        from_: str,
        to: str,
        link_id: Optional[str] = None,
        country: Optional[str] = None,
        device: Optional[str] = None,
        os: Optional[str] = None,
        browser: Optional[str] = None,
        referer_domain: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        variant_url: Optional[str] = None,
        domain: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> AnalyticsSummary:
        """Total and unique clicks for a date range (max 366 days), optionally
        filtered by link, geo, device, or UTM fields. ``from_``/``to`` are
        required ISO dates."""
        params = _query_params(
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
        response = self._client.get(
            "/analytics/summary",
            params=params,
            headers=request_headers(options),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return AnalyticsSummary.model_validate(response.json()["data"])

    def timeseries(
        self,
        *,
        from_: str,
        to: str,
        link_id: Optional[str] = None,
        country: Optional[str] = None,
        device: Optional[str] = None,
        os: Optional[str] = None,
        browser: Optional[str] = None,
        referer_domain: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        variant_url: Optional[str] = None,
        domain: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> AnalyticsTimeseries:
        """Daily click counts across the same filters as :meth:`query`."""
        params = _query_params(
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
        response = self._client.get(
            "/analytics/timeseries",
            params=params,
            headers=request_headers(options),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return AnalyticsTimeseries.model_validate(response.json()["data"])

    def events(
        self,
        *,
        limit: int = 20,
        before: Optional[str] = None,
        link_id: Optional[str] = None,
        country: Optional[str] = None,
        device: Optional[str] = None,
        os: Optional[str] = None,
        browser: Optional[str] = None,
        referer_domain: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        variant_url: Optional[str] = None,
        domain: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> Page[AnalyticsEvent]:
        """Raw click events, newest first. Single page — see :meth:`events_all`."""
        params = build_query(
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
        response = self._client.get(
            "/analytics/events",
            params=params,
            headers=request_headers(options),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        data = response.json()["data"]
        return Page[AnalyticsEvent](
            items=[AnalyticsEvent.model_validate(item) for item in data["items"]],
            has_more=data["pagination"]["hasMore"],
            next_cursor=data["pagination"]["next"],
        )

    def events_all(
        self,
        *,
        limit: int = 20,
        link_id: Optional[str] = None,
        country: Optional[str] = None,
        device: Optional[str] = None,
        os: Optional[str] = None,
        browser: Optional[str] = None,
        referer_domain: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        variant_url: Optional[str] = None,
        domain: Optional[str] = None,
    ) -> Iterator[AnalyticsEvent]:
        """Iterates through every raw click event, auto-paginating. Memory-safe."""

        def fetch_page(cursor: str) -> Page[AnalyticsEvent]:
            return self.events(
                limit=limit,
                before=cursor or None,
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

        return paginate(fetch_page)


class AsyncAnalyticsResource:
    """Async equivalent of :class:`AnalyticsResource` — every method is ``async def``."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client

    async def query(
        self,
        *,
        from_: str,
        to: str,
        link_id: Optional[str] = None,
        country: Optional[str] = None,
        device: Optional[str] = None,
        os: Optional[str] = None,
        browser: Optional[str] = None,
        referer_domain: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        variant_url: Optional[str] = None,
        domain: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> AnalyticsSummary:
        params = _query_params(
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
        response = await self._client.get(
            "/analytics/summary",
            params=params,
            headers=request_headers(options),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return AnalyticsSummary.model_validate(response.json()["data"])

    async def timeseries(
        self,
        *,
        from_: str,
        to: str,
        link_id: Optional[str] = None,
        country: Optional[str] = None,
        device: Optional[str] = None,
        os: Optional[str] = None,
        browser: Optional[str] = None,
        referer_domain: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        variant_url: Optional[str] = None,
        domain: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> AnalyticsTimeseries:
        params = _query_params(
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
        response = await self._client.get(
            "/analytics/timeseries",
            params=params,
            headers=request_headers(options),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return AnalyticsTimeseries.model_validate(response.json()["data"])

    async def events(
        self,
        *,
        limit: int = 20,
        before: Optional[str] = None,
        link_id: Optional[str] = None,
        country: Optional[str] = None,
        device: Optional[str] = None,
        os: Optional[str] = None,
        browser: Optional[str] = None,
        referer_domain: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        variant_url: Optional[str] = None,
        domain: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> Page[AnalyticsEvent]:
        params = build_query(
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
        response = await self._client.get(
            "/analytics/events",
            params=params,
            headers=request_headers(options),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        data = response.json()["data"]
        return Page[AnalyticsEvent](
            items=[AnalyticsEvent.model_validate(item) for item in data["items"]],
            has_more=data["pagination"]["hasMore"],
            next_cursor=data["pagination"]["next"],
        )

    def events_all(
        self,
        *,
        limit: int = 20,
        link_id: Optional[str] = None,
        country: Optional[str] = None,
        device: Optional[str] = None,
        os: Optional[str] = None,
        browser: Optional[str] = None,
        referer_domain: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        variant_url: Optional[str] = None,
        domain: Optional[str] = None,
    ) -> AsyncIterator[AnalyticsEvent]:
        """Iterates through every raw click event, auto-paginating. ``async for`` this."""

        async def fetch_page(cursor: str) -> Page[AnalyticsEvent]:
            return await self.events(
                limit=limit,
                before=cursor or None,
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

        return apaginate(fetch_page)
