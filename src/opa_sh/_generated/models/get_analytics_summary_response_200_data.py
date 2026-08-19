from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_analytics_summary_response_200_data_range import (
        GetAnalyticsSummaryResponse200DataRange,
    )


T = TypeVar("T", bound="GetAnalyticsSummaryResponse200Data")


@_attrs_define
class GetAnalyticsSummaryResponse200Data:
    """
    Attributes:
        range_ (GetAnalyticsSummaryResponse200DataRange):
        clamped (bool): True when `range.from` was moved forward because the requested period reached further back than
            the organization's current plan retains analytics for (`analyticsRetentionDays`) — `range` above reflects the
            EFFECTIVE (post-clamp) period the numbers were computed over, not necessarily the requested `from`.
        clicks (float):
        unique_clicks (float):
    """

    range_: GetAnalyticsSummaryResponse200DataRange
    clamped: bool
    clicks: float
    unique_clicks: float

    def to_dict(self) -> dict[str, Any]:
        range_ = self.range_.to_dict()

        clamped = self.clamped

        clicks = self.clicks

        unique_clicks = self.unique_clicks

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "range": range_,
                "clamped": clamped,
                "clicks": clicks,
                "uniqueClicks": unique_clicks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_analytics_summary_response_200_data_range import (
            GetAnalyticsSummaryResponse200DataRange,
        )

        d = dict(src_dict)
        range_ = GetAnalyticsSummaryResponse200DataRange.from_dict(d.pop("range"))

        clamped = d.pop("clamped")

        clicks = d.pop("clicks")

        unique_clicks = d.pop("uniqueClicks")

        get_analytics_summary_response_200_data = cls(
            range_=range_,
            clamped=clamped,
            clicks=clicks,
            unique_clicks=unique_clicks,
        )

        return get_analytics_summary_response_200_data
