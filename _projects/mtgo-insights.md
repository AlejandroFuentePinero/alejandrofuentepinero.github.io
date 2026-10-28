---
title: "MTGO Insights"
excerpt: "Reads 36 players' Magic Online logs into one dashboard: 28 decks, 8,884 matches, and colour only where the games back the claim."
date: 2026-08-11
type: engineering
source: private
stack:
  - Python
  - SQLite
  - Gradio
  - pytest
  - Hugging Face Spaces
---

Thirty-six players sent me their Magic Online game logs, and this dashboard reads them: 8,884 matches in the current format era, one tab for each of 28 decks. Each tab says how the deck did, who it beat, split by turn order and sideboarding, and which cards were on the table when it won. A figure wears a colour only when a confidence interval clears the neutral point. Most cells stay plain, and that is the honest answer rather than a missing one.

I built it in August 2026 for my Modern testing team, Modern being a Magic: The Gathering format. The [Deck Optimisation Engine](/projects/deck-optimisation-engine/) could only read what winners registered. A game log says what both seats actually did.

## Links

- **Source:** private repository. The database joins real Magic Online usernames to inferred decklists and records, which is unremarkable on a laptop and different once published.
- **Deployed:** a protected Hugging Face Space that answers only to contributor logins.
- **Sister for Arena:** [Arena Insights](/projects/arena-insights/)

<figure>
  <picture>
    <source type="image/webp" srcset="/files/mtgo_insights_home.webp">
    <img src="/files/mtgo_insights_home.png" alt="The home page of the dashboard: the corpus in numbers, then the tracked field as a matchup matrix, every deck against every other" width="1456" height="839" loading="lazy" style="width:100%; display:block; margin: 0 auto;">
  </picture>
</figure>

## What it does

- **Reads only what the log states.** Before any code existed I measured 300 to 400 sample logs. No line records a creature dying, life totals are never written, and a card's instance id does not survive a change of zone. So the parser records casts, targets, counters, attacks and results, and reconstructs nothing. A biased picture is worse than a missing one for the decisions the tool exists to support.
- **Infers the deck from the cards it showed.** A log holds no decklist, so a hand-curated set of signature rules names the archetype from the cards observed, the same classifier on both seats. A review queue lists every match that landed unassigned and every verdict a rival rule came within one card of. Hand rulings live in a file beside the inferred verdict, never over it, so they survive every rebuild and the disagreement stays visible. About 95% of classification runs unattended.
- **Reads every rate against the deck's own baseline.** A card's figure is the gap, in percentage points, between the games it was cast in and the games it was not. Both sides are read over the same deck, opponent, turn order and board, never against a flat 50%. The sample sizes print beside every value, and cards cast fewer than 10 times are left out rather than offered.
- **Derives every list from the corpus.** Which decks get a tab, which rows the field matrix holds and which opponents a deck names are all recomputed on each build from one ranking. Nothing is hand-picked.

## Architecture

```sh
uv run python -m mtgo_insights.ingest data/insights.db data/gamelogs   # rebuild the store whole
uv run python -m mtgo_insights.app data/insights.db                     # serve it locally
```

The committed logs are the store of record, and the SQLite database is rebuilt whole from them on every ingest. Every figure on every page is a query over the same event rows, so a card figure and its baseline can never be read over different games. The deployed Space carries the database and nothing else: no ingestion code, no write path, no credentials. It cannot change what it shows, and a redeploy is a rebuild at home.

Every number is bounded to the current format era, which opened with the bans of 18 May 2026. There is no control that widens it. A rate carrying games from a format nobody plays any more is a wrong answer, not a longer-run one.

## The decision that was hard

The matchup table used to colour a cell by where its percentage fell: green above 55%, red below 50%, once the cell held 10 games. Measured across the 15 deck reports of 20 August 2026, that tinted 356 of 356 sound cells. Of the 149 green cells, 139 had a 95% interval whose lower bound sat below 55%. Of the 141 red cells, 131 had an upper bound above 50%.

At the threshold the ordering inverted. A 6 of 10 cell was tinted green on an interval from 31% to 83%. A 7 of 9 cell beside it was greyed for thinness, on a better interval.

A larger sample floor did not fix it. At floors of 20, 30, 40 and 60 games, 120 of 129, 69 of 71, 36 of 38 and 18 of 20 tinted cells still straddled their band. The threshold was never the thing that was wrong. So both tables now ask the same question: a colour is worn only when the interval clears the neutral point whole. On that day 20 of 356 cells kept a colour. Four contributors over one era cannot settle most matchups, and a page that admits it is worth more than one that guesses in colour.

## What was measured

The Space computes every deck report at boot rather than shipping them precomputed. The worry was cost, so I measured it. Ten reports over 2,141 matches took 3.61 seconds to build. Two indexes, one partial index on the cast verb and one on the match key, took that to 0.92 seconds, for 4 megabytes on a 110 megabyte database. At 23 reports on a corpus 5 times larger, the build takes 10.3 seconds, which is the linear cost the first measurement predicted. Precomputing would have bought a second artifact that can disagree with the database it came from.

The baseline question was measured too. The card figure's contrast is the games where the card was not cast. Every low-density card is only ever cast in long games, so a baseline over all games compares it against a mostly-short-game average. Scoping the baseline to the same deck, opponent, turn order and board removes most of that mismatch for free. Matching game length as well moved every card by under 5 points, and was left out.

## What did not work

The first design kept the list of named opponents curated by hand, because which decks a reader asks about seemed like a question the corpus could not answer. By 20 September 2026 the hand-written list had fallen behind the logs. The Others row held 17.5% of the era's games, and 4,164 of its 4,614 games belonged to 50 decks the classifier had already named. One deck held a column of its own on 49 matches while another sat inside the bucket on 220. The list was retired and every surface now derives from one ranking of the corpus.

## Stack

Python 3.13 · SQLite · Gradio · pytest · uv · Hugging Face Spaces

A total of 365 tests run over committed log fixtures. The repo carries 27 architecture decision records, each recording one design choice and the measurement behind it. A glossary gives the code and the page one language, with the near-synonyms to avoid listed under each term.

## Role

Sole builder. Contributors send logs, and the deck rulings in the review queue are mine. I used the dashboard through the team's testing season, and it changed some of my own deck decisions.

## Attribution

Game logs are the contributors' own, sent in by them for this purpose. The project is unofficial and not affiliated with Wizards of the Coast.
