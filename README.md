# opa-sh

[![PyPI version](https://img.shields.io/pypi/v/opa-sh.svg)](https://pypi.org/project/opa-sh/)
[![CI](https://github.com/espocalabs/opa-sdk-python/actions/workflows/ci.yml/badge.svg)](https://github.com/espocalabs/opa-sdk-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/opa-sh.svg)](https://pypi.org/project/opa-sh/)

Official Python SDK for the [Opa link shortener](https://opa.sh) API (`https://api.opa.sh/v1`).

Resource-oriented, fully typed (`pydantic` v2 models, `py.typed`), sync and
async clients side by side, idiomatic Python error handling — failures raise
typed exceptions, not a `Result`/tuple you have to unwrap.

## Install

```bash
pip install opa-sh
# or: uv add opa-sh
# or: poetry add opa-sh
```

## Quick start

```python
from opa_sh import OpaClient

opa = OpaClient(api_key="opa_...")

link = opa.links.create(
    destination_url="https://example.com/black-friday",
    domain="opa.sh",
    tag_ids=["tag_campaign2026"],
)

print(link.short_link)
print(link.destination_url)

opa.close()
```

Or as a context manager, which closes the underlying connection pool for you:

```python
with OpaClient(api_key="opa_...") as opa:
    link = opa.links.create(destination_url="https://example.com")
    print(link.short_link)
```

### Async

Every resource method has an async counterpart on `AsyncOpaClient` — same
names, same arguments, `await`ed:

```python
import asyncio
from opa_sh import AsyncOpaClient


async def main() -> None:
    async with AsyncOpaClient(api_key="opa_...") as opa:
        link = await opa.links.create(destination_url="https://example.com")
        print(link.short_link)


asyncio.run(main())
```

Get your API key at [opa.sh/settings/api-keys](https://app.opa.sh/settings/api-keys).

## Authentication

Server-side only — never expose a key from a browser bundle or a mobile app:

```python
opa = OpaClient(api_key="opa_...")
```

Base URL defaults to `https://api.opa.sh/v1`. Override it for staging or a
self-hosted instance:

```python
opa = OpaClient(api_key="...", base_url="https://api.staging.opa.sh/v1")
```

## Error handling

Every failed call raises a subclass of `OpaError` — a Python-idiomatic
`raise`-based SDK (mirrors Stripe, OpenAI, Anthropic, `boto3`), not a
`Result`/`Either` pattern. Catch `OpaError` to handle any SDK failure, or a
specific subclass to handle one case:

```python
from opa_sh import OpaClient
from opa_sh.errors import NotFoundError, RateLimitError, ValidationError, OpaError

opa = OpaClient(api_key="...")

try:
    link = opa.links.get("lnk_xxx")
except NotFoundError:
    ...  # 404
except ValidationError as e:
    print(e.details)  # e.g. {"issues": [{"path": "destinationUrl", "message": "Required"}]}
except RateLimitError as e:
    print("retry after", e.retry_after, "seconds")
except OpaError as e:
    # catch-all: e.code, e.status, e.message, e.details
    print(e.code, e.status, e.message)
```

| Exception               | HTTP status | Meaning                                                          |
| ------------------------ | ----------- | ----------------------------------------------------------------- |
| `AuthenticationError`    | 401         | Missing or invalid API key.                                       |
| `PermissionDeniedError`  | 403         | Valid credential, insufficient permission or plan capability.     |
| `NotFoundError`          | 404         | The resource doesn't exist.                                       |
| `ConflictError`          | 409         | E.g. a custom `key` already taken, or no domain available.        |
| `ValidationError`        | 422         | Request body or query params failed validation.                   |
| `RateLimitError`         | 429         | Rate limit hit — see `.retry_after` (seconds).                     |
| `ServerError`            | 5xx         | Opa API had an internal error. Safe to retry.                     |
| `NetworkError`           | —           | Connection reset, DNS failure, timeout — never reached the API.    |

All of the above subclass `OpaError`, which subclasses `Exception`.

## Resources

### Links

```python
# Create — only destination_url is required
link = opa.links.create(
    destination_url="https://example.com",
    domain="opa.sh",
    key="custom-slug",  # optional — omit for a random key
    tag_ids=["tag_xxx"],
    password="s3cret",
    expires_at="2027-01-01T00:00:00Z",
)

# Read
link = opa.links.get("lnk_xxx")

# Update — destination_url and domain are required (full replace, not a merge patch)
link = opa.links.update("lnk_xxx", destination_url="https://example.com/new", domain="opa.sh")

# Lifecycle
opa.links.archive("lnk_xxx")  # reversible — the link keeps resolving
opa.links.restore("lnk_xxx")
opa.links.duplicate("lnk_xxx")

# List — single page
page = opa.links.list(search="marketing", limit=50)
print(page.items, page.has_more, page.next_cursor)

# List — every page, auto-paginating (memory-safe generator)
for link in opa.links.list_all(search="marketing"):
    print(link.short_link, link.tags)

# Bulk operations
opa.links.bulk_archive(["lnk_a", "lnk_b", "lnk_c"])
opa.links.bulk_restore(["lnk_a", "lnk_b"])
opa.links.bulk_move(["lnk_a", "lnk_b"], "folder_xxx")
opa.links.bulk_tag(["lnk_a", "lnk_b"], ["tag_q1"])
```

### Analytics

```python
summary = opa.analytics.summary(from_="2026-01-01", to="2026-01-31", link_id="lnk_xxx")
print(summary.clicks, summary.unique_clicks)

timeseries = opa.analytics.timeseries(from_="2026-01-01", to="2026-01-31", link_id="lnk_xxx")
for point in timeseries.points:
    print(point.date, point.clicks)

# Raw click events — single page or auto-paginating
page = opa.analytics.events(link_id="lnk_xxx", limit=100)
for event in opa.analytics.events_all(link_id="lnk_xxx"):
    print(event.timestamp, event.country, event.device)
```

`from_`/`to` are ISO dates (max 366-day range). The trailing underscore on
`from_` avoids colliding with the `from` keyword — it's sent as `from` on the
wire.

### Domains

```python
domains = opa.domains.list()
for domain in domains:
    print(domain.domain, domain.primary, domain.verified)
```

Not paginated — this list is small by nature (verified custom domains plus
the shared app domain).

## Retries and rate limiting

Automatic exponential backoff (with jitter) on `5xx` and `429`, respecting the
`Retry-After` header. Never retries other `4xx` statuses, so idempotent
semantics are preserved for `POST`. Transport-level failures (DNS, connection
reset) are retried the same way, then surfaced as `NetworkError` if every
attempt fails.

```python
opa = OpaClient(
    api_key="...",
    retries=3,  # default: 3
    retry_delay=1.0,  # default: 1.0s base, doubles each attempt (capped at 20s)
)
```

## Pagination

Every `list`-style method comes in two shapes:

- `list(...)` (or `events(...)`) — returns a single `Page[T]`, with
  `.items`, `.has_more`, and `.next_cursor`.
- `list_all(...)` (or `events_all(...)`) — a generator that walks every page
  automatically, yielding items one at a time. Memory-safe: it never holds
  more than one page in memory.

```python
# Sync generator
for link in opa.links.list_all():
    ...

# Async generator — same method name, `async for`
async for link in opa.links.list_all():
    ...
```

An error partway through iteration raises the same `OpaError` subclass you'd
get from the eager `list()` call — you already handle that exception type, so
this doesn't introduce a new failure mode.

## Custom httpx client

For advanced configuration — custom transports, proxies, mTLS, connection
pooling tuned for your workload — pass your own `httpx.Client` /
`httpx.AsyncClient`. The SDK merges the auth header into it and does not
override anything else you've configured:

```python
import httpx
from opa_sh import OpaClient

custom_client = httpx.Client(
    base_url="https://api.opa.sh/v1",
    limits=httpx.Limits(max_connections=50),
    proxy="http://localhost:8080",
)
opa = OpaClient(api_key="...", http_client=custom_client)
```

Note: the SDK's own retry transport (`opa_sh.retry.RetryTransport`) only
applies when it builds the `httpx.Client` itself. A custom `http_client` is
responsible for its own retry/backoff behavior.

## Types

Every response is a `pydantic` v2 model (`Link`, `LinkSummary`, `Domain`,
`AnalyticsSummary`, `AnalyticsTimeseries`, `AnalyticsEvent`, ...) with
`snake_case` attributes and full type hints — the package ships a `py.typed`
marker, so `mypy`/`pyright` pick up types automatically in consuming projects.

```python
from opa_sh import Link, LinkSummary, Domain, Page


def handle(link: Link) -> None:
    print(link.short_link)
```

## Runtime support

- Python 3.9, 3.10, 3.11, 3.12, 3.13
- CPython and PyPy (no C-extension dependencies beyond what `httpx`/`pydantic` already require)

## Contributing

The SDK's request/response shapes are hand-written `pydantic` models in
`src/opa_sh/models.py`, kept in sync by hand against `openapi/v1.json` (the
raw OpenAPI spec has no named component schemas, so a mechanical generator
produces synthetic, unusable names — see that file's module docstring for
detail). `src/opa_sh/_generated/` is a raw client generated by
[`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client)
from the same spec; it's committed as a diff target for the `sync-openapi`
workflow but is **not imported at runtime**.

`openapi/v1.json` is refreshed daily from `https://api.opa.sh/v1/openapi` via
the `sync-openapi` workflow, which opens a PR when the spec changes — extend
it with matching updates to `models.py` and the relevant `resources/*.py`
methods.

```bash
git clone https://github.com/espocalabs/opa-sdk-python
cd opa-sdk-python
uv sync --all-extras
uv run pytest
uv run ruff check .
uv run mypy src
uv build
```

## License

[MIT](./LICENSE) © Espoca Labs
