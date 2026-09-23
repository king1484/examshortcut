import Link from 'next/link';
import type { Metadata } from 'next';
import { getExam, contentStats, availableSections, SECTION_META, listTopics } from '@/lib/content';
import { Md } from '@/components/Md';
import { CountdownChip } from '@/components/CountdownChip';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL 2026 — complete free guide: pattern, syllabus, cutoffs, mocks',
  description: 'SSC CGL exam pattern, eligibility, posts & pay, selection process, topic-wise syllabus with shortcut tricks, cutoff trends and free mock tests in a real CBT interface.',
};

function Row({ k, v }: { k: string; v: React.ReactNode }) {
  return (
    <div className="py-2.5 border-b last:border-0 flex gap-3 text-sm" style={{ borderColor: 'var(--line)' }}>
      <span className="w-36 shrink-0 faint font-semibold">{k}</span>
      <span className="flex-1 min-w-0">{v}</span>
    </div>
  );
}

export default function ExamPage() {
  const exam = getExam();
  const stats = contentStats();

  if (!exam) {
    return (
      <div className="max-w-3xl mx-auto card p-8 text-center">
        <h1 className="text-2xl font-extrabold">SSC CGL guide is being compiled</h1>
        <p className="muted mt-2">The exam data team is still writing. Meanwhile, the <Link className="underline" href="/ssc-cgl/syllabus/">syllabus and notes</Link> may already be up.</p>
      </div>
    );
  }

  const lc = exam.latestCycle ?? {};
  const faqLd = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: (exam.faqs ?? []).map((f: any) => ({
      '@type': 'Question', name: f.q,
      acceptedAnswer: { '@type': 'Answer', text: String(f.a).replace(/[#*`]/g, '') },
    })),
  };

  return (
    <article className="max-w-4xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqLd) }} />
      <p className="text-xs font-bold uppercase tracking-wide" style={{ color: 'var(--brand)' }}>Free complete guide</p>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">{exam.fullName}</h1>
      <Md className="mt-3 text-[15px] muted">{exam.overview}</Md>

      <div className="card p-5 mt-6">
        <div className="flex items-center justify-between flex-wrap gap-2">
          <h2 className="text-lg font-extrabold">{lc.year} cycle — live status</h2>
          <span className="flex items-center gap-2 flex-wrap">
            {lc.tier1 && <CountdownChip date="2026-09-30" />}
            <span className="chip chip-high">Verified {exam.lastVerified}</span>
          </span>
        </div>
        <p className="text-sm muted mt-2">{lc.status}</p>
        <div className="grid sm:grid-cols-2 gap-3 mt-3 text-sm">
          {[['Notification', lc.notificationDate], ['Application window', lc.applicationWindow], ['Tier 1', lc.tier1], ['Tier 2', lc.tier2], ['Vacancies', lc.vacancies ? String(lc.vacancies) : null], ['Fee', lc.fee]].map(([k, v]) => (
            <div key={k} className="rounded-xl p-3" style={{ background: 'var(--surface-2)' }}>
              <div className="text-xs faint font-semibold uppercase">{k}</div>
              <div className="mt-1">{v ?? 'To be announced'}</div>
            </div>
          ))}
        </div>
        {lc.notes && <Md className="mt-3 text-sm">{lc.notes}</Md>}
      </div>

      <nav className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-6">
        {[
          ['/ssc-cgl/syllabus/', '📚 Syllabus & topic notes', `${stats.topics} topics, ${stats.formulas}+ formulas`],
          ['/ssc-cgl/weightage/', '📊 Topic weightage', 'Questions per shift, by topic'],
          ['/ssc-cgl/mocks/', '🖥️ Free mock tests', 'Real CBT interface + analysis'],
          ['/ssc-cgl/cutoffs/', '📈 Cutoff trends', 'Year × category official cutoffs'],
          ['/ssc-cgl/score-calculator/', '🧮 Score calculator', 'Safe-score estimator'],
          ['/ssc-cgl/formula-sheet/', '⚡ Formula sheet', 'Printable, all sections'],
          ['/ssc-cgl/ga/current-affairs/', '📰 Current affairs', 'Apr–Sep 2026, exam-relevant'],
          ['/ssc-cgl/study-plan/', '🗓️ Study plan generator', 'Day-by-day timetable to exam day'],
          ['/ssc-cgl/posts/', '🏛️ Posts & age checker', 'Eligibility + post preference builder'],
          ['/ssc-cgl/calendar/', '⏳ Exam calendar', 'Countdown + add dates to your calendar'],
          ['/ssc-cgl/admit-card/', '🪪 Admit card & answer key', 'Download steps + challenge process'],
          ['/ssc-cgl/typing-test/', '⌨️ Typing test (DEST)', '15-min simulator, SSC error marking'],
        ].map(([href, t, s]) => (
          <Link key={href} href={href} className="card p-4 hover:-translate-y-0.5 transition-transform">
            <div className="font-bold text-sm">{t}</div>
            <div className="text-xs faint mt-0.5">{s}</div>
          </Link>
        ))}
      </nav>

      <h2 className="text-2xl font-extrabold mt-10">Exam pattern</h2>
      {exam.stages.map((st: any) => (
        <div key={st.id} className="mt-4">
          <h3 className="font-bold">{st.name} <span className="chip ml-1">{st.nature}</span></h3>
          <p className="text-xs faint mt-1">{st.mode} · {st.durationMin} min · {st.negative}</p>
          <div className="tbl-wrap mt-2">
            <table className="tbl">
              <thead><tr><th>Section</th><th>Questions</th><th>Marks</th></tr></thead>
              <tbody>
                {st.sections.map((s: any) => (
                  <tr key={s.sectionId}>
                    <td>
                      {availableSections().includes(s.sectionId) ? (
                        <Link className="underline decoration-dotted" href={`/ssc-cgl/${s.sectionId}/`}>{s.name}</Link>
                      ) : s.name}
                    </td>
                    <td>{s.questions}</td><td>{s.marks}</td>
                  </tr>
                ))}
                <tr><td className="font-bold">Total</td><td className="font-bold">{st.totalQuestions}</td><td className="font-bold">{st.totalMarks}</td></tr>
              </tbody>
            </table>
          </div>
          {st.notes && <Md className="mt-2 text-sm muted">{st.notes}</Md>}
        </div>
      ))}

      <h2 className="text-2xl font-extrabold mt-10">Eligibility</h2>
      <div className="card p-5 mt-3">
        <Row k="Nationality" v={<Md inline>{exam.eligibility?.nationality}</Md>} />
        <Row k="Education" v={
          <div className="space-y-1">{(exam.eligibility?.education ?? []).map((e: any, i: number) => (
            <div key={i}><b>{e.posts}:</b> {e.requirement}</div>))}</div>} />
        <Row k="Age" v={
          <div className="space-y-1">{(exam.eligibility?.age ?? []).map((e: any, i: number) => (
            <div key={i}><b>{e.posts}:</b> {e.range}</div>))}</div>} />
        <Row k="Relaxation" v={
          <div className="tbl-wrap"><table className="tbl"><tbody>
            {(exam.eligibility?.ageRelaxation ?? []).map((e: any, i: number) => (
              <tr key={i}><td>{e.category}</td><td>{e.years}</td></tr>))}
          </tbody></table></div>} />
        {exam.eligibility?.notes && <Row k="Notes" v={<Md inline>{exam.eligibility.notes}</Md>} />}
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Posts, pay & who should apply</h2>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>Post</th><th>Department</th><th>Group</th><th>Pay level</th><th>Approx. in-hand</th></tr></thead>
          <tbody>
            {(exam.posts ?? []).map((p: any) => (
              <tr key={p.name}>
                <td className="font-semibold">{p.name}{p.paper2 && <span className="chip ml-1">Paper 2</span>}</td>
                <td>{p.department}</td><td>{p.group}</td><td>{p.payLevel}</td><td>{p.inHandApprox}</td>
              </tr>))}
          </tbody>
        </table>
      </div>
      {(exam.posts ?? []).some((p: any) => p.special) && (
        <Md className="mt-2 text-sm muted">{`**Special requirements:** ${(exam.posts ?? []).filter((p: any) => p.special).map((p: any) => `${p.name} — ${p.special}`).join(' · ')}`}</Md>
      )}

      <h2 className="text-2xl font-extrabold mt-10">Selection process</h2>
      <Md className="mt-2">{exam.selectionProcess}</Md>
      <h3 className="font-bold mt-4">Normalisation (why your raw score ≠ final score)</h3>
      <Md className="mt-1 text-sm muted">{exam.normalization}</Md>

      <h2 className="text-2xl font-extrabold mt-10">Section strategy at a glance</h2>
      <div className="grid sm:grid-cols-2 gap-3 mt-3">
        {availableSections().map((sid) => {
          const topics = listTopics(sid);
          return (
            <Link key={sid} href={`/ssc-cgl/${sid}/`} className="card p-4" style={{ borderTop: `3px solid ${SECTION_META[sid].color}` }}>
              <div className="font-bold">{SECTION_META[sid].name}</div>
              <div className="text-xs faint">{topics.length} topics ready</div>
            </Link>
          );
        })}
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Notification dates history</h2>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>Year</th><th>Vacancies</th><th>Notification</th><th>Tier 1</th><th>Tier 2</th><th>Final result</th></tr></thead>
          <tbody>
            {(exam.timeline ?? []).slice().sort((a: any, b: any) => b.year - a.year).map((t: any) => (
              <tr key={t.year}><td className="font-bold">{t.year}</td><td>{t.vacancies ?? '—'}</td><td>{t.notification ?? '—'}</td><td>{t.tier1 ?? '—'}</td><td>{t.tier2 ?? '—'}</td><td>{t.finalResult ?? '—'}</td></tr>
            ))}
          </tbody>
        </table>
      </div>

      <h2 className="text-2xl font-extrabold mt-10">FAQs</h2>
      <div className="mt-3 space-y-2">
        {(exam.faqs ?? []).map((f: any, i: number) => (
          <details key={i} className="card p-4">
            <summary className="font-semibold cursor-pointer text-sm">{f.q}</summary>
            <Md className="mt-2 text-sm">{f.a}</Md>
          </details>
        ))}
      </div>

      {exam.documents && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Documents for document verification</h2>
          <Md className="mt-2 text-sm">{exam.documents}</Md>
        </>
      )}

      <h2 className="text-2xl font-extrabold mt-10">Sources</h2>
      <ul className="text-sm mt-2 space-y-1 list-disc pl-5">
        {(exam.sources ?? []).map((s: any, i: number) => (
          <li key={i}><a className="underline" href={s.url} target="_blank" rel="noopener noreferrer">{s.title}</a></li>
        ))}
      </ul>
    </article>
  );
}
