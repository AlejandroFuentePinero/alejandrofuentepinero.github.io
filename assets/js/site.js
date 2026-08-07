/* Design system behaviour: theme toggle, nav disclosure, lazy embed frames.
   Vanilla JS, no dependencies. The matching pre-paint script lives inline in
   the head (_includes/theme-script.html). */
(function () {
  "use strict";

  var root = document.documentElement;

  /* Theme toggle. The explicit choice persists in localStorage; with no
     stored choice the CSS prefers-color-scheme rules decide. */
  function currentTheme() {
    var set = root.getAttribute("data-theme");
    if (set === "dark" || set === "light") return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    try {
      localStorage.setItem("theme", theme);
    } catch (e) {
      /* private mode: the toggle still works for this page view */
    }
    syncToggles();
  }

  function syncToggles() {
    var dark = currentTheme() === "dark";
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.setAttribute("aria-pressed", dark ? "true" : "false");
    });
  }

  document.addEventListener("click", function (event) {
    var toggle = event.target.closest("[data-theme-toggle]");
    if (toggle) {
      applyTheme(currentTheme() === "dark" ? "light" : "dark");
    }
  });

  syncToggles();

  /* Nav disclosure on small screens. */
  var header = document.querySelector(".site-header");
  var navToggle = document.querySelector("[data-nav-toggle]");

  function setNav(open) {
    if (!header || !navToggle) return;
    if (open) {
      header.setAttribute("data-open", "");
    } else {
      header.removeAttribute("data-open");
    }
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  if (navToggle) {
    navToggle.addEventListener("click", function () {
      setNav(!header.hasAttribute("data-open"));
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setNav(false);
    });

    document.addEventListener("click", function (event) {
      if (header.hasAttribute("data-open") && !header.contains(event.target)) {
        setNav(false);
      }
    });
  }

  /* Lazy embed frames. The iframe is created only when the frame nears the
     viewport. Success is the iframe load event; a quiet timeout swaps in the
     fallback (screenshot plus link) instead of a broken frame. */
  var FAIL_TIMEOUT = 15000;

  function loadFrame(frame) {
    if (frame.getAttribute("data-state") !== "idle") return;
    frame.setAttribute("data-state", "loading");

    var iframe = document.createElement("iframe");
    iframe.className = "embed-frame__iframe";
    iframe.src = frame.getAttribute("data-embed-src");
    iframe.title = frame.getAttribute("data-embed-title") || "Embedded app";
    iframe.setAttribute("loading", "lazy");

    var timer = setTimeout(function () {
      frame.setAttribute("data-state", "failed");
      iframe.remove();
    }, FAIL_TIMEOUT);

    iframe.addEventListener("load", function () {
      clearTimeout(timer);
      frame.setAttribute("data-state", "loaded");
    });

    iframe.addEventListener("error", function () {
      clearTimeout(timer);
      frame.setAttribute("data-state", "failed");
      iframe.remove();
    });

    frame.appendChild(iframe);
  }

  var frames = document.querySelectorAll("[data-embed-src]");

  if (frames.length) {
    if ("IntersectionObserver" in window) {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              observer.unobserve(entry.target);
              loadFrame(entry.target);
            }
          });
        },
        /* rootMargin 0 on purpose (DECISIONS.md 36 mitigation): the Space
           can only boot, and only steal scroll, while the frame is already
           on screen. */
        { rootMargin: "0px" }
      );
      frames.forEach(function (frame) {
        observer.observe(frame);
      });
    } else {
      frames.forEach(loadFrame);
    }
  }

  /* Projects type filter, progressive enhancement: the control ships
     hidden and every project visible. JS reveals the control; filtering
     only ever hides cards, so with JS off all projects show. */
  var filter = document.querySelector("[data-filter]");

  if (filter) {
    filter.hidden = false;
    var filterButtons = filter.querySelectorAll("button[data-type]");
    var cards = document.querySelectorAll("[data-project-type]");

    filter.addEventListener("click", function (event) {
      var button = event.target.closest("button[data-type]");
      if (!button) return;
      var type = button.getAttribute("data-type");
      filterButtons.forEach(function (b) {
        b.setAttribute("aria-pressed", b === button ? "true" : "false");
      });
      cards.forEach(function (card) {
        card.hidden =
          type !== "all" && card.getAttribute("data-project-type") !== type;
      });
    });
  }
})();
