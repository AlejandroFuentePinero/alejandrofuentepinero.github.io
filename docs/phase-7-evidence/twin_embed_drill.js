/* Gate 7: the digital twin embed drill.

   Three proofs, in one headless Chrome run against the built _site:

   1. Lazy: on a fresh home page load, no request reaches the Space
      host until the frame is scrolled into view. Scrolling to it
      creates the iframe and the first Space request fires.
   2. Fallback: with every request to the Space host blocked, the
      frame reaches data-state="failed" (iframe error or the 15s
      timeout in assets/js/site.js) and the screenshot fallback with
      its open link becomes visible.
   3. Full screen: clicking "Open full screen" opens a new tab on the
      Space URL.

   Evidence screenshots (loaded and fallback states) are written next
   to this script.

   Run from the repo root after `bundle exec jekyll build`:
     NODE_PATH=<dir with puppeteer-core> node docs/phase-7-evidence/twin_embed_drill.js
*/
"use strict";

const puppeteer = require("puppeteer-core");
const { serveSite } = require("./serve_site");

const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const SITE = __dirname + "/../../_site";
const SPACE_HOST = "alejandrofupi-digital-twin.hf.space";

(async () => {
  const { server, port } = await serveSite(SITE);
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: "new",
    args: ["--window-size=1280,900"],
  });
  let failed = false;
  const lines = [];
  const check = (ok, line) => {
    failed = failed || !ok;
    lines.push(`${ok ? "PASS" : "FAIL"} ${line}`);
  };

  // 1 and 3: lazy load, then full screen
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    const spaceRequests = [];
    page.on("request", (r) => {
      if (r.url().includes(SPACE_HOST)) spaceRequests.push(r.url());
    });
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: "networkidle0" });
    await new Promise((r) => setTimeout(r, 1000));

    const stateBefore = await page.$eval("[data-embed-src]", (el) =>
      el.getAttribute("data-state")
    );
    check(
      spaceRequests.length === 0 && stateBefore === "idle",
      `lazy: before scrolling, embed state "${stateBefore}", Space requests ${spaceRequests.length}`
    );

    await page.$eval("[data-embed-src]", (el) => el.scrollIntoView());
    await page
      .waitForFunction(
        () =>
          ["loading", "loaded"].includes(
            document
              .querySelector("[data-embed-src]")
              .getAttribute("data-state")
          ),
        { timeout: 10000 }
      )
      .catch(() => {});
    await new Promise((r) => setTimeout(r, 2000));
    check(
      spaceRequests.length > 0,
      `lazy: after scrolling into view, iframe created and ${spaceRequests.length} Space request(s) fired`
    );

    const loaded = await page
      .waitForFunction(
        () =>
          document
            .querySelector("[data-embed-src]")
            .getAttribute("data-state") === "loaded",
        { timeout: 30000 }
      )
      .then(() => true)
      .catch(() => false);
    check(loaded, "load: embed reaches data-state loaded (Space HTML answered)");
    await page.screenshot({
      path: __dirname + "/twin-embed-loaded.png",
    });

    // 3: full screen opens the Space in a new tab
    const targetPromise = browser.waitForTarget(
      (t) => t.url().includes(SPACE_HOST),
      { timeout: 15000 }
    );
    await page.$eval(".embed-frame__header .embed-frame__open", (a) => a.click());
    const target = await targetPromise.then((t) => t.url()).catch(() => null);
    check(
      target !== null,
      `full screen: "Open full screen" opened a new tab on ${target}`
    );
    await page.close();
  }

  // 2: fallback with the Space blocked
  {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.setRequestInterception(true);
    page.on("request", (r) => {
      if (r.url().includes(SPACE_HOST)) r.abort("connectionrefused");
      else r.continue();
    });
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: "networkidle0" });
    await page.$eval("[data-embed-src]", (el) => el.scrollIntoView());
    const failedState = await page
      .waitForFunction(
        () =>
          document
            .querySelector("[data-embed-src]")
            .getAttribute("data-state") === "failed",
        { timeout: 20000 }
      )
      .then(() => true)
      .catch(() => false);
    check(failedState, "fallback: with the Space blocked, embed reaches data-state failed");

    const fb = await page.evaluate(() => {
      const fallback = document.querySelector(".embed-frame__fallback");
      const img = document.querySelector(".embed-frame__fallback-shot");
      const link = document.querySelector(".embed-frame__fallback-bar .embed-frame__open");
      const visible = (el) =>
        el && getComputedStyle(el).display !== "none" && el.offsetParent !== null;
      return {
        fallbackVisible: visible(fallback),
        imgVisible: visible(img),
        linkHref: link ? link.href : null,
      };
    });
    check(
      fb.fallbackVisible && fb.imgVisible,
      `fallback: screenshot fallback visible (container ${fb.fallbackVisible}, image ${fb.imgVisible})`
    );
    check(
      fb.linkHref !== null && fb.linkHref.includes(SPACE_HOST),
      `fallback: open link points at the Space (${fb.linkHref})`
    );
    await page.screenshot({
      path: __dirname + "/twin-embed-fallback.png",
    });
    await page.close();
  }

  await browser.close();
  server.close();
  console.log(lines.join("\n"));
  console.log(failed ? "\nRESULT: FAIL" : "\nRESULT: PASS");
  process.exit(failed ? 1 : 0);
})();
