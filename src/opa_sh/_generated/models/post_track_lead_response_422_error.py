from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_track_lead_response_422_error_issues_item import (
        PostTrackLeadResponse422ErrorIssuesItem,
    )


T = TypeVar("T", bound="PostTrackLeadResponse422Error")


@_attrs_define
class PostTrackLeadResponse422Error:
    """
    Attributes:
        code (Literal['validation_error']):
        message (str):
        issues (list[PostTrackLeadResponse422ErrorIssuesItem] | Unset):
    """

    code: Literal["validation_error"]
    message: str
    issues: list[PostTrackLeadResponse422ErrorIssuesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_track_lead_response_422_error_issues_item import (
            PostTrackLeadResponse422ErrorIssuesItem,
        )

        d = dict(src_dict)
        code = cast(Literal["validation_error"], d.pop("code"))
        if code != "validation_error":
            raise ValueError(f"code must match const 'validation_error', got '{code}'")

        message = d.pop("message")

        _issues = d.pop("issues", UNSET)
        issues: list[PostTrackLeadResponse422ErrorIssuesItem] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = PostTrackLeadResponse422ErrorIssuesItem.from_dict(issues_item_data)

                issues.append(issues_item)

        post_track_lead_response_422_error = cls(
            code=code,
            message=message,
            issues=issues,
        )

        post_track_lead_response_422_error.additional_properties = d
        return post_track_lead_response_422_error

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
