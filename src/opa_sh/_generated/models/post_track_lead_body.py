from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_track_lead_body_metadata import PostTrackLeadBodyMetadata


T = TypeVar("T", bound="PostTrackLeadBody")


@_attrs_define
class PostTrackLeadBody:
    """
    Attributes:
        click_id (str):
        event_name (str):
        customer_external_id (str):
        customer_email (str | Unset):
        customer_name (str | Unset):
        customer_avatar (str | Unset):
        metadata (PostTrackLeadBodyMetadata | Unset):
    """

    click_id: str
    event_name: str
    customer_external_id: str
    customer_email: str | Unset = UNSET
    customer_name: str | Unset = UNSET
    customer_avatar: str | Unset = UNSET
    metadata: PostTrackLeadBodyMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        click_id = self.click_id

        event_name = self.event_name

        customer_external_id = self.customer_external_id

        customer_email = self.customer_email

        customer_name = self.customer_name

        customer_avatar = self.customer_avatar

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clickId": click_id,
                "eventName": event_name,
                "customerExternalId": customer_external_id,
            }
        )
        if customer_email is not UNSET:
            field_dict["customerEmail"] = customer_email
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if customer_avatar is not UNSET:
            field_dict["customerAvatar"] = customer_avatar
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_track_lead_body_metadata import PostTrackLeadBodyMetadata

        d = dict(src_dict)
        click_id = d.pop("clickId")

        event_name = d.pop("eventName")

        customer_external_id = d.pop("customerExternalId")

        customer_email = d.pop("customerEmail", UNSET)

        customer_name = d.pop("customerName", UNSET)

        customer_avatar = d.pop("customerAvatar", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostTrackLeadBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostTrackLeadBodyMetadata.from_dict(_metadata)

        post_track_lead_body = cls(
            click_id=click_id,
            event_name=event_name,
            customer_external_id=customer_external_id,
            customer_email=customer_email,
            customer_name=customer_name,
            customer_avatar=customer_avatar,
            metadata=metadata,
        )

        post_track_lead_body.additional_properties = d
        return post_track_lead_body

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
