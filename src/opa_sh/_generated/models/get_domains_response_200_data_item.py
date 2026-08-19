from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_domains_response_200_data_item_type import GetDomainsResponse200DataItemType

T = TypeVar("T", bound="GetDomainsResponse200DataItem")


@_attrs_define
class GetDomainsResponse200DataItem:
    """
    Attributes:
        id (str):
        domain (str):
        type_ (GetDomainsResponse200DataItemType):
        verified (bool):
        primary (bool):
        allowed_hosts (list[str]):
    """

    id: str
    domain: str
    type_: GetDomainsResponse200DataItemType
    verified: bool
    primary: bool
    allowed_hosts: list[str]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        domain = self.domain

        type_ = self.type_.value

        verified = self.verified

        primary = self.primary

        allowed_hosts = self.allowed_hosts

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "domain": domain,
                "type": type_,
                "verified": verified,
                "primary": primary,
                "allowedHosts": allowed_hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        domain = d.pop("domain")

        type_ = GetDomainsResponse200DataItemType(d.pop("type"))

        verified = d.pop("verified")

        primary = d.pop("primary")

        allowed_hosts = cast(list[str], d.pop("allowedHosts"))

        get_domains_response_200_data_item = cls(
            id=id,
            domain=domain,
            type_=type_,
            verified=verified,
            primary=primary,
            allowed_hosts=allowed_hosts,
        )

        return get_domains_response_200_data_item
