from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostTrackIdentifyResponse200Data")


@_attrs_define
class PostTrackIdentifyResponse200Data:
    """
    Attributes:
        customer_id (str):
        anonymous_id (str):
        external_id (str):
        merged (bool):
    """

    customer_id: str
    anonymous_id: str
    external_id: str
    merged: bool

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        anonymous_id = self.anonymous_id

        external_id = self.external_id

        merged = self.merged

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "customerId": customer_id,
                "anonymousId": anonymous_id,
                "externalId": external_id,
                "merged": merged,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_id = d.pop("customerId")

        anonymous_id = d.pop("anonymousId")

        external_id = d.pop("externalId")

        merged = d.pop("merged")

        post_track_identify_response_200_data = cls(
            customer_id=customer_id,
            anonymous_id=anonymous_id,
            external_id=external_id,
            merged=merged,
        )

        return post_track_identify_response_200_data
