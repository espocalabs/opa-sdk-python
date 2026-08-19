from enum import Enum


class GetLinksResponse200DataItemsItemQrSettingsType0ErrorCorrectionLevel(str, Enum):
    H = "H"
    L = "L"
    M = "M"
    Q = "Q"

    def __str__(self) -> str:
        return str(self.value)
