"""``opa.track`` — stateless server-side identity and event tracking."""

import httpx


class TrackResource:
    """Synchronous ``opa.track`` resource."""

    def __init__(self, client: httpx.Client) -> None:
        self._client = client


class AsyncTrackResource:
    """Async equivalent of :class:`TrackResource`."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client
