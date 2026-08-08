#!/usr/bin/env python3
"""Prose checker for the site, per REFURB_BRIEF.md section 6.

Fails on:
  1. Any em dash or en dash outside a verbatim record region.
  2. Any banned word or construction in prose.
  3. Any sentence over the tier limit (20 words Tier A, 25 Tier B).
  4. Any paragraph over 4 sentences.
  5. Any unexpanded acronym on first use in prose.
  6. Any page over its word budget.
  7. Any literal digit inside the stats band include.
  8. Any app pitch in _data/apps.yml over its 25-word card ceiling.
  9. Any publication excerpt over 25 words or asking a question, any
     publication summary over 120 words, and any publication body prose
     outside its record markers.
 10. Any talk excerpt over 20 words or asking a question, any talk
     summary over 100 words, and any prose outside the record markers on
     a talk that has its own page.
 11. Any teaching-entry prose failing the Tier B checks, any dash
     outside a teaching file's record regions, and the 2 entries'
     combined prose over the shared teaching section budget.
 12. Any meta description that is not lifted verbatim from its page:
     each _pages description must be a substring of the page's visible
     prose (the home page's must equal the site description in
     _config.yml), stay within 160 characters, and exist on every
     _pages file except the 404. Collection pages derive their
     descriptions from the excerpt fields checked above.
 13. Any literal alt text with a dash, a banned word, or more than 25
     words (the card ceiling). Empty alt is the decorative-image
     convention and passes. Liquid-derived alt strings mirror checked
     fields and are skipped where the Liquid is stripped.
 14. Any literal value in _includes/jsonld.html beyond the schema.org
     constants: every fact in the structured data must render through
     Liquid from front matter, _config.yml or a data file.

Scope: the files in FILES and TEACHING_FILES below plus the stats
include. The styleguide (internal, exempt) and the redirect stubs (no
prose) are deliberately absent, and the 8 rows-only talk bodies render
as redirects, so nothing a reader can see is unchecked.

Publication files (_publications/) render their prose from front matter:
the excerpt is the index finding (25-word ceiling, no questions) and the
summary is the plain-language block that opens the page (Tier B, 120
words). Those two fields are the checked prose. The title and citation
fields are verbatim records (citation en dashes sit inside numeric
ranges, which the brief permits), media titles are third-party records
verified against their sources, and the body is the original abstract
inside record markers. None of those are checked, by the same principle
as the record regions: never rewritten, so nothing in them is
actionable.

Talk files (_talks/) follow the same shape. All 12 carry an excerpt,
which is the row entry on /research/ (20-word ceiling, no questions,
REFURB_BRIEF 2.4). The 4 talks with their own pages also carry a summary
(Tier B, 100 words) and keep the submitted abstract inside record
markers, so their bodies must hold nothing else. The other 8 render as
redirects (DECISIONS 39), so their bodies never reach a reader and are
treated as unrendered records: only the excerpt is checked. Titles,
venues, locations, awards, the also lines, and the poster and thesis
blocks are records.

Project pages (_projects/) have no total word budget: level 3 is
unbounded per CONTENT_MAP section 8. They instead carry 2 budgets of
their own, from REFURB_BRIEF section 2.4: at most 120 visible words
before the first heading, and a card excerpt of at most 25 words.

Verbatim records (citations, degree and course titles, grant and award
lines, the nomination list) sit between <!-- record --> and
<!-- /record --> markers in the source and are skipped by every check:
records are never rewritten, so nothing in them is actionable. Chip and
label spans, filter buttons and Liquid output are presentation tokens,
not prose, and are removed before checking. Words inside Liquid include
parameters (the twin frame context line) are not visible to this script;
the Gate evidence counts them by hand.

Teaching files (_teaching/) render inline on /research/ through Liquid
(DECISIONS 41), so the page-level check on research.html never sees
them: they are read directly, the way _data/apps.yml is. The course
list and the student project abstract are records inside collapsed
blocks; the visible framing prose is Tier B. The 2 entries share the
CONTENT_MAP teaching budget of 120 words, and their words also join the
/research/ page budget, together with the publication and talk excerpts
its rows render, so the 700-word page budget measures what the page
actually serves.

The post (_posts/) is checked like a page: Tier B, with the level 2
budget of 120 words on the owner's prose. The publisher's description
sits inside record markers and the chapter list renders from
_data/book_chapters.yml through Liquid, so neither counts.

The /apps/ entries (pitch, demonstrates, note) live in _data/apps.yml,
which Liquid renders into the page, so the page file alone never shows
them. The data file is flat one-line YAML and is read here directly to
stay stdlib-only: its strings join the apps.html blocks, so every check
above covers them and they count toward the /apps/ budget. Each pitch
also carries the 25-word card ceiling from REFURB_BRIEF section 2.4.

Usage:
  python3 scripts/prose_check.py             check, exit 1 on violations
  python3 scripts/prose_check.py --metrics   also print the metrics table
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# file -> (tier, word budget). Budgets from CONTENT_MAP.md section 8;
# terms and sitemap budgets set in DECISIONS.md (Phase 5). A budget of
# None means no total cap (project pages, level 3 unbounded).
FILES = {
    "_pages/home.html": ("B", 450),
    "_pages/work.md": ("B", 420),
    "_pages/skills.md": ("B", None),
    "_pages/projects.html": ("B", 440),
    "_pages/apps.html": ("A", 200),
    "_pages/digital-twin.html": ("A", 80),
    "_pages/research.html": ("B", 700),
    "_pages/contact.md": ("B", 60),
    "_pages/404.md": ("A", 30),
    "_pages/sitemap.md": ("A", 120),
    "_pages/terms.md": ("A", 150),
    "_pages/threatened_species.md": ("B", 150),
    "_projects/7ph-graph.md": ("A", None),
    "_projects/ai-jie.md": ("A", None),
    "_projects/digital-twin.md": ("A", None),
    "_projects/job-intelligence-engine.md": ("A", None),
    "_projects/llm-engineering-lab.md": ("A", None),
    "_projects/mlb-analytics-sql.md": ("A", None),
    "_projects/python-labs.md": ("A", None),
    "_projects/bird-elevational-migration.md": ("A", None),
    "_projects/dynamic-community-reshuffling.md": ("A", None),
    "_projects/ecosystem-pathway-cascades.md": ("A", None),
    "_projects/forecasting-popviability-ringtails.md": ("A", None),
    "_projects/forest-gap-abundance-gradients.md": ("A", None),
    "_projects/heightened-protection-bird-trends.md": ("A", None),
    "_projects/physiological-stress-climate-populations.md": ("A", None),
    "_projects/predicting-abundance-from-niche-theory.md": ("A", None),
    "_projects/spatiotemporal-bird-climate-impacts.md": ("A", None),
    # Publications: the budget is the 120-word summary ceiling; the
    # excerpt carries its own 25-word ceiling (REFURB_BRIEF 2.4).
    "_publications/delafuente_pacheco_2017_bosque.md": ("B", 120),
    "_publications/gallardo_et_al_2018.md": ("B", 120),
    "_publications/delafuente_et_al_2021_ecography.md": ("B", 120),
    "_publications/Williams_delafuente_2021.md": ("B", 120),
    "_publications/iriarte_et_al_2021.md": ("B", 120),
    "_publications/delafuente_et_al_2022_ddi_reshuffling.md": ("B", 120),
    "_publications/delafuente_williams_2022_possums_ddi.md": ("B", 120),
    "_publications/delafuente_et_al_2023_GCB.md": ("B", 120),
    "_publications/herbivory_awt_2024_oecologia.md": ("B", 120),
    "_publications/delafuente_2025_GCB.md": ("B", 120),
    "_publications/siri_et_al_2025.md": ("B", 120),
    "_publications/delafuente_2026_NCC.md": ("B", 120),
    # Talks: the budget is the 100-word summary ceiling on the 4 files
    # with pages; the excerpt carries its own 20-word ceiling. The 8
    # rows-only files have no summary and no page (CONTENT_MAP 6).
    "_talks/zenq_2023.md": ("B", 100),
    "_talks/esa_scbo_2022.md": ("B", 100),
    "_talks/PhD_completion_seminar.md": ("B", 100),
    "_talks/IBRC_2025.md": ("B", 100),
    "_talks/cbcs_brisbane_2023.md": ("B", 100),
    "_talks/chilean_congress_ornithology_2017.md": ("B", 100),
    "_talks/coder_nmix.md": ("B", 100),
    "_talks/NFFF_2025.md": ("B", 100),
    "_talks/tess_2021.md": ("B", 100),
    "_talks/tess_2023.md": ("B", 100),
    "_talks/wtma_workshop.md": ("B", 100),
    "_talks/zenq_2022.md": ("B", 100),
    # The post: Tier B, level 2 budget on the owner's prose. Records
    # (the publisher's description, the chapter list) are exempt.
    "_posts/2021-12-01-action-plan-australian-birds.md": ("B", 120),
}

# Checked by check_teaching: read directly because the entries render
# inline on /research/ through Liquid (DECISIONS 41). The budget is the
# CONTENT_MAP section total, shared across both files.
TEACHING_FILES = [
    "_teaching/james_cook_university.md",
    "_teaching/mentoring.md",
]
TEACHING_BUDGET = 120

STATS_INCLUDE = "_includes/stats-band.html"
APPS_DATA = "_data/apps.yml"
JSONLD_INCLUDE = "_includes/jsonld.html"
CONFIG = "_config.yml"

# The 404 is the one _pages file that serves no crawler and needs no
# description; every other _pages file in FILES must carry one.
DESCRIPTION_EXEMPT = {"_pages/404.md"}
DESCRIPTION_LIMIT = 160
ALT_BUDGET = 25

# The only literal strings _includes/jsonld.html may contain: schema.org
# structure, never facts.
JSONLD_CONSTANTS = {
    "https://schema.org", "Person", "ScholarlyArticle", "CreativeWork",
    "SoftwareApplication", "Periodical",
}

SENTENCE_LIMIT = {"A": 20, "B": 25}
PARAGRAPH_LIMIT = 4
PROJECT_LEAD_BUDGET = 120
PROJECT_EXCERPT_BUDGET = 25
APP_PITCH_BUDGET = 25
PUB_EXCERPT_BUDGET = 25
TALK_EXCERPT_BUDGET = 20

EM_DASH = "—"
EN_DASH = "–"

# Acronyms treated as words, plus proper names that look like acronyms
# (TERMINOLOGY.md, acronym policy).
ACRONYM_ALLOW = {
    "AI", "CV", "PDF", "XML", "URL", "CONAF", "CSIRO", "ORCID",
    # Added in the _projects pass (TERMINOLOGY.md, acronym policy):
    # ubiquitous technical terms treated as words, and acronym-shaped
    # proper names (products, software, model and class names).
    "API", "SQL", "JSON", "JSONL", "GPU", "DVD",
    "GPT", "JAGS", "JIE", "SBERT", "SHAP", "SNE", "AA",
}

# Acronym -> expansion that must appear earlier on the same page.
ACRONYM_EXPANSIONS = {
    "EPBC": "environment protection and biodiversity conservation",
    "IUCN": "international union for conservation of nature",
    "LLM": "large language model",
    "RAG": "retrieval-augmented generation",
    "WCS": "wildlife conservation society",
    "DOI": "digital object identifier",
    "MRR": "mean reciprocal rank",
    "MLB": "major league baseball",
    "MCP": "model context protocol",
}

# Banned words and constructions, REFURB_BRIEF.md section 6.2. The
# triadic list and the emphasis fragment are not machine-checkable and
# stay a review item.
BANNED = [
    (r"\bdelve", "delve"),
    (r"\bleverag(?:e|es|ed|ing)\b", "leverage as a verb"),
    (r"\bseamless", "seamless"),
    (r"\brobust", "robust"),
    (r"\bcutting-edge\b", "cutting-edge"),
    (r"\bstate-of-the-art\b", "state-of-the-art"),
    (r"\bpassionate", "passionate"),
    (r"\bjourney", "journey"),
    (r"\blandscape\b(?!\s+ecology)", "landscape (non-literal)"),
    (r"\brealm", "realm"),
    (r"\btapestr", "tapestry"),
    (r"\bnavigat(?:e|es|ed|ing)\b", "navigate (non-literal)"),
    (r"\bunlock", "unlock"),
    (r"\bempower", "empower"),
    (r"\bharness", "harness"),
    (r"\belevate", "elevate"),
    (r"in today's world", "in today's world"),
    (r"it's worth noting", "it's worth noting"),
    (r"at the end of the day", "at the end of the day"),
    (r"\bnot just\b", "not just X but Y"),
    (r"is(?:n't| not) just", "isn't just X, it's Y"),
    (r"\bdive into\b", "dive into"),
    (r"\bunder the hood\b", "under the hood"),
    (r"^\s*(?:Importantly|Notably),", "paragraph opener Importantly/Notably"),
]

RECORD_RE = re.compile(r"<!--\s*record\s*-->.*?<!--\s*/record\s*-->", re.S)
FRONT_MATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
LIQUID_RE = re.compile(r"\{%-?.*?-?%\}|\{\{.*?\}\}", re.S)
CHROME_RE = re.compile(
    r"<p[^>]*class=\"[^\"]*chips[^\"]*\"[^>]*>.*?</p>"
    r"|<span[^>]*class=\"[^\"]*(?:chip|label)[^\"]*\"[^>]*>.*?</span>"
    r"|<button[^>]*>.*?</button>",
    re.S,
)
BLOCK_END_RE = re.compile(
    r"</(?:p|li|h[1-6]|summary|dt|dd|td|th|figcaption|title)>|<br\s*/?>"
)
TAG_RE = re.compile(r"<[^>]+>")
ENTITY_RE = re.compile(r"&[#a-zA-Z0-9]+;")
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
KRAMDOWN_ATTR_RE = re.compile(r"\{[:#][^}]*\}")
ACRONYM_RE = re.compile(r"\b[A-Z]{2,}\b")

# Protect these before sentence splitting so their periods do not end
# sentences.
ABBREVIATIONS = ["Ph.D.", "M.S.", "B.S.", "Dr.", "St.", "vs.", "e.g.", "i.e."]


def strip_records(text):
    return RECORD_RE.sub("", text)


def extract_blocks(text):
    """Return visible text blocks (paragraphs, headings, list items)."""
    text = FRONT_MATTER_RE.sub("", text)
    text = strip_records(text)
    text = LIQUID_RE.sub(" ", text)
    text = CHROME_RE.sub(" ", text)
    text = BLOCK_END_RE.sub("\n\n", text)
    text = TAG_RE.sub(" ", text)
    text = ENTITY_RE.sub(" ", text)
    text = MD_LINK_RE.sub(r"\1", text)
    text = KRAMDOWN_ATTR_RE.sub(" ", text)
    blocks = []
    for raw_block in re.split(r"\n\s*\n", text):
        for line in raw_block.splitlines():
            line = re.sub(r"^\s*(?:[*+-]|#{1,6}|\d+\.)\s+", "", line).strip()
            line = line.replace("**", "")
            line = line.strip("*_` ")
            if line:
                blocks.append(line)
    return blocks


def split_sentences(block):
    protected = block
    for abbr in ABBREVIATIONS:
        protected = protected.replace(abbr, abbr.replace(".", ""))
    protected = re.sub(
        r"(\d)\.(\d)", lambda m: m.group(1) + "" + m.group(2), protected
    )
    sentences = []
    for part in re.split(r"(?<=[.!?])\s+", protected):
        part = part.replace("", ".").strip()
        if part and re.search(r"[.!?]", part):
            sentences.append(part)
    return sentences


def word_count(text):
    return len(text.split())


def apps_data_strings(fails):
    """Check _data/apps.yml and return its prose strings in file order."""
    raw = (ROOT / APPS_DATA).read_text(encoding="utf-8")
    for name, char in (("em dash", EM_DASH), ("en dash", EN_DASH)):
        count = raw.count(char)
        if count:
            fails.append(f"{APPS_DATA}: {count} {name}(es)")
    texts = []
    app_id = None
    for line in raw.splitlines():
        id_match = re.match(r"^-\s*id:\s*(\S+)", line)
        if id_match:
            app_id = id_match.group(1)
            continue
        field_match = re.match(r'^\s+(pitch|demonstrates|note):\s*"(.*)"', line)
        if not field_match:
            continue
        field, text = field_match.groups()
        if field == "pitch":
            n = word_count(text)
            if n > APP_PITCH_BUDGET:
                fails.append(
                    f"{APPS_DATA}: {app_id} pitch of {n} words "
                    f"(max {APP_PITCH_BUDGET})"
                )
        if text:
            texts.append(text)
    return texts


def check_teaching(report):
    """The 2 teaching entries, read directly (they render inline on
    /research/ through Liquid, so check_file never sees them). Per-file
    Tier B checks plus the shared section budget. Returns the combined
    word count, which joins the /research/ page budget."""
    total_words = 0
    failures = []
    for rel_path in TEACHING_FILES:
        raw = (ROOT / rel_path).read_text(encoding="utf-8")
        fails = []
        stripped = strip_records(raw)
        for name, char in (("em dash", EM_DASH), ("en dash", EN_DASH)):
            count = stripped.count(char)
            if count:
                fails.append(f"{count} {name}(es) outside record regions")
        blocks = extract_blocks(raw)
        all_sentences = run_prose_checks(blocks, "B", fails)
        words = sum(word_count(b) for b in blocks)
        total_words += words
        file_report(report, rel_path, "B", words, None, None,
                    PROJECT_LEAD_BUDGET, all_sentences, fails)
        failures.extend(f"{rel_path}: {fail}" for fail in fails)
    if total_words > TEACHING_BUDGET:
        failures.append(
            f"_teaching: {total_words} words of section prose across both "
            f"entries, over the shared budget of {TEACHING_BUDGET}"
        )
    return total_words, failures


def rendered_excerpt_words():
    """Words the /research/ rows render from publication and talk front
    matter. Each excerpt is already checked in its own file; here they
    count toward the page budget of the page that renders them."""
    total = 0
    for rel_path in FILES:
        if not rel_path.startswith(("_publications/", "_talks/")):
            continue
        raw = (ROOT / rel_path).read_text(encoding="utf-8")
        front = FRONT_MATTER_RE.match(raw).group(0)
        excerpt_match = EXCERPT_RE.search(front)
        if excerpt_match:
            total += word_count(clean_prose(excerpt_match.group(1)))
    return total


def run_prose_checks(blocks, tier, fails):
    """The checks every prose block gets: banned words, sentence and
    paragraph limits, acronym expansion. Returns the sentence list."""
    prose_text = "\n".join(blocks)

    for pattern, label in BANNED:
        for block in blocks:
            if re.search(pattern, block, re.I):
                fails.append(f'banned word or construction "{label}" in: "{block[:70]}"')

    all_sentences = []
    limit = SENTENCE_LIMIT[tier]
    for block in blocks:
        # Toolchain rows ("Python · Gradio · ...") are token lists, not
        # prose: version dots would otherwise read as sentence ends.
        if " · " in block:
            continue
        sentences = split_sentences(block)
        all_sentences.extend(sentences)
        if len(sentences) > PARAGRAPH_LIMIT:
            fails.append(
                f'paragraph of {len(sentences)} sentences (max {PARAGRAPH_LIMIT}): "{block[:70]}"'
            )
        for sentence in sentences:
            n = word_count(sentence)
            if n > limit:
                fails.append(
                    f'sentence of {n} words (tier {tier} max {limit}): "{sentence[:70]}"'
                )

    seen = set()
    lower_prose = prose_text.lower()
    for match in ACRONYM_RE.finditer(prose_text):
        acronym = match.group(0)
        if acronym in seen or acronym in ACRONYM_ALLOW:
            continue
        seen.add(acronym)
        expansion = ACRONYM_EXPANSIONS.get(acronym)
        if expansion is None:
            fails.append(
                f'unknown acronym "{acronym}": expand it, add an expansion to '
                "ACRONYM_EXPANSIONS, or allowlist it per TERMINOLOGY.md"
            )
        elif lower_prose.find(expansion) < 0 or lower_prose.find(expansion) > match.start():
            fails.append(f'acronym "{acronym}" used before its expansion')
    return all_sentences


def file_report(report, rel_path, tier, words, budget, lead, lead_budget,
                all_sentences, fails):
    lengths = [word_count(s) for s in all_sentences]
    report[rel_path] = {
        "tier": tier,
        "words": words,
        "budget": budget,
        "lead": lead,
        "lead_budget": lead_budget,
        "sentences": len(all_sentences),
        "mean": round(sum(lengths) / len(lengths), 1) if lengths else 0,
        "longest": max(lengths) if lengths else 0,
        "fails": fails,
    }


def check_file(rel_path, tier, budget, report, extra_words=0):
    path = ROOT / rel_path
    raw = path.read_text(encoding="utf-8")
    fails = []

    body = FRONT_MATTER_RE.sub("", raw)
    for name, char in (("em dash", EM_DASH), ("en dash", EN_DASH)):
        count = strip_records(body).count(char) + len(
            re.findall(char, FRONT_MATTER_RE.match(raw).group(0) if FRONT_MATTER_RE.match(raw) else "")
        )
        if count:
            fails.append(f"{count} {name}(es) outside record regions")

    blocks = extract_blocks(raw)
    if rel_path == "_pages/apps.html":
        blocks += apps_data_strings(fails)

    if rel_path.startswith("_pages/"):
        front_match = FRONT_MATTER_RE.match(raw)
        check_description(rel_path, front_match.group(0) if front_match else "",
                          blocks, fails)
    check_alt_texts(body, fails)

    all_sentences = run_prose_checks(blocks, tier, fails)

    words = sum(word_count(b) for b in blocks) + extra_words
    if budget is not None and words > budget:
        fails.append(f"page at {words} words, over its budget of {budget}")

    lead_words = None
    if rel_path.startswith("_projects/"):
        lead_words = check_project_page(raw, fails)

    file_report(report, rel_path, tier, words, budget, lead_words,
                PROJECT_LEAD_BUDGET, all_sentences, fails)
    return fails


HEADING_RE = re.compile(r"^#{1,6}\s", re.M)
EXCERPT_RE = re.compile(r"^excerpt:\s*[\"']?(.*?)[\"']?\s*$", re.M)
DESCRIPTION_RE = re.compile(r"^description\s*:\s*\"(.*)\"\s*(?:#.*)?$", re.M)
ALT_RE = re.compile(r'alt="([^"]*)"')
JSONLD_LITERAL_RE = re.compile(r':\s*"([^"]*)"')
SUMMARY_RE = re.compile(r"^summary: \|\n((?:  .*\n|\n)*)", re.M)
REDIRECT_TO_RE = re.compile(r"^redirect_to:", re.M)


def clean_prose(text):
    """Reduce a front matter prose string to checkable text."""
    text = MD_LINK_RE.sub(r"\1", text)
    return text.replace("**", "").strip()


def check_front_matter(rel_path, tier, budget, excerpt_budget, report,
                       has_page):
    """Publications and talks render their prose from front matter: the
    excerpt (the index finding or the talk row) and the summary (the
    plain-language block that opens the page) are the checked prose.
    Titles, citations, venues, awards, also lines and the poster and
    thesis blocks are verbatim records, media titles are third-party
    records, and the body is the original abstract inside record
    markers.

    has_page is False for the 8 rows-only talks, which render as
    redirects: they carry the excerpt alone, and their unrendered bodies
    are treated as records."""
    path = ROOT / rel_path
    raw = path.read_text(encoding="utf-8")
    fails = []
    front = FRONT_MATTER_RE.match(raw).group(0)
    body = FRONT_MATTER_RE.sub("", raw)

    if has_page:
        leftover = strip_records(body).strip()
        if leftover:
            fails.append(f'body prose outside record markers: "{leftover[:60]}"')

    blocks = []
    excerpt_words = 0
    excerpt_match = EXCERPT_RE.search(front)
    if excerpt_match is None:
        fails.append("no excerpt in front matter (the research index needs one)")
    else:
        excerpt = clean_prose(excerpt_match.group(1))
        excerpt_words = word_count(excerpt)
        if excerpt_words > excerpt_budget:
            fails.append(f"excerpt of {excerpt_words} words (max {excerpt_budget})")
        if "?" in excerpt:
            fails.append("excerpt asks a question (index entries state the finding)")
        blocks.append(excerpt)

    summary_words = 0
    summary_match = SUMMARY_RE.search(front)
    if summary_match is None:
        if has_page:
            fails.append("no summary in front matter (the page opens with it)")
    elif not has_page:
        fails.append("summary on a redirect entry, where nothing renders it")
    else:
        text = re.sub(r"^  ", "", summary_match.group(1), flags=re.M)
        paragraphs = [clean_prose(p) for p in re.split(r"\n\s*\n", text) if p.strip()]
        summary_words = sum(word_count(p) for p in paragraphs)
        if summary_words > budget:
            fails.append(f"summary at {summary_words} words, over its budget of {budget}")
        blocks.extend(paragraphs)

    for name, char in (("em dash", EM_DASH), ("en dash", EN_DASH)):
        count = sum(block.count(char) for block in blocks)
        if count:
            fails.append(f"{count} {name}(es) in the excerpt or summary")

    all_sentences = run_prose_checks(blocks, tier, fails)
    file_report(report, rel_path, tier, summary_words, budget, excerpt_words,
                excerpt_budget, all_sentences, fails)
    return fails


def check_project_page(raw, fails):
    """Project-page budgets: lead of 120 words before the first heading
    (REFURB_BRIEF 2.4) and a card excerpt of 25 words."""
    body = FRONT_MATTER_RE.sub("", raw)
    heading = HEADING_RE.search(body)
    lead_text = body[: heading.start()] if heading else body
    lead_words = sum(word_count(b) for b in extract_blocks(lead_text))
    if lead_words > PROJECT_LEAD_BUDGET:
        fails.append(
            f"{lead_words} words before the first heading "
            f"(max {PROJECT_LEAD_BUDGET})"
        )

    front = FRONT_MATTER_RE.match(raw)
    excerpt = EXCERPT_RE.search(front.group(0)) if front else None
    if excerpt is None:
        fails.append("no excerpt in front matter (cards and the sitemap need one)")
    else:
        n = word_count(excerpt.group(1))
        if n > PROJECT_EXCERPT_BUDGET:
            fails.append(
                f"excerpt of {n} words (max {PROJECT_EXCERPT_BUDGET})"
            )
    return lead_words


def check_description(rel_path, front, blocks, fails):
    """The meta description on a _pages file is lifted verbatim from the
    page (DECISIONS, Phase 6): it must be a substring of the visible
    prose, so the fact never exists in 2 versions. The home page's must
    equal the site description in _config.yml, its one settled source."""
    match = DESCRIPTION_RE.search(front)
    if match is None:
        if rel_path not in DESCRIPTION_EXEMPT:
            fails.append("no description in front matter (crawlers fall "
                         "back to the site description)")
        return
    description = match.group(1)
    if len(description) > DESCRIPTION_LIMIT:
        fails.append(f"description of {len(description)} characters "
                     f"(max {DESCRIPTION_LIMIT})")
    if rel_path == "_pages/home.html":
        config = (ROOT / CONFIG).read_text(encoding="utf-8")
        site_description = DESCRIPTION_RE.search(config)
        if site_description is None or description != site_description.group(1):
            fails.append("home description differs from the site "
                         "description in _config.yml")
    elif all(description not in block for block in blocks):
        fails.append("description is not a verbatim substring of the "
                     "page's visible prose")


def check_alt_texts(body, fails):
    """Literal alt text is visitor-facing prose: no dashes, no banned
    words, at most the 25-word card ceiling. Empty alt (the decorative
    convention) passes, and Liquid output is stripped first because
    derived alt strings mirror fields checked elsewhere. Alt text
    depicts an image rather than introducing terms, so the acronym rule
    does not apply."""
    for match in ALT_RE.finditer(strip_records(body)):
        alt = LIQUID_RE.sub(" ", match.group(1)).strip()
        if not alt:
            continue
        for name, char in (("em dash", EM_DASH), ("en dash", EN_DASH)):
            if char in alt:
                fails.append(f'{name} in alt text: "{alt[:60]}"')
        for pattern, label in BANNED:
            if re.search(pattern, alt, re.I):
                fails.append(f'banned word or construction "{label}" '
                             f'in alt text: "{alt[:60]}"')
        n = word_count(alt)
        if n > ALT_BUDGET:
            fails.append(f'alt text of {n} words (max {ALT_BUDGET}): '
                         f'"{alt[:60]}"')


def check_jsonld_include():
    """Every value in the JSON-LD include must render through Liquid;
    the only literal strings allowed are the schema.org constants, so
    no fact can be typed into the structured data by hand."""
    raw = (ROOT / JSONLD_INCLUDE).read_text(encoding="utf-8")
    raw = re.sub(r"{%-?\s*comment\s*-?%}.*?{%-?\s*endcomment\s*-?%}", "",
                 raw, flags=re.S)
    raw = LIQUID_RE.sub(" ", raw)
    fails = []
    for match in JSONLD_LITERAL_RE.finditer(raw):
        value = match.group(1)
        if value and value not in JSONLD_CONSTANTS:
            fails.append(f'{JSONLD_INCLUDE}: literal value "{value[:50]}" '
                         "(facts must render through Liquid)")
    return fails


def check_stats_include():
    raw = (ROOT / STATS_INCLUDE).read_text(encoding="utf-8")
    digits = re.findall(r"[0-9]", raw)
    if digits:
        return [f"{STATS_INCLUDE}: {len(digits)} literal digit(s) found"]
    return []


def main():
    show_metrics = "--metrics" in sys.argv
    report = {}
    failures = []

    teaching_words, teaching_failures = check_teaching(report)
    research_extra = teaching_words + rendered_excerpt_words()

    for rel_path, (tier, budget) in FILES.items():
        if rel_path.startswith("_publications/"):
            fails = check_front_matter(rel_path, tier, budget,
                                       PUB_EXCERPT_BUDGET, report,
                                       has_page=True)
        elif rel_path.startswith("_talks/"):
            raw = (ROOT / rel_path).read_text(encoding="utf-8")
            front = FRONT_MATTER_RE.match(raw).group(0)
            fails = check_front_matter(rel_path, tier, budget,
                                       TALK_EXCERPT_BUDGET, report,
                                       has_page=not REDIRECT_TO_RE.search(front))
        else:
            extra = research_extra if rel_path == "_pages/research.html" else 0
            fails = check_file(rel_path, tier, budget, report,
                               extra_words=extra)
        for fail in fails:
            failures.append(f"{rel_path}: {fail}")
    failures.extend(teaching_failures)
    failures.extend(check_stats_include())
    failures.extend(check_jsonld_include())

    if show_metrics:
        header = (
            f'{"file":<52}{"tier":<6}{"words":<12}{"lead":<9}'
            f'{"sents":<7}{"mean":<7}{"longest":<9}{"dashes":<8}{"banned"}'
        )
        print(header)
        for rel_path, r in report.items():
            dash_fails = sum("dash" in f for f in r["fails"])
            banned_fails = sum("banned" in f for f in r["fails"])
            budget = "-" if r["budget"] is None else str(r["budget"])
            lead = "-" if r["lead"] is None else f'{r["lead"]}/{r["lead_budget"]}'
            print(
                f'{rel_path:<52}{r["tier"]:<6}'
                f'{str(r["words"]) + "/" + budget:<12}{lead:<9}'
                f'{r["sentences"]:<7}{r["mean"]:<7}{r["longest"]:<9}'
                f"{dash_fails:<8}{banned_fails}"
            )
        print()

    if failures:
        print(f"prose_check: {len(failures)} violation(s)")
        for failure in failures:
            print(f"  {failure}")
        return 1
    print(
        f"prose_check: clean ({len(FILES) + len(TEACHING_FILES)} files "
        "and the stats include)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
