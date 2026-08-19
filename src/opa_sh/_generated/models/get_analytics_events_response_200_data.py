from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_analytics_events_response_200_data_items_item import (
        GetAnalyticsEventsResponse200DataItemsItem,
    )
    from ..models.get_analytics_events_response_200_data_pagination import (
        GetAnalyticsEventsResponse200DataPagination,
    )


T = TypeVar("T", bound="GetAnalyticsEventsResponse200Data")


@_attrs_define
class GetAnalyticsEventsResponse200Data:
    """
    Attributes:
        items (list[GetAnalyticsEventsResponse200DataItemsItem]):
        pagination (GetAnalyticsEventsResponse200DataPagination):
    """

    items: list[GetAnalyticsEventsResponse200DataItemsItem]
    pagination: GetAnalyticsEventsResponse200DataPagination

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_analytics_events_response_200_data_items_item import (
            GetAnalyticsEventsResponse200DataItemsItem,
        )
        from ..models.get_analytics_events_response_200_data_pagination import (
            GetAnalyticsEventsResponse200DataPagination,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GetAnalyticsEventsResponse200DataItemsItem.from_dict(items_item_data)

            items.append(items_item)

        pagination = GetAnalyticsEventsResponse200DataPagination.from_dict(d.pop("pagination"))

        get_analytics_events_response_200_data = cls(
            items=items,
            pagination=pagination,
        )

        return get_analytics_events_response_200_data
