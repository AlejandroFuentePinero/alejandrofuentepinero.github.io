# Gate 4 evidence

Produced on branch `refurb/phase-4-structure`, 2026-08-07. The `docs` directory is on the build exclude list; none of this ships.

## Screenshots

`<width>-<theme>-<page>.jpg`: every page type at 390, 768 and 1440, in light and dark. Page types: home, work, projects, project-page (7PH Graph), apps, research, publication-page (ringtail possum 2022), talk-page (elevational shifts 2022), threatened-species, contact, sitemap, post, 404. Captured from the built site via headless Chrome with the theme persisted in `localStorage`, exactly as the toggle stores it.

## Twin embed

- `twin-embed-evidence.txt`: DOM-level proof that no iframe exists while the frame is below the fold, that the iframe is created and reaches the loaded state when the frame enters the viewport, and that a hanging Space connection trips the 15 second timeout into the fallback state.
- `1440-twin-embed-loading.jpg`: the frame as it enters the viewport, space reserved, placeholder showing while the Space boots. `1440-twin-embed-fallback.jpg`: the graceful failure (screenshot plus link). A composited capture of the loaded cross-origin iframe is not reliably available from headless Chrome; the loaded state is proven in the text file and was verified interactively.

## URL integrity

- `crawl_old_urls.py`: serves the built site with GitHub Pages resolution semantics and requests every URL the site served before Phase 4 plus every new URL, following meta refresh redirect chains.
- `crawl-report.txt`: the run against this branch's build. Pass means the URL ends in a 200, directly or through a redirect chain.

## Build

- `build-output.txt`: full `bundle exec jekyll build` output, warning-free.
