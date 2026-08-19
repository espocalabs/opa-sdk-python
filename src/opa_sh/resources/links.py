"""``opa.links`` — create, read, update, archive/restore and bulk-manage short links."""

import builtins
from collections.abc import AsyncIterator, Iterator
from typing import Optional

import httpx

from .._internal.request_options import RequestOptions, request_timeout
from .._internal.serialize import build_body, build_query
from ..errors import raise_for_response
from ..models import (
    ArchiveLinkResult,
    BulkArchiveResult,
    BulkMoveResult,
    BulkRestoreResult,
    BulkTagResult,
    Link,
    LinkSummary,
    LinkTargeting,
    Page,
    QrSettings,
    RestoreLinkResult,
)
from ..pagination import apaginate, paginate


class LinksResource:
    """Synchronous ``opa.links`` resource."""

    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def list(
        self,
        *,
        limit: int = 20,
        after: Optional[str] = None,
        before: Optional[str] = None,
        search: Optional[str] = None,
        archived: Optional[bool] = None,
        options: Optional[RequestOptions] = None,
    ) -> Page[LinkSummary]:
        """Lists links, newest first. Single page — see :meth:`list_all` to walk every page."""
        params = build_query(
            limit=limit, after=after, before=before, search=search, archived=archived
        )
        response = self._client.get(
            "/links",
            params=params,
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        data = response.json()["data"]
        return Page[LinkSummary](
            items=[LinkSummary.model_validate(item) for item in data["items"]],
            has_more=data["pagination"]["hasMore"],
            next_cursor=data["pagination"]["next"],
        )

    def list_all(
        self,
        *,
        limit: int = 20,
        search: Optional[str] = None,
        archived: Optional[bool] = None,
    ) -> Iterator[LinkSummary]:
        """Iterates through every link, auto-paginating. Memory-safe."""

        def fetch_page(cursor: str) -> Page[LinkSummary]:
            return self.list(limit=limit, after=cursor or None, search=search, archived=archived)

        return paginate(fetch_page)

    def get(self, link_id: str, *, options: Optional[RequestOptions] = None) -> Link:
        """Fetches a single link by id."""
        response = self._client.get(f"/links/{link_id}", timeout=request_timeout(options))
        raise_for_response(response)
        return Link.model_validate(response.json()["data"])

    def create(
        self,
        *,
        destination_url: str,
        domain: Optional[str] = None,
        key: Optional[str] = None,
        folder_id: Optional[str] = None,
        tag_ids: Optional[builtins.list[str]] = None,
        utm_template_id: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        utm_term: Optional[str] = None,
        utm_content: Optional[str] = None,
        utm_referral: Optional[str] = None,
        comments: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        expires_at: Optional[str] = None,
        expired_url: Optional[str] = None,
        do_index: Optional[bool] = None,
        password: Optional[str] = None,
        test_variants: Optional[str] = None,
        test_completed_at: Optional[str] = None,
        targeting: Optional[LinkTargeting] = None,
        qr_settings: Optional[QrSettings] = None,
        options: Optional[RequestOptions] = None,
    ) -> Link:
        """Creates a link. Only ``destination_url`` is required — ``domain``
        defaults to the team's primary custom domain, else the app's default
        short domain."""
        body = build_body(
            destination_url=destination_url,
            domain=domain,
            key=key,
            folder_id=folder_id,
            tag_ids=tag_ids,
            utm_template_id=utm_template_id,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            utm_referral=utm_referral,
            comments=comments,
            title=title,
            description=description,
            image_url=image_url,
            expires_at=expires_at,
            expired_url=expired_url,
            do_index=do_index,
            password=password,
            test_variants=test_variants,
            test_completed_at=test_completed_at,
            targeting=targeting,
            qr_settings=qr_settings,
        )
        response = self._client.post(
            "/links",
            json=body,
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return Link.model_validate(response.json()["data"])

    def update(
        self,
        link_id: str,
        *,
        destination_url: str,
        domain: str,
        folder_id: Optional[str] = None,
        tag_ids: Optional[builtins.list[str]] = None,
        utm_template_id: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        utm_term: Optional[str] = None,
        utm_content: Optional[str] = None,
        utm_referral: Optional[str] = None,
        comments: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        expires_at: Optional[str] = None,
        expired_url: Optional[str] = None,
        do_index: Optional[bool] = None,
        password: Optional[str] = None,
        clear_password: Optional[bool] = None,
        test_variants: Optional[str] = None,
        test_completed_at: Optional[str] = None,
        targeting: Optional[LinkTargeting] = None,
        qr_settings: Optional[QrSettings] = None,
        options: Optional[RequestOptions] = None,
    ) -> Link:
        """Full-payload update. ``destination_url`` and ``domain`` are
        required by the API (it's a full replace, not a merge patch) — every
        other field keeps its current value when omitted."""
        body = build_body(
            destination_url=destination_url,
            domain=domain,
            folder_id=folder_id,
            tag_ids=tag_ids,
            utm_template_id=utm_template_id,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            utm_referral=utm_referral,
            comments=comments,
            title=title,
            description=description,
            image_url=image_url,
            expires_at=expires_at,
            expired_url=expired_url,
            do_index=do_index,
            password=password,
            clear_password=clear_password,
            test_variants=test_variants,
            test_completed_at=test_completed_at,
            targeting=targeting,
            qr_settings=qr_settings,
        )
        response = self._client.patch(
            f"/links/{link_id}",
            json=body,
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return Link.model_validate(response.json()["data"])

    def archive(
        self, link_id: str, *, options: Optional[RequestOptions] = None
    ) -> ArchiveLinkResult:
        """Archives a link (reversible with :meth:`restore`). The link keeps resolving."""
        response = self._client.delete(f"/links/{link_id}", timeout=request_timeout(options))
        raise_for_response(response)
        return ArchiveLinkResult.model_validate(response.json()["data"])

    def restore(
        self, link_id: str, *, options: Optional[RequestOptions] = None
    ) -> RestoreLinkResult:
        """Un-archives a link."""
        response = self._client.post(
            f"/links/{link_id}/restore",
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return RestoreLinkResult.model_validate(response.json()["data"])

    def duplicate(self, link_id: str, *, options: Optional[RequestOptions] = None) -> Link:
        """Duplicates a link, returning the newly created copy in full detail."""
        response = self._client.post(
            f"/links/{link_id}/duplicate",
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return Link.model_validate(response.json()["data"])

    def bulk_archive(
        self, link_ids: builtins.list[str], *, options: Optional[RequestOptions] = None
    ) -> BulkArchiveResult:
        """Archives up to the given set of links in one call."""
        response = self._client.post(
            "/links/bulk/archive",
            json={"linkIds": link_ids},
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return BulkArchiveResult.model_validate(response.json()["data"])

    def bulk_restore(
        self, link_ids: builtins.list[str], *, options: Optional[RequestOptions] = None
    ) -> BulkRestoreResult:
        """Restores a set of previously archived links in one call."""
        response = self._client.post(
            "/links/bulk/restore",
            json={"linkIds": link_ids},
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return BulkRestoreResult.model_validate(response.json()["data"])

    def bulk_move(
        self,
        link_ids: builtins.list[str],
        folder_id: str,
        *,
        options: Optional[RequestOptions] = None,
    ) -> BulkMoveResult:
        """Moves a set of links into a folder in one call."""
        response = self._client.post(
            "/links/bulk/move",
            json={"linkIds": link_ids, "folderId": folder_id},
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return BulkMoveResult.model_validate(response.json()["data"])

    def bulk_tag(
        self,
        link_ids: builtins.list[str],
        tag_ids: builtins.list[str],
        *,
        options: Optional[RequestOptions] = None,
    ) -> BulkTagResult:
        """Adds a set of tags to a set of links in one call."""
        response = self._client.post(
            "/links/bulk/tag",
            json={"linkIds": link_ids, "tagIds": tag_ids},
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return BulkTagResult.model_validate(response.json()["data"])


class AsyncLinksResource:
    """Async equivalent of :class:`LinksResource` — every method is ``async def``."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        limit: int = 20,
        after: Optional[str] = None,
        before: Optional[str] = None,
        search: Optional[str] = None,
        archived: Optional[bool] = None,
        options: Optional[RequestOptions] = None,
    ) -> Page[LinkSummary]:
        params = build_query(
            limit=limit, after=after, before=before, search=search, archived=archived
        )
        response = await self._client.get(
            "/links",
            params=params,
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        data = response.json()["data"]
        return Page[LinkSummary](
            items=[LinkSummary.model_validate(item) for item in data["items"]],
            has_more=data["pagination"]["hasMore"],
            next_cursor=data["pagination"]["next"],
        )

    def list_all(
        self,
        *,
        limit: int = 20,
        search: Optional[str] = None,
        archived: Optional[bool] = None,
    ) -> AsyncIterator[LinkSummary]:
        """Iterates through every link, auto-paginating. ``async for`` this."""

        async def fetch_page(cursor: str) -> Page[LinkSummary]:
            return await self.list(
                limit=limit, after=cursor or None, search=search, archived=archived
            )

        return apaginate(fetch_page)

    async def get(self, link_id: str, *, options: Optional[RequestOptions] = None) -> Link:
        response = await self._client.get(f"/links/{link_id}", timeout=request_timeout(options))
        raise_for_response(response)
        return Link.model_validate(response.json()["data"])

    async def create(
        self,
        *,
        destination_url: str,
        domain: Optional[str] = None,
        key: Optional[str] = None,
        folder_id: Optional[str] = None,
        tag_ids: Optional[builtins.list[str]] = None,
        utm_template_id: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        utm_term: Optional[str] = None,
        utm_content: Optional[str] = None,
        utm_referral: Optional[str] = None,
        comments: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        expires_at: Optional[str] = None,
        expired_url: Optional[str] = None,
        do_index: Optional[bool] = None,
        password: Optional[str] = None,
        test_variants: Optional[str] = None,
        test_completed_at: Optional[str] = None,
        targeting: Optional[LinkTargeting] = None,
        qr_settings: Optional[QrSettings] = None,
        options: Optional[RequestOptions] = None,
    ) -> Link:
        body = build_body(
            destination_url=destination_url,
            domain=domain,
            key=key,
            folder_id=folder_id,
            tag_ids=tag_ids,
            utm_template_id=utm_template_id,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            utm_referral=utm_referral,
            comments=comments,
            title=title,
            description=description,
            image_url=image_url,
            expires_at=expires_at,
            expired_url=expired_url,
            do_index=do_index,
            password=password,
            test_variants=test_variants,
            test_completed_at=test_completed_at,
            targeting=targeting,
            qr_settings=qr_settings,
        )
        response = await self._client.post(
            "/links",
            json=body,
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return Link.model_validate(response.json()["data"])

    async def update(
        self,
        link_id: str,
        *,
        destination_url: str,
        domain: str,
        folder_id: Optional[str] = None,
        tag_ids: Optional[builtins.list[str]] = None,
        utm_template_id: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        utm_term: Optional[str] = None,
        utm_content: Optional[str] = None,
        utm_referral: Optional[str] = None,
        comments: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        expires_at: Optional[str] = None,
        expired_url: Optional[str] = None,
        do_index: Optional[bool] = None,
        password: Optional[str] = None,
        clear_password: Optional[bool] = None,
        test_variants: Optional[str] = None,
        test_completed_at: Optional[str] = None,
        targeting: Optional[LinkTargeting] = None,
        qr_settings: Optional[QrSettings] = None,
        options: Optional[RequestOptions] = None,
    ) -> Link:
        body = build_body(
            destination_url=destination_url,
            domain=domain,
            folder_id=folder_id,
            tag_ids=tag_ids,
            utm_template_id=utm_template_id,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            utm_referral=utm_referral,
            comments=comments,
            title=title,
            description=description,
            image_url=image_url,
            expires_at=expires_at,
            expired_url=expired_url,
            do_index=do_index,
            password=password,
            clear_password=clear_password,
            test_variants=test_variants,
            test_completed_at=test_completed_at,
            targeting=targeting,
            qr_settings=qr_settings,
        )
        response = await self._client.patch(
            f"/links/{link_id}",
            json=body,
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return Link.model_validate(response.json()["data"])

    async def archive(
        self, link_id: str, *, options: Optional[RequestOptions] = None
    ) -> ArchiveLinkResult:
        response = await self._client.delete(f"/links/{link_id}", timeout=request_timeout(options))
        raise_for_response(response)
        return ArchiveLinkResult.model_validate(response.json()["data"])

    async def restore(
        self, link_id: str, *, options: Optional[RequestOptions] = None
    ) -> RestoreLinkResult:
        response = await self._client.post(
            f"/links/{link_id}/restore",
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return RestoreLinkResult.model_validate(response.json()["data"])

    async def duplicate(self, link_id: str, *, options: Optional[RequestOptions] = None) -> Link:
        response = await self._client.post(
            f"/links/{link_id}/duplicate",
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return Link.model_validate(response.json()["data"])

    async def bulk_archive(
        self, link_ids: builtins.list[str], *, options: Optional[RequestOptions] = None
    ) -> BulkArchiveResult:
        response = await self._client.post(
            "/links/bulk/archive",
            json={"linkIds": link_ids},
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return BulkArchiveResult.model_validate(response.json()["data"])

    async def bulk_restore(
        self, link_ids: builtins.list[str], *, options: Optional[RequestOptions] = None
    ) -> BulkRestoreResult:
        response = await self._client.post(
            "/links/bulk/restore",
            json={"linkIds": link_ids},
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return BulkRestoreResult.model_validate(response.json()["data"])

    async def bulk_move(
        self,
        link_ids: builtins.list[str],
        folder_id: str,
        *,
        options: Optional[RequestOptions] = None,
    ) -> BulkMoveResult:
        response = await self._client.post(
            "/links/bulk/move",
            json={"linkIds": link_ids, "folderId": folder_id},
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return BulkMoveResult.model_validate(response.json()["data"])

    async def bulk_tag(
        self,
        link_ids: builtins.list[str],
        tag_ids: builtins.list[str],
        *,
        options: Optional[RequestOptions] = None,
    ) -> BulkTagResult:
        response = await self._client.post(
            "/links/bulk/tag",
            json={"linkIds": link_ids, "tagIds": tag_ids},
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return BulkTagResult.model_validate(response.json()["data"])
