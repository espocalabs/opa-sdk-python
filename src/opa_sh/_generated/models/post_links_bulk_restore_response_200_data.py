from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostLinksBulkRestoreResponse200Data")


@_attrs_define
class PostLinksBulkRestoreResponse200Data:
    """
    Attributes:
        restored_count (float):
    """

    restored_count: float

    def to_dict(self) -> dict[str, Any]:
        restored_count = self.restored_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restoredCount": restored_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restored_count = d.pop("restoredCount")

        post_links_bulk_restore_response_200_data = cls(
            restored_count=restored_count,
        )

        return post_links_bulk_restore_response_200_data
