from enum import Enum


class GetLinksResponse200DataItemsItemQrSettingsType0MarkerCenterStyle(str, Enum):
    DOT = "dot"
    SQUARE = "square"

    def __str__(self) -> str:
        return str(self.value)
