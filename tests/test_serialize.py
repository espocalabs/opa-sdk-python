"""Unit coverage for `_internal/serialize.py::build_body`.

See `test_links.py` for the integration-level version of the same
regression (asserting the actual bytes sent over the wire via respx).
"""

import json

from opa_sh._internal.serialize import build_body
from opa_sh.models import LinkTargeting, QrSettings


def test_build_body_drops_none_fields() -> None:
    body = build_body(destination_url="https://example.com", domain=None, title=None)
    assert body == {"destinationUrl": "https://example.com"}


def test_build_body_converts_snake_case_keys_to_camel_case() -> None:
    body = build_body(utm_source="newsletter", folder_id="fld_1")
    assert body == {"utmSource": "newsletter", "folderId": "fld_1"}


def test_build_body_serializes_pydantic_models_as_json_strings() -> None:
    """`targeting`/`qrSettings` are the only BaseModel-typed fields any
    resource method passes through `build_body` today, and the API's
    request schema (unlike its response schema) declares both as
    JSON-encoded strings, not nested objects. `build_body` must therefore
    `json.dumps()` a BaseModel value rather than emit it as a dict."""
    body = build_body(
        targeting=LinkTargeting(ios="https://apps.apple.com/app/example"),
        qr_settings=QrSettings(foreground_color="#000000", background_color="#FFFFFF"),
    )
    assert isinstance(body["targeting"], str)
    assert json.loads(body["targeting"]) == {"ios": "https://apps.apple.com/app/example"}
    assert isinstance(body["qrSettings"], str)
    assert json.loads(body["qrSettings"]) == {
        "foregroundColor": "#000000",
        "backgroundColor": "#FFFFFF",
    }


def test_build_body_model_dump_excludes_none_fields_before_stringifying() -> None:
    body = build_body(targeting=LinkTargeting(ios="https://example.com", android=None, geo=None))
    parsed = json.loads(body["targeting"])
    assert parsed == {"ios": "https://example.com"}
    assert "android" not in parsed
    assert "geo" not in parsed
