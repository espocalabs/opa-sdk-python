from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetAnalyticsEventsResponse200DataPagination")


@_attrs_define
class GetAnalyticsEventsResponse200DataPagination:
    """
    Attributes:
        has_more (bool):
        next_ (None | str):
    """

    has_more: bool
    next_: str | None

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        next_: str | None
        next_ = self.next_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hasMore": has_more,
                "next": next_,
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

        get_analytics_events_response_200_data_pagination = cls(
            has_more=has_more,
            next_=next_,
        )

        return get_analytics_events_response_200_data_pagination
