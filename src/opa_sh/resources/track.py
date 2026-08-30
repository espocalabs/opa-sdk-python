"""``opa.track`` — stateless server-side identity and event tracking."""

from typing import Any, Optional

import httpx

from .._internal.request_options import RequestOptions, request_timeout
from .._internal.serialize import build_body
from ..errors import raise_for_response
from ..models import IdentifyResult, TrackConversionResult, TrackEventResult


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

    def lead(
        self,
        *,
        click_id: str,
        event_name: str,
        customer_external_id: str,
        customer_email: Optional[str] = None,
        customer_name: Optional[str] = None,
        customer_avatar: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        options: Optional[RequestOptions] = None,
    ) -> TrackConversionResult:
        """Records a lead using the API's existing conversion wire contract."""
        response = self._client.post(
            "/track/lead",
            json=build_body(
                click_id=click_id,
                event_name=event_name,
                customer_external_id=customer_external_id,
                customer_email=customer_email,
                customer_name=customer_name,
                customer_avatar=customer_avatar,
                metadata=metadata,
            ),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return TrackConversionResult.model_validate(response.json()["data"])

    def sale(
        self,
        *,
        customer_external_id: str,
        amount: int,
        currency: str = "brl",
        event_name: str = "Purchase",
        payment_processor: Optional[str] = None,
        invoice_id: Optional[str] = None,
        click_id: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        options: Optional[RequestOptions] = None,
    ) -> TrackConversionResult:
        """Records a sale; provide ``invoice_id`` so automatic retries are idempotent."""
        response = self._client.post(
            "/track/sale",
            json=build_body(
                customer_external_id=customer_external_id,
                amount=amount,
                currency=currency,
                event_name=event_name,
                payment_processor=payment_processor,
                invoice_id=invoice_id,
                click_id=click_id,
                metadata=metadata,
            ),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return TrackConversionResult.model_validate(response.json()["data"])


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

    async def lead(
        self,
        *,
        click_id: str,
        event_name: str,
        customer_external_id: str,
        customer_email: Optional[str] = None,
        customer_name: Optional[str] = None,
        customer_avatar: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        options: Optional[RequestOptions] = None,
    ) -> TrackConversionResult:
        response = await self._client.post(
            "/track/lead",
            json=build_body(
                click_id=click_id,
                event_name=event_name,
                customer_external_id=customer_external_id,
                customer_email=customer_email,
                customer_name=customer_name,
                customer_avatar=customer_avatar,
                metadata=metadata,
            ),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return TrackConversionResult.model_validate(response.json()["data"])

    async def sale(
        self,
        *,
        customer_external_id: str,
        amount: int,
        currency: str = "brl",
        event_name: str = "Purchase",
        payment_processor: Optional[str] = None,
        invoice_id: Optional[str] = None,
        click_id: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        options: Optional[RequestOptions] = None,
    ) -> TrackConversionResult:
        response = await self._client.post(
            "/track/sale",
            json=build_body(
                customer_external_id=customer_external_id,
                amount=amount,
                currency=currency,
                event_name=event_name,
                payment_processor=payment_processor,
                invoice_id=invoice_id,
                click_id=click_id,
                metadata=metadata,
            ),
            timeout=request_timeout(options),
        )
        raise_for_response(response)
        return TrackConversionResult.model_validate(response.json()["data"])
