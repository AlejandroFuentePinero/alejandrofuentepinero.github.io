#!/usr/bin/env python3
"""Gate 7 full link check against the live domain.

Extends the Gate 4 crawl (docs/phase-4-evidence/crawl_old_urls.py, whose
URL inventory it imports) in three ways:

  A. The complete Gate 4 inventory, every MIGRATIONS.md redirect and every
     kept and new URL, requested on the live domain. HTTP redirects and
     jekyll-redirect-from meta-refresh pages are followed; every chain must
     end in a 200.
  B. Every internal link and asset reference in the built site (href, src,
     srcset, meta content, CSS url()), requested on the live domain.
     Fragment links are also verified against the built HTML: the target
     page must contain the anchor id.
  C. Every external link in the built site, requested with browser-like
     headers. AUDIT.md section 5 records which hosts wall off non-browser
     clients; those hosts are listed here and a walled status from one of
     them counts as a pass only if the status matches the recorded
     bot-wall behaviour. Anything else must return 200.

Run from the repo root after `bundle exec jekyll build`. The build must be
content-identical to the deployed branch for section B and C extraction to
describe the live site (verified this phase: refurb/main and main differ
by a merge commit only).
"""

import concurrent.futures
import html
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SITE = ROOT / "_site"

sys.path.insert(0, str(ROOT / "docs" / "phase-4-evidence"))
import crawl_old_urls  # noqa: E402  (the Gate 4 inventory)

LIVE = "https://alejandrofuentepinero.github.io"

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# Hosts AUDIT.md section 5 verified as fine in a real browser while
# refusing non-browser clients. status codes seen from scripted requests.
BOT_WALLED = {
    "onlinelibrary.wiley.com": {403},
    "doi.org": {403},  # resolves into Wiley et al.
    "www.nytimes.com": {403},
    "www.jcu.edu.au": {403},
    "www.pnas.org": {403},
    "www.scielo.cl": {403},
    "www.sciencedirect.com": {403},
    "moxfield.com": {403},
    "www.linkedin.com": {999},
    "linkedin.com": {999},
}

# Free-tier app hosts that answer scripted clients with a wake or boot
# page. Both apps were loaded in real Chrome during this QA run and reach
# their full UI; the evidence screenshots are committed beside this
# script.
SLEEPY_APPS = {
    "alejandrodelafuente.shinyapps.io": {202},  # "starting app" page
    "job-intelligence-engine.streamlit.app": {303},  # sleep/wake flow
}

REFRESH = crawl_old_urls.REFRESH

# The macOS framework Python ships no CA bundle; use certifi when
# installed, else the system bundle.
try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")


def fetch(url, timeout=30):
    """GET a URL with browser headers. Returns (status, body, final_url)."""
    quoted = urllib.parse.quote(url, safe="/%:?=&#.-_~")
    req = urllib.request.Request(quoted, headers=BROWSER_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            body = r.read(2_000_000).decode("utf-8", "replace")
            return r.status, body, r.geturl()
    except urllib.error.HTTPError as err:
        return err.code, "", url
    except Exception as err:  # DNS, TLS, timeout
        return f"error: {err.__class__.__name__}", "", url


def resolve_live(path):
    """Follow HTTP and meta-refresh redirects on the live domain."""
    chain = [path]
    for _ in range(6):
        status, body, final = fetch(LIVE + chain[-1].split("#")[0])
        if status != 200:
            return chain, status
        m = REFRESH.search(body)
        if not m:
            return chain, 200
        target = urllib.parse.unquote(html.unescape(m.group(1)).replace(LIVE, ""))
        chain.append(target)
    return chain, "loop"


HREF = re.compile(r'(?:href|src)="([^"]+)"')
META_URL = re.compile(r'content="(https?://[^"]+|/[^"]*)"')
SRCSET = re.compile(r'srcset="([^"]+)"')
CSS_URL = re.compile(r'url\(["\']?([^)"\']+)["\']?\)')


def built_links():
    """Extract every internal and external reference from the built site.

    Returns (internal, external, fragments): internal paths, external URLs,
    and (source page, target path, fragment) triples for anchor checks.
    """
    internal, external, fragments = set(), set(), set()
    for page in SITE.rglob("*.html"):
        text = page.read_text(encoding="utf-8", errors="replace")
        page_url = "/" + str(page.relative_to(SITE))
        refs = HREF.findall(text) + META_URL.findall(text)
        for chunk in SRCSET.findall(text):
            refs += [part.strip().split(" ")[0] for part in chunk.split(",")]
        for raw in refs:
            url = html.unescape(raw)
            if url.startswith(LIVE):
                url = url[len(LIVE):] or "/"
            if url.startswith("//"):
                url = "https:" + url
            if url.startswith("http://") or url.startswith("https://"):
                external.add(url)
            elif url.startswith("/"):
                path, _, frag = url.partition("#")
                if path:
                    internal.add(path)
                if frag:
                    fragments.add((page_url, path or page_url, frag))
            elif url.startswith("#") and len(url) > 1:
                # bare href="#" is the styleguide's deliberate component
                # placeholder (DECISIONS 34) and is skipped
                fragments.add((page_url, page_url, url[1:]))
            # mailto:, data:, relative-free strings are out of scope
    for css in SITE.rglob("*.css"):
        base = "/" + str(css.relative_to(SITE).parent)
        for raw in CSS_URL.findall(css.read_text(encoding="utf-8", errors="replace")):
            if raw.startswith("data:"):
                continue
            if raw.startswith("/"):
                internal.add(raw.partition("#")[0])
            elif not raw.startswith("http"):
                joined = urllib.parse.urljoin(base + "/", raw)
                internal.add(joined.partition("#")[0])
    return sorted(internal), sorted(external), sorted(fragments)


ID_ATTR = 'id="{}"'
NAME_ATTR = 'name="{}"'


def local_file_for(path):
    """Map a site path to its built file, GitHub Pages semantics."""
    p = SITE / urllib.parse.unquote(path).lstrip("/")
    if p.is_dir():
        p = p / "index.html"
    if not p.exists() and not path.endswith("/"):
        cand = Path(str(p) + ".html")
        if cand.exists():
            return cand
    return p if p.exists() else None


def check_fragment(entry):
    src, path, frag = entry
    target = local_file_for(path)
    if target is None or target.suffix != ".html":
        return False, f"{src} -> {path}#{frag} (target page not found)"
    text = target.read_text(encoding="utf-8", errors="replace")
    ok = ID_ATTR.format(frag) in text or NAME_ATTR.format(frag) in text
    return ok, f"{src} -> {path}#{frag}"


def classify_external(url, status):
    host = urllib.parse.urlsplit(url).netloc
    if status == 200:
        return "PASS", "200"
    walled = BOT_WALLED.get(host)
    if walled and status in walled:
        return "PASS", f"{status}, bot wall recorded in AUDIT.md section 5"
    sleepy = SLEEPY_APPS.get(host)
    if sleepy and status in sleepy:
        return "PASS", f"{status}, free-tier wake page, app verified live in Chrome"
    return "FAIL", str(status)


def main():
    lines, failures = [], 0

    def record(ok, line):
        nonlocal failures
        failures += 0 if ok else 1
        lines.append(("PASS " if ok else "FAIL ") + line)

    lines.append("== A. Gate 4 inventory on the live domain ==")
    for kind, url in crawl_old_urls.inventory():
        chain, status = resolve_live(url)
        record(status == 200, f"[{kind:8s}] {' -> '.join(chain)} ({status})")

    internal, external, fragments = built_links()

    lines.append("")
    lines.append(f"== B. Internal references from the built site ({len(internal)} unique) ==")
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        results = pool.map(lambda p: (p, fetch(LIVE + p)[0]), internal)
    for path, status in results:
        record(status == 200, f"{path} ({status})")

    lines.append("")
    lines.append(f"== B2. Fragment anchors, verified in the built HTML ({len(fragments)}) ==")
    for entry in fragments:
        ok, desc = check_fragment(entry)
        record(ok, desc)

    lines.append("")
    lines.append(f"== C. External links, browser headers ({len(external)} unique) ==")
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        results = pool.map(lambda u: (u, fetch(u)[0]), external)
    for url, status in sorted(results):
        verdict, why = classify_external(url, status)
        record(verdict == "PASS", f"{url} ({why})")

    total = len([l for l in lines if l.startswith(("PASS", "FAIL"))])
    summary = f"\n{total} checks, {total - failures} passed, {failures} failed\n"
    report = "\n".join(lines) + summary
    print(report)
    (HERE / "link-check-report.txt").write_text(report)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
