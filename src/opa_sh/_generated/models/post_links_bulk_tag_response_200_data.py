from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostLinksBulkTagResponse200Data")


@_attrs_define
class PostLinksBulkTagResponse200Data:
    """
    Attributes:
        tagged_count (float):
    """

    tagged_count: float

    def to_dict(self) -> dict[str, Any]:
        tagged_count = self.tagged_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "taggedCount": tagged_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tagged_count = d.pop("taggedCount")

        post_links_bulk_tag_response_200_data = cls(
            tagged_count=tagged_count,
        )

        return post_links_bulk_tag_response_200_data
