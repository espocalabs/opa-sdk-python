"""Pydantic v2 models for the Opa API.

Hand-written (not generated) for clean, idiomatic Python names — the raw
OpenAPI spec has no named component schemas (everything is inline), so a
mechanical generator produces synthetic names like
``GetLinksIdResponse200Data``. These models mirror the same JSON shapes
using ``snake_case`` attributes with ``camelCase`` aliases, so a field
like ``destinationUrl`` in an API response becomes ``link.destination_url``
here.

The API's JSON shapes are the source of truth. When
``openapi/v1.json`` changes, update these models to match — the
``_generated/`` package (see ``opa_sh._generated``) is regenerated
automatically by the ``sync-openapi`` CI workflow and is useful as a diff
target for spotting shape changes, even though it isn't imported at
runtime.
"""

from typing import Generic, Literal, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

__all__ = [
    "OpaModel",
    "Tag",
    "Folder",
    "QrSettings",
    "LinkTargeting",
    "Link",
    "LinkSummary",
    "Domain",
    "AnalyticsRange",
    "AnalyticsSummary",
    "AnalyticsTimeseriesPoint",
    "AnalyticsTimeseries",
    "AnalyticsEvent",
    "Page",
    "ArchiveLinkResult",
    "RestoreLinkResult",
    "BulkArchiveResult",
    "BulkRestoreResult",
    "BulkMoveResult",
    "BulkTagResult",
]

T = TypeVar("T")


class OpaModel(BaseModel):
    """Base class for every response model.

    Fields are declared ``snake_case``; ``alias_generator`` maps them to
    the API's ``camelCase`` JSON keys automatically. ``populate_by_name``
    lets you also construct instances with the Python (snake_case) names
    directly, which is what the SDK's own request-building code does.
    Unknown fields from newer API responses are ignored rather than
    raising, so a server-side addition never breaks a pinned SDK version.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="ignore",
    )


# --- Shared nested shapes ----------------------------------------------------


class Tag(OpaModel):
    id: str
    name: str
    color: str


class Folder(OpaModel):
    id: str
    name: str


class QrSettings(OpaModel):
    foreground_color: Optional[str] = None
    background_color: Optional[str] = None
    error_correction_level: Optional[Literal["L", "M", "Q", "H"]] = None
    logo_mode: Optional[Literal["default", "none", "custom"]] = None
    custom_logo_url: Optional[str] = None
    logo_size: Optional[int] = None
    dot_style: Optional[Literal["square", "dots", "classy"]] = None
    marker_border_style: Optional[Literal["square", "extra-rounded", "dot"]] = None
    marker_center_style: Optional[Literal["square", "dot"]] = None


class LinkTargeting(OpaModel):
    ios: Optional[str] = None
    android: Optional[str] = None
    geo: Optional["dict[str, str]"] = None


# --- Links --------------------------------------------------------------------


class Link(OpaModel):
    """Full link detail — returned by ``get``, ``create``, ``update``, ``duplicate``."""

    id: str
    domain: str
    key: str
    short_link: str
    destination_url: str
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    comments: Optional[str] = None
    folder_id: str
    tag_ids: list[str] = Field(default_factory=list)
    utm_template_id: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_campaign: Optional[str] = None
    utm_term: Optional[str] = None
    utm_content: Optional[str] = None
    utm_referral: Optional[str] = None
    expires_at: Optional[str] = None
    expired_url: Optional[str] = None
    do_index: bool = False
    has_password: bool = False
    test_variants_count: int = 0
    test_completed_at: Optional[str] = None
    targeting: Optional[LinkTargeting] = None
    qr_settings: Optional[QrSettings] = None


class LinkSummary(OpaModel):
    """Lighter shape returned by ``list`` — no targeting/QR detail."""

    id: str
    domain: str
    key: str
    short_link: str
    destination_url: str
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    comments: Optional[str] = None
    created_at: str
    expires_at: Optional[str] = None
    disabled_at: Optional[str] = None
    test_completed_at: Optional[str] = None
    test_variants_count: int = 0
    qr_settings: Optional[QrSettings] = None
    folder: Optional[Folder] = None
    tags: list[Tag] = Field(default_factory=list)


class ArchiveLinkResult(OpaModel):
    id: str
    archived: Literal[True] = True


class RestoreLinkResult(OpaModel):
    id: str
    archived: Literal[False] = False


class BulkArchiveResult(OpaModel):
    archived_count: int


class BulkRestoreResult(OpaModel):
    restored_count: int


class BulkMoveResult(OpaModel):
    moved_count: int


class BulkTagResult(OpaModel):
    tagged_count: int


# --- Domains --------------------------------------------------------------------


class Domain(OpaModel):
    """A domain usable as a link's short-link host."""

    id: str
    domain: str
    type: Literal["USER_DOMAIN", "APP_DOMAIN"]
    verified: bool
    primary: bool
    allowed_hosts: list[str] = Field(default_factory=list)


# --- Analytics --------------------------------------------------------------------


class AnalyticsRange(OpaModel):
    # `from` is a Python keyword, so the attribute is `from_` with an
    # explicit alias override (the inherited `to_camel` generator would
    # otherwise turn it into `from_` -> `from` anyway, but this is clearer).
    from_: str = Field(alias="from")
    to: str


class AnalyticsSummary(OpaModel):
    range: AnalyticsRange
    clamped: bool
    clicks: int
    unique_clicks: int


class AnalyticsTimeseriesPoint(OpaModel):
    date: str
    clicks: int


class AnalyticsTimeseries(OpaModel):
    range: AnalyticsRange
    clamped: bool
    points: list[AnalyticsTimeseriesPoint] = Field(default_factory=list)


class AnalyticsEvent(OpaModel):
    timestamp: str
    link_id: str
    country: str
    city: str
    device: str
    os: str
    browser: str
    referer_domain: str
    referer_url: str
    utm_source: str
    utm_campaign: str
    variant_url: str
    click_id: str


# --- Pagination --------------------------------------------------------------------


class Page(BaseModel, Generic[T]):
    """A single normalized page of a cursor-paginated list endpoint.

    Regardless of the underlying API's cursor parameter name (``after`` for
    links, ``before`` for analytics events), a page always exposes
    ``items``, ``has_more``, and ``next_cursor``.
    """

    items: list[T]
    has_more: bool
    next_cursor: Optional[str] = None
