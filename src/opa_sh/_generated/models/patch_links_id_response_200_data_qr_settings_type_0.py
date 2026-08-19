from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.patch_links_id_response_200_data_qr_settings_type_0_dot_style import (
    PatchLinksIdResponse200DataQrSettingsType0DotStyle,
)
from ..models.patch_links_id_response_200_data_qr_settings_type_0_error_correction_level import (
    PatchLinksIdResponse200DataQrSettingsType0ErrorCorrectionLevel,
)
from ..models.patch_links_id_response_200_data_qr_settings_type_0_logo_mode import (
    PatchLinksIdResponse200DataQrSettingsType0LogoMode,
)
from ..models.patch_links_id_response_200_data_qr_settings_type_0_marker_border_style import (
    PatchLinksIdResponse200DataQrSettingsType0MarkerBorderStyle,
)
from ..models.patch_links_id_response_200_data_qr_settings_type_0_marker_center_style import (
    PatchLinksIdResponse200DataQrSettingsType0MarkerCenterStyle,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchLinksIdResponse200DataQrSettingsType0")


@_attrs_define
class PatchLinksIdResponse200DataQrSettingsType0:
    """
    Attributes:
        foreground_color (str | Unset):
        background_color (str | Unset):
        error_correction_level (PatchLinksIdResponse200DataQrSettingsType0ErrorCorrectionLevel | Unset):
        logo_mode (PatchLinksIdResponse200DataQrSettingsType0LogoMode | Unset):
        custom_logo_url (str | Unset):
        logo_size (int | Unset):
        dot_style (PatchLinksIdResponse200DataQrSettingsType0DotStyle | Unset):
        marker_border_style (PatchLinksIdResponse200DataQrSettingsType0MarkerBorderStyle | Unset):
        marker_center_style (PatchLinksIdResponse200DataQrSettingsType0MarkerCenterStyle | Unset):
    """

    foreground_color: str | Unset = UNSET
    background_color: str | Unset = UNSET
    error_correction_level: (
        PatchLinksIdResponse200DataQrSettingsType0ErrorCorrectionLevel | Unset
    ) = UNSET
    logo_mode: PatchLinksIdResponse200DataQrSettingsType0LogoMode | Unset = UNSET
    custom_logo_url: str | Unset = UNSET
    logo_size: int | Unset = UNSET
    dot_style: PatchLinksIdResponse200DataQrSettingsType0DotStyle | Unset = UNSET
    marker_border_style: PatchLinksIdResponse200DataQrSettingsType0MarkerBorderStyle | Unset = UNSET
    marker_center_style: PatchLinksIdResponse200DataQrSettingsType0MarkerCenterStyle | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        foreground_color = self.foreground_color

        background_color = self.background_color

        error_correction_level: str | Unset = UNSET
        if not isinstance(self.error_correction_level, Unset):
            error_correction_level = self.error_correction_level.value

        logo_mode: str | Unset = UNSET
        if not isinstance(self.logo_mode, Unset):
            logo_mode = self.logo_mode.value

        custom_logo_url = self.custom_logo_url

        logo_size = self.logo_size

        dot_style: str | Unset = UNSET
        if not isinstance(self.dot_style, Unset):
            dot_style = self.dot_style.value

        marker_border_style: str | Unset = UNSET
        if not isinstance(self.marker_border_style, Unset):
            marker_border_style = self.marker_border_style.value

        marker_center_style: str | Unset = UNSET
        if not isinstance(self.marker_center_style, Unset):
            marker_center_style = self.marker_center_style.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if foreground_color is not UNSET:
            field_dict["foregroundColor"] = foreground_color
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if error_correction_level is not UNSET:
            field_dict["errorCorrectionLevel"] = error_correction_level
        if logo_mode is not UNSET:
            field_dict["logoMode"] = logo_mode
        if custom_logo_url is not UNSET:
            field_dict["customLogoUrl"] = custom_logo_url
        if logo_size is not UNSET:
            field_dict["logoSize"] = logo_size
        if dot_style is not UNSET:
            field_dict["dotStyle"] = dot_style
        if marker_border_style is not UNSET:
            field_dict["markerBorderStyle"] = marker_border_style
        if marker_center_style is not UNSET:
            field_dict["markerCenterStyle"] = marker_center_style

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        foreground_color = d.pop("foregroundColor", UNSET)

        background_color = d.pop("backgroundColor", UNSET)

        _error_correction_level = d.pop("errorCorrectionLevel", UNSET)
        error_correction_level: (
            PatchLinksIdResponse200DataQrSettingsType0ErrorCorrectionLevel | Unset
        )
        if isinstance(_error_correction_level, Unset):
            error_correction_level = UNSET
        else:
            error_correction_level = PatchLinksIdResponse200DataQrSettingsType0ErrorCorrectionLevel(
                _error_correction_level
            )

        _logo_mode = d.pop("logoMode", UNSET)
        logo_mode: PatchLinksIdResponse200DataQrSettingsType0LogoMode | Unset
        if isinstance(_logo_mode, Unset):
            logo_mode = UNSET
        else:
            logo_mode = PatchLinksIdResponse200DataQrSettingsType0LogoMode(_logo_mode)

        custom_logo_url = d.pop("customLogoUrl", UNSET)

        logo_size = d.pop("logoSize", UNSET)

        _dot_style = d.pop("dotStyle", UNSET)
        dot_style: PatchLinksIdResponse200DataQrSettingsType0DotStyle | Unset
        if isinstance(_dot_style, Unset):
            dot_style = UNSET
        else:
            dot_style = PatchLinksIdResponse200DataQrSettingsType0DotStyle(_dot_style)

        _marker_border_style = d.pop("markerBorderStyle", UNSET)
        marker_border_style: PatchLinksIdResponse200DataQrSettingsType0MarkerBorderStyle | Unset
        if isinstance(_marker_border_style, Unset):
            marker_border_style = UNSET
        else:
            marker_border_style = PatchLinksIdResponse200DataQrSettingsType0MarkerBorderStyle(
                _marker_border_style
            )

        _marker_center_style = d.pop("markerCenterStyle", UNSET)
        marker_center_style: PatchLinksIdResponse200DataQrSettingsType0MarkerCenterStyle | Unset
        if isinstance(_marker_center_style, Unset):
            marker_center_style = UNSET
        else:
            marker_center_style = PatchLinksIdResponse200DataQrSettingsType0MarkerCenterStyle(
                _marker_center_style
            )

        patch_links_id_response_200_data_qr_settings_type_0 = cls(
            foreground_color=foreground_color,
            background_color=background_color,
            error_correction_level=error_correction_level,
            logo_mode=logo_mode,
            custom_logo_url=custom_logo_url,
            logo_size=logo_size,
            dot_style=dot_style,
            marker_border_style=marker_border_style,
            marker_center_style=marker_center_style,
        )

        return patch_links_id_response_200_data_qr_settings_type_0
