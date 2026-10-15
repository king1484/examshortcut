import type { Metadata } from 'next';
import Link from 'next/link';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Content sources and corrections',
  description: 'Who maintains ExamShortcut, how original lessons differ from imported questions and automatic exam reviews, and how to report corrections.',
  alternates: { canonical: '/editorial-policy/' },
};

export default function EditorialPolicy() {
  return <article className="max-w-3xl mx-auto lesson">
    <h1 className="text-3xl font-extrabold">Content sources and corrections</h1>
    <p className="text-sm muted mt-2">Updated 15 October 2026 · Maintained by Vinay</p>
    <p className="mt-4">ExamShortcut is an independent study resource. Vinay maintains the website and handles correction requests. We distinguish explanations written for this site from exam information, imported practice material and automatically compiled reports. None of these resources guarantees an exam result.</p>
    <section className="lesson-sec"><h2 className="text-xl font-bold">Lessons and study guides</h2>
      <p className="mt-3">Our study guides explain a method, show small worked examples and link to relevant lessons. Practice examples are study exercises, not claims about questions in a future paper. A shortcut should state the conditions under which it works. For arithmetic, a correct option is not enough: the calculation and the explanation should agree.</p>
      <p className="mt-3">Software assists with drafting, calculations and structural checks. Such checks can find missing fields or invalid answer positions; they cannot prove that every explanation or factual statement is correct. Please report unclear working as well as wrong answers.</p>
    </section>
    <section className="lesson-sec"><h2 className="text-xl font-bold">Exam facts and previous-year material</h2>
      <p className="mt-3">Exam dates, eligibility, vacancies and scoring rules should be confirmed against the examining body&apos;s current notice. A historical cutoff is a past result, not a promise about the next cycle. Follow the official-source links on an exam page before making an application decision.</p>
      <p className="mt-3">The practice collection includes original exercises and questions imported from publicly accessible previous-year or memory-based sources. These are identified in their test descriptions; some are reduced subsets. Public availability and attribution do not by themselves establish permission to reproduce material. We do not claim ownership of third-party questions or passages. Rights holders can contact us with the page and source details for review.</p>
    </section>
    <section className="lesson-sec"><h2 className="text-xl font-bold">Automatic shift analyses</h2>
      <p className="mt-3">The collector finds date- and shift-labelled reviews, extracts candidate reports and combines them into short summaries. It runs independently of the maintainer&apos;s laptop. These pages are automated summaries, not manually verified papers or official SSC statements.</p>
      <ul className="list-disc pl-5 mt-3 space-y-2">
        <li><b>Pending:</b> no usable report has been published for that shift.</li>
        <li><b>Partial:</b> source coverage is limited or a quality check withheld a figure. Read the notes and linked sources before relying on the summary.</li>
        <li><b>Reported:</b> the source threshold is met. This describes source coverage, not certainty or official verification.</li>
      </ul>
      <p className="mt-3">Section attempt counts must fit the section size. Overall totals must not be copied into individual sections. Interview questions about difficulty or timing are excluded from the recalled-question list. Different channels can repeat the same candidate report, so several links do not necessarily mean several independent observations.</p>
      <p className="mt-3">Difficulty is subjective. Attempt ranges are what reports say, not recommended attempts or safe-score predictions. A missing Shift 3 report means insufficient usable evidence; it does not mean the exam was cancelled. We show source disagreements where available and withhold invalid figures instead of inventing replacements.</p>
    </section>
    <section className="lesson-sec"><h2 className="text-xl font-bold">How content is checked</h2>
      <p className="mt-3">Before a practice paper is published it must pass an automated check: every question needs options, a valid answer position and a solution, and the stated answer must match the text of the keyed option. We also scan imports for garbled characters and for stray text attached to options or solutions. These checks catch structural errors; they do not replace a careful read, and some answer keys in imported papers have not been independently re-solved.</p>
      <p className="mt-3">When a paper&apos;s explanations stay too close to their source, we hold the paper back and rewrite them in our own words before it is republished. Each material change is noted in the <Link className="underline" href="/updates/">updates log</Link>.</p>
    </section>
    <section className="lesson-sec"><h2 className="text-xl font-bold">Request a correction</h2>
      <p className="mt-3">Send the page URL, the question or statement, and the reason it needs correction through our <Link className="underline" href="/contact/">contact page</Link>. Include your working or a reliable source if possible. You do not need to send an admit card, identity document or account password.</p>
      <p className="mt-3">A confirmed error is corrected or withheld. Material corrections to automatic reports carry a correction note. We do not promise a response time, and an update date alone does not mean every statement on a page has been rechecked.</p>
    </section>
    <p className="mt-6"><Link className="underline" href="/study-guides/">Explore the study guides</Link> · <Link className="underline" href="/about/">About ExamShortcut</Link></p>
  </article>;
}
