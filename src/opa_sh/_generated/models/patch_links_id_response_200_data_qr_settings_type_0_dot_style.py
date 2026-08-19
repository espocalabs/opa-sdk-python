from enum import Enum


class PatchLinksIdResponse200DataQrSettingsType0DotStyle(str, Enum):
    CLASSY = "classy"
    DOTS = "dots"
    SQUARE = "square"

    def __str__(self) -> str:
        return str(self.value)
