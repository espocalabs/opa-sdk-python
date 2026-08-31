from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostTrackIdentifyResponse409Error")


@_attrs_define
class PostTrackIdentifyResponse409Error:
    """
    Attributes:
        code (Literal['identity_conflict']):
        message (str):
    """

    code: Literal["identity_conflict"]
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = cast(Literal["identity_conflict"], d.pop("code"))
        if code != "identity_conflict":
            raise ValueError(f"code must match const 'identity_conflict', got '{code}'")

        message = d.pop("message")

        post_track_identify_response_409_error = cls(
            code=code,
            message=message,
        )

        post_track_identify_response_409_error.additional_properties = d
        return post_track_identify_response_409_error

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
