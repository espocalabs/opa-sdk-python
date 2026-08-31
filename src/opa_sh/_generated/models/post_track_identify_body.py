from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_track_identify_body_traits import PostTrackIdentifyBodyTraits


T = TypeVar("T", bound="PostTrackIdentifyBody")


@_attrs_define
class PostTrackIdentifyBody:
    """
    Attributes:
        anonymous_id (str):
        external_id (str):
        traits (PostTrackIdentifyBodyTraits | Unset):
        click_id (str | Unset):
    """

    anonymous_id: str
    external_id: str
    traits: PostTrackIdentifyBodyTraits | Unset = UNSET
    click_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anonymous_id = self.anonymous_id

        external_id = self.external_id

        traits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traits, Unset):
            traits = self.traits.to_dict()

        click_id = self.click_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anonymousId": anonymous_id,
                "externalId": external_id,
            }
        )
        if traits is not UNSET:
            field_dict["traits"] = traits
        if click_id is not UNSET:
            field_dict["clickId"] = click_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_track_identify_body_traits import PostTrackIdentifyBodyTraits

        d = dict(src_dict)
        anonymous_id = d.pop("anonymousId")

        external_id = d.pop("externalId")

        _traits = d.pop("traits", UNSET)
        traits: PostTrackIdentifyBodyTraits | Unset
        if isinstance(_traits, Unset):
            traits = UNSET
        else:
            traits = PostTrackIdentifyBodyTraits.from_dict(_traits)

        click_id = d.pop("clickId", UNSET)

        post_track_identify_body = cls(
            anonymous_id=anonymous_id,
            external_id=external_id,
            traits=traits,
            click_id=click_id,
        )

        post_track_identify_body.additional_properties = d
        return post_track_identify_body

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
