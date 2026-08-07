# Gate 7 manual checklist: Firefox, Safari desktop, iOS Safari

Chrome was verified by automation (chrome-console-report.txt and the
other reports beside this file). These checks were not run by the
automation and need a human pass in each browser. About 5 minutes per
browser. Every URL is on https://alejandrofuentepinero.github.io.

## All three browsers

1. `/`: Newsreader serif in the hero, Inter body, no fallback-font
   flash that persists. Stats band shows 5 figures with hairline rules.
2. `/`: click the theme toggle twice, dark then light, instant both
   ways. Hard reload (hold Shift on desktop) after choosing dark: the
   page must never flash light before painting dark.
3. `/`: scroll to the digital twin. The frame shows "The app loads
   when it comes into view", then the chat boots inside it. "Open full
   screen" opens the Space in a new tab.
4. `/projects/`: the filter row appears, "Research" hides engineering
   cards, "All" restores them.
5. `/research/ringtail-possum-collapse-2022/`: "Original abstract as
   published" opens and closes on click, marker glyph rotates.
6. `/work/`: open the print dialog (Cmd+P). The preview must be the
   light palette with no header, nav or toggle.

## Firefox only

7. System setting "reduce motion" (macOS: System Settings,
   Accessibility, Display), then reload `/`: hovering links and cards
   must change colour with no transition delay.

## Safari desktop only

8. `/apps/`: the four app screenshots render (webp with png fallback,
   Safari 16 and later takes the webp).
9. Private window on `/`: the theme toggle must still work for the
   page view (localStorage writes fail silently, by design).

## iOS Safari only

10. `/` at phone width: the nav collapses to the Menu button, opens,
    closes on tap-out, and no horizontal scroll exists anywhere on
    the page.
11. `/`: the twin embed is usable, the chat input focuses, and the
    keyboard does not break the layout.
12. `/research/`: tap targets on the publication rows are big enough
    to hit reliably, and disclosures open on first tap.
