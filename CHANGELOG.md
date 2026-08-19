# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
