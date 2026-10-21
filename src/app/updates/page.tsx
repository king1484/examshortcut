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
    date: '21 October 2026',
    title: 'Statistics corrections and clearer score comparisons',
    points: [
      'Corrected 10 statistics practice questions, including wrong answer keys, missing correct options and contradictory explanations.',
      'Added six original questions and expanded the lessons on tied modes, continuous class boundaries, and population versus sample variance. All 62 statistics questions now have independently calculated answer checks.',
      'The SSC CGL score calculator now accepts whole answer counts and lets you select a historical cutoff by year and post list. Removed the unsupported normalisation band and qualification predictions.',
      'Restored redirects from old mock-test addresses to their correct exam pages and repaired the check that had blocked automatic analysis publication.',
      'The analysis archive now shows dates from 30 September onward. Replaced scrolling shift tables with readable cards, improved text contrast, and added date and shift navigation.',
    ],
  },
  {
    date: '19 October 2026',
    title: 'AdSense review clean-up and content corrections',
    points: [
      'Paused the remaining third-party advertising test and removed all non-AdSense ad scripts while the AdSense application is reviewed.',
      'Restored the local ads.txt file for the AdSense publisher and removed the third-party ads.txt redirect.',
      'Corrected SSC CGL Tier 2 timing and merit scoring, fixed a connector explanation, and repaired the study planner date handling.',
      'Tightened page metadata, added missing social preview images, and noindexed incomplete exam-analysis pages.',
    ],
  },
  {
    date: '16–18 October 2026',
    title: 'Advertising tests concluded',
    points: [
      'Tested third-party display and sponsored-link formats while evaluating advertising partners. All of those tests are paused as of 19 October 2026.',
      'No pop-unders, push notifications, overlays or sponsored-offer links are active.',
      'Sign-in, personal progress, forms, calculators and active tests are excluded from advertising.',
      'Updated the privacy policy to describe the current AdSense-only application.',
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
