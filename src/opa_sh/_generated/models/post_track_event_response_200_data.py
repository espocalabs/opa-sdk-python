from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostTrackEventResponse200Data")


@_attrs_define
class PostTrackEventResponse200Data:
    """
    Attributes:
        event_id (str):
        customer_id (str):
        deduped (bool):
    """

    event_id: str
    customer_id: str
    deduped: bool

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        customer_id = self.customer_id

        deduped = self.deduped

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eventId": event_id,
                "customerId": customer_id,
                "deduped": deduped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("eventId")

        customer_id = d.pop("customerId")

        deduped = d.pop("deduped")

        post_track_event_response_200_data = cls(
            event_id=event_id,
            customer_id=customer_id,
            deduped=deduped,
        )

        return post_track_event_response_200_data
