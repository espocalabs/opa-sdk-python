"""Sync and async iteration helpers for cursor-paginated list endpoints.

Every resource's ``list`` method returns a single :class:`~opa_sh.models.Page`.
The ``list_all``/``alist_all`` methods build on top of it here, yielding
items across every page until the cursor runs out. Iteration raises the
underlying :class:`~opa_sh.errors.OpaError` if a page fails partway through —
callers already need to handle that exception type for the eager ``list``
call, so this doesn't introduce a new failure mode.
"""

from collections.abc import AsyncIterator, Awaitable, Iterator
from typing import Callable, TypeVar

from .models import Page

T = TypeVar("T")


def paginate(fetch_page: Callable[[str], Page[T]], first_cursor: str = "") -> Iterator[T]:
    """Walks every page of a sync list endpoint, yielding items one at a time.

    Args:
        fetch_page: Fetches one page given the cursor to resume from
            (``""`` for the first page).
        first_cursor: The initial cursor value, normally left as ``""``.
    """
    cursor = first_cursor
    while True:
        page = fetch_page(cursor)
        yield from page.items
        if not page.has_more or not page.next_cursor:
            return
        cursor = page.next_cursor


async def apaginate(
    fetch_page: Callable[[str], Awaitable[Page[T]]], first_cursor: str = ""
) -> AsyncIterator[T]:
    """Async equivalent of :func:`paginate` — walks every page via ``async for``."""
    cursor = first_cursor
    while True:
        page = await fetch_page(cursor)
        for item in page.items:
            yield item
        if not page.has_more or not page.next_cursor:
            return
        cursor = page.next_cursor
