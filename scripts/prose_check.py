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

Scope: the files in FILES below plus the stats include. Later Phase 5
passes extend FILES collection by collection. The styleguide (internal,
exempt) and the redirect stubs (no prose) are deliberately absent.

Verbatim records (citations, degree and course titles, grant and award
lines, the nomination list) sit between <!-- record --> and
<!-- /record --> markers in the source and are skipped by every check:
records are never rewritten, so nothing in them is actionable. Chip and
label spans, filter buttons and Liquid output are presentation tokens,
not prose, and are removed before checking. Words inside Liquid include
parameters (the twin frame context line) are not visible to this script;
the Gate evidence counts them by hand.

Usage:
  python3 scripts/prose_check.py             check, exit 1 on violations
  python3 scripts/prose_check.py --metrics   also print the metrics table
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# file -> (tier, word budget). Budgets from CONTENT_MAP.md section 8;
# terms and sitemap budgets set in DECISIONS.md (Phase 5).
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
}

STATS_INCLUDE = "_includes/stats-band.html"

SENTENCE_LIMIT = {"A": 20, "B": 25}
PARAGRAPH_LIMIT = 4

EM_DASH = "—"
EN_DASH = "–"

# Acronyms treated as words, plus proper names that look like acronyms
# (TERMINOLOGY.md, acronym policy).
ACRONYM_ALLOW = {"AI", "CV", "PDF", "XML", "URL", "CONAF", "CSIRO", "ORCID"}

# Acronym -> expansion that must appear earlier on the same page.
ACRONYM_EXPANSIONS = {
    "EPBC": "environment protection and biodiversity conservation",
    "IUCN": "international union for conservation of nature",
    "LLM": "large language model",
    "RAG": "retrieval-augmented generation",
    "WCS": "wildlife conservation society",
    "DOI": "digital object identifier",
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
    prose_text = "\n".join(blocks)

    for pattern, label in BANNED:
        for block in blocks:
            if re.search(pattern, block, re.I):
                fails.append(f'banned word or construction "{label}" in: "{block[:70]}"')

    all_sentences = []
    limit = SENTENCE_LIMIT[tier]
    for block in blocks:
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

    words = sum(word_count(b) for b in blocks)
    if words > budget:
        fails.append(f"page at {words} words, over its budget of {budget}")

    lengths = [word_count(s) for s in all_sentences]
    report[rel_path] = {
        "tier": tier,
        "words": words,
        "budget": budget,
        "sentences": len(all_sentences),
        "mean": round(sum(lengths) / len(lengths), 1) if lengths else 0,
        "longest": max(lengths) if lengths else 0,
        "fails": fails,
    }
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

    for rel_path, (tier, budget) in FILES.items():
        for fail in check_file(rel_path, tier, budget, report):
            failures.append(f"{rel_path}: {fail}")
    failures.extend(check_stats_include())

    if show_metrics:
        header = f'{"file":<34}{"tier":<6}{"words":<12}{"sents":<7}{"mean":<7}{"longest":<9}{"dashes":<8}{"banned"}'
        print(header)
        for rel_path, r in report.items():
            dash_fails = sum("dash" in f for f in r["fails"])
            banned_fails = sum("banned" in f for f in r["fails"])
            print(
                f'{rel_path:<34}{r["tier"]:<6}'
                f'{str(r["words"]) + "/" + str(r["budget"]):<12}'
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
