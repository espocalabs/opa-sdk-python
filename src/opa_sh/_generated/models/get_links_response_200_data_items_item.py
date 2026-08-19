from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_links_response_200_data_items_item_folder_type_0 import (
        GetLinksResponse200DataItemsItemFolderType0,
    )
    from ..models.get_links_response_200_data_items_item_qr_settings_type_0 import (
        GetLinksResponse200DataItemsItemQrSettingsType0,
    )
    from ..models.get_links_response_200_data_items_item_tags_item import (
        GetLinksResponse200DataItemsItemTagsItem,
    )


T = TypeVar("T", bound="GetLinksResponse200DataItemsItem")


@_attrs_define
class GetLinksResponse200DataItemsItem:
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
        created_at (str):
        expires_at (None | str):
        disabled_at (None | str):
        test_completed_at (None | str):
        test_variants_count (float):
        qr_settings (GetLinksResponse200DataItemsItemQrSettingsType0 | None):
        folder (GetLinksResponse200DataItemsItemFolderType0 | None):
        tags (list[GetLinksResponse200DataItemsItemTagsItem]):
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
    created_at: str
    expires_at: str | None
    disabled_at: str | None
    test_completed_at: str | None
    test_variants_count: float
    qr_settings: GetLinksResponse200DataItemsItemQrSettingsType0 | None
    folder: GetLinksResponse200DataItemsItemFolderType0 | None
    tags: list[GetLinksResponse200DataItemsItemTagsItem]

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_links_response_200_data_items_item_folder_type_0 import (
            GetLinksResponse200DataItemsItemFolderType0,
        )
        from ..models.get_links_response_200_data_items_item_qr_settings_type_0 import (
            GetLinksResponse200DataItemsItemQrSettingsType0,
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

        created_at = self.created_at

        expires_at: str | None
        expires_at = self.expires_at

        disabled_at: str | None
        disabled_at = self.disabled_at

        test_completed_at: str | None
        test_completed_at = self.test_completed_at

        test_variants_count = self.test_variants_count

        qr_settings: dict[str, Any] | None
        if isinstance(self.qr_settings, GetLinksResponse200DataItemsItemQrSettingsType0):
            qr_settings = self.qr_settings.to_dict()
        else:
            qr_settings = self.qr_settings

        folder: dict[str, Any] | None
        if isinstance(self.folder, GetLinksResponse200DataItemsItemFolderType0):
            folder = self.folder.to_dict()
        else:
            folder = self.folder

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

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
                "createdAt": created_at,
                "expiresAt": expires_at,
                "disabledAt": disabled_at,
                "testCompletedAt": test_completed_at,
                "testVariantsCount": test_variants_count,
                "qrSettings": qr_settings,
                "folder": folder,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_links_response_200_data_items_item_folder_type_0 import (
            GetLinksResponse200DataItemsItemFolderType0,
        )
        from ..models.get_links_response_200_data_items_item_qr_settings_type_0 import (
            GetLinksResponse200DataItemsItemQrSettingsType0,
        )
        from ..models.get_links_response_200_data_items_item_tags_item import (
            GetLinksResponse200DataItemsItemTagsItem,
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

        created_at = d.pop("createdAt")

        def _parse_expires_at(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        def _parse_disabled_at(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        disabled_at = _parse_disabled_at(d.pop("disabledAt"))

        def _parse_test_completed_at(data: object) -> str | None:
            if data is None:
                return data
            return cast(None | str, data)

        test_completed_at = _parse_test_completed_at(d.pop("testCompletedAt"))

        test_variants_count = d.pop("testVariantsCount")

        def _parse_qr_settings(
            data: object,
        ) -> GetLinksResponse200DataItemsItemQrSettingsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qr_settings_type_0 = GetLinksResponse200DataItemsItemQrSettingsType0.from_dict(data)

                return qr_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetLinksResponse200DataItemsItemQrSettingsType0 | None, data)

        qr_settings = _parse_qr_settings(d.pop("qrSettings"))

        def _parse_folder(data: object) -> GetLinksResponse200DataItemsItemFolderType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                folder_type_0 = GetLinksResponse200DataItemsItemFolderType0.from_dict(data)

                return folder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetLinksResponse200DataItemsItemFolderType0 | None, data)

        folder = _parse_folder(d.pop("folder"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = GetLinksResponse200DataItemsItemTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        get_links_response_200_data_items_item = cls(
            id=id,
            domain=domain,
            key=key,
            short_link=short_link,
            destination_url=destination_url,
            title=title,
            description=description,
            image_url=image_url,
            comments=comments,
            created_at=created_at,
            expires_at=expires_at,
            disabled_at=disabled_at,
            test_completed_at=test_completed_at,
            test_variants_count=test_variants_count,
            qr_settings=qr_settings,
            folder=folder,
            tags=tags,
        )

        return get_links_response_200_data_items_item
