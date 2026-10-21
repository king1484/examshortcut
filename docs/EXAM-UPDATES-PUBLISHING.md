# Publishing exam results and useful updates

The public sections are `/exam-updates/` (all notices), `/results/` (published results) and `/answer-keys/` (key and response-sheet notices). Individual stories have one canonical URL under `/exam-updates/<slug>/`; the category hubs link to those same pages. The existing `/updates/` remains the site corrections/changelog page.

## What to prioritise

This is an editorial assessment based on candidate actions and the exam stages visible in retrieved official notices, not a claim about measured keyword volume or guaranteed traffic.

1. **Results and the next stage:** roll-number PDF, shortlist versus final result, correct cycle/advertisement, scorecard availability, documents and next appointment. Initial coverage: SBI PO, SSC GD, CHSL 2025, Havaldar additional result and UP Police final selection.
2. **Admit cards and city slips:** the official link, whether downloads are actually available, matching advertisement, reporting instructions and what to carry. Near-term opportunities: SBI Clerk special-drive mains on 29 October, SBI PO psychometric test on 31 October, CAT scheduled admit-card download on 4 November. Verify the actual release before a download headline.
3. **Answer keys and objection deadlines:** response sheet, official challenge fee/window, how to object and what happens after the final key. Link to the site's existing marks calculators when genuinely relevant. The unified RRB portal resolved the old-site access problem: Technician Grade I and III notices dated 15 October were visually verified, with the published window closing 22 October at 23:55. NTPC UG CBT 2 and Group D older windows are labelled ended. Keep the different grades and CENs separate.
4. **Applications, extensions and corrections:** eligibility cut-off, fee, last date/time, final submission checklist and what fields can be corrected. Follow active notices for our existing exams; do not invent a new recruitment from an expected calendar date.
5. **Exam-day coverage:** existing CGL shift-analysis pages, followed by sourced recalled topics and an explicit coverage label. Preserve the distinction between unofficial analysis and official results/keys.
6. **Useful follow-ups that last:** result-to-next-stage checklists, post preference explainers, official cutoff context, paper-pattern changes and links to the site's original practice material. Reuse and improve the existing exam guides rather than creating near-identical pages for every wording of a query.

Prefer these candidate tasks over unrelated entertainment trends: our lessons, mocks and calculators give these visitors a useful next step. Research did not establish search volumes; measure clicks and impressions after launch in Search Console before claiming a winning topic.

## One content file to publish

Add a story to `content/exam-updates.json`. Each published entry needs:

- A stable unique slug, existing `examId`, `kind`, title, original summary and exact `cycle`/advertisement.
- `published: true` only after fetching the matching official notice and checking the headline against it. Set `false` for a draft; drafts are excluded from pages, search, RSS and sitemaps.
- Explicit ISO timestamps with timezone: `publishedAt` is our first publication, `updatedAt` is a material edit, `verifiedAt` is when the source was checked. Never reset publication time just to look new. `noticeDate` is separate and optional; leave it absent when unknown.
- A status describing what is really available, at least three facts, two useful explanation sections, candidate next steps and labelled official source URLs. No invented result dates, candidate counts, ranks or download availability.

Update `content/exams/<id>/exam.json` and `process.json` at the same time so the guide, calendar and result/admit-card page agree. Check `statusPhases`: an old date phase must not override the new status after hydration. Keep regular and special drives, and old and new cycles, separate.

Run:

```powershell
npm run validate
node --experimental-strip-types --test scripts/test-exam-updates.mjs scripts/test-sitemap.mjs
npm run build
node scripts/verify-seo.mjs
node scripts/verify-exam-updates-export.mjs
```

Commit/push the reviewed content. The **Publish exam updates** GitHub workflow starts on matching content changes, checks the contracts, builds, deploys, notifies IndexNow of changed indexable URLs and verifies live page versions and login. It shares the shift-analysis deployment lock. This is automatic deployment of reviewed content, not an autonomous news-writing or monitoring service. To republish manually: `gh workflow run publish-updates.yml`.

The section is internally linked from the homepage, primary navigation, footer and matching exam guide. Search and RSS regenerate during the build. Do not reuse old article URLs for unrelated recruitments.

## Search and editorial basis

- [Google's helpful-content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content): useful original explanation, clear sourcing and honest authorship; no speculative release promises.
- [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article): article pages include matching visible publication/modification dates, Organization authorship and official-source citations. Markup does not guarantee a rich result or Google News placement.
- [Byline dates](https://developers.google.com/search/docs/appearance/publication-dates): distinguish our publication/update from the date an event occurred.
- [News-sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap): only the last two days of articles belong in a dedicated news sitemap. We use the ordinary canonical sitemap and an RSS feed initially, avoiding an obsolete two-day news feed on a static site. Add a rolling news sitemap only with a reliable refresh mechanism.
- [Google crawling limits](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors): publication and sitemap inclusion do not guarantee immediate indexing. IndexNow notifications are for supporting engines, not a Google instant-indexing API.

Suggested operating order: verify a notice, publish the candidate action and official link, add useful context, update the linked guide, then check live. Speed comes from the shared template and deployment pipeline, while the evidence remains specific to each notice.
