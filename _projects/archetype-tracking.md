---
title: "Archetype Tracking"
excerpt: "Reports 2 Modern archetypes fortnightly for a team meeting. It measures what pilots registered and never performance, and freezes every reading it has reported."
date: 2026-09-11
type: engineering
stack:
  - Python
  - DuckDB
  - matplotlib
  - uv
  - pytest
---

My team meets weekly to talk about the Modern metagame, a Magic: The Gathering format, and this engine writes the numbers for that meeting. The engine reads every decklist Magic Online publishes, plus the full standings of the major paper events, and reports 2 named archetypes fortnight by fortnight. It says how much of the field each holds, whether it converts presence into finishes, whether pilots are still building it or copying it, and which slots moved. Every reading it has reported stays frozen on disk.

It grew out of the [Deck Optimisation Engine](/projects/deck-optimisation-engine/), whose audit found that published lists cannot measure performance. So this engine measures adoption, and says so on every figure that could pass for anything else.

## Links

- **Source:** [archetype-tracking on GitHub](https://github.com/AlejandroFuentePinero/archetype-tracking)
- **Domain language:** [the glossary](https://github.com/AlejandroFuentePinero/archetype-tracking/blob/main/CONTEXT.md)
- **Architecture decision record:** [what a backfill established about the Magic Online stream](https://github.com/AlejandroFuentePinero/archetype-tracking/blob/main/docs/adr/0001-reading-the-published-mtgo-stream.md)
- **Pilot knowledge:** [the heuristics file](https://github.com/AlejandroFuentePinero/archetype-tracking/blob/main/HEURISTICS.md)

<figure>
  <picture>
    <source type="image/webp" srcset="/files/archetype_tracking_presence.webp">
    <img src="/files/archetype_tracking_presence.png" alt="The presence section of a weekly Esper Blink report: share of top-32 slots, share of league trophies, and share by version of the deck" width="1880" height="1694" loading="lazy" style="width:100%; display:block; margin: 0 auto;">
  </picture>
</figure>

## What it does

- **Reads 2 sources and never pools them.** Magic Online publishes the top 32 of a challenge and only the undefeated lists of a league, so every share it yields is a share of a cut. Melee, the platform the big paper events run on, publishes every finisher with their match record, so a paper event yields a true field share. The 2 never share an axis. The store holds 23,576 published lists from 608 Magic Online events, and 3 paper events with 1,861 lists sit beside it.
- **Freezes what it reported.** The store is rebuilt from the cache on every run, and a past week can genuinely move when a league's results fill in. So each week's figures and each fortnight's findings are written once, appended and never rewritten. The report renders what was reported, not what the store now says.
- **Separates building from copying.** Each week it counts how many builds copied the previous week's most-registered main deck. The count is per pilot rather than per publication, because one grinder entering many leagues would otherwise read as the field copying. The week to 6 September published 69 Esper Blink lists on 27 distinct main decks, and only 4 of those had a second pilot behind them.
- **Flags a spike against 2 baselines.** A week is flagged at twice both the median of the 4 weeks behind it and the median week since the bans. A performance figure taken over a copied deck measures adoption density. Either baseline alone misreads a different kind of week. Esper Blink ran 27, 33, 36 and 43 finishes on 4 consecutive weeks against a regime median of 10, and against that baseline alone it would never stop spiking.

## Architecture

```sh
uv run tracker refresh                  # cache published events, rebuild the store
uv run tracker weekly --deck blink      # freeze the closed weeks, render the report
uv run tracker event-fetch --id 405590  # cache one paper event's standings from Melee
```

Which lists a report reads is not a flag. It is the report's own entry in config: the archetype, the camp its volume figures pool over, the camp its build readings are taken on, and the slots it watches. Adding a subject is one entry and a first run. The raw cache is too large to commit, so a committed index records every published list the cache holds, one row per list. Any run can tell its population from the last one's, and withdrawals are reported beside arrivals.

The summary at the top of each report is written by hand. The engine prints the numbers, I write what they mean in a fixed clause order, and that text is committed beside the frozen rows.

## The decision that was hard

Every change the engine reports is read over a fortnight, anchored at the regime boundary of 18 May 2026, the date of the Modern bans, and never overlapping. The obvious unit was the week, and the plots stay weekly. But a week of this deck runs from 9 published lists to 64, so any threshold set as a share of a week measures the sample size. I tested the bars against the data. At every bar from 5 to 25 percentage points, a weekly reading reversed in the following week about 2 times in 5. Raising the bar lost findings without buying purity.

Over a fortnight the same bars reversed between 15 and 22% of the time, and the rate fell as the bar rose. The bins are anchored rather than trailing, so the bin a date falls in never moves, and a row written 6 weeks ago still describes the same fortnight.

## What was measured

The slots pilots argue about by count rather than by presence get their own reading. Two copies going to 3 in a fifth of the camp moves a mean over 80 lists by 3 tenths of a copy. No bar on a mean can hold that. Read as a distribution, the same decision is a fifth of the lists moving from one row to another. So a short list of watched slots is read at 10 points by copy count.

The finer bar holds only because the list is short. Unfiltered, that population gives 78 rows across 8 fortnights at 10 points against 41 at 20, and 38% of them reverse in the next fortnight.

At the paper events, conversion is the deck's share of the top 32 over its share of the whole field. It is the one performance reading Magic Online cannot make, because its challenge data is a cut with no field under it. At Spotlight Dallas, Esper Blink was 61 of 928 lists and held 2 of the top 32, 0.95 times its field share. At Spotlight Brisbane the week before, it was 11 of 571 and held 1 at 1.62 times, with a best finish of 2nd. Both are printed with their counts, because 32 slots is a handful of lists.

## Stack

Python 3.12+ · DuckDB · matplotlib · uv · pytest

A total of 78 tests run over committed Magic Online payload fixtures. The network layer sits outside the test seam on purpose, and fetched counts are spot-checked against the live site. The repo also carries a heuristics file: knowledge from play that decides how a number is read and that no dataset could supply, each entry dated and sourced.

## Attribution

Decklist data comes from published Magic Online event pages and from Melee's public standings. The project is unofficial and not affiliated with Wizards of the Coast or with Melee.
