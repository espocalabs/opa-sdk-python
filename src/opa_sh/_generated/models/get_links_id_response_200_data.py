from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_links_id_response_200_data_qr_settings_type_0 import (
        GetLinksIdResponse200DataQrSettingsType0,
    )
    from ..models.get_links_id_response_200_data_targeting_type_0 import (
        GetLinksIdResponse200DataTargetingType0,
    )


T = TypeVar("T", bound="GetLinksIdResponse200Data")


@_attrs_define
class GetLinksIdResponse200Data:
    """
    Attributes:
        id (str):
        domain (str):
        key (str):
        short_link (str):
        destination_url (str):
        title (None | str):
        description (None | str):
        image_url (None | str):
        comments (None | str):
        folder_id (str):
        tag_ids (list[str]):
        utm_template_id (None | str):
        utm_source (None | str):
        utm_medium (None | str):
        utm_campaign (None | str):
        utm_term (None | str):
        utm_content (None | str):
        utm_referral (None | str):
        expires_at (None | str):
        expired_url (None | str):
        do_index (bool):
        has_password (bool):
        test_variants_count (float):
        test_completed_at (None | str):
        targeting (GetLinksIdResponse200DataTargetingType0 | None):
        qr_settings (GetLinksIdResponse200DataQrSettingsType0 | None):
    """

    id: str
    domain: str
    key: str
    short_link: str
    destination_url: str
    title: str | None
    description: str | None
    image_url: str | None
    comments: str | None
    folder_id: str
    tag_ids: list[str]
    utm_template_id: str | None
    utm_source: str | None
    utm_medium: str | None
    utm_campaign: str | None
    utm_term: str | None
    utm_content: str | None
    utm_referral: str | None
    expires_at: str | None
    expired_url: str | None
    do_index: bool
    has_password: bool
    test_variants_count: float
    test_completed_at: str | None
    targeting: GetLinksIdResponse200DataTargetingType0 | None
    qr_settings: GetLinksIdResponse200DataQrSettingsType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_links_id_response_200_data_qr_settings_type_0 import (
            GetLinksIdResponse200DataQrSettingsType0,
        )
        from ..models.get_links_id_response_200_data_targeting_type_0 import (
            GetLinksIdResponse200DataTargetingType0,
        )

        id = self.id

        domain = self.domain

        key = self.key

        short_link = self.short_link

        destination_url = self.destination_url

        title: str | None
        title = self.title

        description: str | None
        description = self.description

        image_url: str | None
        image_url = self.image_url

        comments: str | None
        comments = self.comments

        folder_id = self.folder_id

        tag_ids = self.tag_ids

        utm_template_id: str | None
        utm_template_id = self.utm_template_id

        utm_source: str | None
        utm_source = self.utm_source

        utm_medium: str | None
        utm_medium = self.utm_medium

        utm_campaign: str | None
        utm_campaign = self.utm_campaign

        utm_term: str | None
        utm_term = self.utm_term

        utm_content: str | None
        utm_content = self.utm_content

        utm_referral: str | None
        utm_referral = self.utm_referral

        expires_at: str | None
        expires_at = self.expires_at

        expired_url: str | None
        expired_url = self.expired_url

        do_index = self.do_index

        has_password = self.has_password

        test_variants_count = self.test_variants_count

        test_completed_at: str | None
        test_completed_at = self.test_completed_at

        targeting: dict[str, Any] | None
        if isinstance(self.targeting, GetLinksIdResponse200DataTargetingType0):
            targeting = self.targeting.to_dict()
        else:
            targeting = self.targeting

        qr_settings: dict[str, Any] | None
        if isinstance(self.qr_settings, GetLinksIdResponse200DataQrSettingsType0):
            qr_settings = self.qr_settings.to_dict()
        else:
            qr_settings = self.qr_settings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "domain": domain,
                "key": key,
                "shortLink": short_link,
                "destinationUrl": destination_url,
                "title": title,
                "description": description,
                "imageUrl": image_url,
                "comments": comments,
                "folderId": folder_id,
                "tagIds": tag_ids,
                "utmTemplateId": utm_template_id,
                "utmSource": utm_source,
                "utmMedium": utm_medium,
                "utmCampaign": utm_campaign,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "utmReferral": utm_referral,
                "expiresAt": expires_at,
                "expiredUrl": expired_url,
                "doIndex": do_index,
                "hasPassword": has_password,
                "testVariantsCount": test_variants_count,
                "testCompletedAt": test_completed_at,
                "targeting": targeting,
                "qrSettings": qr_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_links_id_response_200_data_qr_settings_type_0 import (
            GetLinksIdResponse200DataQrSettingsType0,
        )
        from ..models.get_links_id_response_200_data_targeting_type_0 import (
            GetLinksIdResponse200DataTargetingType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        domain = d.pop("domain")

        key = d.pop("key")

        short_link = d.pop("shortLink")

        destination_url = d.pop("destinationUrl")

        def _parse_title(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_description(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_image_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        def _parse_comments(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        comments = _parse_comments(d.pop("comments"))

        folder_id = d.pop("folderId")

        tag_ids = cast(list[str], d.pop("tagIds"))

        def _parse_utm_template_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        utm_template_id = _parse_utm_template_id(d.pop("utmTemplateId"))

        def _parse_utm_source(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        utm_source = _parse_utm_source(d.pop("utmSource"))

        def _parse_utm_medium(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        utm_medium = _parse_utm_medium(d.pop("utmMedium"))

        def _parse_utm_campaign(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        utm_campaign = _parse_utm_campaign(d.pop("utmCampaign"))

        def _parse_utm_term(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        utm_term = _parse_utm_term(d.pop("utmTerm"))

        def _parse_utm_content(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        utm_content = _parse_utm_content(d.pop("utmContent"))

        def _parse_utm_referral(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        utm_referral = _parse_utm_referral(d.pop("utmReferral"))

        def _parse_expires_at(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        def _parse_expired_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        expired_url = _parse_expired_url(d.pop("expiredUrl"))

        do_index = d.pop("doIndex")

        has_password = d.pop("hasPassword")

        test_variants_count = d.pop("testVariantsCount")

        def _parse_test_completed_at(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        test_completed_at = _parse_test_completed_at(d.pop("testCompletedAt"))

        def _parse_targeting(data: object) -> GetLinksIdResponse200DataTargetingType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                targeting_type_0 = GetLinksIdResponse200DataTargetingType0.from_dict(data)

                return targeting_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetLinksIdResponse200DataTargetingType0 | None, data)

        targeting = _parse_targeting(d.pop("targeting"))

        def _parse_qr_settings(data: object) -> GetLinksIdResponse200DataQrSettingsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qr_settings_type_0 = GetLinksIdResponse200DataQrSettingsType0.from_dict(data)

                return qr_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetLinksIdResponse200DataQrSettingsType0 | None, data)

        qr_settings = _parse_qr_settings(d.pop("qrSettings"))

        get_links_id_response_200_data = cls(
            id=id,
            domain=domain,
            key=key,
            short_link=short_link,
            destination_url=destination_url,
            title=title,
            description=description,
            image_url=image_url,
            comments=comments,
            folder_id=folder_id,
            tag_ids=tag_ids,
            utm_template_id=utm_template_id,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            utm_referral=utm_referral,
            expires_at=expires_at,
            expired_url=expired_url,
            do_index=do_index,
            has_password=has_password,
            test_variants_count=test_variants_count,
            test_completed_at=test_completed_at,
            targeting=targeting,
            qr_settings=qr_settings,
        )

        return get_links_id_response_200_data
