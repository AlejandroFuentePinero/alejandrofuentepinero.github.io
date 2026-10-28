---
title: "Arena Insights"
excerpt: "Reads Arena game logs, including the log owner's own hand, and reports card figures the way 17lands does. Two players, 58 matches so far."
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

Arena, the digital Magic: The Gathering client, writes a log of every game. The log records what both players did. For its owner it also records what they held: the opening hand, each mulligan, every draw and every sideboard. This dashboard reads both halves. The shared half gets the figures [MTGO Insights](/projects/mtgo-insights/) reads from Magic Online logs. The owner's half uses the vocabulary of 17lands, a card statistics site my team already reads, so nobody needs a legend.

The data so far is 2 players and 58 matches of Standard, one of Magic's formats. Most cells stay grey for lack of games, and the page says why.

## Links

- **Source:** private repository, for the same reason as its sister: the database links real Arena screen names to the decks they played and their results.
- **Deployed:** a protected Hugging Face Space. Only contributors can log in.
- **Sister project:** [MTGO Insights](/projects/mtgo-insights/)

<figure>
  <picture>
    <source type="image/webp" srcset="/files/arena_insights_card_table.webp">
    <img src="/files/arena_insights_card_table.png" alt="A deck report's card table, every column split into game 1 and the sideboarded games, with the in-hand figures beside the cast figures" width="1456" height="839" loading="lazy" style="width:100%; display:block; margin: 0 auto;">
  </picture>
</figure>

## What it does

- **Keeps every event the log states, and guesses nothing.** Unlike a Magic Online log, an Arena log is the game engine's own stream of state changes, printed into the client's console text, and about 100 times larger per match. It states every card moving from one zone to another, say from hand to battlefield, and why. It states every point of damage with its source and target, every life change and every card entering the owner's hand. The starting corpus of 55 matches held about 7,000 zone changes in 19 categories, 1,300 damage events, 1,600 life changes and 500 deaths, each with a cause. So the parser keeps its sister's rule of recording only what the log states, and has far less left to guess.
- **Reads the owner's hand with the columns 17lands uses.** For each card: how often it was in hand, in the opening hand, drawn, or never seen, and the win rate in each case against the games without it. The shared figures pool both players. The private figures read the owner's seat only. Each card row shows both counts side by side rather than hiding the difference.
- **Splits every card column by sideboarding.** After game 1 of a match, players may swap cards in from their sideboard, and a card can play a different role after that. So each column is shown once for game 1 and again for games 2 and 3, each read within its own games. The 2 halves are not meant to add up.

## Architecture

```sh
uv run python -m arena_insights.trim <raw> <out>                    # the filter, one file
uv run python -m arena_insights.ingest data/insights.db data/archive # rebuild the store whole
uv run python -m arena_insights.app data/insights.db                 # serve it locally
```

Arena deletes its own log archive without warning, so the trimmed log is the store of record, the copy everything else is rebuilt from. The trim keeps every game engine message and every submitted deck exactly as written, and drops the rest. It is a filter, never a transformation, and 2 tests hold that line. Every archived line is an unchanged raw line, and building from a raw log gives the same result as building from its trimmed form. Over the first 22 session logs the trim took 324 megabytes down to 105.

The project is a copy of its sister that is allowed to diverge, not a shared package. The parts worth sharing are the query builder, the rate helpers and the deploy flow. They are thin beside the parts that had to change: the parser, the schema, the classifier rules and the card table. A shared package would have meant adding extension points to an app that already worked. Instead, a fix found in one app is ported to the other by hand. Each sister commit I review is recorded with what was decided, so a fix that never crosses over is a chosen divergence rather than a silent one.

## The decision that was hard

Whatever the trim drops is gone for good for every contributor who sends a log and deletes their copy. So the drop list is a decision rather than a default, and I measured each entry. The client's menu of legal actions, restated on every game state, would more than double the archive at 110 megabytes, so it goes. The clock readings were on the drop list and came off it. They are 11% of the archive, and they are the only source for any question about thinking time. A field can be dropped later but never recovered.

One entry proved that the care was needed, in the other direction. One type of queued-state message was dropped as client chatter, on the same reasoning as the rest. It turned out to carry 43.8% of one player's casts. So 1 of the 3 judgement calls on the original list was wrong. The loss looked like silence rather than an error, because at the time only the first of the 2 guarantees above was tested.

## What was measured

Before writing any code I measured what the logs actually state, and checked on every match in the starting corpus which information is visible to whom. The owner's own hand carries card identities from the opening hand on. The opponent's hidden information never does, and the project asks nothing of it. Cards are keyed by title id against a snapshot of Arena's card database, which changes its hash with every client update.

I expected the clock readings to need their own table, because the rest of the store holds one row per game event. They did not. The engine restates a clock only when its value changes. So the corpus's 43,784 game states hold just 62,667 clock readings between them, and the time a game took is a subtraction at query time.

## Stack

Python · SQLite · Gradio · pytest · uv · Hugging Face Spaces

A total of 368 tests run over committed fixtures, most of them inherited from the sister and pointed at Arena logs instead. The repo carries 7 architecture decision records and a glossary of its own, because the 2 apps share the language of Magic but not the language of their formats.

## Role

Sole builder. I started it in September 2026 as the sister of MTGO Insights, so the same team could test on Arena too. The corpus holds 2 contributors so far, and its last match is from 4 September 2026. More logs is the only thing that makes the figures better, and the page says so.

## Attribution

Game logs are the contributors' own, sent in by them for this purpose. The in-hand vocabulary follows 17lands. The project is unofficial and not affiliated with Wizards of the Coast or with 17lands.
