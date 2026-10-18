import type { Metadata } from 'next';
import Link from 'next/link';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Site updates and corrections log',
  description: 'A dated log of what changed on ExamShortcut: new exams, content rewrites, corrections and quality checks.',
  alternates: { canonical: '/updates/' },
};

type Entry = { date: string; title: string; points: string[] };

const LOG: Entry[] = [
  {
    date: '18 October 2026',
    title: 'Ezoic display-ad application',
    points: [
      'Removed Adsterra banners, native ads and Sponsored offers, along with their reserved page space.',
      'Connected Ezoic through its consent, header and analytics scripts and configured the domain-specific managed ads.txt file.',
      'Monetag, push ads, popunders and overlay ad units remain inactive during Ezoic review.',
      'Display placements will wait for approval and ad-category settings so advertising can fit around study content.',
    ],
  },
  {
    date: '18 October 2026',
    title: 'Non-adult advertising',
    points: [
      'Kept the existing responsive banners, native banners and labelled Sponsored offers link.',
      'Adult campaigns are excluded through the advertising provider’s settings.',
      'The Social Bar unit remains disabled: the live test showed a notification-style card after support confirmed an interstitial-only setting.',
      'Popunders and push-like overlays are excluded from the website.',
    ],
  },
  {
    date: '18 October 2026',
    title: 'Responsive banners and sponsored offers',
    points: [
      'Added mobile and desktop banners, wide-screen side banners and native banners through the shared layout on every page.',
      'Only formats that fit the screen request ads. Frames load near the viewport and keep advertising scripts separate from accounts and study controls.',
      'Sponsored offers is a clearly labelled link that opens only when selected.',
      'Adult campaigns are enabled for the new units. Popunders and the unrestricted Social Bar tag are not installed.',
    ],
  },
  {
    date: '18 October 2026',
    title: 'Display banners across every page',
    points: [
      'Replaced Adcash with Adsterra’s approved 300×250 display banner.',
      'A single shared placement now covers every page, including formulas, practice, mocks, exam tools and account pages.',
      'The banner sits outside page forms and test controls. Its isolated frame cannot read account data or form inputs.',
      'One banner request when the slot approaches the screen, no automatic refresh, push prompts, popunders or overlays.',
    ],
  },
  {
    date: '18 October 2026',
    title: 'Ordinary display advertising',
    points: [
      'Added a labelled 300×250 Adcash display banner to public study guides, exam analyses, topic overviews and the homepage.',
      'Ads load as their slot approaches the screen, with one request per page visit and no automatic refresh.',
      'Sign-in, account progress, feedback forms, calculators and active tests remain outside advertising placements.',
      'Updated advertising privacy disclosures. Monetag and Infolinks remain disabled.',
    ],
  },
  {
    date: '16 October 2026',
    title: 'Advertising integration and privacy disclosure',
    points: [
      'Removed the Monetag MultiTag trial and its push worker. Advertising is paused while applying for ordinary display ads; Infolinks remains disabled.',
      'Retained the site’s offline handlers under one service-worker registration.',
      'Excluded sign-in, personal progress, feedback forms, calculators and tests from the advertising code.',
      'Updated the privacy policy to explain advertising data and visitor choices.',
    ],
  },
  {
    date: '15 October 2026',
    title: 'Content depth pass',
    points: [
      'Mock-paper pages now show a paper summary, a section-wise breakdown, an attempt strategy and sample solved questions on the page itself, not only behind the start button.',
      'Cutoff, study-plan, mock-index, practice, formula and example pages were expanded with reading guides, worked examples and links to the matching lessons.',
      'Added this updates log and a clearer description of how content is checked on the About and Content & corrections pages.',
    ],
  },
  {
    date: '14 October 2026',
    title: 'Login and feedback',
    points: [
      'Sign-in protection is now verified on the live site after every deployment.',
      'Students can send private feedback and correction reports without creating a public post.',
    ],
  },
  {
    date: '11 October 2026',
    title: 'Corrections to shift-analysis wording',
    points: [
      'Corrected claims about how many candidate reviews a shift summary draws on.',
      'Search engines are now notified after each update so corrections are picked up sooner.',
    ],
  },
  {
    date: '10 October 2026',
    title: 'Original lessons and quality gates',
    points: [
      'Improved original lessons and added the content transparency notes you see on the About and Content & corrections pages.',
      'Shift analyses now withhold a figure when a quality check fails instead of showing a doubtful number, and interview-style reviews are excluded from recalled-question lists.',
      'Duplicate routes were consolidated so each topic has a single address.',
    ],
  },
  {
    date: '9 October 2026',
    title: 'Study guides and revision calendar',
    points: ['Added practical study guides and a free revision calendar planner.'],
  },
  {
    date: '7 October 2026',
    title: 'More exams and a clean-up of imported papers',
    points: [
      'RRB ALP, RRB JE, SBI Clerk, SBI PO and UP Police exam hubs went live.',
      'Fixed garbled characters in imported mock papers.',
      'Removed passage text that had been wrongly attached to the last option of 36 SBI PO questions.',
      'Two CAT 2025 slots were held back because their explanations followed the source site too closely; they were republished only after the explanations were rewritten in our own words.',
    ],
  },
  {
    date: '6 October 2026',
    title: 'Per-exam tools and automated shift analysis',
    points: [
      'Per-exam syllabus, admit-card, calendar and expected-cutoff pages, plus score, rank, salary and normalisation calculators.',
      'Introduced the automated SSC CGL shift-analysis pipeline with transparent Pending / Partial / Reported labels.',
    ],
  },
  {
    date: '4–5 October 2026',
    title: 'Previous-year papers for ten exams',
    points: [
      'Added previous-year practice papers across ten exams, with worked solutions.',
      'Expanded from a single exam to a multi-exam site.',
    ],
  },
  {
    date: '28–30 September 2026',
    title: 'Lessons, subjects and current affairs',
    points: [
      'Readable lessons for every topic, deeper General Awareness and Computer notes, and a month-by-month current-affairs archive.',
      'First shift-wise SSC CGL 2026 Tier 1 analyses.',
      'Fixed formatting problems found in a whole-site audit.',
    ],
  },
];

export default function UpdatesPage() {
  return (
    <article className="max-w-3xl mx-auto lesson">
      <h1 className="text-3xl font-extrabold">Site updates and corrections log</h1>
      <p className="mt-3 muted">
        A dated record of what changed on ExamShortcut. If you find something wrong, send it through the{' '}
        <Link className="underline" href="/feedback/">feedback page</Link>; confirmed errors are corrected or withheld and noted here when they are material.
        Read how we handle sources on the <Link className="underline" href="/editorial-policy/">Content &amp; corrections</Link> page.
      </p>
      <div className="mt-6 space-y-5">
        {LOG.map((e) => (
          <section key={e.date + e.title} className="card p-5">
            <p className="text-xs faint font-semibold uppercase">{e.date}</p>
            <h2 className="text-lg font-bold mt-1">{e.title}</h2>
            <ul className="list-disc pl-5 mt-2 space-y-1.5 text-sm">
              {e.points.map((p) => <li key={p}>{p}</li>)}
            </ul>
          </section>
        ))}
      </div>
      <p className="mt-6 text-sm muted">Daily shift-analysis refreshes are automatic and are not listed individually.</p>
    </article>
  );
}
