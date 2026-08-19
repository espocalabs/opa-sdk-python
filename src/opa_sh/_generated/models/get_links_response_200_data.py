from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_links_response_200_data_items_item import GetLinksResponse200DataItemsItem
    from ..models.get_links_response_200_data_pagination import GetLinksResponse200DataPagination


T = TypeVar("T", bound="GetLinksResponse200Data")


@_attrs_define
class GetLinksResponse200Data:
    """
    Attributes:
        items (list[GetLinksResponse200DataItemsItem]):
        pagination (GetLinksResponse200DataPagination):
    """

    items: list[GetLinksResponse200DataItemsItem]
    pagination: GetLinksResponse200DataPagination

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
        from ..models.get_links_response_200_data_items_item import GetLinksResponse200DataItemsItem
        from ..models.get_links_response_200_data_pagination import (
            GetLinksResponse200DataPagination,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GetLinksResponse200DataItemsItem.from_dict(items_item_data)

            items.append(items_item)

        pagination = GetLinksResponse200DataPagination.from_dict(d.pop("pagination"))

        get_links_response_200_data = cls(
            items=items,
            pagination=pagination,
        )

        return get_links_response_200_data
