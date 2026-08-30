"""``opa.track`` — stateless server-side identity and event tracking."""

from typing import Any, Optional

import httpx

from .._internal.request_options import RequestOptions, request_timeout
from .._internal.serialize import build_body
from ..errors import raise_for_response
from ..models import IdentifyResult, TrackEventResult


class TrackResource:
    """Synchronous ``opa.track`` resource."""

    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def identify(
        self,
        *,
        anonymous_id: str,
        external_id: str,
        traits: Optional[dict[str, Any]] = None,
        click_id: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> IdentifyResult:
        """Binds an anonymous browser identity to a caller-owned external identity."""
        response = self._client.post(
            "/track/identify",
            json=build_body(
                anonymous_id=anonymous_id,
                external_id=external_id,
                traits=traits,
                click_id=click_id,
            ),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return IdentifyResult.model_validate(response.json()["data"])

    def event(
        self,
        *,
        event_id: str,
        event_name: str,
        anonymous_id: Optional[str] = None,
        external_id: Optional[str] = None,
        click_id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        occurred_at: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> TrackEventResult:
        """Records an idempotent event for an explicit anonymous or external identity."""
        response = self._client.post(
            "/track/event",
            json=build_body(
                event_id=event_id,
                event_name=event_name,
                anonymous_id=anonymous_id,
                external_id=external_id,
                click_id=click_id,
                properties=properties,
                occurred_at=occurred_at,
            ),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return TrackEventResult.model_validate(response.json()["data"])


class AsyncTrackResource:
    """Async equivalent of :class:`TrackResource`."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client

    async def identify(
        self,
        *,
        anonymous_id: str,
        external_id: str,
        traits: Optional[dict[str, Any]] = None,
        click_id: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> IdentifyResult:
        response = await self._client.post(
            "/track/identify",
            json=build_body(
                anonymous_id=anonymous_id,
                external_id=external_id,
                traits=traits,
                click_id=click_id,
            ),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return IdentifyResult.model_validate(response.json()["data"])

    async def event(
        self,
        *,
        event_id: str,
        event_name: str,
        anonymous_id: Optional[str] = None,
        external_id: Optional[str] = None,
        click_id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        occurred_at: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> TrackEventResult:
        response = await self._client.post(
            "/track/event",
            json=build_body(
                event_id=event_id,
                event_name=event_name,
                anonymous_id=anonymous_id,
                external_id=external_id,
                click_id=click_id,
                properties=properties,
                occurred_at=occurred_at,
            ),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return TrackEventResult.model_validate(response.json()["data"])
