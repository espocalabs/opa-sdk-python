# `full_test.py`

An end-to-end smoke test that runs every public method of `opa-sh` — sync
and async — against the **real** Opa API. It creates a handful of throwaway
links tagged `sdk-py-test-<timestamp>`, exercises the full surface area, and
archives everything it created in a `finally` block.

## Run it

```bash
cd examples
uv venv
uv pip install -e ..            # install the SDK from the parent dir, editable
uv pip install python-dotenv    # only needed for .env loading
cp .env.example .env
# edit .env and set OPA_API_KEY=opa_...
uv run python full_test.py
```

Or, without a persistent venv:

```bash
cd examples
OPA_API_KEY=opa_... uv run --with-editable .. --with python-dotenv python full_test.py
```

Exits `0` if every call succeeded, `1` if anything failed.

## What it does

- `opa.domains.list()`
- `opa.links.create/get/update/archive/restore/duplicate/list/list_all`
- `opa.links.bulk_archive/bulk_restore` always; `bulk_tag`/`bulk_move` only
  when the account already has an existing tag/folder to reuse (skipped
  otherwise — the SDK has no tag/folder creation API to set one up from
  scratch)
- `opa.analytics.summary/timeseries/events` over a rolling 7-day window
- The same list, again, on `AsyncOpaClient`

Every call is logged as `✓ label → detail` or `✗ label → ErrorType: message`.
Skipped calls (missing prerequisite data on the account) print as `– label`.
