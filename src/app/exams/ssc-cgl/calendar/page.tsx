import Link from 'next/link';
import type { Metadata } from 'next';
import { getExam } from '@/lib/content';
import { ExamCalendar, type CalEvent } from '@/components/ExamCalendar';
import { CalendarPlaybook } from '@/components/exam-pages/ExamDepth';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL 2026 calendar: published dates and upcoming notice checks',
  description: 'SSC CGL Tier 1 tentative keys and responses: 4 November, 9 PM–7 November, 9 PM. Check the official challenge deadline and the next result and Tier 2 notices.',
};

export default function CalendarPage() {
  const exam = getExam();
  const cal = exam?.calendar as { cycle: number; note: string; events: CalEvent[] } | undefined;
  const events = cal?.events ?? [];
  const tier1 = events.find((e) => e.id === 'tier1');

  const jsonLd = events.filter((e) => e.status !== 'done' && (e.id === 'tier1' || e.id === 'tier2')).map((e) => ({
    '@context': 'https://schema.org', '@type': 'Event',
    name: `SSC CGL ${cal?.cycle} ${e.title}`,
    startDate: e.start, endDate: e.end ?? e.start,
    eventStatus: 'https://schema.org/EventScheduled',
    eventAttendanceMode: 'https://schema.org/OfflineEventAttendanceMode',
    location: { '@type': 'Place', name: 'SSC exam centres across India', address: { '@type': 'PostalAddress', addressCountry: 'IN' } },
    organizer: { '@type': 'Organization', name: 'Staff Selection Commission', url: 'https://ssc.gov.in' },
    description: e.note ?? '',
  }));

  return (
    <div className="max-w-3xl mx-auto">
      {jsonLd.length > 0 && <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />}
      <nav className="text-xs faint"><Link href="/exams/ssc-cgl/" className="underline decoration-dotted">SSC CGL</Link> / Exam calendar</nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-2">SSC CGL {cal?.cycle} exam calendar</h1>
      <p className="muted mt-3 text-[15px]">
        {tier1 && <>SSC&apos;s key notice records Tier 1 held <b>30 Sep – 28 Oct 2026</b>. </>}
        The tentative-key viewing and challenge period is <b>4 November, 9 PM–7 November, 9 PM IST</b>.
      </p>
      <div className="mt-6"><ExamCalendar events={events} /></div>
      {cal?.note && <p className="text-xs faint mt-2">{cal.note.replaceAll('*', '')}</p>}

      <p className="text-sm muted mt-4">The <Link href="/exam-updates/ssc-cgl-2026-tier-1-answer-key-november/" className="underline">4 November key notice</Link> gives a ₹50 charge per question/answer challenged and says responses will not remain available after the published window. Result and Tier 2 dates require separate <a href="https://ssc.gov.in/" className="underline" target="_blank" rel="noopener noreferrer">SSC notices</a>; no date is inferred here.</p>

      <h2 className="text-2xl font-extrabold mt-10">Use the time you have</h2>
      <div className="grid sm:grid-cols-2 gap-3 mt-3">
        <Link href="/exams/ssc-cgl/study-plan/" className="card p-4"><div className="font-bold text-sm">🗓️ Build a day-by-day plan to exam day</div><div className="text-xs faint mt-1">Fitted to the days you have left</div></Link>
        <Link href="/exams/ssc-cgl/mocks/" className="card p-4"><div className="font-bold text-sm">📝 Take a full mock</div><div className="text-xs faint mt-1">Real pattern, with negative marking</div></Link>
      </div>
      <CalendarPlaybook id="ssc-cgl" />
    </div>
  );
}
