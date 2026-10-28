---
title: "Arena Insights"
excerpt: "Reads Arena game logs, the log owner's hand included, and shows card figures in 17lands vocabulary. Two players and 58 matches, mostly grey cells."
date: 2026-09-06
type: engineering
source: private
stack:
  - Python
  - SQLite
  - Gradio
  - pytest
  - Hugging Face Spaces
---

An Arena game log states what both seats did. For the log owner's seat it also states what was in hand: the opening 7, each mulligan, every draw and every sideboard list. This dashboard reads both. The public figures are the ones [MTGO Insights](/projects/mtgo-insights/) reads from Magic Online logs. The private figures use the vocabulary of 17lands, the site drafters already read, so nobody needs a legend.

The corpus is 2 players and 58 matches of Standard, a Magic: The Gathering format. Most cells are greyed for thinness, and the page says so rather than colouring them.

I started it in September 2026 as the sister of MTGO Insights, for the same team's testing on Arena, the digital Magic client.

## Links

- **Source:** private repository, for the same reason as its sister: the database joins real Arena screen names to inferred decklists and records.
- **Deployed:** a protected Hugging Face Space that answers only to contributor logins.
- **Sister project:** [MTGO Insights](/projects/mtgo-insights/)

<figure>
  <picture>
    <source type="image/webp" srcset="/files/arena_insights_card_table.webp">
    <img src="/files/arena_insights_card_table.png" alt="A deck report's card table, every column split into game 1 and the sideboarded games, with the in-hand figures beside the cast figures" width="1456" height="839" loading="lazy" style="width:100%; display:block; margin: 0 auto;">
  </picture>
</figure>

## What it does

- **Extracts every stated transition.** A Magic Online log is sentences, and its sister reads only what the words state. An Arena log is the game engine's own state stream embedded in client console text, about 100 times larger per match. It states every zone change with its reason, every point of damage with source and target, every life change and every card entering the owner's hand. Measured over the starting corpus of 55 matches: about 7,000 zone transfers in 19 categories, 1,300 damage events, 1,600 life changes and 500 deaths, each with a stated cause. So the extraction keeps the sister's rule against inference and has far less left to infer.
- **Reads the private seat with 17lands' columns.** Games in hand, opening hand, games drawn and games not seen, each with its lift over the games without the card. The public figures pool both seats, the private figures read the owner's seat only, and one card row carries both counts rather than hiding the difference.
- **Splits every card column by board.** A card is a different card after sideboarding. Each column is shown for game 1 and again for games 2 and 3, read inside its own games, and the halves are not meant to add up.

## Architecture

```sh
uv run python -m arena_insights.trim <raw> <out>                    # the filter, one file
uv run python -m arena_insights.ingest data/insights.db data/archive # rebuild the store whole
uv run python -m arena_insights.app data/insights.db                 # serve it locally
```

Arena purges its own log archive without warning, so the trimmed log is the store of record. The trim keeps every game engine message and every deck submission verbatim and drops the rest. It is a filter and never a transformation, and 2 tests hold that line. Every archived line is a raw line, and a build over a raw log equals a build over its trimmed form. Over the first 22 session logs the trim took 324 megabytes to 105.

The project is a copy of its sister that diverges, not a shared package. The parts worth sharing are the query builder, the rate helpers and the deploy flow. They are thin beside the parts that had to change: the parser, the schema, the classifier rules and the card table. A shared package would have meant extension points in an app that already worked. A fix found in one app is ported by hand. Each sister commit read is recorded with what was decided, so a fix that never crosses is a chosen divergence rather than a silent one.

## The decision that was hard

What the trim drops is permanent for every contributor who sends a log and deletes their copy. So the drop list is a decision rather than a default, and I measured each entry. The client's menu of legal actions, restated on every state, would more than double the archive at 110 megabytes. The clock readings were on the drop list and came off it, at 11% of the archive. They are the only source for a think-time question, and a field can be dropped later but never recovered.

The entry that proved the care was needed went the other way. One queued-state message type was dropped on the same client-chatter reasoning as the rest. It carried 43.8% of one seat's casts. One of 3 judgement calls on the original list was wrong. The loss read as silence rather than as an error, because only the first of the 2 guarantees above was tested at the time.

## What was measured

Before any code existed I measured what the logs actually state, and verified the visibility model on every match in the starting corpus. The owner's own hand carries card identities from the opening hand on. The opponent's hidden information never does, and the project asks nothing of it. Cards are keyed by title id against a snapshot of Arena's card database, which rotates under a new hash on every client update.

The clock readings were expected to force an exception to the one-row-per-transition grain. They did not. The engine restates a clock only when its value changes, so the corpus's 43,784 states carry 62,667 readings between them, and a per-game figure is a subtraction at query time.

## Stack

Python · SQLite · Gradio · pytest · uv · Hugging Face Spaces

A total of 368 tests run over committed fixtures, most of them inherited from the sister and re-pointed at Arena logs. The repo carries 7 architecture decision records and a glossary of its own, because the Magic language is shared and the format language is not.

## Role

Sole builder. The corpus holds 2 contributors so far, and its last match is from 4 September 2026. More logs is the only thing that makes the figures better, and the page says so.

## Attribution

Game logs are the contributors' own, sent in by them for this purpose. The in-hand vocabulary follows 17lands. The project is unofficial and not affiliated with Wizards of the Coast or with 17lands.
