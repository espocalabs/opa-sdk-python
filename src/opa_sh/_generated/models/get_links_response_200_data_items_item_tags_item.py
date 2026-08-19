from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetLinksResponse200DataItemsItemTagsItem")


@_attrs_define
class GetLinksResponse200DataItemsItemTagsItem:
    """
    Attributes:
        id (str):
        name (str):
        color (str):
    """

    id: str
    name: str
    color: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        color = self.color

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "color": color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        color = d.pop("color")

        get_links_response_200_data_items_item_tags_item = cls(
            id=id,
            name=name,
            color=color,
        )

        return get_links_response_200_data_items_item_tags_item
