from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetLinksResponse200DataPagination")


@_attrs_define
class GetLinksResponse200DataPagination:
    """
    Attributes:
        has_more (bool):
        next_ (None | str):
        before (None | str):
    """

    has_more: bool
    next_: str | None
    before: str | None

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        next_: str | None
        next_ = self.next_

        before: str | None
        before = self.before

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hasMore": has_more,
                "next": next_,
                "before": before,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_more = d.pop("hasMore")

        def _parse_next_(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        def _parse_before(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        before = _parse_before(d.pop("before"))

        get_links_response_200_data_pagination = cls(
            has_more=has_more,
            next_=next_,
            before=before,
        )

        return get_links_response_200_data_pagination
