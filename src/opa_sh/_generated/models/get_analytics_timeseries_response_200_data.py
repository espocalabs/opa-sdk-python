from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_analytics_timeseries_response_200_data_points_item import (
        GetAnalyticsTimeseriesResponse200DataPointsItem,
    )
    from ..models.get_analytics_timeseries_response_200_data_range import (
        GetAnalyticsTimeseriesResponse200DataRange,
    )


T = TypeVar("T", bound="GetAnalyticsTimeseriesResponse200Data")


@_attrs_define
class GetAnalyticsTimeseriesResponse200Data:
    """
    Attributes:
        range_ (GetAnalyticsTimeseriesResponse200DataRange):
        clamped (bool): Same meaning as `analytics/summary`'s `clamped` — see that endpoint's response schema.
        points (list[GetAnalyticsTimeseriesResponse200DataPointsItem]):
    """

    range_: GetAnalyticsTimeseriesResponse200DataRange
    clamped: bool
    points: list[GetAnalyticsTimeseriesResponse200DataPointsItem]

    def to_dict(self) -> dict[str, Any]:
        range_ = self.range_.to_dict()

        clamped = self.clamped

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "range": range_,
                "clamped": clamped,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_analytics_timeseries_response_200_data_points_item import (
            GetAnalyticsTimeseriesResponse200DataPointsItem,
        )
        from ..models.get_analytics_timeseries_response_200_data_range import (
            GetAnalyticsTimeseriesResponse200DataRange,
        )

        d = dict(src_dict)
        range_ = GetAnalyticsTimeseriesResponse200DataRange.from_dict(d.pop("range"))

        clamped = d.pop("clamped")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = GetAnalyticsTimeseriesResponse200DataPointsItem.from_dict(
                points_item_data
            )

            points.append(points_item)

        get_analytics_timeseries_response_200_data = cls(
            range_=range_,
            clamped=clamped,
            points=points,
        )

        return get_analytics_timeseries_response_200_data
