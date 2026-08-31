from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostTrackSaleResponse200DataCustomer")


@_attrs_define
class PostTrackSaleResponse200DataCustomer:
    """
    Attributes:
        id (str):
        external_id (str):
        email (None | str):
        name (None | str):
        avatar (None | str):
        created_at (str):
    """

    id: str
    external_id: str
    email: str | None
    name: str | None
    avatar: str | None
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        email: str | None
        email = self.email

        name: str | None
        name = self.name

        avatar: str | None
        avatar = self.avatar

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "externalId": external_id,
                "email": email,
                "name": name,
                "avatar": avatar,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("externalId")

        def _parse_email(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_name(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_avatar(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        avatar = _parse_avatar(d.pop("avatar"))

        created_at = d.pop("createdAt")

        post_track_sale_response_200_data_customer = cls(
            id=id,
            external_id=external_id,
            email=email,
            name=name,
            avatar=avatar,
            created_at=created_at,
        )

        return post_track_sale_response_200_data_customer
