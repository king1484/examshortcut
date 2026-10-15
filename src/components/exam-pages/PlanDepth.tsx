import Link from 'next/link';
import { Md } from '@/components/Md';
import { SECTION_META, getExam, getTopic, getWeightage, listGuides, listMocks } from '@/lib/content';
import { getExamInfo } from '@/lib/exams';
import type { SectionId } from '@/lib/sections';
import { CAT_SECS, CONCEPT_ROTATION } from '@/lib/catSyllabus';
import { plain } from '@/components/exam-subpages/common';
import { RelatedCards, StagesTable, relatedFor, show } from './ExamDepth';

/* eslint-disable @typescript-eslint/no-explicit-any */
/* Server-rendered depth for the SSC CGL and CAT study-plan pages and the CGL guides index. Figures come from
   exam.json, weightage.json, the topic files and the guide files at build time. Week-by-week plans are
   labelled as illustrative: they show one sensible way to use the data, not an official schedule. */

const GRID = ['quant', 'reasoning', 'english', 'ga'] as const;
const secName = (id: string) => (SECTION_META as any)[id]?.name ?? id;
const secShort = (id: string) => (SECTION_META as any)[id]?.short ?? id;

/** Topics for one section ranked by the average questions per shift in weightage.json. */
function ranked(sid: string): { topicId: string; avg: number; latest: string; title: string }[] {
  const w = getWeightage('ssc-cgl');
  const rows: any[] = w?.sections?.[sid] ?? [];
  return [...rows]
    .sort((a, b) => (b.avg ?? 0) - (a.avg ?? 0))
    .map((r) => {
      const years = Object.keys(r.counts ?? {}).sort();
      const t = getTopic(sid as SectionId, r.topicId);
      return { topicId: r.topicId, avg: r.avg ?? 0, latest: years.length ? `${r.counts[years[years.length - 1]]} (${years[years.length - 1]})` : '—', title: t?.title ?? r.topicId };
    })
    .filter((r) => getTopic(sid as SectionId, r.topicId));
}

const topicLink = (sid: string, r: { topicId: string; title: string }) => (
  <Link key={r.topicId} className="underline" href={`/${sid}/${r.topicId}/`}>{r.title}</Link>
);

// ------------------------------------------------------------------ SSC CGL study plan
export function CglStudyPlanDepth() {
  const exam = getExam('ssc-cgl');
  const t1 = (exam?.stages ?? []).find((s: any) => s.id === 'tier1');
  const t2 = (exam?.stages ?? []).find((s: any) => s.id === 't2' || s.id === 'tier2');
  if (!t1 || !t2) return null;
  const t1sec: any[] = t1.sections ?? [];
  const t2sec: any[] = t2.sections ?? [];
  const merit = t2sec.filter((s) => !/qualifying/i.test(String(s.name)));
  const meritMarks = merit.reduce((a, s) => a + s.marks, 0);
  const t1Marks = t1sec.reduce((a, s) => a + s.marks, 0);
  const rows = GRID.map((sid) => {
    const a = t1sec.find((s) => s.sectionId === sid);
    const b = merit.find((s) => s.sectionId === sid);
    const s1 = a ? a.marks / t1Marks : 0;
    const s2 = b ? b.marks / meritMarks : 0;
    return { sid, a, b, s1, s2, blend: (s1 + s2) / 2 };
  });
  const computer = t2sec.find((s) => s.sectionId === 'computer');
  const mocks = listMocks('ssc-cgl');
  const fullMocks = mocks.filter((m) => m.available);
  const guides = listGuides('ssc-cgl');
  const rk = Object.fromEntries(GRID.map((sid) => [sid, ranked(sid)])) as Record<string, ReturnType<typeof ranked>>;
  const weeks = 12;
  const phaseOf = (w: number) => (w <= 4 ? 'Foundation' : w <= 8 ? 'Topic tests and sectionals' : w <= 10 ? 'Full mocks' : 'Revision and Tier 2 bridge');
  const secPerQ1 = Math.round((t1.durationMin * 60) / t1.totalQuestions);
  const perSectionMin = t1.durationMin / t1sec.length;

  return (
    <div className="mt-12">
      <section aria-labelledby="sp-split">
        <h2 id="sp-split" className="text-2xl font-extrabold">How to split your study time by section</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          Both tiers reward the same four subjects, but they weigh them differently. Tier 1 gives each subject {t1sec[0]?.questions} questions and {t1sec[0]?.marks} marks. Tier 2 Paper 1 merit marks total {meritMarks}, and English carries the largest module. The table averages the two shares to give a marks-weighted starting split. It is a starting point for the first weeks: move hours towards the section where your mocks lose the most marks.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Subject</th><th className="text-right">Tier 1 questions / marks</th><th className="text-right">Tier 1 share</th><th className="text-right">Tier 2 questions / marks</th><th className="text-right">Tier 2 merit share</th><th className="text-right">Starting study share</th></tr></thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.sid}>
                  <td className="font-semibold">{secName(r.sid)}</td>
                  <td className="text-right">{r.a ? `${r.a.questions} / ${r.a.marks}` : '—'}</td>
                  <td className="text-right">{show(r.s1 * 100)}%</td>
                  <td className="text-right">{r.b ? `${r.b.questions} / ${r.b.marks}` : '—'}</td>
                  <td className="text-right">{show(r.s2 * 100)}%</td>
                  <td className="text-right font-bold">{show(Math.round(r.blend * 1000) / 10)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="text-sm muted mt-3 max-w-3xl">
          {computer ? `Computer Knowledge (${computer.questions} questions, ${computer.marks} marks) is qualifying only in Tier 2, so it is left out of the merit shares and needs a small, scheduled slot rather than a large one. ` : ''}
          Our <Link className="underline" href="/exams/ssc-cgl/guides/preparation-strategy/">preparation strategy guide</Link> also gives a split for a full-time aspirant, and the planner above adjusts hours to your own strengths.
        </p>
      </section>

      <section className="mt-10" aria-labelledby="sp-time">
        <h2 id="sp-time" className="text-2xl font-extrabold">Time per question in the real papers</h2>
        <div className="max-w-3xl text-sm space-y-3 mt-3">
          <p>
            Tier 1 has {t1.totalQuestions} questions in {t1.durationMin} minutes, which is {secPerQ1} seconds per question on average, or {show(perSectionMin)} minutes for each {t1sec[0]?.questions}-question subject block. {t1.notes ? 'Our exam record adds: ' : ''}{t1.notes ? <Md inline>{String(t1.notes)}</Md> : null}
          </p>
          <p>
            Tier 2 Paper 1 has {t2.totalQuestions} questions in {t2.durationMin} minutes with the marking {plain(t2.negative)}, so a wrong answer costs more relative to a right one than in Tier 1. Practise your timed blocks with that stricter penalty in mind.
          </p>
        </div>
        <StagesTable id="ssc-cgl" caption="Stage-wise pattern for SSC CGL" />
      </section>

      <section className="mt-10" aria-labelledby="sp-top">
        <h2 id="sp-top" className="text-2xl font-extrabold">Which topics to study first</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          The weightage page compiles the typical number of questions per shift for recent Tier 1 papers. The table lists the five topics with the highest average in each subject and links to our notes for each. Counts are typical ranges per shift compiled from candidate recollections, not official figures.
        </p>
        <div className="grid sm:grid-cols-2 gap-3 mt-3">
          {GRID.map((sid) => (
            <div key={sid} className="card p-4">
              <div className="font-bold text-sm" style={{ color: (SECTION_META as any)[sid]?.color }}>{secName(sid)}</div>
              <ul className="text-sm mt-2 space-y-1 list-disc pl-5">
                {rk[sid].slice(0, 5).map((r) => (
                  <li key={r.topicId}>{topicLink(sid, r)} <span className="faint">&mdash; latest count {r.latest}</span></li>
                ))}
              </ul>
              <Link className="underline text-xs mt-2 inline-block" href={`/${sid}/`}>All {secShort(sid)} topics</Link>
            </div>
          ))}
        </div>
        <p className="text-sm muted mt-3 max-w-3xl">
          See the full table on the <Link className="underline" href="/exams/ssc-cgl/weightage/">SSC CGL weightage page</Link> and cross-check with the <Link className="underline" href="/exams/ssc-cgl/syllabus/">syllabus</Link> before you drop any topic.
        </p>
      </section>

      <section className="mt-10" aria-labelledby="sp-weeks">
        <h2 id="sp-weeks" className="text-2xl font-extrabold">A {weeks}-week plan, week by week</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          This is an illustrative plan, not an official schedule. It walks down the ranked topic lists above: the first four weeks cover the top four topics of each subject, the next four weeks cover the next four with a topic test for each, and the last four weeks are for mocks and revision. If you have fewer weeks, compress the foundation block first and keep the mock block intact.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Week</th><th>Phase</th>{GRID.map((sid) => <th key={sid}>{secShort(sid)}</th>)}</tr></thead>
            <tbody>
              {Array.from({ length: weeks }, (_, i) => i + 1).map((w) => (
                <tr key={w}>
                  <td className="font-semibold">{w}</td>
                  <td className="text-sm">{phaseOf(w)}</td>
                  {GRID.map((sid) => {
                    const list = rk[sid];
                    if (w <= 8) { const r = list[w - 1]; return <td key={sid} className="text-sm">{r ? topicLink(sid, r) : '—'}</td>; }
                    if (w <= 10) return <td key={sid} className="text-sm">{sid === 'quant' ? `Full mock ${w - 8}, analysed within a day` : 'Fix errors the mock shows'}</td>;
                    return <td key={sid} className="text-sm">{sid === 'quant' ? 'Formula sheet and mistake notebook' : sid === 'reasoning' ? 'Weak question types only' : sid === 'english' ? 'Vocabulary, cloze and comprehension timing' : 'Static and current-affairs revision'}</td>;
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9 max-w-3xl">
          <li><b>Foundation weeks (1 to 4):</b> read the notes of each topic, learn its shortcuts, then finish the topic test before moving on.</li>
          <li><b>Topic-test weeks (5 to 8):</b> the next four topics in each subject plus one timed {t1.durationMin / t1sec.length}-minute sectional a week for the subject you find hardest.</li>
          <li><b>Mock weeks (9 and 10):</b> a full-length {t1.durationMin}-minute Tier 1 paper at the real timing, then analyse attempts, accuracy and errors before the next one.</li>
          <li><b>Revision weeks (11 and 12):</b> no new topics. Revise from your mistake notebook, take a mock every alternate day, and start Tier 2 vocabulary and comprehension in parallel, since English is the heaviest Tier 2 module.</li>
        </ul>
      </section>

      <section className="mt-10" aria-labelledby="sp-mocks">
        <h2 id="sp-mocks" className="text-2xl font-extrabold">Mocks and revision in your plan</h2>
        <div className="max-w-3xl text-sm space-y-3 mt-3">
          <p>
            Our mock index lists {mocks.length} SSC CGL papers, of which {fullMocks.length} are open now. Take them at the real timing and in the real order, and keep a log of attempts, accuracy and score for each. The log matters more than any one score, because it shows whether you are improving accuracy or just attempting more questions. See the <Link className="underline" href="/exams/ssc-cgl/mocks/">mock index</Link> and the <Link className="underline" href="/exams/ssc-cgl/cutoffs/">cutoff explorer</Link> to set a target.
          </p>
          <p>
            Revision should be built into every week, not saved for the end. A simple rule is to revisit each topic a few days after you finish it, and again before the next mock, using the formula and shortcut pages in your notes. The <Link className="underline" href="/revision-planner/">revision planner</Link> can schedule these revisits for you.
          </p>
        </div>
      </section>

      {guides.length > 0 && (
        <section className="mt-10" aria-labelledby="sp-guides">
          <h2 id="sp-guides" className="text-2xl font-extrabold">Guides to read alongside this plan</h2>
          <div className="grid sm:grid-cols-2 gap-3 mt-3">
            {guides.map((g) => (
              <Link key={g.id} href={`/exams/ssc-cgl/guides/${g.id}/`} className="card p-4 hover:-translate-y-0.5 transition-transform">
                <div className="font-bold text-sm">{plain(g.title)}</div>
                <div className="text-xs faint mt-1">{plain(g.description)}</div>
              </Link>
            ))}
          </div>
        </section>
      )}

      <RelatedCards id="sp-related" heading="More on SSC CGL" cards={relatedFor('ssc-cgl', [])} />
    </div>
  );
}

// ------------------------------------------------------------------ CAT study plan
type Phase = 'concepts' | 'sectional' | 'mocks' | 'final';
/** Same heuristic as CatStudyPlanner (weeks left -> weeks per phase); duplicated so the page can show it without client code. */
function allocate(W: number): Record<Phase, number> {
  const f: [number, number, number, number] = W >= 16 ? [0.4, 0.25, 0.25, 0.1] : W >= 8 ? [0.25, 0.25, 0.35, 0.15] : W >= 4 ? [0.15, 0.25, 0.45, 0.15] : [0, 0.2, 0.55, 0.25];
  let rem = W;
  const take = (n: number) => { const v = Math.max(0, Math.min(rem, n)); rem -= v; return v; };
  const final = take(Math.max(1, Math.round(W * f[3])));
  const mocks = take(Math.round(W * f[2]));
  const sectional = take(Math.round(W * f[1]));
  const left = rem;
  return f[0] > 0 ? { concepts: left, sectional, mocks, final } : { concepts: 0, sectional, mocks: mocks + left, final };
}
const PHASE_LABEL: Record<Phase, string> = { concepts: 'Concepts', sectional: 'Sectional practice', mocks: 'Full mocks', final: 'Analysis and final revision' };
const PHASE_ORDER: Phase[] = ['concepts', 'sectional', 'mocks', 'final'];

export function CatStudyPlanDepth() {
  const exam = getExam('cat');
  const info = getExamInfo('cat');
  const stage = (exam?.stages ?? []).find((s: any) => s.id === 'cat-cbt');
  if (!stage) return null;
  const secs: any[] = stage.sections ?? [];
  const perSecMin = stage.durationMin / secs.length;
  const totalMarks = secs.reduce((a, s) => a + s.marks, 0);
  const focus = info?.sectionFocus ?? {};
  const scenarios = [20, 12, 6, 3];
  const example = 16;
  const alloc = allocate(example);
  const seq: Phase[] = PHASE_ORDER.flatMap((p) => Array<Phase>(alloc[p]).fill(p));
  const seen: Record<string, number> = {};

  return (
    <div className="mt-12">
      <section aria-labelledby="cs-split">
        <h2 id="cs-split" className="text-2xl font-extrabold">How CAT time and marks split across sections</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          CAT is {stage.totalQuestions} questions for {stage.totalMarks} marks in {stage.durationMin} minutes, and each section is locked to {show(perSecMin)} minutes, so you cannot move time from one section to another. Marking is {plain(stage.negative)}. The table shows what each section is worth and how much time each question gets on average. The composition is from the CAT 2025 paper as recorded in our exam data, and the IIMs do not announce question counts in advance, so confirm the pattern from the next official notice.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Section</th><th className="text-right">Questions</th><th className="text-right">Marks</th><th className="text-right">Share of marks</th><th className="text-right">Minutes</th><th className="text-right">Seconds per question</th></tr></thead>
            <tbody>
              {secs.map((s) => (
                <tr key={s.sectionId}>
                  <td className="font-semibold text-sm">{plain(s.name)}</td>
                  <td className="text-right">{s.questions}</td>
                  <td className="text-right">{s.marks}</td>
                  <td className="text-right">{show(Math.round((s.marks / totalMarks) * 1000) / 10)}%</td>
                  <td className="text-right">{show(perSecMin)}</td>
                  <td className="text-right font-bold">{show(Math.round((perSecMin * 60) / s.questions))}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="text-sm muted mt-3 max-w-3xl">
          The three sections carry nearly equal marks, so a plan that ignores one of them is a plan that gives up about a third of the paper. Many IIMs also apply sectional minimum percentiles, so a lopsided score can fail even when the overall percentile is high. This is why the planner above weights your weaker sections more but never drops a section.
        </p>
      </section>

      <section className="mt-10" aria-labelledby="cs-phases">
        <h2 id="cs-phases" className="text-2xl font-extrabold">How the weeks are split into phases</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          The planner splits the weeks you have left into four phases. With many weeks, concepts get the biggest share. With fewer weeks, the concept block shrinks and mock practice grows, and with only a few weeks left there is no new-concept phase at all. The table shows the split the planner produces for a few starting points. It is an illustrative heuristic, not an official schedule.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Weeks left</th>{PHASE_ORDER.map((p) => <th key={p} className="text-right">{PHASE_LABEL[p]}</th>)}</tr></thead>
            <tbody>
              {scenarios.map((W) => {
                const a = allocate(W);
                return (
                  <tr key={W}>
                    <td className="font-semibold">{W}</td>
                    {PHASE_ORDER.map((p) => <td key={p} className="text-right">{a[p]} week{a[p] === 1 ? '' : 's'}</td>)}
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
        <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9 max-w-3xl">
          <li><b>Concepts:</b> learn the method for each topic, then solve problems on it. Keep a mistake notebook from day one.</li>
          <li><b>Sectional practice:</b> timed {show(perSecMin)}-minute sectionals, one section at a time, with the weaker sections more often. In DILR, practise scanning all sets first and choosing which to attempt.</li>
          <li><b>Full mocks:</b> {stage.durationMin}-minute papers in the real order (VARC, then DILR, then QA). Analyse each one before taking the next, and budget about as long for the analysis as for the mock.</li>
          <li><b>Analysis and final revision:</b> no new topics. Revise from the mistake notebook, check the admit card and slot as soon as they are out, and fix the sleep schedule to your slot time.</li>
        </ul>
      </section>

      <section className="mt-10" aria-labelledby="cs-weeks">
        <h2 id="cs-weeks" className="text-2xl font-extrabold">Example: a {example}-week CAT plan, week by week</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          Starting from {example} weeks, the planner gives {alloc.concepts} concept weeks, {alloc.sectional} sectional weeks, {alloc.mocks} mock weeks and {alloc.final} final weeks. Concept weeks rotate through the commonly tested areas of each section, taken from our CAT syllabus reference. CAT has no official syllabus, so these areas are the ones that recur in past papers and prep-portal guides.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Week</th><th>Phase</th><th>Focus</th></tr></thead>
            <tbody>
              {seq.map((p, i) => {
                const j = (seen[p] = (seen[p] ?? -1) + 1);
                const focusText = p === 'concepts'
                  ? `QA: ${CONCEPT_ROTATION.qa[j % CONCEPT_ROTATION.qa.length]}. DILR: ${CONCEPT_ROTATION.dilr[j % CONCEPT_ROTATION.dilr.length]}. VARC: ${CONCEPT_ROTATION.varc[j % CONCEPT_ROTATION.varc.length]}.`
                  : p === 'sectional' ? 'Three or four timed sectionals, same-day review, error log by topic, TITA practice.'
                  : p === 'mocks' ? 'Two or three full mocks with analysis, then short drills only for the errors found.'
                  : i === seq.length - 1 ? 'Last week: no new topics, light revision, one light mock early in the week at most, then rest.' : 'No new topics. A full mock every two to three days, each analysed.';
                return (
                  <tr key={i}>
                    <td className="font-semibold">{i + 1}</td>
                    <td className="text-sm whitespace-nowrap">{PHASE_LABEL[p]}</td>
                    <td className="text-sm">{focusText}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </section>

      <section className="mt-10" aria-labelledby="cs-sections">
        <h2 id="cs-sections" className="text-2xl font-extrabold">What to study in each section</h2>
        <div className="space-y-3 mt-3">
          {CAT_SECS.map((s) => {
            const topics = ((focus as any)[s.sectionId] as string[] | undefined ?? []).map((tid) => ({ tid, t: getTopic(s.sectionId as SectionId, tid) })).filter((x) => x.t);
            return (
              <div key={s.id} className="card p-5">
                <h3 className="font-extrabold">{s.short}: {s.name}</h3>
                <p className="text-sm muted mt-1">{s.composition}</p>
                <ul className="text-sm mt-2 list-disc pl-5 space-y-0.5">
                  {s.areas.map((a) => <li key={a.name}><b>{a.name}:</b> {a.topics.join(', ')}</li>)}
                </ul>
                {info?.sectionApproach?.[s.sectionId as SectionId] && <p className="text-sm mt-3">{plain(info.sectionApproach[s.sectionId as SectionId])}</p>}
                {topics.length > 0 && (
                  <p className="text-sm mt-3"><b>Notes on this site for {s.short}:</b> {topics.map((x, i) => <span key={x.tid}>{i > 0 ? ', ' : ''}<Link className="underline" href={`/${s.sectionId}/${x.tid}/`}>{x.t!.title}</Link></span>)}.</p>
                )}
              </div>
            );
          })}
        </div>
        <p className="text-sm muted mt-3 max-w-3xl">
          For wider practice see the <Link className="underline" href="/english/">English</Link>, <Link className="underline" href="/reasoning/">Reasoning</Link> and <Link className="underline" href="/quant/">Quant</Link> subject pages. They are written for government exams, so use them for the base topics and use full CAT-style mocks for the real difficulty.
        </p>
      </section>

      <RelatedCards id="cs-related" heading="More on CAT" cards={relatedFor('cat', [])} />
    </div>
  );
}

// ------------------------------------------------------------------ SSC CGL guides index
export function CglGuidesDepth() {
  const guides = listGuides('ssc-cgl');
  if (!guides.length) return null;
  const exam = getExam('ssc-cgl');
  const byId = Object.fromEntries(guides.map((g) => [g.id, g]));
  const pick = (id: string) => byId[id];
  const lv = guides.map((g) => g.lastVerified).filter(Boolean).sort().slice(-1)[0];
  const lc = exam?.latestCycle ?? {};
  const steps: [string, string, string][] = [
    ['preparation-strategy', 'Start here', 'Read the overall method once: how Tier 1 and Tier 2 fit together, how to split time by section and how often to take mocks.'],
    ['study-plan-90-days', 'If you have about three months', 'The longest plan leaves room for a first pass of every topic, topic tests and a block of full mocks.'],
    ['study-plan-60-days', 'If you have about two months', 'A compressed plan that keeps the high-weightage topics and the mock block and trims the rest.'],
    ['study-plan-30-days', 'If you have about a month', 'Revision-led: mocks, formulas and the mistake log matter more than new topics.'],
    ['best-books', 'While you choose material', 'Section-wise book suggestions so that you do not collect more resources than you can finish.'],
    ['tier-2-strategy', 'Once Tier 1 is close or done', 'Tier 2 is where the merit list is decided, so read how the modules differ from Tier 1.'],
    ['cgl-vs-chsl', 'If you are choosing between exams', 'A comparison of CGL and CHSL to help you decide where to put your effort.'],
  ];
  return (
    <div className="mt-12">
      <section aria-labelledby="gi-how">
        <h2 id="gi-how" className="text-2xl font-extrabold">How to use these guides</h2>
        <div className="max-w-3xl text-sm space-y-3 mt-3">
          <p>
            There are {guides.length} guides on this page, and they are meant to be read in an order that depends on how much time you have left. They do not repeat one another: the strategy guide explains the method, the three study plans apply it to a fixed number of days, and the remaining guides cover books, Tier 2 and the choice between CGL and CHSL. Each guide links into the notes, formula sheets and mocks on this site so that you can act on it straight away.
          </p>
          <p>
            The facts they rely on are the same ones used across the site: Tier 1 is {(exam?.stages ?? [])[0]?.totalQuestions} questions for {(exam?.stages ?? [])[0]?.totalMarks} marks, and Tier 2 Paper 1 is {(exam?.stages ?? [])[1]?.totalQuestions} questions for {(exam?.stages ?? [])[1]?.totalMarks} marks. {lc.year ? `Our records for the ${lc.year} cycle show applications ${lc.applicationWindow ? `during ${plain(lc.applicationWindow)}` : 'as noted on the exam page'}. ` : ''}Always confirm dates and rules on the official notice.
            {lv ? ` The most recently verified guide was checked on ${lv}.` : ''}
          </p>
        </div>
      </section>

      <section className="mt-10" aria-labelledby="gi-order">
        <h2 id="gi-order" className="text-2xl font-extrabold">Which guide to read first</h2>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Your situation</th><th>Guide</th><th>Why</th></tr></thead>
            <tbody>
              {steps.filter(([id]) => pick(id)).map(([id, when, why]) => (
                <tr key={id}>
                  <td className="font-semibold text-sm">{when}</td>
                  <td className="text-sm"><Link className="underline" href={`/exams/ssc-cgl/guides/${id}/`}>{plain(pick(id).title)}</Link></td>
                  <td className="text-sm">{why}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="mt-10" aria-labelledby="gi-inside">
        <h2 id="gi-inside" className="text-2xl font-extrabold">What is inside each guide</h2>
        <div className="space-y-3 mt-3">
          {guides.map((g) => (
            <div key={g.id} className="card p-5">
              <h3 className="font-extrabold leading-snug"><Link className="underline" href={`/exams/ssc-cgl/guides/${g.id}/`}>{plain(g.title)}</Link></h3>
              <Md className="text-sm muted mt-1">{g.intro}</Md>
              <p className="text-sm mt-2"><b>Sections:</b> {g.sections.map((s) => plain(s.title)).join('; ')}.</p>
              <p className="text-xs faint mt-2">{g.sections.length} sections{g.faqs?.length ? `, ${g.faqs.length} frequently asked questions answered` : ''}{g.lastVerified ? `, last verified ${g.lastVerified}` : ''}.</p>
            </div>
          ))}
        </div>
      </section>

      <section className="mt-10" aria-labelledby="gi-tools">
        <h2 id="gi-tools" className="text-2xl font-extrabold">Tools and reference pages that go with the guides</h2>
        <StagesTable id="ssc-cgl" caption="Stage-wise pattern for SSC CGL" />
        <p className="text-sm muted mt-3 max-w-3xl">
          Use the <Link className="underline" href="/exams/ssc-cgl/study-plan/">study plan generator</Link> to turn a guide into dated tasks, the <Link className="underline" href="/exams/ssc-cgl/weightage/">weightage page</Link> to see which topics repeat, the <Link className="underline" href="/exams/ssc-cgl/mocks/">mocks</Link> to test the plan, and the <Link className="underline" href="/exams/ssc-cgl/cutoffs/">cutoffs</Link> to set a target score.
        </p>
      </section>

      <RelatedCards id="gi-related" heading="More on SSC CGL" cards={relatedFor('ssc-cgl', [])} />
    </div>
  );
}
