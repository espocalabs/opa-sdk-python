import httpx
import pytest
import respx

from opa_sh import LinkTargeting, OpaClient, QrSettings
from opa_sh.errors import NotFoundError, ValidationError

LINK_JSON = {
    "id": "lnk_1",
    "domain": "opa.sh",
    "key": "abc123",
    "shortLink": "https://opa.sh/abc123",
    "destinationUrl": "https://example.com",
    "title": None,
    "description": None,
    "imageUrl": None,
    "comments": None,
    "folderId": "",
    "tagIds": [],
    "utmTemplateId": None,
    "utmSource": None,
    "utmMedium": None,
    "utmCampaign": None,
    "utmTerm": None,
    "utmContent": None,
    "utmReferral": None,
    "expiresAt": None,
    "expiredUrl": None,
    "doIndex": False,
    "hasPassword": False,
    "testVariantsCount": 0,
    "testCompletedAt": None,
    "targeting": None,
    "qrSettings": None,
}

LINK_SUMMARY_JSON = {
    "id": "lnk_1",
    "domain": "opa.sh",
    "key": "abc123",
    "shortLink": "https://opa.sh/abc123",
    "destinationUrl": "https://example.com",
    "title": None,
    "description": None,
    "imageUrl": None,
    "comments": None,
    "createdAt": "2026-01-01T00:00:00Z",
    "expiresAt": None,
    "disabledAt": None,
    "testCompletedAt": None,
    "testVariantsCount": 0,
    "qrSettings": None,
    "folder": None,
    "tags": [{"id": "tag_1", "name": "marketing", "color": "#fff"}],
}


@pytest.fixture
def opa(mock_api: respx.MockRouter) -> OpaClient:
    return OpaClient(api_key="test_key")


def test_create_link(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    route = mock_api.post("/links").mock(return_value=httpx.Response(201, json={"data": LINK_JSON}))
    link = opa.links.create(destination_url="https://example.com", domain="opa.sh")
    assert link.id == "lnk_1"
    assert link.short_link == "https://opa.sh/abc123"
    assert link.destination_url == "https://example.com"
    sent_body = route.calls.last.request.content
    assert b"destinationUrl" in sent_body
    assert b"domain" in sent_body


def test_create_link_omits_none_fields(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    import json

    route = mock_api.post("/links").mock(return_value=httpx.Response(201, json={"data": LINK_JSON}))
    opa.links.create(destination_url="https://example.com")
    body = json.loads(route.calls.last.request.content)
    assert body == {"destinationUrl": "https://example.com"}


def test_create_link_serializes_targeting_and_qr_settings_as_json_strings(
    mock_api: respx.MockRouter, opa: OpaClient
) -> None:
    """Regression test: the API's request schema (unlike its response
    schema) declares `targeting`/`qrSettings` as JSON-encoded *strings*,
    not nested objects — confirmed against the live API, which 422s with
    "expected string, received object" if you send the raw object. See
    `_internal/serialize.py::build_body`."""
    import json

    route = mock_api.post("/links").mock(return_value=httpx.Response(201, json={"data": LINK_JSON}))
    opa.links.create(
        destination_url="https://example.com",
        targeting=LinkTargeting(ios="https://apps.apple.com/app/example"),
        qr_settings=QrSettings(foreground_color="#000000"),
    )
    body = json.loads(route.calls.last.request.content)
    assert isinstance(body["targeting"], str)
    assert json.loads(body["targeting"]) == {"ios": "https://apps.apple.com/app/example"}
    assert isinstance(body["qrSettings"], str)
    assert json.loads(body["qrSettings"]) == {"foregroundColor": "#000000"}


def test_update_link_serializes_targeting_and_qr_settings_as_json_strings(
    mock_api: respx.MockRouter, opa: OpaClient
) -> None:
    import json

    route = mock_api.patch("/links/lnk_1").mock(
        return_value=httpx.Response(200, json={"data": LINK_JSON})
    )
    opa.links.update(
        "lnk_1",
        destination_url="https://example.com",
        domain="opa.sh",
        targeting=LinkTargeting(android="https://play.google.com/store/apps/details?id=com.example"),
        qr_settings=QrSettings(error_correction_level="H"),
    )
    body = json.loads(route.calls.last.request.content)
    assert isinstance(body["targeting"], str)
    assert json.loads(body["targeting"]) == {
        "android": "https://play.google.com/store/apps/details?id=com.example"
    }
    assert isinstance(body["qrSettings"], str)
    assert json.loads(body["qrSettings"]) == {"errorCorrectionLevel": "H"}


def test_get_link(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.get("/links/lnk_1").mock(return_value=httpx.Response(200, json={"data": LINK_JSON}))
    link = opa.links.get("lnk_1")
    assert link.id == "lnk_1"


def test_get_link_not_found(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.get("/links/missing").mock(
        return_value=httpx.Response(
            404, json={"error": {"code": "not_found", "message": "Link not found."}}
        )
    )
    with pytest.raises(NotFoundError):
        opa.links.get("missing")


def test_create_link_validation_error(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.post("/links").mock(
        return_value=httpx.Response(
            422,
            json={
                "error": {
                    "code": "validation_error",
                    "message": "The request did not pass validation.",
                    "issues": [{"path": "destinationUrl", "message": "Required"}],
                }
            },
        )
    )
    with pytest.raises(ValidationError):
        opa.links.create(destination_url="not-a-url")


def test_update_link(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    updated = {**LINK_JSON, "destinationUrl": "https://example.com/new"}
    mock_api.patch("/links/lnk_1").mock(return_value=httpx.Response(200, json={"data": updated}))
    link = opa.links.update("lnk_1", destination_url="https://example.com/new", domain="opa.sh")
    assert link.destination_url == "https://example.com/new"


def test_archive_link(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.delete("/links/lnk_1").mock(
        return_value=httpx.Response(200, json={"data": {"id": "lnk_1", "archived": True}})
    )
    result = opa.links.archive("lnk_1")
    assert result.id == "lnk_1"
    assert result.archived is True


def test_restore_link(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.post("/links/lnk_1/restore").mock(
        return_value=httpx.Response(200, json={"data": {"id": "lnk_1", "archived": False}})
    )
    result = opa.links.restore("lnk_1")
    assert result.archived is False


def test_duplicate_link(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    duplicated = {**LINK_JSON, "id": "lnk_2", "key": "xyz789"}
    mock_api.post("/links/lnk_1/duplicate").mock(
        return_value=httpx.Response(201, json={"data": duplicated})
    )
    link = opa.links.duplicate("lnk_1")
    assert link.id == "lnk_2"


def test_list_links_single_page(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.get("/links").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": {
                    "items": [LINK_SUMMARY_JSON],
                    "pagination": {"hasMore": False, "next": None, "before": None},
                }
            },
        )
    )
    page = opa.links.list()
    assert len(page.items) == 1
    assert page.items[0].id == "lnk_1"
    assert page.items[0].tags[0].name == "marketing"
    assert page.has_more is False
    assert page.next_cursor is None


def test_list_all_links_auto_paginates(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    page1 = {
        "data": {
            "items": [LINK_SUMMARY_JSON],
            "pagination": {"hasMore": True, "next": "lnk_1", "before": None},
        }
    }
    page2_summary = {**LINK_SUMMARY_JSON, "id": "lnk_2"}
    page2 = {
        "data": {
            "items": [page2_summary],
            "pagination": {"hasMore": False, "next": None, "before": None},
        }
    }

    call_count = {"n": 0}

    def responder(request: httpx.Request) -> httpx.Response:
        call_count["n"] += 1
        return httpx.Response(200, json=page1 if call_count["n"] == 1 else page2)

    mock_api.get("/links").mock(side_effect=responder)

    ids = [link.id for link in opa.links.list_all()]
    assert ids == ["lnk_1", "lnk_2"]
    assert call_count["n"] == 2


def test_bulk_archive(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.post("/links/bulk/archive").mock(
        return_value=httpx.Response(200, json={"data": {"archivedCount": 2}})
    )
    result = opa.links.bulk_archive(["lnk_1", "lnk_2"])
    assert result.archived_count == 2


def test_bulk_restore(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.post("/links/bulk/restore").mock(
        return_value=httpx.Response(200, json={"data": {"restoredCount": 2}})
    )
    result = opa.links.bulk_restore(["lnk_1", "lnk_2"])
    assert result.restored_count == 2


def test_bulk_move(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.post("/links/bulk/move").mock(
        return_value=httpx.Response(200, json={"data": {"movedCount": 3}})
    )
    result = opa.links.bulk_move(["lnk_1", "lnk_2", "lnk_3"], "folder_1")
    assert result.moved_count == 3


def test_bulk_tag(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    mock_api.post("/links/bulk/tag").mock(
        return_value=httpx.Response(200, json={"data": {"taggedCount": 1}})
    )
    result = opa.links.bulk_tag(["lnk_1"], ["tag_1"])
    assert result.tagged_count == 1


def test_request_options_timeout_override(mock_api: respx.MockRouter, opa: OpaClient) -> None:
    from opa_sh import RequestOptions

    route = mock_api.post("/links").mock(return_value=httpx.Response(201, json={"data": LINK_JSON}))
    link = opa.links.create(
        destination_url="https://example.com",
        options=RequestOptions(timeout=5.0),
    )
    assert route.called
    assert link.id == "lnk_1"


@pytest.mark.asyncio
async def test_async_create_and_get_link(mock_api: respx.MockRouter) -> None:
    from opa_sh import AsyncOpaClient

    mock_api.post("/links").mock(return_value=httpx.Response(201, json={"data": LINK_JSON}))
    mock_api.get("/links/lnk_1").mock(return_value=httpx.Response(200, json={"data": LINK_JSON}))

    async with AsyncOpaClient(api_key="test_key") as opa_async:
        created = await opa_async.links.create(destination_url="https://example.com")
        fetched = await opa_async.links.get("lnk_1")
    assert created.id == fetched.id == "lnk_1"


@pytest.mark.asyncio
async def test_async_bulk_operations(mock_api: respx.MockRouter) -> None:
    from opa_sh import AsyncOpaClient

    mock_api.post("/links/bulk/archive").mock(
        return_value=httpx.Response(200, json={"data": {"archivedCount": 2}})
    )
    mock_api.post("/links/bulk/restore").mock(
        return_value=httpx.Response(200, json={"data": {"restoredCount": 2}})
    )
    mock_api.post("/links/bulk/move").mock(
        return_value=httpx.Response(200, json={"data": {"movedCount": 3}})
    )
    mock_api.post("/links/bulk/tag").mock(
        return_value=httpx.Response(200, json={"data": {"taggedCount": 1}})
    )

    async with AsyncOpaClient(api_key="test_key") as opa_async:
        archived = await opa_async.links.bulk_archive(["lnk_1", "lnk_2"])
        restored = await opa_async.links.bulk_restore(["lnk_1", "lnk_2"])
        moved = await opa_async.links.bulk_move(["lnk_1", "lnk_2", "lnk_3"], "folder_1")
        tagged = await opa_async.links.bulk_tag(["lnk_1"], ["tag_1"])

    assert archived.archived_count == 2
    assert restored.restored_count == 2
    assert moved.moved_count == 3
    assert tagged.tagged_count == 1


@pytest.mark.asyncio
async def test_async_list_all_links_auto_paginates(mock_api: respx.MockRouter) -> None:
    from opa_sh import AsyncOpaClient

    page1 = {
        "data": {
            "items": [LINK_SUMMARY_JSON],
            "pagination": {"hasMore": True, "next": "lnk_1", "before": None},
        }
    }
    page2 = {
        "data": {
            "items": [{**LINK_SUMMARY_JSON, "id": "lnk_2"}],
            "pagination": {"hasMore": False, "next": None, "before": None},
        }
    }
    call_count = {"n": 0}

    def responder(request: httpx.Request) -> httpx.Response:
        call_count["n"] += 1
        return httpx.Response(200, json=page1 if call_count["n"] == 1 else page2)

    mock_api.get("/links").mock(side_effect=responder)

    async with AsyncOpaClient(api_key="test_key") as opa_async:
        ids = [link.id async for link in opa_async.links.list_all()]
    assert ids == ["lnk_1", "lnk_2"]
