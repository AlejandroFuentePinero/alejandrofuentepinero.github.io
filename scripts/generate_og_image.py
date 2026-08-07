#!/usr/bin/env python3
"""Generate images/og-image.png, the 1200x630 social sharing card.

Run locally and commit the output; GitHub Pages has no build step.
The card is the brief's Phase 6 spec: warm paper, the groodle mark,
name, role. Colours are read from _sass/_tokens.scss (the only place
hex is defined) and the type is the site's own self-hosted fonts, so
the card cannot drift from the design system without a rerun.

Requires Google Chrome for the headless screenshot.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# The role line is the hero's role line, one settled surface for the fact.
NAME = "Alejandro de la Fuente"
ROLE = "AI engineer, raised on rainforest data and honest error bars."


def light_tokens():
    scss = (ROOT / "_sass" / "_tokens.scss").read_text(encoding="utf-8")
    light = scss.split("@mixin tokens-light")[1].split("}")[0]
    return dict(re.findall(r"--([a-z-]+):\s*(#[0-9A-Fa-f]{6})", light))


def main():
    t = light_tokens()
    html = f"""<!doctype html>
<meta charset="utf-8">
<style>
  @font-face {{
    font-family: "Newsreader";
    font-weight: 200 800;
    src: url("{ROOT}/assets/fonts/newsreader-var.woff2") format("woff2");
  }}
  @font-face {{
    font-family: "Inter";
    font-weight: 100 900;
    src: url("{ROOT}/assets/fonts/inter-var.woff2") format("woff2");
  }}
  html, body {{ margin: 0; }}
  body {{
    width: 1200px;
    height: 630px;
    box-sizing: border-box;
    background: {t["paper"]};
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 96px;
  }}
  img {{ width: 88px; height: 88px; margin-bottom: 40px; }}
  h1 {{
    font-family: "Newsreader", serif;
    font-weight: 500;
    font-size: 76px;
    line-height: 1.1;
    color: {t["ink"]};
    margin: 0 0 20px;
  }}
  .rule {{
    width: 72px;
    height: 3px;
    background: {t["accent"]};
    margin: 0 0 28px;
  }}
  p {{
    font-family: "Inter", sans-serif;
    font-weight: 400;
    font-size: 31px;
    color: {t["ink-muted"]};
    margin: 0;
  }}
</style>
<body>
  <img src="{ROOT}/images/groodle_favicon_256.png" alt="">
  <h1>{NAME}</h1>
  <div class="rule"></div>
  <p>{ROLE}</p>
</body>
"""
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", delete=False, encoding="utf-8"
    ) as f:
        f.write(html)
        page = f.name

    out = ROOT / "images" / "og-image.png"
    subprocess.run(
        [
            CHROME,
            "--headless",
            f"--screenshot={out}",
            "--window-size=1200,630",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"file://{page}",
        ],
        check=True,
        capture_output=True,
    )
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
