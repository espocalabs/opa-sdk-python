from collections.abc import Iterator

import pytest
import respx

BASE_URL = "https://api.opa.sh/v1"


@pytest.fixture
def mock_api() -> Iterator[respx.MockRouter]:
    with respx.mock(base_url=BASE_URL, assert_all_called=False) as router:
        yield router
