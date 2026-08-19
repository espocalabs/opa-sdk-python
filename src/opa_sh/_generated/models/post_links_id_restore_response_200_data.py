from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostLinksIdRestoreResponse200Data")


@_attrs_define
class PostLinksIdRestoreResponse200Data:
    """
    Attributes:
        id (str):
        archived (bool):
    """

    id: str
    archived: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        archived = self.archived

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "archived": archived,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        archived = d.pop("archived")

        post_links_id_restore_response_200_data = cls(
            id=id,
            archived=archived,
        )

        return post_links_id_restore_response_200_data
