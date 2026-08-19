from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostLinksBulkArchiveResponse200Data")


@_attrs_define
class PostLinksBulkArchiveResponse200Data:
    """
    Attributes:
        archived_count (float):
    """

    archived_count: float

    def to_dict(self) -> dict[str, Any]:
        archived_count = self.archived_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "archivedCount": archived_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archived_count = d.pop("archivedCount")

        post_links_bulk_archive_response_200_data = cls(
            archived_count=archived_count,
        )

        return post_links_bulk_archive_response_200_data
