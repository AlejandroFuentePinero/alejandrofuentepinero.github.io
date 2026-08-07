#!/usr/bin/env python3
"""Gate 7 HTML validation.

Validator: the Nu Html Checker service at validator.w3.org/nu (the
W3C's living HTML checker; the run below records the version the
service reports in its JSON response). Ten built pages covering every
layout (default, page, project, publication, talk, post, styleguide)
are POSTed to the checker; /404.html rides along as an eleventh.

Run from the repo root after `bundle exec jekyll build`.
"""

import json
import ssl
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "_site"
API = "https://validator.w3.org/nu/?out=json"

try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

PAGES = [
    ("/", "home"),
    ("/work/", "page layout"),
    ("/projects/", "page layout, type filter"),
    ("/apps/", "page layout, app cards and embed data"),
    ("/research/", "page layout, rows and disclosures"),
    ("/styleguide/", "styleguide layout, every component"),
    ("/projects/digital-twin/", "project layout"),
    ("/research/ringtail-possum-collapse-2022/", "publication layout"),
    ("/research/phd-exit-seminar-2024/", "talk layout"),
    ("/posts/action-plan-australian-birds-2021/", "post layout"),
    ("/404.html", "404 page"),
]


def validate(path):
    file = SITE / path.lstrip("/")
    if path.endswith("/"):
        file = SITE / path.strip("/") / "index.html"
    req = urllib.request.Request(
        API,
        data=file.read_bytes(),
        headers={
            "Content-Type": "text/html; charset=utf-8",
            "User-Agent": "gate7-html-validation (site owner QA run)",
        },
    )
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.load(r)


def main():
    lines = []
    failures = 0
    version = None
    for path, note in PAGES:
        result = validate(path)
        version = result.get("version", version)
        msgs = [
            m for m in result.get("messages", [])
            if m.get("type") in ("error", "info", "warning")
        ]
        errors = [m for m in msgs if m.get("type") == "error"]
        warnings = [m for m in msgs if m.get("type") != "error"]
        ok = not errors
        failures += 0 if ok else 1
        lines.append(
            f"{'PASS' if ok else 'FAIL'} {path} ({note}): "
            f"{len(errors)} errors, {len(warnings)} warnings"
        )
        for m in msgs:
            lines.append(
                f"    [{m['type']}] line {m.get('lastLine', '?')}: {m['message']}"
            )
        time.sleep(1)

    header = f"Nu Html Checker {version} (validator.w3.org/nu), run {time.strftime('%Y-%m-%d')}\n"
    report = header + "\n".join(lines) + (
        f"\n\n{len(PAGES)} pages, {len(PAGES) - failures} passed, {failures} failed\n"
    )
    print(report)
    (Path(__file__).parent / "html-validation-report.txt").write_text(report)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
