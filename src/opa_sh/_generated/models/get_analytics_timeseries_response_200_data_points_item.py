from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetAnalyticsTimeseriesResponse200DataPointsItem")


@_attrs_define
class GetAnalyticsTimeseriesResponse200DataPointsItem:
    """
    Attributes:
        date (str):
        clicks (float):
    """

    date: str
    clicks: float

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        clicks = self.clicks

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "clicks": clicks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        clicks = d.pop("clicks")

        get_analytics_timeseries_response_200_data_points_item = cls(
            date=date,
            clicks=clicks,
        )

        return get_analytics_timeseries_response_200_data_points_item
