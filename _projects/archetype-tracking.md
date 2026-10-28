---
title: "Archetype Tracking"
excerpt: "Reports 21 Modern archetypes weekly for a team meeting, from 17,787 published lists and 10 paper events. Measures what pilots registered, never performance."
date: 2026-09-11
type: engineering
stack:
  - Python
  - DuckDB
  - matplotlib
  - uv
  - pytest
---

My team meets weekly to talk about the Modern metagame, the decks people play in that Magic: The Gathering format and how that changes. This engine writes the numbers for the meeting. It reads every decklist Magic Online has published since the 18 May 2026 bans, plus 10 major paper events. It reports 21 archetypes weekly on a public page. A report says how much of the field a deck holds, whether pilots build it or copy it, and which slots moved.

It grew out of the [Deck Optimisation Engine](/projects/deck-optimisation-engine/), whose audit found that published decklists show what people play, not how well it performs. So this engine measures adoption, and says so wherever a figure could pass for performance.

## Links

- **Live reports:** [the current week's report per tracked deck](https://alejandrofupi-mtg-archetype-tracking.static.hf.space), a public Hugging Face Space
- **Source:** [archetype-tracking on GitHub](https://github.com/AlejandroFuentePinero/archetype-tracking)
- **Domain language:** [the glossary](https://github.com/AlejandroFuentePinero/archetype-tracking/blob/main/CONTEXT.md)
- **Architecture decision records:** [docs/adr/](https://github.com/AlejandroFuentePinero/archetype-tracking/tree/main/docs/adr)
- **Pilot knowledge:** [the heuristics file](https://github.com/AlejandroFuentePinero/archetype-tracking/blob/main/HEURISTICS.md)

<figure>
  <picture>
    <source type="image/webp" srcset="/files/archetype_tracking_broodscale.webp">
    <img src="/files/archetype_tracking_broodscale.png" alt="The live Broodscale report: share of published top-32 slots and league trophies week by week, with the paper events marked" width="1440" height="640" loading="lazy" style="width:100%; display:block; margin: 0 auto;">
  </picture>
</figure>

## What it does

- **Reads 2 sources and never mixes them.** Magic Online publishes only a challenge's top 32 and a league's undefeated lists, so any share it gives is a share of winners, not of the field. Melee, the platform the big paper events run on, publishes every player with their match record, so a paper event gives a true share of the field. The 2 are never drawn on the same axis. The store holds 17,787 published lists from 434 Magic Online events. Beside it sit 10 paper events with 7,352 lists, from the Pro Tour in Amsterdam to the Regional Championship in South East Asia.
- **Freezes what it reported.** The store is rebuilt from the cache on every run, and a past week's numbers can genuinely change as late league results arrive. So each week's figures and each fortnight's findings are written once and never rewritten. The report shows what was reported at the time, not what the store says now.
- **Tells building from copying.** Each week it counts how many lists copied the previous week's most-registered main deck, card for card. It counts pilots rather than published lists, because one player entering many leagues would otherwise look like the whole field copying. In the week to 6 September, 69 Esper Blink lists were published across 27 distinct main decks, and only 4 of those decks had more than 1 pilot behind them.
- **Flags a spike against 2 baselines.** A week counts as a spike when it is at least twice the median of the 4 weeks before it and twice the median week since the bans. Either baseline alone misreads a different kind of week. Esper Blink posted 27, 33, 36 and 43 finishes in 4 consecutive weeks against a median of 10 for the era. Against that long baseline alone it would never stop spiking.
- **Reads the paper events into the same storyline.** A major paper event is compared with 2 things, the last closed fortnight on Magic Online and the paper event before it, because the 2 comparisons answer different questions. A watchlist row names a card that the top finishers registered and the rest of the field did not. That is a weaker claim than an adoption row, so it has its own threshold.

## Architecture

```sh
uv run tracker refresh                  # cache published events, rebuild the store
uv run tracker weekly --deck broodscale # freeze the closed weeks, render the report
uv run tracker event-fetch --id 482105  # cache one paper event's standings from Melee
uv run tracker site                     # stage the public page: an index over the latest report per deck
```

Each tracked deck has its own entry in the config file. The entry names the archetype, the group of lists its volume figures count, the group its build readings are taken from, and the card slots it watches. Adding a deck is one entry and a first run. The raw cache is too large to commit, so a committed index records every published list the cache holds, one row per list. Any run can compare its population with the last one's, and lists that disappeared are reported beside lists that arrived.

The summary at the top of each report is written by hand: a lead sentence and one bullet per reading that found something. The engine prints the numbers, I write what they mean, and that text is committed beside the frozen rows. The public page is static: the rendered reports under stable names and an index over them, nothing else. The build refuses to publish a report with no summary.

## The decision that was hard

Every change the engine reports is measured over a fortnight. The fortnights start at 18 May 2026, the date of the Modern bans, run back to back and never overlap. The obvious unit was the week, and the plots stay weekly. But one week of this deck can hold anywhere from 9 published lists to 64. A threshold set as a share of one week mostly measures how big the week was. I tested that against the data: at every threshold from 5 to 25 percentage points, a weekly reading reversed in the following week about 2 times in 5.

Raising the threshold lost findings without making the survivors more reliable. Over a fortnight the same thresholds reversed between 15 and 22% of the time, and the rate fell as the threshold rose. Because the fortnights are fixed rather than rolling, the fortnight a date falls in never changes, and a row written 6 weeks ago still describes the same fortnight.

## What was measured

Some card slots are argued over by count rather than by presence: 2 copies or 3? When a fifth of the pilots go from 2 copies to 3, the average over 80 lists moves by only 3 tenths of a copy. No threshold on an average can catch that. Read as a distribution, the same decision is a fifth of the lists moving from one row to another. So a short list of watched slots is read by copy count, at a 10-point threshold.

The finer threshold works only because the list is short. Applied to every card, it gives 78 rows across 8 fortnights at 10 points against 41 at 20, and 38% of them reverse in the next fortnight.

At the paper events, conversion is the deck's share of the top 32 divided by its share of the whole field. It is the one performance reading Magic Online cannot give, because Magic Online publishes the winners without the field they came from. At Spotlight Dallas, Esper Blink was 61 of 928 lists and held 2 of the top 32, 0.95 times its field share. At Spotlight Brisbane the week before, it was 11 of 571 and held 1, 1.62 times its share, with a best finish of 2nd. Both print with their counts, because 32 slots is a handful of lists.

## What did not work

The frozen rows were rewritten twice before the reports reached a reader, and the record says why. On 13 September 2026 I found 4 defects in the engine, each of which had already written frozen rows.

Split cards, which carry 2 names on one card, kept only their first name on the paper side. So the storyline showed one card vanishing and another arriving in the same fortnight, 14 times. A snapshot taken before its own day's results had finished publishing was trusted. So 2 league days were recorded at 7 and 25 lists against a median of 60 on either side. And 67 rows reported a card returning to the deck when it had always been core to it, read from samples too thin to show an absence. Every frozen row was recomputed under the corrected engine, and the 965 rows that survived kept their wording to the byte.

Eight days later the return reading changed method again. It counted lists, and a league publishes every undefeated run, so one player entering repeatedly with an unusual build looked like the whole deck picking a card up. Four of the 20 return rows frozen for Izzet Prowess were one pilot across 3 league lists in June. The gate now counts distinct pilots, and 63 rows that rested on a single pilot were withdrawn. The rule that came out of it: never rewriting the past protects a stable system, not one still being calibrated against its first real use. A method I have ruled wrong may be withdrawn from the frozen files, with the pass recorded.

## Stack

Python 3.12+ · DuckDB · matplotlib · uv · pytest

A total of 167 tests run over committed Magic Online payload fixtures. The tests never touch the network on purpose, so fetched counts are spot-checked against the live site by hand. The repo carries 8 architecture decision records and a heuristics file. The heuristics are knowledge from actually playing the format, which decides how a number should be read and which no dataset could supply. Each entry is dated and sourced.

## Attribution

Decklist data comes from published Magic Online event pages and from Melee's public standings. The project is unofficial and not affiliated with Wizards of the Coast or with Melee.
