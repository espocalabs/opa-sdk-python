from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetAnalyticsEventsResponse200DataItemsItem")


@_attrs_define
class GetAnalyticsEventsResponse200DataItemsItem:
    """
    Attributes:
        timestamp (str):
        link_id (str):
        country (str):
        city (str):
        device (str):
        os (str):
        browser (str):
        referer_domain (str):
        referer_url (str):
        utm_source (str):
        utm_campaign (str):
        variant_url (str):
        click_id (str):
    """

    timestamp: str
    link_id: str
    country: str
    city: str
    device: str
    os: str
    browser: str
    referer_domain: str
    referer_url: str
    utm_source: str
    utm_campaign: str
    variant_url: str
    click_id: str

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        link_id = self.link_id

        country = self.country

        city = self.city

        device = self.device

        os = self.os

        browser = self.browser

        referer_domain = self.referer_domain

        referer_url = self.referer_url

        utm_source = self.utm_source

        utm_campaign = self.utm_campaign

        variant_url = self.variant_url

        click_id = self.click_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "timestamp": timestamp,
                "linkId": link_id,
                "country": country,
                "city": city,
                "device": device,
                "os": os,
                "browser": browser,
                "refererDomain": referer_domain,
                "refererUrl": referer_url,
                "utmSource": utm_source,
                "utmCampaign": utm_campaign,
                "variantUrl": variant_url,
                "clickId": click_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        link_id = d.pop("linkId")

        country = d.pop("country")

        city = d.pop("city")

        device = d.pop("device")

        os = d.pop("os")

        browser = d.pop("browser")

        referer_domain = d.pop("refererDomain")

        referer_url = d.pop("refererUrl")

        utm_source = d.pop("utmSource")

        utm_campaign = d.pop("utmCampaign")

        variant_url = d.pop("variantUrl")

        click_id = d.pop("clickId")

        get_analytics_events_response_200_data_items_item = cls(
            timestamp=timestamp,
            link_id=link_id,
            country=country,
            city=city,
            device=device,
            os=os,
            browser=browser,
            referer_domain=referer_domain,
            referer_url=referer_url,
            utm_source=utm_source,
            utm_campaign=utm_campaign,
            variant_url=variant_url,
            click_id=click_id,
        )

        return get_analytics_events_response_200_data_items_item
