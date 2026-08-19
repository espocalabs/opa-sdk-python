from enum import Enum


class PostLinksIdDuplicateResponse201DataQrSettingsType0ErrorCorrectionLevel(str, Enum):
    H = "H"
    L = "L"
    M = "M"
    Q = "Q"

    def __str__(self) -> str:
        return str(self.value)
