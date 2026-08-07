#!/usr/bin/env python3
"""Narrow the variable fonts to the weight range the site uses.

The committed woff2 files are the Google Fonts static-CDN latin
subsets (DECISIONS 25). The stylesheet only ever asks for weights 400
to 600 (400 body, 500 display, 600 strong and h4-h6), so the unused
wght masters between 100 and 900 are dead bytes on every first visit.
This script instances each file to wght 400:600 in place, keeping every
glyph and the full opsz axis. It is idempotent: re-running on already
narrowed files changes nothing.

Run locally and commit the output; GitHub Pages has no build step.
Requires fonttools: python3 -m pip install fonttools brotli
If a future design change needs a weight outside 400 to 600, re-fetch
the CDN originals, widen the range here, and rerun.
"""

import os
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
WGHT = (400, 600)


def main():
    for path in sorted(FONTS.glob("*.woff2")):
        before = os.path.getsize(path)
        font = TTFont(path)
        instantiateVariableFont(font, {"wght": WGHT}, inplace=True,
                                updateFontNames=False)
        font.flavor = "woff2"
        font.save(path)
        after = os.path.getsize(path)
        print(f"{path.name}: {before // 1024} KB -> {after // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
