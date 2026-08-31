from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_track_sale_body_metadata import PostTrackSaleBodyMetadata


T = TypeVar("T", bound="PostTrackSaleBody")


@_attrs_define
class PostTrackSaleBody:
    """
    Attributes:
        customer_external_id (str):
        amount (int):
        currency (str | Unset):  Default: 'brl'.
        event_name (str | Unset):  Default: 'Purchase'.
        payment_processor (str | Unset):
        invoice_id (str | Unset):
        click_id (str | Unset):
        metadata (PostTrackSaleBodyMetadata | Unset):
    """

    customer_external_id: str
    amount: int
    currency: str | Unset = "brl"
    event_name: str | Unset = "Purchase"
    payment_processor: str | Unset = UNSET
    invoice_id: str | Unset = UNSET
    click_id: str | Unset = UNSET
    metadata: PostTrackSaleBodyMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_external_id = self.customer_external_id

        amount = self.amount

        currency = self.currency

        event_name = self.event_name

        payment_processor = self.payment_processor

        invoice_id = self.invoice_id

        click_id = self.click_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerExternalId": customer_external_id,
                "amount": amount,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if payment_processor is not UNSET:
            field_dict["paymentProcessor"] = payment_processor
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if click_id is not UNSET:
            field_dict["clickId"] = click_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_track_sale_body_metadata import PostTrackSaleBodyMetadata

        d = dict(src_dict)
        customer_external_id = d.pop("customerExternalId")

        amount = d.pop("amount")

        currency = d.pop("currency", UNSET)

        event_name = d.pop("eventName", UNSET)

        payment_processor = d.pop("paymentProcessor", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        click_id = d.pop("clickId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostTrackSaleBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostTrackSaleBodyMetadata.from_dict(_metadata)

        post_track_sale_body = cls(
            customer_external_id=customer_external_id,
            amount=amount,
            currency=currency,
            event_name=event_name,
            payment_processor=payment_processor,
            invoice_id=invoice_id,
            click_id=click_id,
            metadata=metadata,
        )

        post_track_sale_body.additional_properties = d
        return post_track_sale_body

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
