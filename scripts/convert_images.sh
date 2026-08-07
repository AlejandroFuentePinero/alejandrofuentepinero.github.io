#!/bin/sh
# Convert the site's content images to webp, written beside the originals.
# The originals stay committed as the <picture> fallback. Run locally and
# commit the output; GitHub Pages has no build step (REFURB_BRIEF 1).
# Requires cwebp and gif2webp: brew install webp
#
# Not converted, on purpose: the brand mark and icon set (Phase 6 keeps
# icons png and ico), and every file a record links as a document (paper
# PDFs, certificate images).
set -e
cd "$(dirname "$0")/.."

for f in \
  images/apps/7ph-graph.png \
  images/apps/birds-shiny.png \
  images/apps/digital-twin.png \
  images/apps/job-intelligence-engine.png \
  files/project_pipeline_simple.png \
  files/digital_twin_runtime.png \
  files/7ph_graph_pilot_overview.png \
  files/7ph_graph_metagame_landscape.png \
  files/llm-engineering-cartoon.png
do
  cwebp -q 82 -m 6 -quiet "$f" -o "${f%.png}.webp"
done

# files/app_demo.gif is not converted: animated webp lands at 7.7 MB
# against the gif's 11 MB (measured with -lossy -mixed -min_size -q 70),
# too little to justify a second multi-megabyte file in the repo. The
# gif lazy-loads below the fold. The real fix is a short video file,
# which replaces the asset itself: owner call, FINDINGS 21.
