from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTrackIdentifyBodyTraits")


@_attrs_define
class PostTrackIdentifyBodyTraits:
    """
    Attributes:
        email (str | Unset):
        name (str | Unset):
        avatar (str | Unset):
    """

    email: str | Unset = UNSET
    name: str | Unset = UNSET
    avatar: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        avatar = self.avatar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        avatar = d.pop("avatar", UNSET)

        post_track_identify_body_traits = cls(
            email=email,
            name=name,
            avatar=avatar,
        )

        post_track_identify_body_traits.additional_properties = d
        return post_track_identify_body_traits

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
