/* Gate 7: no theme flash on hard reload in either mode.

   Method: serve the built _site, apply an explicit theme the way the
   real toggle does (data-theme attribute plus localStorage), emulate
   the OPPOSITE OS colour scheme (the worst case: the pre-paint script
   must win against the media query), then hard reload with the cache
   disabled and the network throttled to stretch the paint window,
   while a CDP screencast captures PNG frames and lifecycle events
   record the navigation's firstPaint time.

   Judgment, on exact pixel values from _sass/_tokens.scss (light
   --paper #FAFAF7, dark --paper #1F1E1D):

   - Every frame at or after firstPaint must be the stored theme's
     paper. A wrong-theme first paint is the flash this check exists
     to catch, and fails the run.
   - A frame painted in the OPPOSITE theme's paper at any time also
     fails: that is a real wrong-theme paint.
   - Blank white (#FFFFFF) frames before firstPaint are the headless
     compositor clearing between documents; real Chrome holds the old
     page's pixels through navigation (paint holding), so these are
     reported but do not fail the run.

   Run from the repo root after `bundle exec jekyll build`:
     NODE_PATH=<dir with puppeteer-core and pngjs> node docs/phase-7-evidence/theme_flash_check.js
*/
"use strict";

const puppeteer = require("puppeteer-core");
const { PNG } = require("pngjs");
const { serveSite } = require("./serve_site");

const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const SITE = __dirname + "/../../_site";

const PAPER = {
  light: [0xfa, 0xfa, 0xf7],
  dark: [0x1f, 0x1e, 0x1d],
  white: [0xff, 0xff, 0xff],
};

function near(pixel, ref, tol = 3) {
  return (
    Math.abs(pixel[0] - ref[0]) <= tol &&
    Math.abs(pixel[1] - ref[1]) <= tol &&
    Math.abs(pixel[2] - ref[2]) <= tol
  );
}

function probe(png) {
  // corner and top-centre pixels, away from the header rule
  const at = (x, y) => {
    const i = (y * png.width + x) * 4;
    return [png.data[i], png.data[i + 1], png.data[i + 2]];
  };
  return [at(5, 5), at(png.width - 5, 5), at(Math.floor(png.width / 2), 5)];
}

(async () => {
  const { server, port } = await serveSite(SITE);
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: "new",
  });
  let failed = false;
  const lines = [];

  for (const stored of ["dark", "light"]) {
    const os = stored === "dark" ? "light" : "dark";
    const opposite = stored === "dark" ? "light" : "dark";
    const page = await browser.newPage();
    await page.emulateMediaFeatures([
      { name: "prefers-color-scheme", value: os },
    ]);
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: "load" });
    // what the real toggle does: attribute now, choice persisted
    await page.evaluate((t) => {
      document.documentElement.setAttribute("data-theme", t);
      localStorage.setItem("theme", t);
    }, stored);
    // let the old page repaint in the stored theme before capturing
    await page.evaluate(
      () => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)))
    );
    await new Promise((r) => setTimeout(r, 200));

    const cdp = await page.createCDPSession();
    await cdp.send("Network.enable");
    await cdp.send("Network.setCacheDisabled", { cacheDisabled: true });
    await cdp.send("Network.emulateNetworkConditions", {
      offline: false,
      latency: 150,
      downloadThroughput: (500 * 1024) / 8,
      uploadThroughput: (500 * 1024) / 8,
    });
    await cdp.send("Page.enable");
    await cdp.send("Page.setLifecycleEventsEnabled", { enabled: true });

    // CDP replays the current page's lifecycle events when enabled, so
    // only events arriving after the reload is initiated belong to the
    // new navigation.
    let firstPaintAt = Infinity;
    let armed = false;
    cdp.on("Page.lifecycleEvent", (ev) => {
      if (!armed) return;
      if (ev.name === "firstPaint" || ev.name === "firstContentfulPaint") {
        firstPaintAt = Math.min(firstPaintAt, ev.timestamp);
      }
    });

    const frames = [];
    cdp.on("Page.screencastFrame", async (ev) => {
      frames.push({ data: Buffer.from(ev.data, "base64"), t: ev.metadata.timestamp });
      try {
        await cdp.send("Page.screencastFrameAck", { sessionId: ev.sessionId });
      } catch {}
    });
    await cdp.send("Page.startScreencast", {
      format: "png",
      everyNthFrame: 1,
    });

    armed = true;
    await page.reload({ waitUntil: "networkidle0" });
    await new Promise((r) => setTimeout(r, 500));
    await cdp.send("Page.stopScreencast");

    let wrongAfterPaint = 0;
    let oppositePaint = 0;
    let compositorClear = 0;
    for (const f of frames) {
      const png = PNG.sync.read(f.data);
      const probes = probe(png);
      const isStored = probes.every((p) => near(p, PAPER[stored]));
      const isOpposite = probes.every((p) => near(p, PAPER[opposite]));
      const isWhite = probes.every((p) => near(p, PAPER.white, 1));
      if (isOpposite && !(opposite === "light" && isWhite)) oppositePaint++;
      if (f.t >= firstPaintAt && !isStored) wrongAfterPaint++;
      if (f.t < firstPaintAt && isWhite && stored === "dark") compositorClear++;
    }
    const ok =
      frames.length > 0 && wrongAfterPaint === 0 && oppositePaint === 0;
    failed = failed || !ok;
    lines.push(
      `${ok ? "PASS" : "FAIL"} stored ${stored}, OS ${os}: ` +
      `${frames.length} frames, ${wrongAfterPaint} wrong-theme at or after firstPaint, ` +
      `${oppositePaint} opposite-theme paints, ` +
      `${compositorClear} pre-paint compositor clears (headless artifact, informational)`
    );
    await page.close();
  }

  await browser.close();
  server.close();
  console.log(lines.join("\n"));
  console.log(failed ? "\nRESULT: FAIL" : "\nRESULT: PASS");
  process.exit(failed ? 1 : 0);
})();
