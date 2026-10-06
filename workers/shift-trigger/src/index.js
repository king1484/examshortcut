// Fires the "Shift analysis" GitHub Actions workflow on a reliable clock.
// GitHub's own cron is best-effort and skipped 7 of 8 slots on 2026-10-06; Cloudflare cron triggers are not.
// Secret GITHUB_TOKEN: fine-grained PAT, repo king1484/examshortcut only, permission Actions: Read and write.
const REPO = "king1484/examshortcut";
const WORKFLOW = "shift-analysis.yml";
// Free Workers plan = 5 cron triggers per account, so ONE half-hourly trigger fires and this list picks the slots (UTC).
// Shifts end 11:00 / 14:30 / 18:00 IST: run ~30 min after each, a retry an hour later, an evening pass, a morning refresh.
// IST: 08:30, 11:30, 12:30, 15:00, 16:00, 18:30, 19:30, 21:30
const SLOTS = new Set(["03:00", "06:00", "07:00", "09:30", "10:30", "13:00", "14:00", "16:00"]);

export default {
  async scheduled(event, env, ctx) {
    const t = new Date(event.scheduledTime).toISOString().slice(11, 16);
    if (SLOTS.has(t)) ctx.waitUntil(dispatch(env));
  },
  // No public surface: the URL answers 404 and never triggers anything.
  async fetch() {
    return new Response("not found", { status: 404 });
  },
};

async function dispatch(env) {
  const r = await fetch(`https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW}/dispatches`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": "examshortcut-shift-trigger",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ ref: "master" }),
  });
  if (r.status !== 204) {
    // visible in `wrangler tail` and the Worker's invocation logs
    throw new Error(`workflow_dispatch failed: HTTP ${r.status} ${(await r.text()).slice(0, 200)}`);
  }
  console.log("dispatched", new Date().toISOString());
}
