---
title: "7PH Graph: A Knowledge Graph of a Competitive Metagame"
excerpt: "A live knowledge graph of a competitive Magic format. It shows which cards travel together and refuses to chart weak evidence."
date: 2026-08-02
type: engineering
stack:
  - Python
  - Cypher
  - Gradio
  - Plotly
redirect_from:
  - /datascience/projects/7ph-graph/
---

Stats sites for card games answer which decks win and which cards get played. What none of them can tell you is which cards travel together, at which events, and how that has changed. 7PH Graph answers those questions for the Australian 7 Point Highlander format of Magic: The Gathering. It links 107 events, 1,086 pilots, 4,591 decks and 4,995 cards into one knowledge graph, with an interactive explorer at 7phgraph.com.

The tournament data behind it is incomplete and sometimes contradicts itself, so I built the graph to be honest about what it knows. Every value the build decides carries the name of the rule that decided it, and no chart draws when the evidence cannot hold it up.

## Links

- **Live explorer:** [www.7phgraph.com](https://www.7phgraph.com)
- **Source:** [7ph-graph on GitHub](https://github.com/AlejandroFuentePinero/7ph-graph)
- **Domain language:** [the domain glossary](https://github.com/AlejandroFuentePinero/7ph-graph/blob/main/CONTEXT.md)
- **Architecture decision records:** [docs/adr/](https://github.com/AlejandroFuentePinero/7ph-graph/tree/main/docs/adr)

<figure>
  <picture>
    <source type="image/webp" srcset="/files/7ph_graph_pilot_overview.webp">
    <img src="/files/7ph_graph_pilot_overview.png" alt="7PH Graph, a pilot's neighbourhood drawn as an interactive graph" width="1440" height="1465" loading="lazy" style="width:100%; display:block; margin: 0 auto;">
  </picture>
</figure>

## What it does

- **Draws a subject's neighbourhood.** Pick a pilot or a card and the app draws everything around it as an interactive graph: the decks, the events, the placements and the archetypes. Every node opens its details, and every deck links out to Moxfield.
- **Compares 2 pilots head to head** across the events they both attended, and says so plainly when they never met.
- **Surfaces hidden gems**, the cards that are rare within an archetype yet keep turning up in its best decks. Rare means at most 10% of that archetype's decks. The evidence floor is a fixed 5 decks rather than a share, because a share would let a card in 1 or 2 lucky decks pass as a gem.
- **Charts the metagame over time**: how each archetype's share of the field moves against its average finish, and how quickly individual cards were adopted. The player leaderboard prints an honest interval beside every rank.

When a result is too large to read, the app neither draws it nor cuts it down. It tells you what the query matched and asks you to narrow it, because a truncated graph looks like an answer and is not one. The same rule refuses a pilot with too little history and a pair of pilots who never met.

<figure>
  <picture>
    <source type="image/webp" srcset="/files/7ph_graph_metagame_landscape.webp">
    <img src="/files/7ph_graph_metagame_landscape.png" alt="Archetype share against mean finish, with error bars" width="1240" height="745" loading="lazy" style="width:100%; display:block; margin: 0 auto;">
  </picture>
</figure>

## Architecture

The system splits into 3 commands, and only the first 2 ever talk to the upstream data source:

```sh
graph7ph fetch   # download source data into snapshots/<timestamp>/
graph7ph build   # load the accumulated snapshots into a graph artifact
graph7ph app     # serve the explorer over the prebuilt artifact
```

Each fetch lands as a snapshot that is never edited afterwards. The build then folds the whole sequence of snapshots together, checking each one against everything that came before it. If a fact has been quietly rewritten in a later snapshot, the build notices. It holds the fact at its earlier value and reports the change as something for a human to look at, not a notice to scroll past.

A new graph artifact is promoted only when it passes validation, and the previous one stays on disk for instant rollback. The app itself never fetches or builds anything. It opens a promoted artifact read-only, which means the deployed instance holds no upstream credential at all.

Midway through the project the vendor archived Kùzu, the embedded graph database underneath everything. I moved to Ladybug, the active fork, and graded the migration with the recorded oracle described below.

## The decision that was hard

The tournament data arrives messy. Some events report a finish only as a band, such as top 8. Others report field sizes that their own deck counts contradict. The easy fix was a yes-or-no flag marking a value as estimated.

I chose something stricter: every uncertain value gets a companion column that names the rule which produced it. The column stays empty when the source's own number stands. One query can then answer: which of this deck's numbers did the build decide, and under which rule? The same column will hold whatever new kind of uncertainty the next season brings.

The design paid for itself fast. A total of 28 decks had a placement but no score on the shared scale, so every ranked average silently dropped them. All but 1 of the 28 were top-8 finishes. The bias ran one way, and it hit hardest the pilots who had made the cut.

## What was measured

Leaderboards invite overconfidence, so I measured how far the standings can be trusted. The test is a bootstrap: redraw every contender's finishes at random, with replacement, and rescore the whole field 1,000 times. On average only 4.9 of the top 8 keep their place, and rank 7's honest interval runs from 1 to 40. Every surface that ranks people now prints that uncertainty beside the rank.

The store migration was graded by a recorded oracle rather than by reading the diff. A baseline file captures what every query entry point answers, along with table counts and dropdown catalogues. The baseline command exits non-zero on any difference and refuses to overwrite itself without a force flag, so a regression cannot slip through by being re-recorded.

The visual layer is tested by a real browser rather than by assertions about markup. A Playwright suite measures what the graph document actually paints at desktop width, and an acceptance script walks every tab and state at phone and desktop widths, photographing each one. It then measures every rendered text node against the background it sits on and grades the contrast at the Web Content Accessibility Guidelines AA level.

## What did not work

An early version of the leaderboard drew each contender's form as a rolling window, and the lines looked convincing. Before shipping it I tested what that shape was made of. The test shuffles each pilot's finishes across their own event dates, which destroys any trace of when they played well while keeping how well they played overall. If the chart were showing form, the shuffle should flatten it.

It did not. The real chart moved by 0.0915 and the shuffled versions by 0.0885, with a 90% range of 0.0823 to 0.0947. The movement on screen was sampling noise dressed up as form. A running score replaced the window. I also renamed the tab from Best player race to Player leaderboard, because the old title asserted exactly what the evidence refused.

## Deployment

The app runs as a Hugging Face Space with protected visibility behind [www.7phgraph.com](https://www.7phgraph.com), so the explorer stays reachable while its files stay private. The deployed bundle carries the built graph and the ingestion reports, and a public Space offers both for download.

## Stack

Python 3.11+ · Ladybug (embedded Cypher graph store) · Gradio · Plotly · pyvis · Pydantic · pytest · Playwright · uv · Hugging Face Spaces

The repo carries 26 architecture decision records, each a short document recording one design choice and the reasons behind it. A domain glossary gives the code and the interface one shared language. The test suite is slightly larger than the source it covers.

## Attribution

Metagame data comes from [7phstats](https://7phstats.com). Decklists link out to [Moxfield](https://moxfield.com), free and non-commercial per Moxfield's API terms. The project is unofficial and not affiliated with either service or with Wizards of the Coast.
