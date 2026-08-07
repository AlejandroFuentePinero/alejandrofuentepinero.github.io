#!/usr/bin/env python3
"""Gate 4 URL integrity crawl.

Serves the built _site with GitHub Pages resolution semantics (an
extensionless request resolves to the matching .html file) and requests
every URL the site served before Phase 4, plus every new URL. Redirect
pages (jekyll-redirect-from meta refresh) are followed to their final
destination. Pass: every URL ends in a 200. Run from the repo root
after `bundle exec jekyll build`.
"""

import http.server
import re
import socketserver
import threading
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "_site"
PORT = 4002
HOST = f"http://127.0.0.1:{PORT}"
LIVE = "https://alejandrofuentepinero.github.io"


class PagesHandler(http.server.SimpleHTTPRequestHandler):
    """Static handler that also resolves /foo to /foo.html, as GitHub
    Pages does for extensionless URLs."""

    def translate_path(self, path):
        resolved = super().translate_path(path)
        p = Path(resolved)
        if not p.exists() and not path.endswith("/"):
            candidate = Path(resolved + ".html")
            if candidate.exists():
                return str(candidate)
        return resolved

    def log_message(self, *args):
        pass


# Every URL the built site served before Phase 4 (MIGRATIONS.md), in the
# form browsers request it. Publication and talk permalinks had no
# trailing slash, so both the extensionless and .html forms must resolve.
KEEP = ["/", "/404.html", "/sitemap/", "/terms/"]

TOP_REDIRECTS = [
    "/about/", "/about.html",
    "/academic/", "/academic/cv/", "/cv/", "/resume", "/resume.html",
    "/academic/publications/", "/academic/talks/", "/academic/teaching/",
    "/academic/book_chapter/", "/academic/grants_awards/",
    "/academic/threatened_species/",
    "/datascience/", "/datascience/projects/", "/datascience/skills/",
    "/datascience/education/", "/datascience/communication/",
    "/portfolio/grants/", "/portfolio/awards/",
    "/teaching/james_cook_university/", "/teaching/mentoring/",
    "/posts/2012/08/blog-post-1/",
]

OLD_PROJECTS = [
    "7ph-graph", "ai-jie", "digital-twin", "job_intelligence_engine",
    "llm-engineering-lab", "mlb_analytics_sql", "python_eda_mini_projects",
    "python-ML-projects", "python_oop_minisystems",
    "bird-elevational-migration", "dynamic-community-reshuffling",
    "ecosystem-pathway-cascades", "forecasting-popviability-ringtails",
    "forest-gap-abundance-gradients", "heightened-protection-bird-trends",
    "physiological-stress-climate-populations",
    "predicting-abundance-from-niche-theory",
    "spatiotemporal-bird-climate-impacts",
]

OLD_PUBLICATIONS = [
    "delafuente_pacheco_2017_bosque", "gallardo_et_al_2018",
    "delafuente_et_al_2021_ecography", "Williams_delafuente_2021_plosone",
    "SAREM_NotasMamSud_12-2021_Iriarte", "delafuente_et_al_2023_GCB",
    "delafuente_etal_2024_oecologia", "delafuente_2025_gcb", "siri_2025",
    "delafuente_2026_ncc",
]

MALFORMED = [
    "/publication/Diversity%20and%20Distributions%20-%202022%20-%20de%20la%20Fuente%20-%20Predicted%20alteration%20of%20vertebrate%20communities%20in%20response%20to",
    "/publication/Diversity and Distributions - 2022 - de la Fuente - Predicted alteration of vertebrate communities in response to",
    "/publication/Diversity%20and%20Distributions%20-%202022%20-%20Fuente%20-%20Climate%20change%20threatens%20the%20future%20of%20rain%20forest%20ringtail%20possums%20by%202050",
    "/publication/Diversity and Distributions - 2022 - Fuente - Climate change threatens the future of rain forest ringtail possums by 2050",
]

OLD_TALKS = [
    "ZENQ_2023", "esa_scbo_2022", "esa_2021_poster", "PhD_exit_seminar",
    "IBRC_2025", "cbcs_brisbane_2023", "chilean_congress_ornithology_2017",
    "coder_nmix", "melbourne_2022", "NFFF_2025", "tess_2021", "TESS_2023",
    "tropical_bes_2021", "wtma_workshop_2024", "zenq_2022",
]

NEW_PAGES = [
    "/work/", "/projects/", "/apps/", "/research/", "/contact/",
    "/research/threatened-species/", "/posts/action-plan-australian-birds-2021/",
    "/styleguide/",
]

NEW_PROJECTS = [
    "7ph-graph", "ai-jie", "digital-twin", "job-intelligence-engine",
    "llm-engineering-lab", "mlb-analytics-sql", "python-labs",
    "bird-elevational-migration", "dynamic-community-reshuffling",
    "ecosystem-pathway-cascades", "forecasting-popviability-ringtails",
    "forest-gap-abundance-gradients", "heightened-protection-bird-trends",
    "physiological-stress-climate-populations",
    "predicting-abundance-from-niche-theory",
    "spatiotemporal-bird-climate-impacts",
]

NEW_RESEARCH = [
    "chusquea-flowering-2017", "urban-wetland-birds-2018",
    "abundance-niche-theory-2021", "rainforest-bird-declines-2021",
    "mountain-vizcacha-records-2021", "community-reshuffling-2022",
    "ringtail-possum-collapse-2022", "montane-bird-climate-drivers-2023",
    "foliage-chemistry-herbivory-2024", "physiological-stress-declines-2025",
    "forest-gap-birds-2025", "mountains-magnify-mechanisms-2026",
    "songs-of-disappearance-2023", "elevational-shifts-talk-2022",
    "phd-exit-seminar-2024", "flying-fox-heat-2025",
]


def inventory():
    urls = []
    urls += [("keep", u) for u in KEEP]
    urls += [("redirect", u) for u in TOP_REDIRECTS]
    urls += [("redirect", f"/datascience/projects/{s}/") for s in OLD_PROJECTS]
    for s in OLD_PUBLICATIONS:
        urls.append(("redirect", f"/publication/{s}"))
        urls.append(("redirect", f"/publication/{s}.html"))
    urls += [("redirect", u) for u in MALFORMED]
    urls += [("redirect", u + ".html") for u in MALFORMED]
    for s in OLD_TALKS:
        urls.append(("redirect", f"/talks/{s}"))
        urls.append(("redirect", f"/talks/{s}.html"))
    urls += [("new", u) for u in NEW_PAGES]
    urls += [("new", f"/projects/{s}/") for s in NEW_PROJECTS]
    urls += [("new", f"/research/{s}/") for s in NEW_RESEARCH]
    return urls


REFRESH = re.compile(r'http-equiv="refresh" content="0; url=([^"]+)"')


def fetch(path):
    quoted = urllib.parse.quote(path, safe="/%:?=&#.-_~")
    req = urllib.request.Request(HOST + quoted)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as err:
        return err.code, ""


def resolve(path):
    """Follow meta-refresh redirect pages to the final URL."""
    chain = [path]
    for _ in range(5):
        # A fragment never reaches the server.
        status, body = fetch(chain[-1].split("#")[0])
        if status != 200:
            return chain, status
        m = REFRESH.search(body)
        if not m:
            return chain, 200
        target = m.group(1).replace(LIVE, "")
        target = urllib.parse.unquote(target)
        chain.append(target)
    return chain, "loop"


def main():
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(
        ("127.0.0.1", PORT),
        lambda *a, **k: PagesHandler(*a, directory=str(SITE), **k),
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    failures = 0
    lines = []
    for kind, url in inventory():
        chain, status = resolve(url)
        ok = status == 200
        failures += 0 if ok else 1
        arrow = " -> ".join(chain)
        lines.append(f"{'PASS' if ok else 'FAIL'} [{kind:8s}] {arrow} ({status})")
    server.shutdown()

    report = "\n".join(lines)
    total = len(lines)
    summary = f"\n{total} URLs checked, {total - failures} passed, {failures} failed\n"
    print(report + summary)
    out = Path(__file__).parent / "crawl-report.txt"
    out.write_text(report + summary)
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
