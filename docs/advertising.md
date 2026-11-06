# Display advertising

Adsterra's existing ExamShortcut website entry is 6130612. On 6 November 2026 the existing 320×50 (31792398), 728×90 (31792399) and 300×250 (31786624) banner units were reactivated. Their issued snippets were checked in the publisher dashboard; no new account or payout configuration was created.

Tina in Adsterra support confirmed the requested adult/erotic/dating, gambling/betting/casino, sound and deceptive download/alert category exclusions at approximately 12:42 UTC on 6 November. Support advised allowing 15 minutes for propagation. Both the application and isolated ad document reject requests before 12:57:50 UTC. These are vendor category filters, not an independent guarantee about every future creative; report inappropriate creatives to Adsterra with the affected unit and evidence.

The homepage has one responsive display banner after its latest-notices section. Long guides and update articles have one rectangle after their second section and one responsive banner at the page end. Other permitted reading pages have one banner at the end. Fixed sizes are chosen from the actual container width; narrow containers omit a unit that cannot fit. Ads load near the viewport after browser idle, once per placement, without automatic refresh. Resizing never creates extra impressions for an already selected unit.

Tests, quizzes, monthly current-affairs quiz pages, calculators, mock tests, account pages, forms and revision tools are outside the reading-page allowlist. A session-wide “Hide ads while studying” control removes the placements, including their frames, across client navigation. No popup, popunder, Smartlink, Social Bar, sticky or interstitial integration is installed. Existing inactive formats in the account were left as they were.

`src/lib/adsterra.ts` holds the serving switch, confirmation timestamp, start time and route/size rules. `scripts/generate-ad-documents.mjs` generates the fixed-unit document. Vendor code executes only in `examshortcut.pages.dev/advertising/display`, framed by the production domain with no top-navigation, modal, form, download or autoplay permission. It cannot access the production application's DOM or account storage. The helper has noindex and an exact parent-origin allowlist. Application pages retain their existing frame protections.

Validation: `node --experimental-strip-types --test scripts/test-adsterra.mjs`; `npm run build` includes those checks, document generation and `verify-ad-export.mjs`. Do not add guessed ads.txt seller records; use only lines actually supplied for this account by the vendor.

Compare revenue per 1,000 pageviews, viewability, page speed and reader engagement before increasing density. More banners do not establish a revenue increase. Payment information in Adsterra requires the owner's review separately from this code integration.
