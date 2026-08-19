from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostLinksBulkMoveResponse200Data")


@_attrs_define
class PostLinksBulkMoveResponse200Data:
    """
    Attributes:
        moved_count (float):
    """

    moved_count: float

    def to_dict(self) -> dict[str, Any]:
        moved_count = self.moved_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "movedCount": moved_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        moved_count = d.pop("movedCount")

        post_links_bulk_move_response_200_data = cls(
            moved_count=moved_count,
        )

        return post_links_bulk_move_response_200_data
