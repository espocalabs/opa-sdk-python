from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_links_id_response_200_data_targeting_type_0_geo import (
        GetLinksIdResponse200DataTargetingType0Geo,
    )


T = TypeVar("T", bound="GetLinksIdResponse200DataTargetingType0")


@_attrs_define
class GetLinksIdResponse200DataTargetingType0:
    """
    Attributes:
        ios (str | Unset):
        android (str | Unset):
        geo (GetLinksIdResponse200DataTargetingType0Geo | Unset):
    """

    ios: str | Unset = UNSET
    android: str | Unset = UNSET
    geo: GetLinksIdResponse200DataTargetingType0Geo | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ios = self.ios

        android = self.android

        geo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geo, Unset):
            geo = self.geo.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ios is not UNSET:
            field_dict["ios"] = ios
        if android is not UNSET:
            field_dict["android"] = android
        if geo is not UNSET:
            field_dict["geo"] = geo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_links_id_response_200_data_targeting_type_0_geo import (
            GetLinksIdResponse200DataTargetingType0Geo,
        )

        d = dict(src_dict)
        ios = d.pop("ios", UNSET)

        android = d.pop("android", UNSET)

        _geo = d.pop("geo", UNSET)
        geo: GetLinksIdResponse200DataTargetingType0Geo | Unset
        if isinstance(_geo, Unset):
            geo = UNSET
        else:
            geo = GetLinksIdResponse200DataTargetingType0Geo.from_dict(_geo)

        get_links_id_response_200_data_targeting_type_0 = cls(
            ios=ios,
            android=android,
            geo=geo,
        )

        return get_links_id_response_200_data_targeting_type_0
