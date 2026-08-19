import httpx
import pytest
import respx

from opa_sh import OpaClient
from opa_sh.errors import ValidationError

SUMMARY_JSON = {
    "range": {"from": "2026-01-01", "to": "2026-01-31"},
    "clamped": False,
    "clicks": 120,
    "uniqueClicks": 88,
}

TIMESERIES_JSON = {
    "range": {"from": "2026-01-01", "to": "2026-01-31"},
    "clamped": False,
    "points": [{"date": "2026-01-01", "clicks": 4}, {"date": "2026-01-02", "clicks": 6}],
}

EVENT_JSON = {
    "timestamp": "2026-01-01T12:00:00Z",
    "linkId": "lnk_1",
    "country": "BR",
    "city": "São Paulo",
    "device": "mobile",
    "os": "iOS",
    "browser": "Safari",
    "refererDomain": "google.com",
    "refererUrl": "https://google.com/search",
    "utmSource": "newsletter",
    "utmCampaign": "q1",
    "variantUrl": "",
    "clickId": "clk_1",
}


@pytest.fixture
def opa(mock_api: respx.MockRouter) -> OpaClient:
    return OpaClient(api_key="test_key")


def test_summary(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    route = mock_api.get("/analytics/summary").mock(
        return_value=httpx.Response(200, json={"data": SUMMARY_JSON})
    )
    summary = opa.analytics.summary(from_="2026-01-01", to="2026-01-31")
    assert summary.clicks == 120
    assert summary.unique_clicks == 88
    assert summary.range.from_ == "2026-01-01"
    sent_params = route.calls.last.request.url.params
    assert sent_params["from"] == "2026-01-01"
    assert sent_params["to"] == "2026-01-31"


def test_summary_with_filters(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    route = mock_api.get("/analytics/summary").mock(
        return_value=httpx.Response(200, json={"data": SUMMARY_JSON})
    )
    opa.analytics.summary(from_="2026-01-01", to="2026-01-31", link_id="lnk_1", country="BR")
    params = route.calls.last.request.url.params
    assert params["linkId"] == "lnk_1"
    assert params["country"] == "BR"


def test_summary_missing_range_is_validation_error(
    mock_api: respx.MockRouter, opa: OpaClient
) -> None:
    mock_api.get("/analytics/summary").mock(
        return_value=httpx.Response(
            422,
            json={
                "error": {
                    "code": "validation_error",
                    "message": "from is required",
                }
            },
        )
    )
    with pytest.raises(ValidationError):
        opa.analytics.summary(from_="", to="")


def test_timeseries(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.get("/analytics/timeseries").mock(
        return_value=httpx.Response(200, json={"data": TIMESERIES_JSON})
    )
    ts = opa.analytics.timeseries(from_="2026-01-01", to="2026-01-31")
    assert len(ts.points) == 2
    assert ts.points[0].date == "2026-01-01"
    assert ts.points[0].clicks == 4


def test_events_single_page(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.get("/analytics/events").mock(
        return_value=httpx.Response(
            200,
            json={"data": {"items": [EVENT_JSON], "pagination": {"hasMore": False, "next": None}}},
        )
    )
    page = opa.analytics.events()
    assert len(page.items) == 1
    assert page.items[0].link_id == "lnk_1"
    assert page.items[0].click_id == "clk_1"


def test_events_all_auto_paginates(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    page1 = {
        "data": {
            "items": [EVENT_JSON],
            "pagination": {"hasMore": True, "next": "clk_1"},
        }
    }
    page2 = {
        "data": {
            "items": [{**EVENT_JSON, "clickId": "clk_2"}],
            "pagination": {"hasMore": False, "next": None},
        }
    }
    call_count = {"n": 0}

    def responder(request: httpx.Request) -> httpx.Response:
        call_count["n"] += 1
        return httpx.Response(200, json=page1 if call_count["n"] == 1 else page2)

    mock_api.get("/analytics/events").mock(side_effect=responder)

    click_ids = [event.click_id for event in opa.analytics.events_all()]
    assert click_ids == ["clk_1", "clk_2"]


@pytest.mark.asyncio
async def test_async_summary(mock_api: respx.MockRouter) -> None:
    from opa_sh import AsyncOpaClient

    route = mock_api.get("/analytics/summary").mock(
        return_value=httpx.Response(200, json={"data": SUMMARY_JSON})
    )
    async with AsyncOpaClient(api_key="test_key") as opa_async:
        summary = await opa_async.analytics.summary(from_="2026-01-01", to="2026-01-31")
    assert summary.clicks == 120
    assert summary.unique_clicks == 88
    sent_params = route.calls.last.request.url.params
    assert sent_params["from"] == "2026-01-01"
    assert sent_params["to"] == "2026-01-31"


@pytest.mark.asyncio
async def test_async_timeseries(mock_api: respx.MockRouter) -> None:
    from opa_sh import AsyncOpaClient

    mock_api.get("/analytics/timeseries").mock(
        return_value=httpx.Response(200, json={"data": TIMESERIES_JSON})
    )
    async with AsyncOpaClient(api_key="test_key") as opa_async:
        ts = await opa_async.analytics.timeseries(from_="2026-01-01", to="2026-01-31")
    assert len(ts.points) == 2


@pytest.mark.asyncio
async def test_async_events_all_auto_paginates(mock_api: respx.MockRouter) -> None:
    from opa_sh import AsyncOpaClient

    page1 = {
        "data": {
            "items": [EVENT_JSON],
            "pagination": {"hasMore": True, "next": "clk_1"},
        }
    }
    page2 = {
        "data": {
            "items": [{**EVENT_JSON, "clickId": "clk_2"}],
            "pagination": {"hasMore": False, "next": None},
        }
    }
    call_count = {"n": 0}

    def responder(request: httpx.Request) -> httpx.Response:
        call_count["n"] += 1
        return httpx.Response(200, json=page1 if call_count["n"] == 1 else page2)

    mock_api.get("/analytics/events").mock(side_effect=responder)

    async with AsyncOpaClient(api_key="test_key") as opa_async:
        click_ids = [event.click_id async for event in opa_async.analytics.events_all()]
    assert click_ids == ["clk_1", "clk_2"]
