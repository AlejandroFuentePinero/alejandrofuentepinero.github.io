#!/usr/bin/env python3
"""Regenerate the CV PDF from the /work/ page.

The CV is /work/ printed through the site's print stylesheet (which
forces the light palette, DECISIONS 31) with every disclosure opened,
the method DECISIONS 58 and 74 record. The built page is copied with
`open` added to each <details> block, served locally, and printed with
headless Chrome.

Run from the repo root after `bundle exec jekyll build`, then commit
the output:

    python3 scripts/generate_cv_pdf.py [output.pdf]

The output defaults to files/alejandro-de-la-fuente-cv.pdf. Requires
Google Chrome.
"""

import http.server
import socketserver
import subprocess
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else (
        ROOT / "files" / "alejandro-de-la-fuente-cv.pdf"
    )
    work = SITE / "work" / "index.html"
    if not work.exists():
        print("run `bundle exec jekyll build` first", file=sys.stderr)
        return 1

    original = work.read_text(encoding="utf-8")
    opened = original.replace("<details", "<details open")

    socketserver.TCPServer.allow_reuse_address = True
    # Port 0: the OS picks a free port, so a stale server from an old
    # session can never collide.
    server = socketserver.TCPServer(
        ("127.0.0.1", 0),
        lambda *a, **k: http.server.SimpleHTTPRequestHandler(
            *a, directory=str(SITE), **k
        ),
    )
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()

    try:
        work.write_text(opened, encoding="utf-8")
        subprocess.run(
            [
                CHROME,
                "--headless",
                f"--print-to-pdf={out}",
                "--no-pdf-header-footer",
                "--virtual-time-budget=10000",
                f"http://127.0.0.1:{port}/work/",
            ],
            check=True,
            capture_output=True,
        )
    finally:
        work.write_text(original, encoding="utf-8")
        server.shutdown()

    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
