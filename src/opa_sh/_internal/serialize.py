"""Helpers for turning Pythonic (snake_case) call kwargs into API JSON bodies."""

import json
from typing import Any

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


def build_body(**fields: Any) -> dict[str, Any]:
    """Builds a JSON-ready request body from keyword arguments.

    - Drops any field whose value is ``None`` (the API treats an absent
      field as "use the default", so this is never the same as sending an
      explicit ``null``).
    - Converts each key from ``snake_case`` to the API's ``camelCase``.
    - Serializes any :class:`pydantic.BaseModel` value (e.g. a
      ``QrSettings`` or ``LinkTargeting`` instance) to a JSON **string** via
      its camelCase aliases. This looks surprising — the API returns these
      same fields as nested objects — but the *request* schema
      (``openapi/v1.json``: ``links.post.requestBody`` /
      ``links.{id}.patch.requestBody``, both declare ``targeting``/
      ``qrSettings`` as ``type: string``) really does expect a
      JSON-encoded string on the way in. Confirmed against the live API:
      sending the raw object 422s with
      ``"Invalid input: expected string, received object"`` on both
      fields; sending ``json.dumps(...)`` of the same payload succeeds.
    """
    body: dict[str, Any] = {}
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, BaseModel):
            value = json.dumps(value.model_dump(by_alias=True, exclude_none=True))
        body[to_camel(key)] = value
    return body


# Query strings follow the same snake_case -> camelCase, drop-None rule.
build_query = build_body
