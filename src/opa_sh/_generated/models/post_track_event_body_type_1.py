from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_track_event_body_type_1_properties import PostTrackEventBodyType1Properties


T = TypeVar("T", bound="PostTrackEventBodyType1")


@_attrs_define
class PostTrackEventBodyType1:
    """
    Attributes:
        event_id (str):
        event_name (str):
        external_id (str):
        anonymous_id (str | Unset):
        click_id (str | Unset):
        properties (PostTrackEventBodyType1Properties | Unset):
        occurred_at (datetime.datetime | Unset):
    """

    event_id: str
    event_name: str
    external_id: str
    anonymous_id: str | Unset = UNSET
    click_id: str | Unset = UNSET
    properties: PostTrackEventBodyType1Properties | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        event_name = self.event_name

        external_id = self.external_id

        anonymous_id = self.anonymous_id

        click_id = self.click_id

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventId": event_id,
                "eventName": event_name,
                "externalId": external_id,
            }
        )
        if anonymous_id is not UNSET:
            field_dict["anonymousId"] = anonymous_id
        if click_id is not UNSET:
            field_dict["clickId"] = click_id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_track_event_body_type_1_properties import (
            PostTrackEventBodyType1Properties,
        )

        d = dict(src_dict)
        event_id = d.pop("eventId")

        event_name = d.pop("eventName")

        external_id = d.pop("externalId")

        anonymous_id = d.pop("anonymousId", UNSET)

        click_id = d.pop("clickId", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: PostTrackEventBodyType1Properties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = PostTrackEventBodyType1Properties.from_dict(_properties)

        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = datetime.datetime.fromisoformat(_occurred_at)

        post_track_event_body_type_1 = cls(
            event_id=event_id,
            event_name=event_name,
            external_id=external_id,
            anonymous_id=anonymous_id,
            click_id=click_id,
            properties=properties,
            occurred_at=occurred_at,
        )

        post_track_event_body_type_1.additional_properties = d
        return post_track_event_body_type_1

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
