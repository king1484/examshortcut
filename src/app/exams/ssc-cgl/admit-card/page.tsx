import Link from 'next/link';
import type { Metadata } from 'next';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL 2026 admit card & answer key — download steps, challenge process',
  description: 'When and where the SSC CGL 2026 Tier 1 admit card is released (region-wise, 2–3 days before your exam date), what to check and carry, and how to download the answer key and response sheet to challenge questions and estimate your score.',
};

const STEPS = [
  ['Wait for your region\'s release', 'Admit cards go live region-wise on the zonal SSC websites from about 3 days before your exam date, and the city intimation slip comes earlier (for 2026 it was out on 21 Sep). SSC announces each region\'s release with a notice — check ssc.gov.in daily in exam week.'],
  ['Open the right website', 'Log in on ssc.gov.in (the new portal) or your regional SSC website. You need your registration number / roll number and the password or date of birth you set at application.'],
  ['Download the PDF', 'Download and print the admission certificate in colour if you can. A blurry photo or unreadable signature is the most common exam-day hassle.'],
  ['Verify every field', 'Name, father\'s/mother\'s name, exam date and shift, centre address, category, PwD status, photograph and signature. Any error: contact your regional office immediately — the correction window is short.'],
  ['Check the centre\'s reachability', 'The centre is allotted by SSC and cannot be changed. If it is in another city, plan travel the previous day; gates close an hour before the shift on many centres.'],
];

const CARRY = [
  'Printed admit card — one copy, ideally two',
  'Original photo ID used at application: Aadhaar / PAN / driving licence / voter ID / passport',
  'Two extra passport photos (same as the application photo)',
  'Simple ball pen (some centres provide sheets that need one)',
  'For PwD candidates: the scribe-related documents, if you opted for one',
];

const FAQS: [string, string][] = [
  ['When will the SSC CGL 2026 Tier 1 admit card be released?', 'Region-wise, from about 27 September 2026 — two to three days before each candidate\'s own exam date. Tier 1 runs from 30 September to 30 October 2026, so every candidate should have theirs by 27–28 September at the latest.'],
  ['Is the city intimation slip the same as the admit card?', 'No. The intimation slip only tells you the exam city (and sometimes the date) so you can plan travel. The admit card has your centre address, shift timing and roll number — you need the admit card itself to enter.'],
  ['My admit card is not showing on the website. What do I do?', 'Check your region\'s website rather than only ssc.gov.in — regions release at different hours. If it is still missing on the day before your exam, email or call your regional SSC office immediately; numbers are on the ssc.gov.in contact page. Rejected applications are the usual cause, so also confirm your application status.'],
  ['When is the Tier 1 answer key released?', 'Usually two to three weeks after the last shift — for 2026, expect around mid-November. SSC uploads the provisional answer key and your response sheet together, with a challenge window of roughly five days.'],
  ['How do I challenge a question?', 'Log in on the answer-key page with your roll number and password, select the question, pick the option you believe is correct, pay ₹100 per challenge online, and submit. Challenges are checked by subject experts; if a question is dropped, it is dropped for everyone. The final key that follows is binding.'],
  ['How do I calculate my score from the response sheet?', 'Count your correct and wrong responses per section and apply the marking scheme: Tier 1 gives +2 per correct answer and −0.50 per wrong one; unattempted questions score nothing. Enter the counts in the score calculator on this site to see your estimated score against recent cut-offs.'],
];

export default function AdmitCardPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({
        '@context': 'https://schema.org', '@type': 'FAQPage',
        mainEntity: FAQS.map(([q, a]) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } })),
      }) }} />
      <nav className="text-xs faint"><Link href="/exams/ssc-cgl/" className="underline decoration-dotted">SSC CGL</Link> / Admit card &amp; answer key</nav>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-2">SSC CGL 2026 admit card &amp; answer key</h1>
      <p className="muted mt-3 text-[15px]">
        The admit card (admission certificate) is released region-wise about <b>2–3 days before your own exam date</b> — for Tier 1 2026, from 27 September. The answer key and your response sheet follow two to three weeks after the last shift, with a short window to challenge. Here is exactly how both work.
      </p>

      <h2 className="text-2xl font-extrabold mt-8">Downloading your admit card, step by step</h2>
      <ol className="mt-4 space-y-3">
        {STEPS.map(([t, b], i) => (
          <li key={t} className="card p-4 flex gap-3">
            <span className="w-7 h-7 shrink-0 rounded-full font-extrabold text-sm flex items-center justify-center text-white" style={{ background: 'var(--brand)' }}>{i + 1}</span>
            <div><b className="text-sm">{t}</b><p className="text-sm muted mt-1">{b}</p></div>
          </li>
        ))}
      </ol>

      <h2 className="text-2xl font-extrabold mt-8">What to carry to the centre</h2>
      <div className="card p-5 mt-3">
        <ul className="list-disc ml-5 space-y-1.5 text-[15px]">
          {CARRY.map((x) => <li key={x.slice(0, 24)}>{x}</li>)}
        </ul>
        <p className="text-sm muted mt-3">Leave phones, smartwatches, wallets and jewellery at home or with someone — centres have no safe custody, and a beep at the frisking table can cost you the report time.</p>
      </div>

      <h2 className="text-2xl font-extrabold mt-8">Answer key &amp; response sheet</h2>
      <div className="card p-5 mt-3 text-[15px] space-y-2">
        <p>After Tier 1 ends, SSC uploads three things together on ssc.gov.in: the <b>provisional answer key</b>, <b>your response sheet</b> (what you actually marked in every question), and a <b>challenge window</b> of about five days at ₹100 per question.</p>
        <p>Compare your responses with the key and estimate your score before deciding what to challenge. Challenge only where you are confident the key is wrong — fee is refunded only if your challenge is accepted, and dropped questions are removed from everyone&apos;s evaluation.</p>
        <p>The <b>final answer key</b> published after challenges is what results are built on, and it is binding — no further representation is entertained.</p>
      </div>

      <div className="grid sm:grid-cols-3 gap-3 mt-6">
        <Link href="/exams/ssc-cgl/calendar/" className="card p-4"><div className="font-bold text-sm">⏳ All 2026 dates</div><div className="text-xs faint mt-1">Countdown + add to your calendar</div></Link>
        <Link href="/exams/ssc-cgl/score-calculator/" className="card p-4"><div className="font-bold text-sm">🧮 Estimate your score</div><div className="text-xs faint mt-1">From response-sheet counts, vs cut-offs</div></Link>
        <Link href="/exams/ssc-cgl/mocks/" className="card p-4"><div className="font-bold text-sm">🖥️ Practise the interface</div><div className="text-xs faint mt-1">Full mocks in the real CBT layout</div></Link>
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Frequently asked</h2>
      <div className="mt-3 space-y-2">
        {FAQS.map(([q, a]) => (
          <details key={q} className="card p-4">
            <summary className="font-bold text-sm cursor-pointer">{q}</summary>
            <p className="text-sm muted mt-2">{a}</p>
          </details>
        ))}
      </div>
      <p className="text-xs faint mt-4">Dates here follow the SSC CGL 2026 notification and recent-cycle practice. For anything binding — centre allotment, scribe norms, challenge fees — the notice on ssc.gov.in is the authority.</p>
    </div>
  );
}
