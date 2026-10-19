import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getExam, getCutoffs, contentStats, SECTION_META, listTopics, listMocks } from '@/lib/content';
import { EXAMS, getExamInfo } from '@/lib/exams';
import { Md } from '@/components/Md';
import { splitLead } from '@/lib/lead';
import { DatePhases } from '@/components/DatePhases';
import { CycleTimeline } from '@/components/CycleTimeline';
import { MoreOnExam, SscMtsArchiveNote, isSscMtsArchive } from '@/components/exam-subpages/common';
import { ExamGuideLinks } from '@/components/exam-pages/ExamInfoPages';
import { CatToolsBlock } from '@/components/cat/CatToolsNav';
import { ExamToolsBlock } from '@/components/exam-tools/ExamToolsBlock';
import { ExamPhoto } from '@/components/ExamPhoto';

const BUILT_AT = Date.now();

export const dynamic = 'force-static';
export const dynamicParams = false;

/** ssc-cgl keeps its own hand-built hub (and tools) under /exams/ssc-cgl/. */
export function generateStaticParams() {
  return EXAMS.filter((e) => e.id !== 'ssc-cgl').map((e) => ({ exam: e.id }));
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam: id } = await params;
  const info = getExamInfo(id);
  const data = getExam(id);
  if (!info) return {};
  const year = data?.latestCycle?.year ?? new Date().getFullYear();
  const archive = isSscMtsArchive(id);
  const title = `${info.name} ${year} — pattern, syllabus & eligibility`;
  return {
    title: { absolute: title },
    description: `${archive ? 'Archive of the SSC MTS 2025 cycle. ' : ''}${info.name}: ${info.blurb} Pattern, eligibility, posts and pay, selection, syllabus with shortcut tricks and FAQs.`,
    alternates: { canonical: `/exams/${id}/` },
  };
}

function Row({ k, v }: { k: string; v: React.ReactNode }) {
  return (
    <div className="py-2.5 border-b last:border-0 flex gap-3 text-sm" style={{ borderColor: 'var(--line)' }}>
      <span className="w-36 shrink-0 faint font-semibold">{k}</span>
      <span className="flex-1 min-w-0">{v}</span>
    </div>
  );
}

/* eslint-disable @typescript-eslint/no-explicit-any */
export default async function ExamHub({ params }: { params: Params }) {
  const { exam: id } = await params;
  const info = getExamInfo(id);
  if (!info || id === 'ssc-cgl') notFound();
  const exam = getExam(id);
  const stats = contentStats();
  const mocks = listMocks(id).filter((m) => m.available);
  const hasCutoffs = !!getCutoffs(id);

  if (!exam) {
    return (
      <div className="max-w-3xl mx-auto card p-8 text-center">
        <h1 className="text-2xl font-extrabold">{info.name} guide is being compiled</h1>
        <p className="muted mt-2">Meanwhile, the <Link className="underline" href="/learn/">syllabus and notes</Link> are already up.</p>
      </div>
    );
  }

  const lc = exam.latestCycle ?? {};
  const sections = info.sections;
  const isMba = info.category === 'MBA';
  const timeline: any[] = exam.timeline ?? [];
  const hasVacancies = timeline.some((t) => t.vacancies != null);
  const hasConducted = timeline.some((t) => t.conducted);
  const hasCandidates = timeline.some((t) => t.registered);
  const faqLd = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: (exam.faqs ?? []).map((f: any) => ({
      '@type': 'Question', name: f.q,
      acceptedAnswer: { '@type': 'Answer', text: String(f.a).replace(/[#*`]/g, '') },
    })),
  };
  const crumbLd = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
      { '@type': 'ListItem', position: 2, name: 'Exams', item: 'https://examshortcut.in/exams/' },
      { '@type': 'ListItem', position: 3, name: info.name, item: `https://examshortcut.in/exams/${id}/` },
    ],
  };
  const links: [string, string, string][] = [
    ['/learn/', '📚 Syllabus & topic notes', `${stats.topics} topics, ${stats.formulas}+ formulas`],
    ...(mocks.length ? [[`/exams/${id}/mocks/`, '🖥️ Mock tests', 'Real CBT interface + analysis'] as [string, string, string]] : []),
    ...(hasCutoffs ? [[`/exams/${id}/cutoffs/`, '📈 Cutoffs', 'Official, category-wise'] as [string, string, string]] : []),
    ['/formula-sheet/', '⚡ Formula sheet', 'Printable, all sections'],
    ['/daily-quiz/', '🎯 Daily quiz', 'A fresh mix every day'],
    ['/current-affairs/', '📰 Current affairs', 'Exam-relevant, month-wise'],
    ...(sections.includes('ga') ? [['/static-gk/', '🗺️ Static GK tables', 'Dances, parks, firsts, books, sports'] as [string, string, string]] : []),
    ['/vocab/', '🔤 Vocab bank', 'Idioms, one-word, synonyms, spellings'],
    ['/revision/', '📝 Mistake notebook', 'Your wrong answers, ready to revise'],
  ];

  const overview = splitLead(exam.overview);

  return (
    <article className="max-w-4xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify([faqLd, crumbLd]) }} />
      <p className="text-xs font-bold uppercase tracking-wide" style={{ color: 'var(--brand)' }}>Complete exam guide</p>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-1">{exam.fullName}</h1>
      <SscMtsArchiveNote id={id} self />
      <Md className="mt-3 text-[15px] muted">{overview.lead}</Md>

      <div id="status" className="card p-5 mt-6 scroll-mt-28">
        <div className="flex items-center justify-between flex-wrap gap-2">
          <h2 className="text-lg font-extrabold">{lc.year} cycle — status</h2>
          <span className="chip">✓ Verified {new Date(`${exam.lastVerified}T00:00:00+05:30`).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'Asia/Kolkata' })}</span>
        </div>
        <div className="status-callout">
          <span className="status-kicker">Latest</span>
          <div className="mt-1.5"><DatePhases phases={[{ node: <Md>{lc.status}</Md> }, ...(lc.statusPhases ?? []).map((ph: { from: string; status: string }) => ({ from: ph.from, node: <Md>{ph.status}</Md> }))]} /></div>
        </div>
        {lc.milestones && (
          <div style={{ ['--cycle-n' as string]: lc.milestones.length }}>
            <CycleTimeline milestones={lc.milestones} builtAt={BUILT_AT} />
          </div>
        )}
        <div className="cycle-facts">
          {lc.vacancies && <span className="cycle-fact"><b>Vacancies</b>{Number(lc.vacancies).toLocaleString('en-IN')}</span>}
          {lc.fee && <span className="cycle-fact"><b>Fee</b>{lc.fee}</span>}
        </div>
        {lc.notes && <Md className="mt-3 text-sm muted">{lc.notes}</Md>}
      </div>

      <nav className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-6">
        {links.map(([href, t, s]) => (
          <Link key={href} href={href} className="card p-4 hover:-translate-y-0.5 transition-transform">
            <div className="font-bold text-sm">{t}</div>
            <div className="text-xs faint mt-0.5">{s}</div>
          </Link>
        ))}
      </nav>

      <ExamPhoto id={id} />

      {overview.rest && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">About this exam</h2>
          <Md className="mt-2 text-[15px] muted">{overview.rest}</Md>
        </>
      )}

      <MoreOnExam id={id} />
      <ExamGuideLinks id={id} />
      <ExamToolsBlock id={id} />
      {id === 'cat' && <CatToolsBlock />}

      <h2 className="text-2xl font-extrabold mt-10">Exam pattern</h2>
      {(exam.stages ?? []).map((st: any) => (
        <div key={st.id} className="mt-4">
          <h3 className="font-bold">{st.name} {st.nature && <span className="chip ml-1">{st.nature}</span>}</h3>
          <p className="text-xs faint mt-1">{[st.mode, st.durationMin != null && `${st.durationMin} min`, st.negative].filter(Boolean).join(' · ')}</p>
          {(st.sections ?? []).length > 0 && <div className="tbl-wrap mt-2">
            <table className="tbl">
              <thead><tr><th>Section</th><th>Questions</th><th>Marks</th></tr></thead>
              <tbody>
                {(st.sections ?? []).map((s: any) => (
                  <tr key={s.name}>
                    <td>
                      {s.sectionId && sections.includes(s.sectionId) ? (
                        <Link className="underline decoration-dotted" href={`/${s.sectionId}/`}>{s.name}</Link>
                      ) : s.name}
                    </td>
                    <td>{s.questions}</td><td>{s.marks}</td>
                  </tr>
                ))}
                {st.totalQuestions != null && <tr><td className="font-bold">Total</td><td className="font-bold">{st.totalQuestions}</td><td className="font-bold">{st.totalMarks}</td></tr>}
              </tbody>
            </table>
          </div>}
          {st.notes && <Md className="mt-2 text-sm muted">{st.notes}</Md>}
        </div>
      ))}

      <h2 className="text-2xl font-extrabold mt-10">Eligibility</h2>
      <div className="card p-5 mt-3">
        <Row k="Nationality" v={<Md inline>{exam.eligibility?.nationality}</Md>} />
        <Row k="Education" v={
          <div className="space-y-1">{(exam.eligibility?.education ?? []).map((e: any, i: number) => (
            <div key={i}><b>{e.posts}:</b> <Md inline>{e.requirement}</Md></div>))}</div>} />
        <Row k="Age" v={
          <div className="space-y-1">{(exam.eligibility?.age ?? []).map((e: any, i: number) => (
            <div key={i}><b>{e.posts}:</b> {e.range}</div>))}</div>} />
        {(exam.eligibility?.ageRelaxation ?? []).length > 0 && <Row k="Relaxation" v={
          <div className="tbl-wrap"><table className="tbl"><tbody>
            {(exam.eligibility?.ageRelaxation ?? []).map((e: any, i: number) => (
              <tr key={i}><td>{e.category}</td><td>{e.years}</td></tr>))}
          </tbody></table></div>} />}
        {exam.eligibility?.notes && <Row k="Notes" v={<Md inline>{exam.eligibility.notes}</Md>} />}
      </div>

      <h2 className="text-2xl font-extrabold mt-10">{isMba ? 'Institutes & programs' : 'Posts, pay & who should apply'}</h2>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead>{isMba
            ? <tr><th>Program</th><th>Institute</th><th>Type</th><th>Duration</th></tr>
            : <tr><th>Post</th><th>Department</th><th>Group</th><th>Pay level</th><th>Approx. in-hand</th></tr>}</thead>
          <tbody>
            {(exam.posts ?? []).map((p: any) => (
              <tr key={p.id ?? p.name}>
                <td className="font-semibold">{p.name}</td>
                <td>{p.department}</td><td>{p.group}</td><td>{p.payLevel}</td>{!isMba && <td>{p.inHandApprox}</td>}
              </tr>))}
          </tbody>
        </table>
      </div>
      {(exam.posts ?? []).some((p: any) => p.special) && (
        <Md className="mt-2 text-sm muted">{`**${isMba ? 'How each institute shortlists' : 'Special requirements'}:** ${(exam.posts ?? []).filter((p: any) => p.special).map((p: any) => `${isMba ? p.department : p.name} — ${p.special}`).join(' · ')}`}</Md>
      )}

      <h2 className="text-2xl font-extrabold mt-10">Selection process</h2>
      <Md className="mt-2">{exam.selectionProcess}</Md>
      {exam.normalization && (
        <>
          <h3 className="font-bold mt-4">Normalisation (why your raw score ≠ final score)</h3>
          <Md className="mt-1 text-sm muted">{exam.normalization}</Md>
        </>
      )}

      <h2 className="text-2xl font-extrabold mt-10">Preparation topics</h2>
      <p className="muted text-sm mt-1">Every topic below has full notes, formulas, shortcut tricks and practice — tap in.</p>
      <div className="grid sm:grid-cols-2 gap-3 mt-3">
        {sections.map((sid) => {
          const topics = listTopics(sid);
          return (
            <div key={sid} className="card p-4" style={{ borderTop: `3px solid ${SECTION_META[sid].color}` }}>
              <div className="flex items-baseline justify-between gap-2">
                <Link href={`/${sid}/`} className="font-bold underline underline-offset-2">{info.sectionLabels?.[sid] ?? SECTION_META[sid].name}</Link>
                <span className="text-xs faint shrink-0">{topics.length} topics</span>
              </div>
              <ul className="mt-2 space-y-1 text-sm">
                {topics.map((t) => (
                  <li key={t.id}>
                    <Link href={`/${sid}/${t.id}/`} className="underline decoration-dotted underline-offset-2">{t.title}</Link>
                  </li>
                ))}
              </ul>
            </div>
          );
        })}
      </div>

      {(exam.timeline ?? []).length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Notification dates history</h2>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Year</th>{hasConducted && <th>Conducted by</th>}{hasVacancies && <th>Vacancies</th>}<th>Notification</th><th>Exam</th><th>Result</th>{hasCandidates && <th>Candidates</th>}</tr></thead>
              <tbody>
                {(exam.timeline ?? []).slice().sort((a: any, b: any) => b.year - a.year).map((t: any) => (
                  <tr key={t.year}><td className="font-bold">{t.year}</td>{hasConducted && <td>{t.conducted ?? '—'}</td>}{hasVacancies && <td>{t.vacancies ?? '—'}</td>}<td>{t.notification ?? '—'}</td><td>{t.exam ?? t.tier1 ?? '—'}</td><td>{t.result ?? t.finalResult ?? '—'}</td>{hasCandidates && <td>{t.registered ?? '—'}</td>}</tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}

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
    </article>
  );
}
