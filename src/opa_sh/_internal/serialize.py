"""Helpers for turning Pythonic (snake_case) call kwargs into API JSON bodies."""

from typing import Any

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


def build_body(**fields: Any) -> dict[str, Any]:
    """Builds a JSON-ready request body from keyword arguments.

    - Drops any field whose value is ``None`` (the API treats an absent
      field as "use the default", so this is never the same as sending an
      explicit ``null``).
    - Converts each key from ``snake_case`` to the API's ``camelCase``.
    - Recursively dumps any :class:`pydantic.BaseModel` value (e.g. a
      ``QrSettings`` or ``LinkTargeting`` instance) via its camelCase
      aliases.
    """
    body: dict[str, Any] = {}
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, BaseModel):
            value = value.model_dump(by_alias=True, exclude_none=True)
        body[to_camel(key)] = value
    return body


# Query strings follow the same snake_case -> camelCase, drop-None rule.
build_query = build_body
