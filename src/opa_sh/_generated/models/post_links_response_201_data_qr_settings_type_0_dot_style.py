from enum import Enum


class PostLinksResponse201DataQrSettingsType0DotStyle(str, Enum):
    CLASSY = "classy"
    DOTS = "dots"
    SQUARE = "square"

    def __str__(self) -> str:
        return str(self.value)
