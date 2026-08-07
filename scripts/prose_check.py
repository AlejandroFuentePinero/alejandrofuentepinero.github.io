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

Scope: the files in FILES below plus the stats include. Later Phase 5
passes extend FILES collection by collection. The styleguide (internal,
exempt) and the redirect stubs (no prose) are deliberately absent.

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
    "_pages/projects.html": ("B", 440),
    "_pages/apps.html": ("A", 200),
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
}

STATS_INCLUDE = "_includes/stats-band.html"
APPS_DATA = "_data/apps.yml"

SENTENCE_LIMIT = {"A": 20, "B": 25}
PARAGRAPH_LIMIT = 4
PROJECT_LEAD_BUDGET = 120
PROJECT_EXCERPT_BUDGET = 25
APP_PITCH_BUDGET = 25
PUB_EXCERPT_BUDGET = 25

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


def check_file(rel_path, tier, budget, report):
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

    all_sentences = run_prose_checks(blocks, tier, fails)

    words = sum(word_count(b) for b in blocks)
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
PUB_SUMMARY_RE = re.compile(r"^summary: \|\n((?:  .*\n|\n)*)", re.M)


def clean_prose(text):
    """Reduce a front matter prose string to checkable text."""
    text = MD_LINK_RE.sub(r"\1", text)
    return text.replace("**", "").strip()


def check_publication(rel_path, tier, budget, report):
    """Publication files render their prose from front matter: the
    excerpt (the index finding) and the summary (the plain-language
    block that opens the page) are the checked prose. The title and
    citation are verbatim records, media titles are third-party records,
    and the body is the original abstract inside record markers."""
    path = ROOT / rel_path
    raw = path.read_text(encoding="utf-8")
    fails = []
    front = FRONT_MATTER_RE.match(raw).group(0)
    body = FRONT_MATTER_RE.sub("", raw)

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
        if excerpt_words > PUB_EXCERPT_BUDGET:
            fails.append(f"excerpt of {excerpt_words} words (max {PUB_EXCERPT_BUDGET})")
        if "?" in excerpt:
            fails.append("excerpt asks a question (index entries state the finding)")
        blocks.append(excerpt)

    summary_words = 0
    summary_match = PUB_SUMMARY_RE.search(front)
    if summary_match is None:
        fails.append("no summary in front matter (the page opens with it)")
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
                PUB_EXCERPT_BUDGET, all_sentences, fails)
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

    for rel_path, (tier, budget) in FILES.items():
        if rel_path.startswith("_publications/"):
            fails = check_publication(rel_path, tier, budget, report)
        else:
            fails = check_file(rel_path, tier, budget, report)
        for fail in fails:
            failures.append(f"{rel_path}: {fail}")
    failures.extend(check_stats_include())

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
    print(f"prose_check: clean ({len(FILES)} files and the stats include)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
