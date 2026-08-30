# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-08-30

### Added

- Stateless `opa.track` and async counterpart with `identify`, `event`, `lead`,
  and `sale` operations.
- Typed Pydantic response models for identity reconciliation, product events,
  customers, and conversions.
- Anonymous-to-known identity handoff without storing a current user in the
  shared SDK client.

`event_id` and `invoice_id` are the idempotency keys for automatic retries and
webhook redelivery. The tracking contract remains hand-written until the
canonical OpenAPI document publishes these endpoints.

## [0.2.1] - 2026-08-19

Built `examples/full_test.py` — an end-to-end smoke test that exercises
every public method of both `OpaClient` and `AsyncOpaClient` against the
**real** Opa API (not mocks) — and ran it. It found one real request-body
bug, fixed here, plus two backend-side inconsistencies that aren't fixable
from this repo (noted below for the API team).

### Fixed

- `opa.links.create()` / `opa.links.update()` sent `targeting` and
  `qrSettings` as nested JSON objects when passed a `LinkTargeting` /
  `QrSettings` instance. The API's request schema (confirmed against both
  `openapi/v1.json`, which declares these fields as `type: string`, and
  the live API, which 422s with `"Invalid input: expected string, received
  object"` on both fields) expects a **JSON-encoded string**, not an
  object — the response shape is an object, but the request shape isn't
  the same shape. `build_body()` now `json.dumps()`s any
  `pydantic.BaseModel` value instead of passing its dict through directly.
  This was a real, previously-untested bug: no existing test asserted on
  the serialized bytes for either field, so it shipped unnoticed in 0.2.0.
- Corrected `ConflictError`'s docstring, which claimed a custom `key`
  already taken on a domain raises it. A live check found that scenario
  currently returns `500 internal_error` (surfacing as `ServerError`), not
  409 — and `openapi/v1.json` doesn't document a 409 response for any
  endpoint. The exception class is kept (for any 409 the API does return,
  e.g. `no_domain_available`), but the misleading example is gone.

### Known backend-side gaps (not SDK bugs — logged for the API team, no code
change possible here)

- `GET /links/{id}` archives via `DELETE /links/{id}` (`ArchiveLinkResult`
  reports `archived: true`), but a subsequent `GET /links?archived=true` /
  `archived=false` returns the same link in both, and `LinkSummary.disabled_at`
  never populates. Either the archived-state filter isn't applied
  server-side, or there's replication lag longer than immediate-consistency
  callers would expect.
- `GET /domains` returns `[]` for at least one real account that
  successfully creates links against the implicit default domain — contradicts
  its own documented contract ("verified custom domains plus the shared
  app domain").
- Creating a link with a `key` that's already taken returns `500
  internal_error` instead of a `409`/`422` — looks like an unhandled
  database unique-constraint violation rather than a validated conflict
  response.

### Added

- `examples/` — a runnable smoke-test project (own `pyproject.toml`,
  `.env.example`, README) that installs `opa-sh` editable from the parent
  directory and runs `full_test.py` against a real account. Not part of
  the published package.
- 6 new regression tests (`tests/test_serialize.py`, plus 2 more in
  `tests/test_links.py`) locking in the `targeting`/`qrSettings`
  JSON-string serialization fix.

## [0.2.0] - 2026-08-19

### Breaking changes

Aligned the SDK with the real Opa API. A cross-check of the SDK against
`openapi/v1.json` and the `/api/v1` backend (see the `opa` repo's
`docs/sdk-audit-2026-08-19.md`) found a handful of remaining discrepancies
after 0.1.1 — mostly documentation/test drift, plus one real endpoint move:

- Bulk endpoints moved from `POST /links/bulk-{action}` to
  `POST /links/bulk/{action}` (`bulk-archive` → `bulk/archive`, and the
  same for `restore`, `move`, `tag`) — mirrors a backend route rename
  landing in the same release window. `LinksResource`/`AsyncLinksResource`
  now call the new paths; the request/response bodies are unchanged.
- `analytics.query()` renamed to `analytics.summary()` (sync and async),
  matching the real endpoint name (`GET /analytics/summary`). Signature
  (`from_`, `to`, and the rest of the filters) is unchanged.
- `ValidationError` now maps only to HTTP 422. The API has no code path
  that ever produces a 400 for validation failures — `validation_error` is
  fixed at 422 in the backend's status map — so the SDK no longer misroutes
  a hypothetical 400 into `ValidationError`; it now falls through to the
  generic `OpaError`, consistent with any other unmapped 4xx.
- Corrected the documented API key prefix from `opa_live_...` to `opa_...`
  (README, docstrings, tests) — the API has never had a live/test key
  distinction; this was a documentation-only inaccuracy, not a runtime
  validation change.

No compatibility shims — the SDK was greenfield with zero external
consumers at the time of this release.

### Confirmed already correct (no change needed)

A few items flagged in the audit as historically common SDK-doc mistakes
turned out to already be right in this codebase, so nothing changed for
them: `Link`/`LinkSummary` already used `short_link` (never `short_url`)
and never exposed invented `qr_code_url`/`clicks` fields; `list()` already
used `search` (not a nonexistent `tag` filter); `analytics.summary()`
(formerly `.query()`) already took `from_`/`to` ISO dates with no fabricated
`range`/`interval` presets; and the pagination cursor is deliberately
exposed as `Page.next_cursor` — a Python-idiomatic rename of the wire
field `pagination.next`, the same pattern already used for `short_link` and
`unique_clicks` — not a bug.

## [0.1.1] - 2026-08-19

### Fixed

- Removed the `bearer_token` client option. The Opa API only accepts
  `x-api-key` authentication — bearer was exposed by mistake and would
  result in rejected requests. `api_key` is now required at construction.
- Removed the `idempotency_key` option from `RequestOptions`. The Opa API
  does not support an `Idempotency-Key` header — it was exposed by mistake
  and had no effect on the server. `RequestOptions` now only carries
  `timeout`.

## [0.1.0] - 2026-08-19

### Added

- Initial release.
- `OpaClient` (sync) and `AsyncOpaClient` (async), both backed by `httpx`.
- `opa.links` — create, get, update, archive, restore, duplicate, list
  (single page and auto-paginating), and bulk archive/restore/move/tag.
- `opa.analytics` — summary query, timeseries, and raw click events (single
  page and auto-paginating).
- `opa.domains` — list domains available to shorten links under.
- Exception hierarchy rooted at `OpaError`, with `AuthenticationError`,
  `PermissionDeniedError`, `NotFoundError`, `ConflictError`,
  `ValidationError`, `RateLimitError`, `ServerError`, and `NetworkError`.
- Automatic retry with exponential backoff on `5xx`/`429`, honoring
  `Retry-After`.
- Idempotency key support (`RequestOptions.idempotency_key`) on mutating
  calls.
- Full type hints, `pydantic` v2 response models, `py.typed` marker.
- Python 3.9+ support.
