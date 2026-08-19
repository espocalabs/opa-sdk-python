from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_links_id_response_422_error import PatchLinksIdResponse422Error


T = TypeVar("T", bound="PatchLinksIdResponse422")


@_attrs_define
class PatchLinksIdResponse422:
    """
    Attributes:
        error (PatchLinksIdResponse422Error):
    """

    error: PatchLinksIdResponse422Error
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_links_id_response_422_error import PatchLinksIdResponse422Error

        d = dict(src_dict)
        error = PatchLinksIdResponse422Error.from_dict(d.pop("error"))

        patch_links_id_response_422 = cls(
            error=error,
        )

        patch_links_id_response_422.additional_properties = d
        return patch_links_id_response_422

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
