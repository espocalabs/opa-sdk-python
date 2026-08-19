from enum import Enum


class GetLinksResponse200DataItemsItemQrSettingsType0LogoMode(str, Enum):
    CUSTOM = "custom"
    DEFAULT = "default"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
