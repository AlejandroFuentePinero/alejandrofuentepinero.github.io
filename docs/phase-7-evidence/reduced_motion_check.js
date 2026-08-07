/* Gate 7: prefers-reduced-motion kills every transition and animation,
   both themes.

   Method: serve the built _site, load representative pages in headless
   Chrome with prefers-reduced-motion emulated, and read the computed
   transition and animation durations of every element. The site's kill
   switch (_typography.scss) sets 0.01ms, the imperceptible-not-zero
   idiom, so the pass bar is: no element above 5ms. A control run
   without the emulation proves the scan sees the site's real
   transitions (a nonzero count), so a clean reduced run cannot be a
   scan that saw nothing.

   Run from the repo root after `bundle exec jekyll build`:
     NODE_PATH=<dir with puppeteer-core> node docs/phase-7-evidence/reduced_motion_check.js
*/
"use strict";

const puppeteer = require("puppeteer-core");
const { serveSite } = require("./serve_site");

const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const SITE = __dirname + "/../../_site";
const PAGES = ["/", "/styleguide/", "/projects/", "/work/", "/research/"];

/* The scan is injected as a string so it runs in the page. */
const SCAN = `(() => {
  let seen = 0;
  const offenders = [];
  for (const el of document.querySelectorAll("*")) {
    const cs = getComputedStyle(el);
    const parse = (v) => v.split(",").map((s) => {
      s = s.trim();
      const n = parseFloat(s) || 0;
      return s.endsWith("ms") ? n / 1000 : n;
    });
    const durs = parse(cs.transitionDuration).concat(parse(cs.animationDuration));
    const max = Math.max(...durs);
    if (max > 0) seen++;
    if (max > 0.005) {
      offenders.push(
        el.tagName.toLowerCase() +
        (el.className && typeof el.className === "string" ? "." + el.className.split(" ")[0] : "") +
        " t:" + cs.transitionDuration + " a:" + cs.animationDuration
      );
    }
  }
  return { seen, offenders, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
})()`;

(async () => {
  const { server, port } = await serveSite(SITE);
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: "new",
  });
  let failed = false;
  const lines = [];

  for (const theme of ["light", "dark"]) {
    for (const motion of ["no-preference", "reduce"]) {
      const page = await browser.newPage();
      await page.emulateMediaFeatures([
        { name: "prefers-reduced-motion", value: motion },
        { name: "prefers-color-scheme", value: theme },
      ]);
      for (const path of PAGES) {
        await page.goto(`http://127.0.0.1:${port}${path}`, {
          waitUntil: "networkidle0",
        });
        const r = await page.evaluate(SCAN);
        if (motion === "no-preference") {
          // control: the scan must see the site's transitions
          const ok = r.seen > 0;
          failed = failed || !ok;
          lines.push(
            `${ok ? "PASS" : "FAIL"} [control ${theme}] ${path} sees ${r.seen} elements with motion durations`
          );
        } else {
          const ok = r.offenders.length === 0 && r.scrollBehavior !== "smooth";
          failed = failed || !ok;
          lines.push(
            `${ok ? "PASS" : "FAIL"} [reduce  ${theme}] ${path} offenders above 5ms: ${r.offenders.length}` +
            (r.offenders.length ? "  " + r.offenders.slice(0, 5).join(" | ") : "")
          );
        }
      }
      await page.close();
    }
  }

  await browser.close();
  server.close();
  console.log(lines.join("\n"));
  console.log(failed ? "\nRESULT: FAIL" : "\nRESULT: PASS");
  process.exit(failed ? 1 : 0);
})();
