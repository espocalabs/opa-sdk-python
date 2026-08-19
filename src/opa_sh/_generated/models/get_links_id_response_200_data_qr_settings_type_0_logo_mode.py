from enum import Enum


class GetLinksIdResponse200DataQrSettingsType0LogoMode(str, Enum):
    CUSTOM = "custom"
    DEFAULT = "default"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
