"""Sanity checks that the public API surface imports and constructs cleanly.

Not exhaustive behavioral coverage (see test_links.py, test_analytics.py,
test_domains.py, test_errors.py, test_retry.py, test_pagination.py for
that) — this just guards against the package's `__init__.py` exports
drifting out of sync with what actually exists in the submodules.
"""

import opa_sh


def test_top_level_exports_exist() -> None:
    for name in [
        "OpaClient",
        "AsyncOpaClient",
        "RequestOptions",
        "DEFAULT_BASE_URL",
        "__version__",
        "OpaError",
        "AuthenticationError",
        "PermissionDeniedError",
        "NotFoundError",
        "ConflictError",
        "ValidationError",
        "RateLimitError",
        "ServerError",
        "NetworkError",
        "LinksResource",
        "AsyncLinksResource",
        "AnalyticsResource",
        "AsyncAnalyticsResource",
        "DomainsResource",
        "AsyncDomainsResource",
        "TrackResource",
        "AsyncTrackResource",
        "Link",
        "LinkSummary",
        "Domain",
        "Page",
        "IdentifyResult",
        "TrackEventResult",
        "ConversionCustomer",
        "ConversionEvent",
        "TrackConversionResult",
    ]:
        assert hasattr(opa_sh, name), f"opa_sh.{name} is missing"


def test_version_is_semver_like() -> None:
    parts = opa_sh.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


def test_error_hierarchy() -> None:
    assert issubclass(opa_sh.AuthenticationError, opa_sh.OpaError)
    assert issubclass(opa_sh.PermissionDeniedError, opa_sh.OpaError)
    assert issubclass(opa_sh.NotFoundError, opa_sh.OpaError)
    assert issubclass(opa_sh.ConflictError, opa_sh.OpaError)
    assert issubclass(opa_sh.ValidationError, opa_sh.OpaError)
    assert issubclass(opa_sh.RateLimitError, opa_sh.OpaError)
    assert issubclass(opa_sh.ServerError, opa_sh.OpaError)
    assert issubclass(opa_sh.NetworkError, opa_sh.OpaError)
    assert issubclass(opa_sh.OpaError, Exception)


def test_client_classes_expose_all_four_resources() -> None:
    opa = opa_sh.OpaClient(api_key="test_key")
    try:
        assert isinstance(opa.links, opa_sh.LinksResource)
        assert isinstance(opa.analytics, opa_sh.AnalyticsResource)
        assert isinstance(opa.domains, opa_sh.DomainsResource)
        assert isinstance(opa.track, opa_sh.TrackResource)
    finally:
        opa.close()


def test_async_client_classes_expose_all_four_resources() -> None:
    opa = opa_sh.AsyncOpaClient(api_key="test_key")
    assert isinstance(opa.links, opa_sh.AsyncLinksResource)
    assert isinstance(opa.analytics, opa_sh.AsyncAnalyticsResource)
    assert isinstance(opa.domains, opa_sh.AsyncDomainsResource)
    assert isinstance(opa.track, opa_sh.AsyncTrackResource)


def test_link_model_round_trips_camelcase_json() -> None:
    link = opa_sh.Link.model_validate(
        {
            "id": "lnk_1",
            "domain": "opa.sh",
            "key": "abc",
            "shortLink": "https://opa.sh/abc",
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
    )
    assert link.short_link == "https://opa.sh/abc"
    assert link.destination_url == "https://example.com"
    dumped = link.model_dump(by_alias=True)
    assert dumped["shortLink"] == "https://opa.sh/abc"
    assert dumped["destinationUrl"] == "https://example.com"


def test_models_ignore_unknown_fields_forward_compatibly() -> None:
    domain = opa_sh.Domain.model_validate(
        {
            "id": "dom_1",
            "domain": "opa.sh",
            "type": "APP_DOMAIN",
            "verified": True,
            "primary": True,
            "allowedHosts": [],
            "someBrandNewFieldFromTheFuture": "should not raise",
        }
    )
    assert domain.id == "dom_1"
