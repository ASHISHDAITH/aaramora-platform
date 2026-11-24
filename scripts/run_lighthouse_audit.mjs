import { mkdir, readFile, writeFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import { resolve } from "node:path";

const base = process.env.AARAMORA_AUDIT_BASE_URL ?? "http://127.0.0.1:8765";
const outputDir = resolve("artifacts/lighthouse");
const routes = [
  { name: "home", path: "/" },
  { name: "get-help", path: "/get-help.html" },
  { name: "relationships", path: "/relationships.html" },
  { name: "reading-library", path: "/reading-library.html" },
];
const presets = ["mobile", "desktop"];
const summaries = [];

await mkdir(outputDir, { recursive: true });

for (const route of routes) {
  for (const preset of presets) {
    const outputPath = resolve(outputDir, `${route.name}-${preset}.json`);
    const args = [
      `${base}${route.path}`,
      "--quiet",
      "--only-categories=performance,accessibility,best-practices,seo",
      "--output=json",
      `--output-path=${outputPath}`,
      "--chrome-flags=--headless --no-sandbox --disable-dev-shm-usage",
    ];
    if (preset === "desktop") args.push("--preset=desktop");

    process.stdout.write(`Lighthouse ${preset}: ${route.path}\n`);
    const run = spawnSync("lighthouse", args, {
      encoding: "utf8",
      env: process.env,
      maxBuffer: 20 * 1024 * 1024,
    });
    if (run.status !== 0) {
      process.stderr.write(run.stderr || run.stdout || "Lighthouse returned a non-zero exit code.\n");
      throw new Error(`Lighthouse failed for ${route.path} (${preset}) with status ${run.status}`);
    }

    const report = JSON.parse(await readFile(outputPath, "utf8"));
    const categories = Object.fromEntries(
      Object.entries(report.categories ?? {}).map(([key, value]) => [
        key,
        value.score === null ? null : Math.round(value.score * 100),
      ]),
    );
    const metric = id => report.audits?.[id]?.displayValue ?? null;
    summaries.push({
      route: route.path,
      preset,
      categories,
      metrics: {
        firstContentfulPaint: metric("first-contentful-paint"),
        largestContentfulPaint: metric("largest-contentful-paint"),
        totalBlockingTime: metric("total-blocking-time"),
        cumulativeLayoutShift: metric("cumulative-layout-shift"),
        speedIndex: metric("speed-index"),
      },
      finalUrl: report.finalDisplayedUrl ?? report.finalUrl ?? null,
    });
  }
}

await writeFile(
  resolve(outputDir, "summary.json"),
  JSON.stringify(
    {
      generatedAt: new Date().toISOString(),
      baseUrl: base,
      routes,
      reports: summaries,
      note: "Lighthouse lab scores are diagnostic measurements, not WCAG or clinical certification.",
    },
    null,
    2,
  ),
  "utf8",
);
for (const result of summaries) {
  process.stdout.write(
    `${result.route} [${result.preset}] ${JSON.stringify(result.categories)}\n`,
  );
}
