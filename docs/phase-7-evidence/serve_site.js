/* Tiny static server for the built _site with GitHub Pages resolution
   semantics (an extensionless request resolves to the matching .html
   file). Listens on an OS-assigned port so a stale server from an old
   session can never collide. Shared by the Gate 7 browser checks. */
"use strict";

const http = require("http");
const fs = require("fs");
const path = require("path");

const MIME = {
  ".html": "text/html",
  ".css": "text/css",
  ".js": "text/javascript",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".webp": "image/webp",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".woff2": "font/woff2",
  ".pdf": "application/pdf",
  ".xml": "application/xml",
  ".json": "application/json",
  ".ico": "image/x-icon",
  ".txt": "text/plain",
};

function serveSite(siteDir) {
  const server = http.createServer((req, res) => {
    let p;
    try {
      p = decodeURIComponent(req.url.split("?")[0].split("#")[0]);
    } catch {
      res.writeHead(400);
      return res.end();
    }
    let file = path.normalize(path.join(siteDir, p));
    if (!file.startsWith(path.normalize(siteDir))) {
      res.writeHead(403);
      return res.end();
    }
    if (fs.existsSync(file) && fs.statSync(file).isDirectory()) {
      file = path.join(file, "index.html");
    }
    if (!fs.existsSync(file) && fs.existsSync(file + ".html")) {
      file += ".html";
    }
    if (!fs.existsSync(file)) {
      res.writeHead(404);
      return res.end("not found");
    }
    res.writeHead(200, {
      "content-type": MIME[path.extname(file)] || "application/octet-stream",
    });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise((resolve) =>
    server.listen(0, "127.0.0.1", () =>
      resolve({ server, port: server.address().port })
    )
  );
}

module.exports = { serveSite };
