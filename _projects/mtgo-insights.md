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

Thirty-six players sent me their Magic Online game logs, and this dashboard reads them: 8,884 matches from the current format era, one tab for each of 28 decks. Each tab shows how the deck did, which decks it beat, split by who went first and by sideboarding, and which cards were on the table when it won. A figure is coloured only when the games behind it put it clearly above or below even, so most cells stay plain on purpose.

I built it in August 2026 for my Modern testing team, Modern being a Magic: The Gathering format. [Its predecessor](/projects/deck-optimisation-engine/) could only read the decklists winners registered. A game log says what both players did.

## Links

- **Source:** private repository. The database links real Magic Online usernames to the decks they played and their results. That is harmless on my laptop and a different thing once published.
- **Deployed:** a protected Hugging Face Space. Only contributors can log in.
- **Sister for Arena:** [Arena Insights](/projects/arena-insights/)

<figure>
  <picture>
    <source type="image/webp" srcset="/files/mtgo_insights_home.webp">
    <img src="/files/mtgo_insights_home.png" alt="The home page of the dashboard: the corpus in numbers, then the tracked field as a matchup matrix, every deck against every other" width="1456" height="839" loading="lazy" style="width:100%; display:block; margin: 0 auto;">
  </picture>
</figure>

## What it does

- **Reads only what the log states.** Before writing any code I measured 300 to 400 sample logs. No line says that a creature died, life totals are never written, and a card loses its identifier when it changes zone. So the parser records what the log states (casts, targets, counters, attacks and results) and reconstructs nothing. For the decisions the tool supports, a biased picture is worse than a missing one.
- **Works out the deck from the cards it showed.** A log holds no decklist, so a hand-written set of signature rules names the deck from the cards seen, and the same rules run on both players. A review queue lists every match no rule could name, and every match where a rival rule came within one card of winning. My hand rulings live in a file beside the inferred verdict and never overwrite it, so they survive every rebuild and the disagreement stays visible. About 95% of matches are classified without me.
- **Compares every card against the deck's own baseline.** A card's figure is the gap, in percentage points, between the win rate in games where it was cast and in games where it was not. Both sides are read over the same deck, opponent, turn order and board (before or after sideboarding), never against a flat 50%. Sample sizes print beside every value, and cards cast fewer than 10 times are left out rather than shown.
- **Builds every list from the data.** Which decks get a tab, which rows the matchup matrix holds and which opponents a deck names are all recomputed on each build from one ranking. Nothing is hand-picked.

## Architecture

```sh
uv run python -m mtgo_insights.ingest data/insights.db data/gamelogs   # rebuild the store whole
uv run python -m mtgo_insights.app data/insights.db                     # serve it locally
```

The committed logs are the store of record, the copy everything else is rebuilt from, and the SQLite database is rebuilt from them whole on every ingest. Every figure on every page is a query over the same event rows, so a card's figure and its baseline can never come from different games. The deployed Space carries the database and nothing else: no ingestion code, no way to write, no credentials. It cannot change what it shows, and a redeploy means a rebuild at home.

Every number is limited to the current format era, which began with the bans of 18 May 2026. There is no control to widen it. A rate that includes games from a format nobody plays any more is a wrong answer, not a longer-run one.

## The decision that was hard

The matchup table used to colour a cell by its percentage: green above 55%, red below 50%, once the cell held 10 games. Across the 15 deck reports of 20 August 2026, that coloured 356 of 356 cells with enough games. But of the 149 green cells, 139 had a 95% confidence interval whose lower end sat below 55%. Of the 141 red cells, 131 had an upper end above 50%. The colours claimed more than the games could back.

At the threshold the ordering even inverted. A cell at 6 wins of 10 was green, on an interval from 31% to 83%. The cell beside it, at 7 of 9, was greyed as too thin, on a better interval.

A larger minimum sample did not fix it. At floors of 20, 30, 40 and 60 games, 120 of 129, 69 of 71, 36 of 38 and 18 of 20 coloured cells still straddled their band. The threshold was never the thing that was wrong. So both tables now ask one question: a cell gets a colour only when its whole interval clears the neutral point. On that day 20 of 356 cells kept a colour. Four contributors over one era cannot settle most matchups, and a page that admits it is worth more than one that guesses in colour.

## What was measured

The Space computes every deck report when it starts rather than shipping them precomputed. The worry was cost, so I measured it. Ten reports over 2,141 matches took 3.61 seconds to build. Two database indexes, one on the cast events and one on the match key, brought that to 0.92 seconds, at a cost of 4 megabytes on a 110 megabyte database. At 23 reports on a corpus 5 times larger, the build takes 10.3 seconds, the linear cost the first measurement predicted. Precomputing would have bought a second artifact that can disagree with the database it came from.

The baseline question was measured too. A card's figure is compared against the games where the card was not cast. A card with few copies in the deck is only ever cast in long games. A baseline over all games would then compare it against an average dominated by short games. Limiting the baseline to the same deck, opponent, turn order and board removes most of that mismatch for free. Matching game length as well moved every card by under 5 points, so I left it out.

## What did not work

The first design kept the list of named opponents written by hand, because which decks a reader asks about seemed like a question the data could not answer. By 20 September 2026 the hand-written list had fallen behind the logs. The Others row held 17.5% of the era's games, and 4,164 of its 4,614 games belonged to 50 decks the classifier had already named. One deck had a column of its own on 49 matches while another sat inside Others on 220. The list was retired, and every surface now derives from one ranking of the data.

## Stack

Python 3.13 · SQLite · Gradio · pytest · uv · Hugging Face Spaces

A total of 365 tests run over committed log fixtures. The repo carries 27 architecture decision records, each recording one design choice and the measurement behind it. A glossary gives the code and the page one language, with the near-synonyms to avoid listed under each term.

## Role

Sole builder. Contributors send logs, and the deck rulings in the review queue are mine. I used the dashboard through the team's testing season, and it changed some of my own deck decisions.

## Attribution

Game logs are the contributors' own, sent in by them for this purpose. The project is unofficial and not affiliated with Wizards of the Coast.
