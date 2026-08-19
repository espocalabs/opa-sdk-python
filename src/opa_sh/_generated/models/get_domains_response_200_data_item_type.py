from enum import Enum


class GetDomainsResponse200DataItemType(str, Enum):
    APP_DOMAIN = "APP_DOMAIN"
    USER_DOMAIN = "USER_DOMAIN"

    def __str__(self) -> str:
        return str(self.value)
