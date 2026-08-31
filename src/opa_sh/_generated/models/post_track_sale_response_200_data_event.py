from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_track_sale_response_200_data_event_metadata_type_0 import (
        PostTrackSaleResponse200DataEventMetadataType0,
    )


T = TypeVar("T", bound="PostTrackSaleResponse200DataEvent")


@_attrs_define
class PostTrackSaleResponse200DataEvent:
    """
    Attributes:
        id (str):
        event_type (str):
        event_name (str):
        click_id (None | str):
        customer_id (str):
        value_cents (float | None):
        currency (None | str):
        invoice_id (None | str):
        payment_processor (None | str):
        metadata (None | PostTrackSaleResponse200DataEventMetadataType0):
        occurred_at (str):
        created_at (str):
    """

    id: str
    event_type: str
    event_name: str
    click_id: str | None
    customer_id: str
    value_cents: float | None
    currency: str | None
    invoice_id: str | None
    payment_processor: str | None
    metadata: PostTrackSaleResponse200DataEventMetadataType0 | None
    occurred_at: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_track_sale_response_200_data_event_metadata_type_0 import (
            PostTrackSaleResponse200DataEventMetadataType0,
        )

        id = self.id

        event_type = self.event_type

        event_name = self.event_name

        click_id: str | None
        click_id = self.click_id

        customer_id = self.customer_id

        value_cents: float | None
        value_cents = self.value_cents

        currency: str | None
        currency = self.currency

        invoice_id: str | None
        invoice_id = self.invoice_id

        payment_processor: str | None
        payment_processor = self.payment_processor

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, PostTrackSaleResponse200DataEventMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        occurred_at = self.occurred_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "eventType": event_type,
                "eventName": event_name,
                "clickId": click_id,
                "customerId": customer_id,
                "valueCents": value_cents,
                "currency": currency,
                "invoiceId": invoice_id,
                "paymentProcessor": payment_processor,
                "metadata": metadata,
                "occurredAt": occurred_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_track_sale_response_200_data_event_metadata_type_0 import (
            PostTrackSaleResponse200DataEventMetadataType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        event_type = d.pop("eventType")

        event_name = d.pop("eventName")

        def _parse_click_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        click_id = _parse_click_id(d.pop("clickId"))

        customer_id = d.pop("customerId")

        def _parse_value_cents(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        value_cents = _parse_value_cents(d.pop("valueCents"))

        def _parse_currency(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_invoice_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        invoice_id = _parse_invoice_id(d.pop("invoiceId"))

        def _parse_payment_processor(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        payment_processor = _parse_payment_processor(d.pop("paymentProcessor"))

        def _parse_metadata(data: object) -> PostTrackSaleResponse200DataEventMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PostTrackSaleResponse200DataEventMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostTrackSaleResponse200DataEventMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

        occurred_at = d.pop("occurredAt")

        created_at = d.pop("createdAt")

        post_track_sale_response_200_data_event = cls(
            id=id,
            event_type=event_type,
            event_name=event_name,
            click_id=click_id,
            customer_id=customer_id,
            value_cents=value_cents,
            currency=currency,
            invoice_id=invoice_id,
            payment_processor=payment_processor,
            metadata=metadata,
            occurred_at=occurred_at,
            created_at=created_at,
        )

        return post_track_sale_response_200_data_event
