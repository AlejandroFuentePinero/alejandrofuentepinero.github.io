---
title: "7PH Graph: A Knowledge Graph of a Competitive Metagame"
excerpt: "A live knowledge graph of a competitive Magic format: 107 events, 4,591 decks, every chart backed by provenance and statistical guards."
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

7PH Graph is a live knowledge graph of the Australian 7 Point Highlander metagame, a competitive Magic: The Gathering format. It links 107 events, 1,083 pilots, 4,591 decks and 4,995 cards behind an interactive explorer at 7phgraph.com.

Tabular stats sites answer aggregate questions well. This graph answers the relational ones: which cards travel together, at which events, and how that changed.

The source data is incomplete and sometimes contradicts itself. So every value the build decides carries the name of the rule that decided it. Charts refuse to draw when the evidence cannot support them.

## Links

- **Live explorer:** [www.7phgraph.com](https://www.7phgraph.com)
- **Source:** [7ph-graph on GitHub](https://github.com/AlejandroFuentePinero/7ph-graph)
- **Domain language:** [the domain glossary](https://github.com/AlejandroFuentePinero/7ph-graph/blob/main/CONTEXT.md)
- **Architecture decision records:** [docs/adr/](https://github.com/AlejandroFuentePinero/7ph-graph/tree/main/docs/adr)

<figure>
  <img src="/files/7ph_graph_pilot_overview.png" alt="7PH Graph, a pilot's neighbourhood drawn as an interactive graph" style="width:100%; display:block; margin: 0 auto;">
</figure>

## What it does

- **Draws a subject's neighbourhood.** Pick a pilot or a card and the app returns an interactive graph: decks, events, placements, archetypes. Each node opens its details, and each deck links out to Moxfield.
- **Compares 2 subjects head to head** over the events they share, and refuses when there are none.
- **Surfaces hidden gems**, cards that are rare in an archetype yet keep appearing in its best decks. The rarity ceiling is a share of the slice. The evidence floor is a fixed count of decks, because a relative floor would admit lucky-draw noise.
- **Charts the metagame over time**: archetype share against mean finish, and adoption curves per card. The player leaderboard carries an honest interval on every rank.

The app neither draws nor truncates a result too large to read. It reports what the query matched and asks you to narrow it. A truncated graph looks like an answer and is not one. The same rule covers a pilot with too little history and a pair who never met.

<figure>
  <img src="/files/7ph_graph_metagame_landscape.png" alt="Archetype share against mean finish, with error bars" style="width:100%; display:block; margin: 0 auto;">
</figure>

## Architecture

3 commands split the system, and only the first 2 talk upstream:

```sh
graph7ph fetch   # download source data into snapshots/<timestamp>/
graph7ph build   # load the accumulated snapshots into a graph artifact
graph7ph app     # serve the explorer over the prebuilt artifact
```

Each fetch lands as an immutable snapshot. The build folds the whole sequence and validates each snapshot against the union of everything before it. The build catches a rewrite buried in an interior snapshot, holds the fact at its pre-change value, and reports it. The flag is an action for a human, not a notice.

The build promotes a new artifact only when it validates, and keeps the previous one for instant rollback. The app never fetches or builds. It opens a promoted artifact read-only. The deployed instance therefore carries no upstream credential at all.

The graph store changed under the project when the vendor archived Kùzu. The project moved to Ladybug, the active fork, with the migration graded as described below.

## The decision that was hard

The source ships placements it never normalised and field sizes its own deck counts contradict. Some finishes exist only as a tie band. The easy design was a boolean estimated flag. The shipped design gives each uncertain value a companion column holding a rule name.

The column is null where the source's own number stands. It holds a rule name where a pass here produced the value, and none where no rule fit. One query then answers: which of this deck's numbers did we decide, and under which rule? The design covers classes of uncertainty not yet invented.

It earned its keep fast. 28 decks held a known placement with no norm, so every ranked average silently dropped them. 27 of the 28 were top-8 finishes. The bias ran in one direction and hit hardest the pilots who made the cut.

## What was measured

A bootstrap on the standings quantifies rank stability. Only 4.9 of the top 8 survive a resample on average. Rank 7's honest interval runs from 1 to 40. Every surface that ranks people states that uncertainty.

A recorded oracle graded the store migration, not a reading of the diff. `baseline/subgraphs.json` captures what every query entry point answers, plus table counts and dropdown catalogues. The baseline command exits non-zero on any difference and refuses to overwrite itself without a force flag.

A browser, not an assertion, tests the visual layer. A Playwright suite measures what the graph document actually paints at desktop width. An acceptance script drives every tab and state at phone and desktop widths and photographs each one.

The script then measures every rendered text node against the background it is painted on. The pass grades contrast at the Web Content Accessibility Guidelines AA level.

## What did not work

An early leaderboard plotted each contender's form as a rolling window. The shape looked convincing, so I tested it before shipping. The test permutes each pilot's finishes across their own event dates. That destroys any timing signal and preserves how well they played.

Observed movement was 0.0915 against a shuffled 0.0885, with a 90% range of 0.0823 to 0.0947. The chart was drawing sampling noise and calling it form. A running score replaced it.

I also renamed the tab from Best player race to Player leaderboard. The old title asserted what the evidence refused.

## Deployment

The app runs as a Hugging Face Space with protected visibility behind [www.7phgraph.com](https://www.7phgraph.com). The Space stays reachable while its files stay private. The deployed bundle carries the built graph and the ingestion reports, and a public Space offers both for download.

## Stack

Python 3.11+ · Ladybug (embedded Cypher graph store) · Gradio · Plotly · pyvis · Pydantic · pytest · Playwright · uv · Hugging Face Spaces

The repo carries 24 architecture decision records and a domain glossary the code and the interface both speak. The test suite is slightly larger than the source it covers.

## Attribution

Metagame data comes from [7phstats](https://7phstats.com). Decklists link out to [Moxfield](https://moxfield.com), free and non-commercial per Moxfield's API terms. The project is unofficial and not affiliated with either service or with Wizards of the Coast.
