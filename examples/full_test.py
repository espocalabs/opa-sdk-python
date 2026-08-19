#!/usr/bin/env python3
"""End-to-end smoke test for `opa-sh`, run against the *real* Opa API.

Exercises every public method on both `OpaClient` (sync) and
`AsyncOpaClient` (async), logs a checkmark/cross for each call, and cleans
up everything it creates in a `finally` block. Any inconsistency between
what the SDK sends/expects and what the real API actually does shows up
here as a `✗` line.

Usage:
    cd examples
    uv run --with-editable .. --with python-dotenv python full_test.py

Requires `OPA_API_KEY` in the environment (or a `.env` file next to this
script — see `.env.example`).
"""

from __future__ import annotations

import asyncio
import os
import sys
import time
import traceback
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from opa_sh import (
    AsyncOpaClient,
    LinkTargeting,
    OpaClient,
    OpaError,
    QrSettings,
    RequestOptions,
)

RUN_ID = time.strftime("%Y%m%d%H%M%S")
SUFFIX = f"sdk-py-test-{RUN_ID}"
CALL_TIMEOUT = 30.0


# --------------------------------------------------------------------------- #
# Result tracking
# --------------------------------------------------------------------------- #


@dataclass
class Results:
    passed: list[str] = field(default_factory=list)
    failed: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)

    def ok(self, label: str) -> None:
        self.passed.append(label)

    def fail(self, label: str) -> None:
        self.failed.append(label)

    def skip(self, label: str) -> None:
        self.skipped.append(label)


RESULTS = Results()


def log_ok(label: str, detail: str = "") -> None:
    RESULTS.ok(label)
    suffix = f" → {detail}" if detail else ""
    print(f"✓ {label}{suffix}")


def log_fail(label: str, error: BaseException) -> None:
    RESULTS.fail(label)
    print(f"✗ {label} → {error.__class__.__name__}: {error}")


def log_skip(label: str, reason: str) -> None:
    RESULTS.skip(label)
    print(f"– {label} (skipped: {reason})")


def step(label: str, fn: Callable[[], Any]) -> Any:
    """Runs `fn`, logging a pass/fail line. Returns the value, or `None` on failure."""
    try:
        value = fn()
        detail = _summarize(value)
        log_ok(label, detail)
        return value
    except Exception as exc:  # noqa: BLE001 - we want to catch and log everything
        log_fail(label, exc)
        return None


async def astep(label: str, coro: Any) -> Any:
    """Async equivalent of :func:`step`."""
    try:
        value = await coro
        detail = _summarize(value)
        log_ok(label, detail)
        return value
    except Exception as exc:  # noqa: BLE001
        log_fail(label, exc)
        return None


def _summarize(value: Any) -> str:
    if value is None:
        return ""
    if hasattr(value, "short_link"):
        return f"link.short_link = {value.short_link!r}"
    if hasattr(value, "id") and hasattr(value, "archived"):
        return f"id={value.id!r} archived={value.archived!r}"
    if hasattr(value, "clicks"):
        return f"clicks={value.clicks} unique_clicks={getattr(value, 'unique_clicks', '?')}"
    if hasattr(value, "points"):
        return f"{len(value.points)} points"
    if hasattr(value, "items"):
        return f"{len(value.items)} items, has_more={value.has_more}"
    if isinstance(value, list):
        return f"{len(value)} items"
    if hasattr(value, "archived_count"):
        return f"archived_count={value.archived_count}"
    if hasattr(value, "restored_count"):
        return f"restored_count={value.restored_count}"
    if hasattr(value, "moved_count"):
        return f"moved_count={value.moved_count}"
    if hasattr(value, "tagged_count"):
        return f"tagged_count={value.tagged_count}"
    return repr(value)[:120]


# --------------------------------------------------------------------------- #
# Sync phase
# --------------------------------------------------------------------------- #


def run_sync_tests(api_key: str) -> list[str]:
    print("\n=== SYNC (OpaClient) ===\n")
    created_ids: list[str] = []
    opts = RequestOptions(timeout=CALL_TIMEOUT)

    with OpaClient(api_key=api_key) as opa:
        # --- domains -------------------------------------------------------
        domains = step("opa.domains.list", lambda: opa.domains.list())
        domain_name: Optional[str] = None
        if domains:
            primary = next((d for d in domains if d.primary), domains[0])
            domain_name = primary.domain

        # --- links.create ----------------------------------------------------
        link1 = step(
            "opa.links.create (minimal, no domain)",
            lambda: opa.links.create(destination_url=f"https://example.com/{SUFFIX}-1"),
        )
        if link1:
            created_ids.append(link1.id)

        link2 = step(
            "opa.links.create (all optional fields)",
            lambda: opa.links.create(
                destination_url=f"https://example.com/{SUFFIX}-2",
                domain=domain_name,
                title="SDK Python full test",
                description="Created by examples/full_test.py",
                comments="safe to delete",
                utm_source="sdk-test",
                utm_medium="script",
                utm_campaign=SUFFIX,
                do_index=False,
                targeting=LinkTargeting(ios="https://apps.apple.com/app/example"),
                qr_settings=QrSettings(
                    foreground_color="#000000",
                    background_color="#FFFFFF",
                    error_correction_level="M",
                ),
                options=opts,
            ),
        )
        if link2:
            created_ids.append(link2.id)

        # --- links.get ---------------------------------------------------
        if link1:
            step("opa.links.get (link1)", lambda: opa.links.get(link1.id, options=opts))
        else:
            log_skip("opa.links.get (link1)", "link1 was not created")
        if link2:
            step("opa.links.get (link2)", lambda: opa.links.get(link2.id, options=opts))
        else:
            log_skip("opa.links.get (link2)", "link2 was not created")

        # --- links.update --------------------------------------------------
        if link1:
            updated = step(
                "opa.links.update (link1)",
                lambda: opa.links.update(
                    link1.id,
                    destination_url=f"https://example.com/{SUFFIX}-1-updated",
                    domain=link1.domain,
                    options=opts,
                ),
            )
            if updated:
                assert updated.destination_url.endswith("-updated"), "update did not stick"
        else:
            log_skip("opa.links.update (link1)", "link1 was not created")

        # --- links.archive / restore ---------------------------------------
        if link1:
            step("opa.links.archive (link1)", lambda: opa.links.archive(link1.id, options=opts))
            step("opa.links.restore (link1)", lambda: opa.links.restore(link1.id, options=opts))
        else:
            log_skip("opa.links.archive/restore (link1)", "link1 was not created")

        # --- links.duplicate -------------------------------------------------
        dup = None
        if link2:
            dup = step("opa.links.duplicate (link2)", lambda: opa.links.duplicate(link2.id, options=opts))
            if dup:
                created_ids.append(dup.id)
        else:
            log_skip("opa.links.duplicate (link2)", "link2 was not created")

        # --- links.list / list_all -------------------------------------------
        step(
            "opa.links.list (search=sdk-py-test)",
            lambda: opa.links.list(search="sdk-py-test", options=opts),
        )
        all_items = step(
            "opa.links.list_all (search=sdk-py-test)",
            lambda: list(opa.links.list_all(search="sdk-py-test")),
        )
        if all_items is not None and created_ids:
            found = {item.id for item in all_items} & set(created_ids)
            if not found:
                log_fail(
                    "opa.links.list_all consistency",
                    AssertionError("none of the freshly created links showed up in list_all"),
                )
            else:
                log_ok("opa.links.list_all consistency", f"found {len(found)}/{len(created_ids)}")

        # --- bulk operations -------------------------------------------------
        bulk_target = [i for i in created_ids if i][:2]
        if bulk_target:
            step(
                "opa.links.bulk_archive",
                lambda: opa.links.bulk_archive(bulk_target, options=opts),
            )
            step(
                "opa.links.bulk_restore",
                lambda: opa.links.bulk_restore(bulk_target, options=opts),
            )
        else:
            log_skip("opa.links.bulk_archive/bulk_restore", "no links created")

        # bulk_tag: only if some link already carries a tag we can reuse.
        tag_id = None
        if all_items:
            for item in all_items:
                if item.tags:
                    tag_id = item.tags[0].id
                    break
        if tag_id and bulk_target:
            step(
                "opa.links.bulk_tag",
                lambda: opa.links.bulk_tag(bulk_target, [tag_id], options=opts),
            )
        else:
            log_skip("opa.links.bulk_tag", "no existing tag_id available on this account")

        # bulk_move: only if some link already carries a folder we can reuse.
        folder_id = None
        if all_items:
            for item in all_items:
                if item.folder:
                    folder_id = item.folder.id
                    break
        if folder_id and bulk_target:
            step(
                "opa.links.bulk_move",
                lambda: opa.links.bulk_move(bulk_target, folder_id, options=opts),
            )
        else:
            log_skip("opa.links.bulk_move", "no existing folder_id available on this account")

        # --- analytics --------------------------------------------------------
        from_date = time.strftime("%Y-%m-%d", time.gmtime(time.time() - 7 * 86400))
        to_date = time.strftime("%Y-%m-%d", time.gmtime())
        link_for_analytics = link1.id if link1 else None

        step(
            "opa.analytics.summary (from_/to, 7d)",
            lambda: opa.analytics.summary(
                from_=from_date, to=to_date, link_id=link_for_analytics, options=opts
            ),
        )
        step(
            "opa.analytics.timeseries (from_/to, 7d)",
            lambda: opa.analytics.timeseries(
                from_=from_date, to=to_date, link_id=link_for_analytics, options=opts
            ),
        )
        step(
            "opa.analytics.events (limit=10)",
            lambda: opa.analytics.events(limit=10, link_id=link_for_analytics, options=opts),
        )

        # --- cleanup -----------------------------------------------------------
        try:
            live_ids = [i for i in created_ids if i]
            if live_ids:
                opa.links.bulk_archive(live_ids)
                print(f"\n[cleanup] archived {len(live_ids)} sync-created link(s): {live_ids}")
        except Exception as exc:  # noqa: BLE001
            print(f"\n[cleanup] WARNING: sync cleanup failed: {exc.__class__.__name__}: {exc}")

    return created_ids


# --------------------------------------------------------------------------- #
# Async phase
# --------------------------------------------------------------------------- #


async def run_async_tests(api_key: str) -> list[str]:
    print("\n=== ASYNC (AsyncOpaClient) ===\n")
    created_ids: list[str] = []
    opts = RequestOptions(timeout=CALL_TIMEOUT)

    async with AsyncOpaClient(api_key=api_key) as opa:
        # --- domains -------------------------------------------------------
        domains = await astep("opa.domains.list (async)", opa.domains.list())
        domain_name: Optional[str] = None
        if domains:
            primary = next((d for d in domains if d.primary), domains[0])
            domain_name = primary.domain

        # --- links.create ----------------------------------------------------
        link1 = await astep(
            "opa.links.create (async, minimal, no domain)",
            opa.links.create(destination_url=f"https://example.com/{SUFFIX}-async-1"),
        )
        if link1:
            created_ids.append(link1.id)

        link2 = await astep(
            "opa.links.create (async, all optional fields)",
            opa.links.create(
                destination_url=f"https://example.com/{SUFFIX}-async-2",
                domain=domain_name,
                title="SDK Python full test (async)",
                description="Created by examples/full_test.py",
                comments="safe to delete",
                utm_source="sdk-test",
                utm_medium="script",
                utm_campaign=SUFFIX,
                do_index=False,
                targeting=LinkTargeting(android="https://play.google.com/store/apps/details?id=com.example"),
                qr_settings=QrSettings(
                    foreground_color="#000000",
                    background_color="#FFFFFF",
                    error_correction_level="M",
                ),
                options=opts,
            ),
        )
        if link2:
            created_ids.append(link2.id)

        # --- links.get ---------------------------------------------------
        if link1:
            await astep("opa.links.get (async, link1)", opa.links.get(link1.id, options=opts))
        else:
            log_skip("opa.links.get (async, link1)", "link1 was not created")
        if link2:
            await astep("opa.links.get (async, link2)", opa.links.get(link2.id, options=opts))
        else:
            log_skip("opa.links.get (async, link2)", "link2 was not created")

        # --- links.update --------------------------------------------------
        if link1:
            updated = await astep(
                "opa.links.update (async, link1)",
                opa.links.update(
                    link1.id,
                    destination_url=f"https://example.com/{SUFFIX}-async-1-updated",
                    domain=link1.domain,
                    options=opts,
                ),
            )
            if updated:
                assert updated.destination_url.endswith("-updated"), "async update did not stick"
        else:
            log_skip("opa.links.update (async, link1)", "link1 was not created")

        # --- links.archive / restore ---------------------------------------
        if link1:
            await astep(
                "opa.links.archive (async, link1)", opa.links.archive(link1.id, options=opts)
            )
            await astep(
                "opa.links.restore (async, link1)", opa.links.restore(link1.id, options=opts)
            )
        else:
            log_skip("opa.links.archive/restore (async, link1)", "link1 was not created")

        # --- links.duplicate -------------------------------------------------
        dup = None
        if link2:
            dup = await astep(
                "opa.links.duplicate (async, link2)", opa.links.duplicate(link2.id, options=opts)
            )
            if dup:
                created_ids.append(dup.id)
        else:
            log_skip("opa.links.duplicate (async, link2)", "link2 was not created")

        # --- links.list / list_all -------------------------------------------
        await astep(
            "opa.links.list (async, search=sdk-py-test)",
            opa.links.list(search="sdk-py-test", options=opts),
        )

        async def _collect_list_all() -> list[Any]:
            return [item async for item in opa.links.list_all(search="sdk-py-test")]

        all_items = await astep("opa.links.list_all (async, search=sdk-py-test)", _collect_list_all())
        if all_items is not None and created_ids:
            found = {item.id for item in all_items} & set(created_ids)
            if not found:
                log_fail(
                    "opa.links.list_all consistency (async)",
                    AssertionError("none of the freshly created links showed up in list_all"),
                )
            else:
                log_ok(
                    "opa.links.list_all consistency (async)",
                    f"found {len(found)}/{len(created_ids)}",
                )

        # --- bulk operations -------------------------------------------------
        bulk_target = [i for i in created_ids if i][:2]
        if bulk_target:
            await astep(
                "opa.links.bulk_archive (async)",
                opa.links.bulk_archive(bulk_target, options=opts),
            )
            await astep(
                "opa.links.bulk_restore (async)",
                opa.links.bulk_restore(bulk_target, options=opts),
            )
        else:
            log_skip("opa.links.bulk_archive/bulk_restore (async)", "no links created")

        tag_id = None
        if all_items:
            for item in all_items:
                if item.tags:
                    tag_id = item.tags[0].id
                    break
        if tag_id and bulk_target:
            await astep(
                "opa.links.bulk_tag (async)",
                opa.links.bulk_tag(bulk_target, [tag_id], options=opts),
            )
        else:
            log_skip("opa.links.bulk_tag (async)", "no existing tag_id available on this account")

        folder_id = None
        if all_items:
            for item in all_items:
                if item.folder:
                    folder_id = item.folder.id
                    break
        if folder_id and bulk_target:
            await astep(
                "opa.links.bulk_move (async)",
                opa.links.bulk_move(bulk_target, folder_id, options=opts),
            )
        else:
            log_skip("opa.links.bulk_move (async)", "no existing folder_id available on this account")

        # --- analytics --------------------------------------------------------
        from_date = time.strftime("%Y-%m-%d", time.gmtime(time.time() - 7 * 86400))
        to_date = time.strftime("%Y-%m-%d", time.gmtime())
        link_for_analytics = link1.id if link1 else None

        await astep(
            "opa.analytics.summary (async, from_/to, 7d)",
            opa.analytics.summary(
                from_=from_date, to=to_date, link_id=link_for_analytics, options=opts
            ),
        )
        await astep(
            "opa.analytics.timeseries (async, from_/to, 7d)",
            opa.analytics.timeseries(
                from_=from_date, to=to_date, link_id=link_for_analytics, options=opts
            ),
        )
        await astep(
            "opa.analytics.events (async, limit=10)",
            opa.analytics.events(limit=10, link_id=link_for_analytics, options=opts),
        )

        # --- cleanup -----------------------------------------------------------
        try:
            live_ids = [i for i in created_ids if i]
            if live_ids:
                await opa.links.bulk_archive(live_ids)
                print(f"\n[cleanup] archived {len(live_ids)} async-created link(s): {live_ids}")
        except Exception as exc:  # noqa: BLE001
            print(f"\n[cleanup] WARNING: async cleanup failed: {exc.__class__.__name__}: {exc}")

    return created_ids


# --------------------------------------------------------------------------- #
# `from_` keyword-collision regression check (sync + async)
# --------------------------------------------------------------------------- #


def check_from_keyword(api_key: str) -> None:
    """`from` is a Python keyword — the SDK param must be `from_`, never `from`.

    This isn't testable via `**kwargs` (a `from=...` call is a `SyntaxError`,
    not a runtime error) so this just documents + asserts the signature uses
    `from_`, via introspection, instead of trying to call it the wrong way.
    """
    import inspect

    from opa_sh.resources.analytics import AnalyticsResource

    sig = inspect.signature(AnalyticsResource.summary)
    if "from_" in sig.parameters and "from" not in sig.parameters:
        log_ok("analytics.summary uses `from_` (not `from`, a Python keyword)")
    else:
        log_fail(
            "analytics.summary parameter name",
            AssertionError(f"expected `from_` in signature, got {list(sig.parameters)}"),
        )


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main() -> int:
    api_key = os.environ.get("OPA_API_KEY")
    if not api_key:
        print("ERROR: OPA_API_KEY not set. Copy .env.example to .env and fill it in.")
        return 1

    print(f"opa-sh full_test.py — run id {RUN_ID}")

    check_from_keyword(api_key)

    sync_created: list[str] = []
    async_created: list[str] = []
    hard_error: Optional[BaseException] = None

    try:
        sync_created = run_sync_tests(api_key)
    except Exception as exc:  # noqa: BLE001
        hard_error = exc
        print(f"\n[FATAL] sync phase crashed: {exc.__class__.__name__}: {exc}")
        traceback.print_exc()

    try:
        async_created = asyncio.run(run_async_tests(api_key))
    except Exception as exc:  # noqa: BLE001
        hard_error = hard_error or exc
        print(f"\n[FATAL] async phase crashed: {exc.__class__.__name__}: {exc}")
        traceback.print_exc()

    # Best-effort final sweep in case a phase crashed before its own cleanup ran.
    leftover = [i for i in (sync_created + async_created) if i]
    if leftover:
        try:
            with OpaClient(api_key=api_key) as opa:
                opa.links.bulk_archive(leftover)
            print(f"\n[cleanup] final sweep archived {len(leftover)} link(s)")
        except OpaError as exc:
            print(f"\n[cleanup] final sweep note: {exc.__class__.__name__}: {exc}")

    # --- summary -------------------------------------------------------------
    print("\n=== SUMMARY ===")
    print(f"passed:  {len(RESULTS.passed)}")
    print(f"failed:  {len(RESULTS.failed)}")
    print(f"skipped: {len(RESULTS.skipped)}")
    if RESULTS.failed:
        print("\nFailed calls:")
        for label in RESULTS.failed:
            print(f"  - {label}")
    if RESULTS.skipped:
        print("\nSkipped calls:")
        for label in RESULTS.skipped:
            print(f"  - {label}")

    if hard_error is not None or RESULTS.failed:
        print("\nRESULT: FAIL")
        return 1

    print("\nRESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
