from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_track_sale_response_200_data_customer import (
        PostTrackSaleResponse200DataCustomer,
    )
    from ..models.post_track_sale_response_200_data_event import PostTrackSaleResponse200DataEvent


T = TypeVar("T", bound="PostTrackSaleResponse200Data")


@_attrs_define
class PostTrackSaleResponse200Data:
    """
    Attributes:
        event (PostTrackSaleResponse200DataEvent):
        customer (PostTrackSaleResponse200DataCustomer):
        deduped (bool): True when a matching event already existed (a re-reported lead `(customer, eventName)` or a
            replayed sale `invoiceId`) and this request recorded nothing new — the returned `event`/`customer` are the
            canonical pre-existing ones. The response is `200` either way.
    """

    event: PostTrackSaleResponse200DataEvent
    customer: PostTrackSaleResponse200DataCustomer
    deduped: bool

    def to_dict(self) -> dict[str, Any]:
        event = self.event.to_dict()

        customer = self.customer.to_dict()

        deduped = self.deduped

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event": event,
                "customer": customer,
                "deduped": deduped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_track_sale_response_200_data_customer import (
            PostTrackSaleResponse200DataCustomer,
        )
        from ..models.post_track_sale_response_200_data_event import (
            PostTrackSaleResponse200DataEvent,
        )

        d = dict(src_dict)
        event = PostTrackSaleResponse200DataEvent.from_dict(d.pop("event"))

        customer = PostTrackSaleResponse200DataCustomer.from_dict(d.pop("customer"))

        deduped = d.pop("deduped")

        post_track_sale_response_200_data = cls(
            event=event,
            customer=customer,
            deduped=deduped,
        )

        return post_track_sale_response_200_data
