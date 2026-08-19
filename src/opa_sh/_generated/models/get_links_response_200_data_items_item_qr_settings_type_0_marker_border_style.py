from enum import Enum


class GetLinksResponse200DataItemsItemQrSettingsType0MarkerBorderStyle(str, Enum):
    DOT = "dot"
    EXTRA_ROUNDED = "extra-rounded"
    SQUARE = "square"

    def __str__(self) -> str:
        return str(self.value)
