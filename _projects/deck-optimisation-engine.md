---
title: "Deck Optimisation Engine"
excerpt: "Mines Magic Online decklists to tune one Modern deck. Its own audit showed the data measures adoption, not performance, and the engine says so."
date: 2026-08-19
type: engineering
stack:
  - Python
  - DuckDB
  - uv
  - pytest
---

Before a paper tournament I wanted to know what the best players of my Modern deck were registering, and where my list stood. Modern is a Magic: The Gathering format, and Magic Online publishes the winning decklists from its events. The engine reads those lists for one deck, sorts them into camps, and reports what each camp plays, what it dropped, and where my list differs. The store holds 19,691 lists from 508 events.

Then I audited the engine against its own database, and the audit split it in 2. The adoption readings hold. The performance readings run at 6 to 9% statistical power on a sample that only shows winners, so the engine demotes them and says so.

## Links

- **Source:** [deck-optimisation-engine on GitHub](https://github.com/AlejandroFuentePinero/deck-optimisation-engine)
- **The audit:** [what published decklists can and cannot optimise](https://github.com/AlejandroFuentePinero/deck-optimisation-engine/blob/main/docs/postmortem-2026-08-08.md)
- **Domain language:** [the glossary](https://github.com/AlejandroFuentePinero/deck-optimisation-engine/blob/main/CONTEXT.md)

## What it does

- **Names its population on every reading.** Every number is taken over one camp, in one class of event, over one window of time. A share pooled across 2 of those is a number nobody reported, so the engine refuses to print one.
- **Tracks movement, not presence.** It watches cards migrate between the main deck and the sideboard, the 15 spare cards swapped in between games, and it watches cards still climbing in the freshest window. When a camp abandons a slot, the engine reports what it played there instead.
- **Audits my own 75 against its camp**, starting with the slot that has the least support. A deck is 75 cards, 60 in the main deck and 15 in the sideboard. Each open question becomes a dated record with an evidence log and a verdict.
- **Rebuilds from cache.** Every fetched event lands in a local cache, and the store is rebuilt from that cache on every run, so no reading ever depends on a live fetch.

## What the audit changed

The engine could also run an outcome contrast: do the lists carrying a given card place better than the lists without it? The audit asked what that instrument could actually detect. Its detection floor, the smallest effect it can tell apart from noise, sits at 22 to 32 percentage points. The effects a flex slot can produce are roughly 10 times smaller. Every contrast the engine had ever run came back undetectable.

The deeper problem is the sample. Published lists are conditioned on winning: challenges publish the top 32, leagues publish only undefeated 5-0 records, and losing lists never appear at all. No amount of statistical care repairs a dataset that has thrown away the losers.

So every performance reading now prints its own detection floor and reads as a disconfirmation instrument. It can rule out a large effect, and it will almost never confirm that a card helps. The vocabulary moved with the verdict: this is an adoption measurement device, and adoption is not performance.

## How it runs

```sh
deck-engine refresh     # cache published events, then rebuild the store
deck-engine reference   # audit the 75 against its camp, least-backed slot first
deck-engine report      # the whole run as one self-contained file
```

The fetch layer is a sequential scraper with no parallelism, so a backfill is slow by design and stays polite to the site. It retries a page up to 5 times with lengthening pauses, because the site sometimes serves a page that looks complete and is empty. A stub taken at face value would silently drop published lists from the cache.

## Stack

Python 3.12+ · DuckDB · uv · pytest

A total of 163 tests run over committed event payloads. The network layer sits outside the test seam on purpose, so I spot-check fetched counts against the live site instead.

## Attribution

Decklist data comes from published Magic Online event pages. The project is unofficial and not affiliated with Wizards of the Coast.
