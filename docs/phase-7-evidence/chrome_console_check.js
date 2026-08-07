/* Gate 7 cross-browser sweep, the Chrome-provable half.

   For every page type at desktop (1280x900) and phone (390x844)
   widths: load from the built _site and assert zero console errors,
   zero uncaught page errors and zero failed local requests. Then
   exercise the three JS behaviours: the theme toggle flips data-theme,
   the nav disclosure opens and closes at phone width, and the projects
   type filter hides and reveals cards.

   Firefox, Safari and iOS cannot be automated from this machine
   honestly; docs/phase-7-evidence/manual-browser-checklist.md carries
   the human checklist instead.

   Run from the repo root after `bundle exec jekyll build`:
     NODE_PATH=<dir with puppeteer-core> node docs/phase-7-evidence/chrome_console_check.js
*/
"use strict";

const puppeteer = require("puppeteer-core");
const { serveSite } = require("./serve_site");

const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const SITE = __dirname + "/../../_site";

const PAGES = [
  "/", "/work/", "/projects/", "/apps/", "/research/", "/contact/",
  "/projects/digital-twin/", "/research/ringtail-possum-collapse-2022/",
  "/research/phd-exit-seminar-2024/",
  "/posts/action-plan-australian-birds-2021/", "/styleguide/", "/404.html",
];

(async () => {
  const { server, port } = await serveSite(SITE);
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: "new",
  });
  let failed = false;
  const lines = [];
  const check = (ok, line) => {
    failed = failed || !ok;
    lines.push(`${ok ? "PASS" : "FAIL"} ${line}`);
  };

  for (const viewport of [{ width: 1280, height: 900 }, { width: 390, height: 844 }]) {
    const page = await browser.newPage();
    await page.setViewport(viewport);
    const problems = [];
    page.on("console", (m) => {
      if (m.type() === "error") problems.push(`console: ${m.text()}`);
    });
    page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`));
    page.on("requestfailed", (r) => {
      // the twin iframe is exercised separately in twin_embed_drill.js
      if (!r.url().includes("hf.space")) {
        problems.push(`requestfailed: ${r.url()} ${r.failure().errorText}`);
      }
    });
    for (const path of PAGES) {
      problems.length = 0;
      await page.goto(`http://127.0.0.1:${port}${path}`, {
        waitUntil: "networkidle0",
      });
      check(
        problems.length === 0,
        `[${viewport.width}px] ${path} console/page/request errors: ${problems.length}` +
        (problems.length ? "  " + problems.join(" | ") : "")
      );
    }
    await page.close();
  }

  // behaviours
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: "networkidle0" });
    const before = await page.evaluate(() =>
      document.documentElement.getAttribute("data-theme")
    );
    await page.click("[data-theme-toggle]");
    const after = await page.evaluate(() =>
      document.documentElement.getAttribute("data-theme")
    );
    await page.click("[data-theme-toggle]");
    const back = await page.evaluate(() =>
      document.documentElement.getAttribute("data-theme")
    );
    check(
      after !== before && back !== after,
      `theme toggle: ${before} -> ${after} -> ${back}`
    );

    await page.goto(`http://127.0.0.1:${port}/projects/`, {
      waitUntil: "networkidle0",
    });
    const filterVisible = await page.$eval("[data-filter]", (el) => !el.hidden);
    const total = (await page.$$("[data-project-type]")).length;
    await page.click('[data-filter] button[data-type="engineering"]');
    const hidden = await page.$$eval(
      "[data-project-type]",
      (cards) => cards.filter((c) => c.hidden).length
    );
    await page.click('[data-filter] button[data-type="all"]');
    const hiddenAfterAll = await page.$$eval(
      "[data-project-type]",
      (cards) => cards.filter((c) => c.hidden).length
    );
    check(
      filterVisible && hidden > 0 && hidden < total && hiddenAfterAll === 0,
      `projects filter: ${total} cards, engineering hides ${hidden}, all restores (${hiddenAfterAll} hidden)`
    );
    await page.close();
  }
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 390, height: 844 });
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: "networkidle0" });
    const open = async () =>
      page.evaluate(() =>
        document.querySelector(".site-header").hasAttribute("data-open")
      );
    const wasClosed = !(await open());
    await page.click("[data-nav-toggle]");
    const opened = await open();
    await page.keyboard.press("Escape");
    const closed = !(await open());
    check(
      wasClosed && opened && closed,
      `nav disclosure at 390px: closed -> open on toggle -> closed on Escape`
    );
    await page.close();
  }

  await browser.close();
  server.close();
  console.log(lines.join("\n"));
  console.log(failed ? "\nRESULT: FAIL" : "\nRESULT: PASS");
  process.exit(failed ? 1 : 0);
})();
