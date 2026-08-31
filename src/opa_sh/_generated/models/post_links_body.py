from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostLinksBody")


@_attrs_define
class PostLinksBody:
    """
    Attributes:
        destination_url (str):
        domain (str | Unset):
        key (str | Unset):  Default: ''.
        folder_id (str | Unset):  Default: ''.
        tag_ids (list[str] | Unset):
        utm_template_id (str | Unset):  Default: ''.
        utm_source (str | Unset):  Default: ''.
        utm_medium (str | Unset):  Default: ''.
        utm_campaign (str | Unset):  Default: ''.
        utm_term (str | Unset):  Default: ''.
        utm_content (str | Unset):  Default: ''.
        utm_referral (str | Unset):  Default: ''.
        comments (str | Unset):  Default: ''.
        title (str | Unset):  Default: ''.
        description (str | Unset):  Default: ''.
        image_url (str | Unset):  Default: ''.
        expires_at (str | Unset):  Default: ''.
        expired_url (str | Unset):  Default: ''.
        do_index (bool | Unset):  Default: False.
        track_conversions (bool | Unset):
        password (str | Unset):  Default: ''.
        test_variants (str | Unset):  Default: ''.
        test_completed_at (str | Unset):  Default: ''.
        targeting (str | Unset): Device/geo redirect overrides. A JSON-encoded string (`JSON.stringify`d) matching
            `LinkTargeting` — or the plain object itself, which is JSON-encoded automatically. An empty string (the default)
            means no targeting. Requires the `targeting` plan capability. Default: ''.
        qr_settings (str | Unset): Per-link QR code style override. A JSON-encoded string (`JSON.stringify`d) matching
            the QR settings shape — or the plain object itself, which is JSON-encoded automatically. An empty string (the
            default) inherits the account-level default. Requires the `qrCustomization` plan capability. Default: ''.
    """

    destination_url: str
    domain: str | Unset = UNSET
    key: str | Unset = ""
    folder_id: str | Unset = ""
    tag_ids: list[str] | Unset = UNSET
    utm_template_id: str | Unset = ""
    utm_source: str | Unset = ""
    utm_medium: str | Unset = ""
    utm_campaign: str | Unset = ""
    utm_term: str | Unset = ""
    utm_content: str | Unset = ""
    utm_referral: str | Unset = ""
    comments: str | Unset = ""
    title: str | Unset = ""
    description: str | Unset = ""
    image_url: str | Unset = ""
    expires_at: str | Unset = ""
    expired_url: str | Unset = ""
    do_index: bool | Unset = False
    track_conversions: bool | Unset = UNSET
    password: str | Unset = ""
    test_variants: str | Unset = ""
    test_completed_at: str | Unset = ""
    targeting: str | Unset = ""
    qr_settings: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_url = self.destination_url

        domain = self.domain

        key = self.key

        folder_id = self.folder_id

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        utm_template_id = self.utm_template_id

        utm_source = self.utm_source

        utm_medium = self.utm_medium

        utm_campaign = self.utm_campaign

        utm_term = self.utm_term

        utm_content = self.utm_content

        utm_referral = self.utm_referral

        comments = self.comments

        title = self.title

        description = self.description

        image_url = self.image_url

        expires_at = self.expires_at

        expired_url = self.expired_url

        do_index = self.do_index

        track_conversions = self.track_conversions

        password = self.password

        test_variants = self.test_variants

        test_completed_at = self.test_completed_at

        targeting = self.targeting

        qr_settings = self.qr_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinationUrl": destination_url,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if key is not UNSET:
            field_dict["key"] = key
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if utm_template_id is not UNSET:
            field_dict["utmTemplateId"] = utm_template_id
        if utm_source is not UNSET:
            field_dict["utmSource"] = utm_source
        if utm_medium is not UNSET:
            field_dict["utmMedium"] = utm_medium
        if utm_campaign is not UNSET:
            field_dict["utmCampaign"] = utm_campaign
        if utm_term is not UNSET:
            field_dict["utmTerm"] = utm_term
        if utm_content is not UNSET:
            field_dict["utmContent"] = utm_content
        if utm_referral is not UNSET:
            field_dict["utmReferral"] = utm_referral
        if comments is not UNSET:
            field_dict["comments"] = comments
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if expired_url is not UNSET:
            field_dict["expiredUrl"] = expired_url
        if do_index is not UNSET:
            field_dict["doIndex"] = do_index
        if track_conversions is not UNSET:
            field_dict["trackConversions"] = track_conversions
        if password is not UNSET:
            field_dict["password"] = password
        if test_variants is not UNSET:
            field_dict["testVariants"] = test_variants
        if test_completed_at is not UNSET:
            field_dict["testCompletedAt"] = test_completed_at
        if targeting is not UNSET:
            field_dict["targeting"] = targeting
        if qr_settings is not UNSET:
            field_dict["qrSettings"] = qr_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_url = d.pop("destinationUrl")

        domain = d.pop("domain", UNSET)

        key = d.pop("key", UNSET)

        folder_id = d.pop("folderId", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        utm_template_id = d.pop("utmTemplateId", UNSET)

        utm_source = d.pop("utmSource", UNSET)

        utm_medium = d.pop("utmMedium", UNSET)

        utm_campaign = d.pop("utmCampaign", UNSET)

        utm_term = d.pop("utmTerm", UNSET)

        utm_content = d.pop("utmContent", UNSET)

        utm_referral = d.pop("utmReferral", UNSET)

        comments = d.pop("comments", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        expired_url = d.pop("expiredUrl", UNSET)

        do_index = d.pop("doIndex", UNSET)

        track_conversions = d.pop("trackConversions", UNSET)

        password = d.pop("password", UNSET)

        test_variants = d.pop("testVariants", UNSET)

        test_completed_at = d.pop("testCompletedAt", UNSET)

        targeting = d.pop("targeting", UNSET)

        qr_settings = d.pop("qrSettings", UNSET)

        post_links_body = cls(
            destination_url=destination_url,
            domain=domain,
            key=key,
            folder_id=folder_id,
            tag_ids=tag_ids,
            utm_template_id=utm_template_id,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            utm_referral=utm_referral,
            comments=comments,
            title=title,
            description=description,
            image_url=image_url,
            expires_at=expires_at,
            expired_url=expired_url,
            do_index=do_index,
            track_conversions=track_conversions,
            password=password,
            test_variants=test_variants,
            test_completed_at=test_completed_at,
            targeting=targeting,
            qr_settings=qr_settings,
        )

        post_links_body.additional_properties = d
        return post_links_body

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
