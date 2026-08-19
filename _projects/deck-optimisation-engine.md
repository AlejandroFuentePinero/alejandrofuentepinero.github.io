---
title: "Deck Optimisation Engine"
excerpt: "Mines published Magic Online decklists to inform one Modern deck's flex slots. Its own audit retired the performance readings and kept the adoption ones."
date: 2026-08-19
type: engineering
stack:
  - Python
  - DuckDB
  - uv
  - pytest
---

Deck Optimisation Engine reads published Magic Online decklists for one Modern archetype. It reports what the archetype's camps register, what they have dropped, and where my own list differs. The store holds 19,691 lists from 508 events.

An audit against that database settled what the engine may claim. The adoption readings hold up. The performance readings do not. They run at 6 to 9% statistical power, on a sample that publishes only winners.

The engine keeps the first set and demotes the second.

## Links

- **Source:** [deck-optimisation-engine on GitHub](https://github.com/AlejandroFuentePinero/deck-optimisation-engine)
- **The audit:** [what published decklists can and cannot optimise](https://github.com/AlejandroFuentePinero/deck-optimisation-engine/blob/main/docs/postmortem-2026-08-08.md)
- **Domain language:** [the glossary](https://github.com/AlejandroFuentePinero/deck-optimisation-engine/blob/main/CONTEXT.md)

## What it does

- **Names its population on every reading.** One camp, in one stratum, over one window. A share across 2 populations is a number no population reported, so the engine refuses to print one.
- **Tracks movement, not presence.** Cards migrating between mainboard and sideboard, and cards climbing in the fresh window. When a camp leaves a slot, the engine reports what it played instead.
- **Audits my own 75 against its camp**, least-backed slot first. Each open question files as a dated record with an evidence log and a verdict.
- **Rebuilds from cache.** Every fetched event lands in a local cache, and the store rebuilds from that cache on every run. No reading depends on a live fetch.

## What the audit changed

The engine could report an outcome contrast: whether lists carrying a card place better. The audit measured what that instrument can detect. Its floor sits at 22 to 32 percentage points, and the effects it chases are roughly 10 times smaller. Every contrast the engine had run came back undetectable.

Published lists are conditioned on winning. Challenges publish the top 32, leagues publish 5-0 records, and losing lists never appear. No care in the statistics repairs that.

So every performance reading now prints its own detection floor and reads as a disconfirmation instrument. It can rule a large effect out. It will almost never confirm that a card helps.

The vocabulary moved with the verdict. This is an adoption measurement device, and adoption is not performance.

## How it runs

```sh
deck-engine refresh     # cache published events, then rebuild the store
deck-engine reference   # audit the 75 against its camp, least-backed slot first
deck-engine report      # the whole run as one self-contained file
```

The fetch layer is a sequential scraper with no parallelism, so a backfill is slow by construction. It retries a page 5 times with lengthening backoff, because the site sometimes serves a 200 with missing content. A stub taken at face value drops published lists from the cache silently.

## Stack

Python 3.12+ · DuckDB · uv · pytest

163 tests run over committed event payload fixtures. The network layer sits outside the test seam by design. I spot-check fetched counts against the live site instead.

## Attribution

Decklist data comes from published Magic Online event pages. The project is unofficial and not affiliated with Wizards of the Coast.
