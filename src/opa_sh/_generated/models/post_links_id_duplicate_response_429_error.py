from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostLinksIdDuplicateResponse429Error")


@_attrs_define
class PostLinksIdDuplicateResponse429Error:
    """
    Attributes:
        code (Literal['rate_limited']):
        message (str):
    """

    code: Literal["rate_limited"]
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
        code = cast(Literal["rate_limited"], d.pop("code"))
        if code != "rate_limited":
            raise ValueError(f"code must match const 'rate_limited', got '{code}'")

        message = d.pop("message")

        post_links_id_duplicate_response_429_error = cls(
            code=code,
            message=message,
        )

        post_links_id_duplicate_response_429_error.additional_properties = d
        return post_links_id_duplicate_response_429_error

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
