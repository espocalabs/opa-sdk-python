import pytest

from opa_sh.models import Page
from opa_sh.pagination import apaginate, paginate


def _page(items: list, has_more: bool, next_cursor: "str | None") -> Page:
    return Page(items=items, has_more=has_more, next_cursor=next_cursor)


def test_paginate_walks_every_page() -> None:
    pages = {
        "": _page([1, 2], True, "cursor-1"),
        "cursor-1": _page([3, 4], True, "cursor-2"),
        "cursor-2": _page([5], False, None),
    }

    def fetch_page(cursor: str) -> Page:
        return pages[cursor]

    assert list(paginate(fetch_page)) == [1, 2, 3, 4, 5]


def test_paginate_single_page() -> None:
    def fetch_page(cursor: str) -> Page:
        return _page(["a", "b"], False, None)

    assert list(paginate(fetch_page)) == ["a", "b"]


def test_paginate_empty_page() -> None:
    def fetch_page(cursor: str) -> Page:
        return _page([], False, None)

    assert list(paginate(fetch_page)) == []


def test_paginate_stops_if_has_more_but_no_next_cursor() -> None:
    """A page claiming `has_more=True` with no cursor shouldn't infinite-loop."""

    def fetch_page(cursor: str) -> Page:
        return _page([1], True, None)

    assert list(paginate(fetch_page)) == [1]


@pytest.mark.asyncio
async def test_apaginate_walks_every_page() -> None:
    pages = {
        "": _page([1, 2], True, "cursor-1"),
        "cursor-1": _page([3], False, None),
    }

    async def fetch_page(cursor: str) -> Page:
        return pages[cursor]

    items = [item async for item in apaginate(fetch_page)]
    assert items == [1, 2, 3]


@pytest.mark.asyncio
async def test_apaginate_propagates_errors() -> None:
    class Boom(Exception):
        pass

    async def fetch_page(cursor: str) -> Page:
        raise Boom("page fetch failed")

    with pytest.raises(Boom):
        async for _ in apaginate(fetch_page):
            pass
