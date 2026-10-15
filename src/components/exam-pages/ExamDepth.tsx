import Link from 'next/link';
import type { ReactNode } from 'react';
import { Md } from '@/components/Md';
import { SECTION_META, getExam, listMocks } from '@/lib/content';
import { EXAMS, getExamInfo, type ExamCategory } from '@/lib/exams';
import { getCalendar, getProcess, hasPage } from '@/lib/examPages';
import { hasTool } from '@/lib/examTools';
import { plain } from '@/components/exam-subpages/common';

/* eslint-disable @typescript-eslint/no-explicit-any */
/* Server-rendered depth blocks for the exam-level pages: cutoffs, mock index, calendar, admit card.
   Everything is derived from content/exams/<id>/{exam,cutoffs,process}.json at build time, so no figure
   here is typed in by hand: tables, differences and counts are computed from the data, and the advice is
   general guidance that always points back to the official notice. Additive only: these blocks sit
   below the existing page content. */

// ------------------------------------------------------------------ small helpers
export const show = (n: number) => (Number.isInteger(n) ? String(n) : String(Math.round(n * 100) / 100));
const signed = (n: number) => (n > 0 ? '+' : n < 0 ? '−' : '') + show(Math.abs(n));
const human = (k: string) => k.replace(/_/g, ' ').replace(/([a-z])([A-Z])/g, '$1 $2').replace(/^./, (c) => c.toUpperCase());
const isObj = (v: any): boolean => typeof v === 'object' && v !== null;
const median = (a: number[]) => {
  const s = [...a].sort((x, y) => x - y);
  const m = Math.floor(s.length / 2);
  return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
};
const trunc = (s: string, n: number) => (s.length > n ? `${s.slice(0, n - 1).trimEnd()}…` : s);

const HEADINGS: Record<string, string> = {
  iims: 'IIMs', otherColleges: 'Other top colleges', tier1: 'Tier 1', tier2: 'Tier 2', paper1: 'Paper 1', paper2: 'Paper 2',
  prelims: 'Prelims', mains: 'Mains', final: 'Final selection', cbt: 'CBT', cbt1: 'CBT 1', cbt2: 'CBT 2', pet: 'PET',
  qualifying: 'Qualifying marks', reserveList: 'Reserve list', written: 'Written exam',
};
const sectionTitle = (k: string) => HEADINGS[k] ?? human(k);

function fmtVal(v: any): string {
  if (typeof v === 'number') return show(v);
  if (isObj(v)) return Object.entries(v).map(([k, x]) => `${human(k)} ${fmtVal(x)}`).join(' / ');
  return plain(v);
}

export const examCard = 'card p-4 hover:-translate-y-0.5 transition-transform';

// ------------------------------------------------------------------ stages
export function stageFacts(s: any): string {
  const bits: string[] = [];
  if (s.totalQuestions) bits.push(`${s.totalQuestions} questions`);
  if (s.totalMarks) bits.push(`${s.totalMarks} marks`);
  if (s.durationMin) bits.push(`${s.durationMin} minutes`);
  return bits.join(', ');
}
const hasNegative = (s: any) => !!s.negative && !/^not applicable/i.test(String(s.negative));

/** One row per stage of the exam: role, format, scoring. Pure data from exam.json. */
export function StagesTable({ id, caption }: { id: string; caption?: string }) {
  const exam = getExam(id);
  const stages: any[] = exam?.stages ?? [];
  if (!stages.length) return null;
  return (
    <div className="tbl-wrap mt-3">
      <table className="tbl">
        {caption && <caption className="text-xs faint text-left pb-1">{caption}</caption>}
        <thead><tr><th>Stage</th><th>Role in selection</th><th>Format</th><th>Size</th><th>Negative marking</th></tr></thead>
        <tbody>
          {stages.map((s) => (
            <tr key={s.id}>
              <td className="font-semibold">{plain(s.name)}</td>
              <td className="text-sm">{plain(s.nature)}</td>
              <td className="text-sm">{plain(s.mode)}</td>
              <td className="text-sm whitespace-nowrap">{stageFacts(s) || '—'}</td>
              <td className="text-sm">{hasNegative(s) ? plain(s.negative) : '—'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

// ------------------------------------------------------------------ related links
export interface LinkCard { href: string; title: string; sub: string }

/** Links to the other pages that exist for this exam (only pages that are actually generated). */
export function relatedFor(id: string, skip: string[] = []): LinkCard[] {
  const info = getExamInfo(id);
  if (!info) return [];
  const n = info.name;
  const out: LinkCard[] = [{ href: `/exams/${id}/`, title: `${n} complete guide`, sub: 'Status, pattern, eligibility and FAQs' }];
  const add = (key: string, href: string, title: string, sub: string, ok = true) => { if (ok && !skip.includes(key)) out.push({ href, title, sub }); };
  const cgl = id === 'ssc-cgl';
  add('pattern', `/exams/${id}/exam-pattern/`, `${n} exam pattern`, 'Stages, marks, negative marking');
  add('syllabus', `/exams/${id}/syllabus/`, `${n} syllabus`, 'Section-wise topics', cgl || id === 'cat' || hasPage(id, 'syllabus'));
  add('eligibility', `/exams/${id}/eligibility/`, `${n} eligibility`, 'Age, qualification, relaxation');
  add('salary', `/exams/${id}/salary-and-posts/`, info.category === 'MBA' ? `${n} institutes and programs` : `${n} salary and posts`, info.category === 'MBA' ? 'IIMs, FMS and CAP programs' : 'Posts, pay level, in-hand pay');
  add('cutoffs', `/exams/${id}/cutoffs/`, `${n} cutoffs`, 'Official, category-wise', cgl || !!getExam(id));
  add('expected', cgl ? '/exams/ssc-cgl/cutoffs/expected-2026/' : `/exams/${id}/expected-cutoff/`, `${n} expected cutoff`, 'Past trend, marked as an estimate', cgl ? true : hasPage(id, 'expected-cutoff'));
  add('calendar', `/exams/${id}/calendar/`, `${n} important dates`, 'Notification to result', cgl || hasPage(id, 'calendar'));
  add('admit', `/exams/${id}/admit-card/`, `${n} admit card and result`, 'Download, answer key, scorecard', cgl || hasPage(id, 'admit-card'));
  add('mocks', `/exams/${id}/mocks/`, `${n} mock tests`, 'Real interface, full analysis', cgl || listMocks(id).some((m) => m.available));
  add('score', `/exams/${id}/score-calculator/`, `${n} score calculator`, 'Marks from your attempts', cgl || id === 'cat' || hasTool(id, 'score-calculator'));
  add('rank', `/exams/${id}/rank-estimator/`, `${n} rank estimator`, 'A planning estimate', cgl || hasTool(id, 'rank-estimator'));
  add('norm', `/exams/${id}/normalisation-calculator/`, `${n} normalisation calculator`, 'Marks across shifts', hasTool(id, 'normalisation-calculator'));
  return out;
}

export function RelatedCards({ cards, heading, id }: { cards: LinkCard[]; heading: string; id: string }) {
  if (!cards.length) return null;
  return (
    <section className="mt-10" aria-labelledby={id}>
      <h2 id={id} className="text-2xl font-extrabold">{heading}</h2>
      <nav className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-3">
        {cards.map((c) => (
          <Link key={c.href} href={c.href} className={examCard}>
            <div className="font-bold text-sm">{c.title}</div>
            <div className="text-xs faint mt-0.5">{c.sub}</div>
          </Link>
        ))}
      </nav>
    </section>
  );
}

/** Other exams in the same category, so a reader comparing options can jump across. */
export function peerCards(id: string, tail: 'cutoffs' | 'exam-pattern' | 'calendar' = 'exam-pattern', max = 4): LinkCard[] {
  const info = getExamInfo(id);
  if (!info) return [];
  return EXAMS.filter((e) => e.category === info.category && e.id !== id && e.status === 'live')
    .slice(0, max)
    .map((e) => ({ href: `/exams/${e.id}/${tail}/`, title: `${e.name} ${tail === 'cutoffs' ? 'cutoffs' : tail === 'calendar' ? 'dates' : 'exam pattern'}`, sub: e.blurb }));
}

// ------------------------------------------------------------------ cutoff digest
type Kind = 'inst' | 'cat' | 'many' | 'nestedBig' | 'nestedSmall' | 'text';
function kindOf(r: any): Kind {
  if (r?.institute) return 'inst';
  const vals = Object.values(r?.cutoffs ?? {});
  if (!vals.length) return 'text';
  if (vals.some((v) => isObj(v))) return vals.length > 8 ? 'nestedBig' : 'nestedSmall';
  if (vals.every((v) => typeof v === 'number')) return vals.length > 8 ? 'many' : 'cat';
  return 'text';
}
const rowLabel = (r: any, fb: string) => [r.year ?? r.cycle, r.list ?? r.stage].filter(Boolean).map((x) => plain(x)).join(' — ') || fb;
const shortLabel = (r: any, i: number) => trunc(String(r.year ?? r.cycle ?? r.stage ?? r.list ?? `List ${i + 1}`), 34);
const seriesKey = (r: any) => `${r.maxMarks ?? ''}|${String(r.list ?? r.stage ?? '').replace(/\([^)]*\)/g, '').replace(/\s+/g, ' ').trim().toLowerCase()}`;
const seriesName = (r: any) => String(r.list ?? r.stage ?? '').replace(/\([^)]*\)/g, '').replace(/\s+/g, ' ').trim();

function RowText({ r }: { r: any }) {
  const reserve = isObj(r.reserveList) ? (r.reserveList as Record<string, any>) : null;
  const notes = [r.note, r.notes, typeof r.categoryNotes === 'string' ? r.categoryNotes : null].filter((x) => typeof x === 'string' && x) as string[];
  return (
    <>
      {reserve && (
        <p className="text-sm mt-2"><b>Reserve list:</b> {Object.entries(reserve).filter(([k, v]) => k !== 'notes' && typeof v === 'number').map(([k, v]) => `${k} ${show(v as number)}`).join(', ')}.{typeof reserve.notes === 'string' ? ` ${plain(reserve.notes)}` : ''}</p>
      )}
      {isObj(r.categoryNotes) && (
        <>
          <p className="text-xs font-bold uppercase faint mt-3">Other category figures noted for this list</p>
          <ul className="text-sm mt-1 list-disc pl-5 space-y-0.5">
            {Object.entries(r.categoryNotes as Record<string, any>).map(([k, v]) => <li key={k}><b>{human(k)}:</b> {plain(v)}</li>)}
          </ul>
        </>
      )}
      {notes.map((t, i) => <Md key={i} className="text-sm muted mt-2">{t}</Md>)}
    </>
  );
}

function CatTable({ rows, sectionKey }: { rows: any[]; sectionKey: string }) {
  const cats = [...new Set(rows.flatMap((r) => Object.keys(r.cutoffs ?? {})))];
  const sorted = rows.every((r) => typeof r.year === 'number') ? [...rows].sort((a, b) => b.year - a.year) : rows;
  if (cats.length > 8) {
    return (
      <div className="space-y-3 mt-3">
        {sorted.map((r, i) => (
          <div key={i} className="card p-4">
            <div className="font-semibold text-sm">{rowLabel(r, sectionTitle(sectionKey))}{r.maxMarks ? <span className="faint font-normal"> (out of {r.maxMarks})</span> : null}</div>
            <ul className="text-sm mt-2 grid sm:grid-cols-2 gap-x-6 gap-y-0.5">
              {Object.entries(r.cutoffs ?? {}).map(([k, v]) => <li key={k}><b>{human(k)}:</b> {fmtVal(v)}</li>)}
            </ul>
            <RowText r={r} />
          </div>
        ))}
      </div>
    );
  }
  return (
    <>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>List</th><th>Out of</th>{cats.map((c) => <th key={c}>{human(c)}</th>)}</tr></thead>
          <tbody>
            {sorted.map((r, i) => (
              <tr key={i}>
                <td className="text-xs max-w-72"><b>{r.year ?? r.cycle}</b>{r.list || r.stage ? <> · {plain(r.list ?? r.stage)}</> : null}</td>
                <td>{r.maxMarks ?? '—'}</td>
                {cats.map((c) => <td key={c}>{r.cutoffs?.[c] !== undefined ? fmtVal(r.cutoffs[c]) : '—'}</td>)}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {sorted.map((r, i) => <RowText key={i} r={r} />)}
    </>
  );
}

function ManyBlock({ rows, sectionKey }: { rows: any[]; sectionKey: string }) {
  const years = rows.map((r) => r.year);
  const merge = rows.length > 1 && rows.length <= 4 && years.every((y) => typeof y === 'number') && new Set(years).size === rows.length;
  const stats = (r: any) => {
    const e = Object.entries(r.cutoffs ?? {}).filter(([, v]) => typeof v === 'number') as [string, number][];
    if (e.length < 2) return null;
    const lo = e.reduce((a, b) => (b[1] < a[1] ? b : a));
    const hi = e.reduce((a, b) => (b[1] > a[1] ? b : a));
    return { n: e.length, lo, hi, med: median(e.map((x) => x[1])) };
  };
  if (merge) {
    const sorted = [...rows].sort((a, b) => b.year - a.year);
    const keys = [...new Set(sorted.flatMap((r) => Object.keys(r.cutoffs ?? {})))];
    return (
      <>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>State / entry</th>{sorted.map((r, i) => <th key={i}>{r.year}</th>)}</tr></thead>
            <tbody>
              {keys.map((k) => (
                <tr key={k}>
                  <td className="font-semibold">{human(k)}</td>
                  {sorted.map((r, i) => <td key={i}>{r.cutoffs?.[k] !== undefined ? fmtVal(r.cutoffs[k]) : '—'}</td>)}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <ul className="text-sm mt-3 space-y-1 list-disc pl-5">
          {sorted.map((r, i) => {
            const s = stats(r);
            return s ? (
              <li key={i}><b>{r.year}:</b> {s.n} entries, lowest {show(s.lo[1])} ({human(s.lo[0])}), highest {show(s.hi[1])} ({human(s.hi[0])}), median {show(s.med)}{r.maxMarks ? ` on a scale of ${r.maxMarks}` : ''}. The spread between the lowest and highest entry is {show(s.hi[1] - s.lo[1])} marks.</li>
            ) : null;
          })}
        </ul>
        {sorted.map((r, i) => <RowText key={i} r={r} />)}
      </>
    );
  }
  return (
    <div className="space-y-4 mt-3">
      {rows.map((r, i) => {
        const s = stats(r);
        return (
          <div key={i} className="card p-4">
            <div className="font-semibold text-sm">{rowLabel(r, sectionTitle(sectionKey))}{r.maxMarks ? <span className="faint font-normal"> (out of {r.maxMarks})</span> : null}</div>
            {s && <p className="text-sm muted mt-1">{s.n} entries. Lowest {show(s.lo[1])} ({human(s.lo[0])}), highest {show(s.hi[1])} ({human(s.hi[0])}), median {show(s.med)}; a spread of {show(s.hi[1] - s.lo[1])} marks.</p>}
            <ul className="text-sm mt-2 grid sm:grid-cols-2 gap-x-6 gap-y-0.5">
              {Object.entries(r.cutoffs ?? {}).map(([k, v]) => <li key={k}><b>{human(k)}:</b> {fmtVal(v)}</li>)}
            </ul>
            <RowText r={r} />
          </div>
        );
      })}
    </div>
  );
}

function NestedBigBlock({ rows, sectionKey }: { rows: any[]; sectionKey: string }) {
  const sorted = rows.every((r) => typeof r.year === 'number') ? [...rows].sort((a, b) => b.year - a.year) : rows;
  return (
    <div className="space-y-4 mt-3">
      {sorted.map((r, i) => {
        const places = Object.entries(r.cutoffs ?? {}) as [string, any][];
        const cats = [...new Set(places.flatMap(([, v]) => (isObj(v) ? Object.keys(v) : [])))];
        return (
          <div key={i} className="card p-4">
            <div className="font-semibold text-sm">{rowLabel(r, sectionTitle(sectionKey))}{r.maxMarks ? <span className="faint font-normal"> (out of {r.maxMarks})</span> : null}</div>
            <p className="text-sm muted mt-1">{places.length} states and union territories have a published figure in this list. For each category the table shows the lowest, median and highest state figure.</p>
            <div className="tbl-wrap mt-2">
              <table className="tbl">
                <thead><tr><th>Category</th><th>Lowest state</th><th>Median</th><th>Highest state</th><th>Spread</th></tr></thead>
                <tbody>
                  {cats.map((c) => {
                    const e = places.filter(([, v]) => isObj(v) && typeof v[c] === 'number').map(([s, v]) => [s, v[c] as number] as [string, number]);
                    if (e.length < 2) return null;
                    const lo = e.reduce((a, b) => (b[1] < a[1] ? b : a));
                    const hi = e.reduce((a, b) => (b[1] > a[1] ? b : a));
                    return (
                      <tr key={c}>
                        <td className="font-semibold">{c}</td>
                        <td>{show(lo[1])} <span className="faint text-xs">({lo[0]})</span></td>
                        <td>{show(median(e.map((x) => x[1])))}</td>
                        <td>{show(hi[1])} <span className="faint text-xs">({hi[0]})</span></td>
                        <td>{show(hi[1] - lo[1])}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
            <RowText r={r} />
          </div>
        );
      })}
    </div>
  );
}

function NestedSmallBlock({ rows, sectionKey }: { rows: any[]; sectionKey: string }) {
  return (
    <div className="space-y-4 mt-3">
      {rows.map((r, i) => {
        const cats = Object.entries(r.cutoffs ?? {}) as [string, any][];
        const cols = [...new Set(cats.flatMap(([, v]) => (isObj(v) ? Object.keys(v) : [])))];
        return (
          <div key={i} className="card p-4">
            <div className="font-semibold text-sm">{rowLabel(r, sectionTitle(sectionKey))}{r.maxMarks ? <span className="faint font-normal"> (out of {r.maxMarks})</span> : null}</div>
            <div className="tbl-wrap mt-2">
              <table className="tbl">
                <thead><tr><th>Category</th>{cols.map((c) => <th key={c}>{human(c)}</th>)}</tr></thead>
                <tbody>
                  {cats.map(([c, v]) => (
                    <tr key={c}>
                      <td className="font-semibold">{c}</td>
                      {cols.map((k) => <td key={k}>{isObj(v) && v[k] !== undefined ? fmtVal(v[k]) : !isObj(v) && k === cols[0] ? fmtVal(v) : '—'}</td>)}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <RowText r={r} />
          </div>
        );
      })}
    </div>
  );
}

function TextBlock({ rows, sectionKey }: { rows: any[]; sectionKey: string }) {
  return (
    <div className="space-y-4 mt-3">
      {rows.map((r, i) => {
        const e = Object.entries(r.cutoffs ?? {});
        return (
          <div key={i} className="card p-4">
            <div className="font-semibold text-sm">{rowLabel(r, sectionTitle(sectionKey))}{r.maxMarks ? <span className="faint font-normal"> (out of {r.maxMarks})</span> : null}</div>
            {e.length > 0 && (
              <ul className="text-sm mt-2 space-y-1 list-disc pl-5">
                {e.map(([k, v]) => <li key={k}><b>{human(k)}:</b> {fmtVal(v)}</li>)}
              </ul>
            )}
            <RowText r={r} />
          </div>
        );
      })}
    </div>
  );
}

function InstituteTable({ rows }: { rows: any[] }) {
  const ge = (o: any) => (isObj(o) ? (o.General ?? o.UR ?? Object.entries(o).find(([k, v]) => k !== 'label' && k !== 'notes' && typeof v === 'string')?.[1]) : undefined);
  return (
    <>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>Institute</th><th>Tier</th><th>Qualifying rule (General)</th><th>Shortlist level (General)</th></tr></thead>
          <tbody>
            {rows.map((r, i) => (
              <tr key={i}>
                <td className="font-semibold text-sm">{plain(r.institute)}</td>
                <td className="text-sm">{plain(r.tier ?? '—')}</td>
                <td className="text-sm">{plain(ge(r.qualifying) ?? '—')}</td>
                <td className="text-sm">{plain(ge(r.shortlist) ?? '—')}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <ul className="text-sm mt-3 space-y-1.5 list-disc pl-5">
        {rows.map((r, i) => {
          const q = isObj(r.qualifying) ? plain(r.qualifying.notes ?? r.qualifying.label ?? '') : '';
          const s = isObj(r.shortlist) ? plain(r.shortlist.notes ?? r.shortlist.label ?? '') : '';
          const text = [q, s].filter(Boolean).join(' ');
          return text ? <li key={i}><b>{plain(r.institute)}:</b> {text}</li> : null;
        })}
      </ul>
    </>
  );
}

const TARGET_TIPS: Record<ExamCategory, string[]> = {
  SSC: [
    'Plan for the highest category figure that applies to your post list and category, not for the lowest qualifying mark. Qualifying percentages only keep you in the race; merit is decided among those who qualify.',
    'Remember that cutoffs are declared post-list by post-list. A figure quoted for one list may be higher or lower than the figure for the post you want, so check the list that matches your preference order.',
    'Because the exam runs in many shifts and the notice describes score normalisation, track your accuracy and attempts rather than a raw score. A raw score is only a rough indicator of the normalised marks that are finally compared.',
  ],
  Railways: [
    'Railway cutoffs are published per Railway Recruitment Board and per post category, so the same raw performance can land differently depending on the zone you chose. Look at the zone where you applied before judging any single figure.',
    'The rows marked as representative or as examples are there to show a realistic range, not to be used as the number for your zone. Your zone and post-level figure appears only in that board’s own result notice.',
    'Because the CBT is held across many days and shifts, marks are normalised. Compare your normalised score, not the raw score you remember from your shift.',
  ],
  MBA: [
    'There is no pass mark for the exam itself. What matters is the percentile that each institute asks for in its own admission policy, so read the qualifying rules of your target institutes before deciding what percentile to aim for.',
    'A sectional floor can matter as much as the overall percentile: a strong overall score with one weak section can fail a sectional requirement. Practise so that no section drops below your target.',
    'Shortlists are composite, mixing the exam percentile with academics, work experience and diversity weights, so the same percentile can convert at one institute and not at another.',
  ],
  Banking: [
    'Banking exams use stage-wise cutoffs, usually with sectional minimums in addition to an overall score. Aim to clear every section comfortably, because a very high total does not rescue a section that falls below its own minimum.',
    'The preliminary stage is a screening hurdle that does not count towards the final merit list in most of these exams, so use it to qualify with a margin and keep your main effort for the stage that decides your rank.',
    'Where cutoffs are state-wise or category-wise, compare yourself against the state and category you actually applied under, not against a national average.',
  ],
  Police: [
    'In police recruitment the written exam is only the first gate; physical standard and efficiency tests and document checks follow. Use the written-exam cutoff to decide how much margin you need and plan your physical preparation in parallel.',
    'Cutoffs are usually declared separately for male and female candidates and for each category. Read the row that matches your own category and gender and ignore the others.',
    'Sections that you find easy are where marks are won; use previous-year papers to learn the time pressure of the written exam instead of relying on a single score.',
  ],
};

/**
 * Server-rendered digest below the interactive cutoff explorer: every table is built from cutoffs.json,
 * so it adds crawlable depth without hand-typing a single number.
 */
export function CutoffDigest({ id, data }: { id: string; data: Record<string, any> }) {
  const info = getExamInfo(id);
  const exam = getExam(id);
  if (!info || !exam) return null;
  const n = info.name;
  const sections = Object.entries(data).filter(([k, v]) => k !== 'notes' && k !== 'sources' && Array.isArray(v) && v.length > 0 && isObj(v[0])) as [string, any[]][];
  const stages: any[] = exam.stages ?? [];
  const scored = stages.filter((s) => s.totalQuestions || s.totalMarks);
  const lead = scored.find((s) => hasNegative(s));

  // every distinct "out of" scale used on the page
  const scales = [...new Set(sections.flatMap(([, rows]) => rows.map((r) => r.maxMarks).filter((m) => typeof m === 'number')))].sort((a: number, b: number) => a - b) as number[];

  // latest numeric category row per section, for the reading bullets
  const readings: string[] = [];
  for (const [k, rows] of sections) {
    const cat = rows.filter((r) => kindOf(r) === 'cat' && typeof r.maxMarks === 'number');
    if (!cat.length) continue;
    if (cat.some((r) => Object.keys(r.cutoffs).some((c) => /^(example|range)/i.test(c)))) continue;
    const sorted = cat.every((r) => typeof r.year === 'number') ? [...cat].sort((a, b) => b.year - a.year) : cat;
    const r = sorted[0];
    const nums = Object.entries(r.cutoffs).filter(([, v]) => typeof v === 'number') as [string, number][];
    if (nums.length < 2) continue;
    const top = nums.reduce((a, b) => (b[1] > a[1] ? b : a));
    const low = nums.reduce((a, b) => (b[1] < a[1] ? b : a));
    readings.push(`${sectionTitle(k)}, ${rowLabel(r, sectionTitle(k))}: the highest category figure is ${human(top[0])} at ${show(top[1])} out of ${r.maxMarks} (${show((top[1] / r.maxMarks) * 100)} percent of the maximum), and the lowest is ${human(low[0])} at ${show(low[1])}. That is a gap of ${show(top[1] - low[1])} marks between categories.`);
  }

  // year-over-year change tables
  type Series = { name: string; max: any; rows: any[] };
  const series: Series[] = [];
  for (const [, rows] of sections) {
    const groups = new Map<string, any[]>();
    for (const r of rows) {
      if (kindOf(r) !== 'cat' || typeof r.year !== 'number') continue;
      const key = seriesKey(r);
      groups.set(key, [...(groups.get(key) ?? []), r]);
    }
    for (const g of groups.values()) {
      const byYear = new Map<number, any>();
      g.forEach((r) => { if (!byYear.has(r.year)) byYear.set(r.year, r); });
      if (byYear.size >= 2) series.push({ name: seriesName(g[0]), max: g[0].maxMarks, rows: [...byYear.values()].sort((a, b) => a.year - b.year) });
    }
  }

  const peerTail = sections.length ? 'cutoffs' : 'exam-pattern';
  const hasNumbers = sections.some(([, rows]) => rows.some((r) => ['cat', 'many', 'nestedBig', 'nestedSmall'].includes(kindOf(r))));
  const instOnly = !hasNumbers && sections.some(([, rows]) => rows.some((r) => kindOf(r) === 'inst'));

  return (
    <div className="mt-12">
      <section aria-labelledby="digest-figures">
        <h2 id="digest-figures" className="text-2xl font-extrabold">{n} cutoff figures, list by list</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          {instOnly
            ? `${n} has no single pass mark and no national cutoff. Every institute that accepts the score sets its own qualifying percentile and builds its own shortlist, so the figures below are institute-wise. The qualifying rules are the institutes’ published policy; the shortlist levels are compiled bands that describe who was typically called, and they are not official cutoffs.`
            : hasNumbers
            ? `Every figure below is taken from the cutoff data we keep for ${n}, laid out in plain tables so you can scan all lists at once. ${scales.length > 1 ? `Be careful with the scales: the lists use ${scales.length} different maximum marks (${scales.join(', ')}), so a number out of ${scales[0]} cannot be compared with one out of ${scales[scales.length - 1]}. ` : scales.length === 1 ? `All lists on this page are out of ${scales[0]} marks. ` : ''}Where a row carries a note about how the figure was produced, that note is printed under its table.`
            : `${n} does not release a table of cutoff marks in the way some other exams do. The sections below set out what is and is not published, so that you know how selection actually works and where to look.`}
        </p>
        {sections.map(([k, rows]) => {
          const years = [...new Set(rows.map((r) => r.year).filter((y) => typeof y === 'number'))].sort() as number[];
          const groups: Record<Kind, any[]> = { inst: [], cat: [], many: [], nestedBig: [], nestedSmall: [], text: [] };
          rows.forEach((r) => groups[kindOf(r)].push(r));
          return (
            <div key={k} className="mt-8">
              <h3 className="text-xl font-bold">{sectionTitle(k)}</h3>
              <p className="text-xs faint mt-1">{rows.length} {rows.length === 1 ? 'entry' : 'entries'}{years.length ? `, covering ${years.length === 1 ? years[0] : `${years[0]} to ${years[years.length - 1]}`}` : ''}.</p>
              {groups.inst.length > 0 && <InstituteTable rows={groups.inst} />}
              {groups.cat.length > 0 && <CatTable rows={groups.cat} sectionKey={k} />}
              {groups.many.length > 0 && <ManyBlock rows={groups.many} sectionKey={k} />}
              {groups.nestedBig.length > 0 && <NestedBigBlock rows={groups.nestedBig} sectionKey={k} />}
              {groups.nestedSmall.length > 0 && <NestedSmallBlock rows={groups.nestedSmall} sectionKey={k} />}
              {groups.text.length > 0 && <TextBlock rows={groups.text} sectionKey={k} />}
            </div>
          );
        })}
      </section>

      {readings.length > 0 && (
        <section className="mt-10" aria-labelledby="digest-reading">
          <h2 id="digest-reading" className="text-2xl font-extrabold">What the latest figures say</h2>
          <p className="text-sm muted mt-2 max-w-3xl">These lines are computed from the tables above, so they stay in step with the data. They describe the published numbers only and say nothing about the next cycle.</p>
          <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9">
            {readings.map((t) => <li key={t}>{t}</li>)}
          </ul>
        </section>
      )}

      {series.length > 0 && (
        <section className="mt-10" aria-labelledby="digest-yoy">
          <h2 id="digest-yoy" className="text-2xl font-extrabold">Year-over-year movement</h2>
          <p className="text-sm muted mt-2 max-w-3xl">
            For the lists that appear in more than one year, the tables show how each category figure changed from the previous listed year. A rise means the line got harder to clear; a fall means it got easier. Paper difficulty, the number of candidates, the number of vacancies and changes in the marking scheme all feed into these swings, so treat them as context and not as a forecast.
          </p>
          {series.map((s, i) => {
            const cats = [...new Set(s.rows.flatMap((r) => Object.keys(r.cutoffs).filter((c) => typeof r.cutoffs[c] === 'number')))].slice(0, 6);
            const first = s.rows[0], last = s.rows[s.rows.length - 1];
            const c0 = cats.find((c) => typeof first.cutoffs[c] === 'number' && typeof last.cutoffs[c] === 'number') ?? cats[0];
            return (
              <div key={i} className="card p-4 mt-4">
                <div className="font-semibold text-sm">{s.name}{s.max ? <span className="faint font-normal"> (out of {s.max})</span> : null}</div>
                <div className="tbl-wrap mt-2">
                  <table className="tbl">
                    <thead><tr><th>Year</th>{cats.map((c) => <th key={c}>{c} change</th>)}</tr></thead>
                    <tbody>
                      {[...s.rows].reverse().map((r) => {
                        const idx = s.rows.indexOf(r);
                        const prev = idx > 0 ? s.rows[idx - 1] : null;
                        return (
                          <tr key={r.year}>
                            <td className="font-bold">{r.year}</td>
                            {cats.map((c) => {
                              const v = r.cutoffs[c], p = prev?.cutoffs?.[c];
                              return <td key={c}>{typeof v !== 'number' ? '—' : typeof p === 'number' ? `${signed(Math.round((v - p) * 100) / 100)} (now ${show(v)})` : prev ? `now ${show(v)}` : `${show(v)} (first year)`}</td>;
                            })}
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
                {c0 && typeof first.cutoffs[c0] === 'number' && typeof last.cutoffs[c0] === 'number' && (
                  <p className="text-sm muted mt-2">From {first.year} to {last.year} the {c0} figure moved from {show(first.cutoffs[c0])} to {show(last.cutoffs[c0])}, a net change of {signed(Math.round((last.cutoffs[c0] - first.cutoffs[c0]) * 100) / 100)} marks over {last.year - first.year} {last.year - first.year === 1 ? 'year' : 'years'}.</p>
                )}
              </div>
            );
          })}
        </section>
      )}

      <section className="mt-10" aria-labelledby="digest-read">
        <h2 id="digest-read" className="text-2xl font-extrabold">How to read {n} cutoffs</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          A cutoff is only meaningful next to the stage it belongs to. {n} is conducted by {info.basics.conductingBody}, and its selection runs through these stages: {info.basics.stages}. The table sets out what each stage does, how big it is and how wrong answers are treated, because those three facts decide how to interpret any number you see above.
        </p>
        <StagesTable id={id} />
        <div className="max-w-3xl text-sm space-y-3 mt-5">
          <p><b>Qualifying cutoff versus shortlisting cutoff versus final cutoff.</b> A qualifying cutoff is a minimum that the exam body fixes in advance for each category; clearing it means you are eligible to be considered, not that you are selected. A shortlisting cutoff is the mark at which the body stopped when it called candidates for the next stage, and it depends on vacancies and on how everyone performed. A final cutoff is the score of the last candidate selected in a list. These three are very different numbers, which is why the rows above carry labels such as stage, list and cycle.</p>
          {lead && <p><b>Marking scheme effect.</b> For the stage “{plain(lead.name)}”, the scheme is: {plain(lead.negative)}. Under a scheme like this, a score is the net of correct answers minus the penalty on wrong ones, so two candidates with the same number of attempts can finish far apart. When you compare your mock scores with the cutoff, always compare net scores computed the same way.</p>}
          <p><b>Category and gender.</b> Where the figures are split by category (UR, EWS, OBC, SC, ST) or by male and female, read only the column that applies to you. Reserved-category figures are often lower than the general figure because each category is ranked in its own merit list, but small seat counts can invert this in individual states or zones, as some notes above point out.</p>
          <p><b>Sources and reproductions.</b> Cutoffs are compiled from the official result notices of the conducting body, and where the official notice does not print a figure we say so rather than fill the gap. Decimals can differ slightly between reproductions, and the official notice for your cycle always decides.</p>
        </div>
        {exam.normalization && (
          <div className="card p-5 mt-5 max-w-3xl">
            <h3 className="font-bold">Normalisation, shifts and score adjustment</h3>
            <Md className="text-sm mt-2">{String(exam.normalization)}</Md>
          </div>
        )}
        {exam.selectionProcess && (
          <div className="card p-5 mt-4 max-w-3xl">
            <h3 className="font-bold">From cutoff to selection</h3>
            <Md className="text-sm mt-2">{String(exam.selectionProcess)}</Md>
          </div>
        )}
      </section>

      <section className="mt-10" aria-labelledby="digest-target">
        <h2 id="digest-target" className="text-2xl font-extrabold">Turning cutoffs into a target score</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          Cutoffs are useful only if they change what you do. A practical method is to take the most recent comparable list for your category, treat the last few cycles as a band instead of a single number, and set your mock-test target a comfortable margin above the top of that band. The margin is your insurance against a harder paper, a larger applicant pool and fewer vacancies.
        </p>
        <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9 max-w-3xl">
          {TARGET_TIPS[info.category].map((t) => <li key={t}>{t}</li>)}
          {scored.length > 0 && <li>The scored stage that matters most for your first target is {plain(scored[0].name)}: {stageFacts(scored[0])}. Practise at exactly this size and time in our mocks so that the pace is familiar on the day.</li>}
          <li>Whatever number you pick, confirm the live cycle’s qualifying rules and category lists on the official notice of {info.basics.conductingBody} before you rely on any figure here.</li>
        </ul>
      </section>

      <RelatedCards id="digest-related" heading={`More on ${n}`} cards={relatedFor(id, ['cutoffs'])} />
      {peerCards(id, peerTail).length > 0 && <RelatedCards id="digest-peers" heading={`Compare with other ${info.category} exams`} cards={peerCards(id, peerTail)} />}
    </div>
  );
}

// ------------------------------------------------------------------ mock index guide
const KIND_LABEL: Record<string, string> = {
  full: 'Full-length mock written for this site',
  'pyq-pattern': 'Practice paper in the exam pattern (memory-based or pattern-based)',
  'real-pyq': 'Previous-year paper, imported with answers',
};

const SECTION_ADVICE: Record<string, string> = {
  quant: 'Take a first pass that picks up the quick arithmetic and formula-based questions, and park lengthy calculation or data questions for the second pass. Note down each question you skipped and why, because skipping decisions are a skill you can train.',
  reasoning: 'Do the questions with short rules (series, coding, direction, ranking) first and leave the large puzzle sets for when you have secured the easy marks. Spend a fixed number of seconds deciding whether a set is solvable before you invest time in it.',
  english: 'Read the question stems first for grammar, vocabulary and error-spotting items, which are quick marks, then move to passages. Time yourself on the passage separately in mocks so that you know how long a reading comprehension block really takes.',
  ga: 'General awareness is the fastest section when you know the answer and an expensive gamble when you do not. Decide in advance which topics you will attempt only when sure, and use the mock result to learn where your recall is weak.',
  computer: 'Computer questions are short factual items. Attempt them quickly and spend the saved time on the section that costs you the most seconds per mark.',
};

export function MockGuide({ id }: { id: string }) {
  const info = getExamInfo(id);
  const exam = getExam(id);
  if (!info || !exam) return null;
  const n = info.name;
  const mocks = listMocks(id);
  const open = mocks.filter((m) => m.available);
  const totalQ = open.reduce((a, m) => a + m.questionCount, 0);
  const stages: any[] = exam.stages ?? [];
  const main = stages.find((s) => s.totalQuestions && s.durationMin && (s.sections ?? []).length) ?? stages.find((s) => s.totalQuestions);
  const secs: any[] = main?.sections ?? [];
  const separate = !!main && /lock|separately timed|sectional tim|section-wise tim|sectional time/i.test(String(main.notes ?? ''));
  const kinds = [...new Set(mocks.map((m) => m.kind))];
  const approach = info.sectionApproach ?? {};

  return (
    <div className="mt-12">
      <section aria-labelledby="mg-library">
        <h2 id="mg-library" className="text-2xl font-extrabold">What is on offer for {n}</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          {mocks.length > 0
            ? `There ${mocks.length === 1 ? 'is' : 'are'} ${mocks.length} ${n} ${mocks.length === 1 ? 'paper' : 'papers'} listed, ${open.length} ${open.length === 1 ? 'is' : 'are'} ready to attempt now, and the ready ones hold ${totalQ} questions in total. The table lists the size, time and marking of each paper, and what kind of paper it is, so that you can pick the right one for your stage of preparation.`
            : `No ${n} paper is listed yet. Until one is added, use the exam pattern below to build your own practice sessions from the topic pages.`}
        </p>
        {mocks.length > 0 && (
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Paper</th><th>Type</th><th>Questions</th><th>Time</th><th>Marking</th><th>Sections</th></tr></thead>
              <tbody>
                {mocks.map((m) => (
                  <tr key={m.id}>
                    <td className="font-semibold text-sm">{m.available ? <Link className="underline" href={`/exams/${id}/mocks/${m.id}/`}>{m.title}</Link> : m.title}</td>
                    <td className="text-sm">{KIND_LABEL[m.kind] ?? m.kind}</td>
                    <td className="text-sm">{m.available ? m.questionCount : 'being set'}</td>
                    <td className="text-sm whitespace-nowrap">{m.durationMin} min</td>
                    <td className="text-sm whitespace-nowrap">+{show(m.plus)} / {'−'}{show(m.minus)}</td>
                    <td className="text-sm">{m.sections.map((s) => m.sectionNames?.[s] ?? info.sectionLabels?.[s] ?? SECTION_META[s].name).join(', ')}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
        {(kinds.includes('pyq-pattern') || kinds.includes('real-pyq')) && (
          <div className="callout mt-4 text-sm max-w-3xl">
            <b>About the source of these papers.</b> A paper labelled as a previous-year paper is imported from a published paper together with its answers and explanations; where some questions were left out (for example because a figure was unavailable or the key looked doubtful) the paper title says so and the question count above shows the true size. A paper labelled as pattern-based or memory-based is rebuilt from a publicly shared recollection or follows the official pattern, and it is not an official question paper. Use both kinds for practice and analysis, never as a prediction of the real paper.
          </div>
        )}
      </section>

      {main && (
        <section className="mt-10" aria-labelledby="mg-pattern">
          <h2 id="mg-pattern" className="text-2xl font-extrabold">The real {plain(main.name)} you are preparing for</h2>
          <p className="text-sm muted mt-2 max-w-3xl">
            A mock is only useful if it copies the real test, so start from the facts of the stage: {stageFacts(main)}{hasNegative(main) ? `, with ${plain(main.negative)}` : ''}. {separate ? 'Section timing in this exam is enforced section by section, so you cannot carry unused minutes from one section to the next; practise inside the per-section clock.' : 'Time is shared across the sections of the paper, so the order in which you attack the sections is part of your strategy.'}
          </p>
          {secs.length > 0 && (
            <div className="tbl-wrap mt-3">
              <table className="tbl">
                <thead><tr><th>Section</th><th>Questions</th><th>Marks</th>{main.durationMin && main.totalQuestions ? <th>Pro-rata time (guide)</th> : null}</tr></thead>
                <tbody>
                  {secs.map((s) => (
                    <tr key={s.name}>
                      <td className="font-semibold">{plain(s.name)}</td>
                      <td>{s.questions ?? '—'}</td>
                      <td>{s.marks ?? '—'}</td>
                      {main.durationMin && main.totalQuestions ? <td>{s.questions ? `about ${Math.round((main.durationMin * s.questions) / main.totalQuestions)} min (${Math.round((main.durationMin * 60) / main.totalQuestions)} s a question)` : '—'}</td> : null}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
          <p className="text-xs faint mt-2">The pro-rata time simply divides the total time by the number of questions. It is a pacing guide for your own mock practice, not an official allocation; follow the official instructions for the live test.</p>
        </section>
      )}

      {secs.length > 0 && (
        <section className="mt-10" aria-labelledby="mg-sections">
          <h2 id="mg-sections" className="text-2xl font-extrabold">Attempt strategy, section by section</h2>
          <div className="mt-3 space-y-3">
            {secs.map((s) => {
              const sid = s.sectionId as keyof typeof SECTION_ADVICE | undefined;
              const text = (sid && (approach as any)[sid]) || (sid && SECTION_ADVICE[sid]) || `Learn how long this section takes you in a timed mock and which question types give you marks fastest, then take those first.`;
              return (
                <div key={s.name} className="card p-4">
                  <div className="font-bold text-sm">{plain(s.name)}{s.questions ? <span className="faint font-normal"> · {s.questions} questions{s.marks ? `, ${s.marks} marks` : ''}</span> : null}</div>
                  <Md className="text-sm muted mt-1">{String(text)}</Md>
                </div>
              );
            })}
          </div>
        </section>
      )}

      <section className="mt-10" aria-labelledby="mg-routine">
        <h2 id="mg-routine" className="text-2xl font-extrabold">How to use each mock</h2>
        <ol className="card p-5 mt-3 text-sm space-y-2 list-decimal pl-9 max-w-3xl">
          <li><b>Set up like exam day.</b> Sit down at a fixed time, close other tabs and use only rough paper and a pen. {main?.durationMin ? `Give yourself the full ${main.durationMin} minutes without pausing.` : 'Do not pause the timer.'}</li>
          <li><b>Attempt in two passes.</b> First pass: answer what you can do confidently and mark the rest for review. Second pass: return to the marked questions in order of how close you were to solving them.</li>
          <li><b>{main && hasNegative(main) ? `Respect the penalty (${plain(main.negative)}).` : 'Respect the marking scheme.'}</b> Guess only when you can remove at least one option; otherwise leave the question and move on.</li>
          <li><b>Analyse before you take the next paper.</b> Spend about as long reviewing as you spent taking the test. For every wrong or skipped question, write down whether the cause was a concept gap, a calculation slip, a misread question or a time problem.</li>
          <li><b>Track three numbers.</b> Attempts, accuracy and net score for every section. Improving accuracy usually raises the net score faster than attempting more.</li>
          <li><b>Feed the mistake notebook.</b> Wrong answers go straight into your <Link className="underline" href="/revision/">mistake notebook</Link>; revisit it before the next mock.</li>
        </ol>
      </section>

      <section className="mt-10" aria-labelledby="mg-schedule">
        <h2 id="mg-schedule" className="text-2xl font-extrabold">When to take mocks in your preparation</h2>
        <div className="max-w-3xl text-sm space-y-3 mt-3">
          <p><b>Early on:</b> do not start with full papers. Learn the basics from the topic pages and the <Link className="underline" href={`/exams/${id}/syllabus/`}>syllabus</Link>, then take one paper as a diagnostic so that you know your starting accuracy by section.</p>
          <p><b>Middle phase:</b> alternate topic practice with one paper a week. Use the analysis to choose what to study next rather than following a fixed order.</p>
          <p><b>Last weeks:</b> raise the frequency, keep exact exam timings, and stop learning new topics in the final days. A paper taken the night before the exam mostly adds anxiety, so prefer revision of your notebook instead.</p>
          <p>These are suggestions, not an official schedule; your own timeline depends on the exam date in the <Link className="underline" href={`/exams/${id}/calendar/`}>important dates</Link> and on how much time you have.</p>
        </div>
      </section>

      <RelatedCards id="mg-related" heading={`Plan your ${n} preparation around the mocks`} cards={relatedFor(id, ['mocks'])} />
    </div>
  );
}

// ------------------------------------------------------------------ calendar playbook
const ACTION: [RegExp, string][] = [
  [/notif|advert|cen\b|release/i, 'Read the full notice, not a summary: eligibility, age as on the cut-off date, vacancies, exam pattern and the application rules.'],
  [/appl|regist|window/i, 'Fill the form carefully in one sitting, keep photo and signature files ready in the stated size, and save the final submitted copy.'],
  [/fee|payment/i, 'Pay the fee before the stated deadline and keep the transaction proof, because an unpaid application is not counted.'],
  [/correct|edit|modif/i, 'Use the correction window to fix errors only; the notice states which fields can be changed and what it costs.'],
  [/city|slot|intimation/i, 'Check the exam city and date allotted to you and plan travel and stay early.'],
  [/admit|call letter|e-call/i, 'Download and print the admit card, check each detail against your ID, and report any mismatch to the helpline at once.'],
  [/answer|key|objection/i, 'Compare your responses with the key, raise objections only within the window, and note the fee per objection if one applies.'],
  [/result|merit|score/i, 'Save the result and scorecard, compare your marks with the cutoffs, and check the next-stage instructions.'],
  [/document|dv|verification/i, 'Keep originals and self-attested copies ready as listed in the notice; missing papers can cost you the seat.'],
  [/pet|pst|physical|medical/i, 'Prepare for the physical or medical standards early and read the exact test format in the notice.'],
  [/interview|wat|gd|personality/i, 'Prepare your profile, your reasons for the post and current developments in your field.'],
  [/exam|cbt|test|prelim|main|tier|paper/i, 'Revise rather than learn, practise at exam timing, and plan the travel and sleep around your slot.'],
];
const actionFor = (title: string) => ACTION.find(([re]) => re.test(title))?.[1] ?? 'Check the official notice for what is required at this step and note the date.';

const fmtD = (iso: string) => new Date(`${iso}T00:00:00+05:30`).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'Asia/Kolkata' });

export function CalendarPlaybook({ id }: { id: string }) {
  const info = getExamInfo(id);
  const exam = getExam(id);
  const cal = getCalendar(id);
  if (!info || !exam || !cal) return null;
  const n = info.name;
  const pr = getProcess(id);
  const portal = pr?.portal ?? 'the official website';
  const events = [...cal.events].sort((a, b) => a.start.localeCompare(b.start));
  const lc = exam.latestCycle ?? {};
  const facts: [string, string][] = ([
    ['Notification', lc.notificationDate],
    ['Application window', lc.applicationWindow],
    ['First stage', lc.tier1],
    ['Second stage', lc.tier2],
    ['Vacancies', lc.vacancies],
    ['Application fee', lc.fee],
  ] as [string, unknown][]).filter(([, v]) => v !== undefined && v !== null && v !== '').map(([k, v]) => [k, plain(v)]);
  const past: any[] = Array.isArray(exam.timeline) ? exam.timeline : [];
  const confirmed = events.filter((e) => e.status !== 'expected').length;

  return (
    <div className="mt-12">
      <section aria-labelledby="cp-plan">
        <h2 id="cp-plan" className="text-2xl font-extrabold">What to do at each step of the {n} timeline</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          {events.length} dates are tracked for the {cal.cycle} cycle and {confirmed} of them are done or confirmed. The table pairs each date with the action that usually matters at that point. The actions are general good practice for this kind of exam; the exact rules for your cycle are in the official notice of {info.basics.conductingBody}.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Date</th><th>Step</th><th>Status</th><th>What to do</th></tr></thead>
            <tbody>
              {events.map((e) => (
                <tr key={e.id}>
                  <td className="whitespace-nowrap text-sm">{fmtD(e.start)}{e.end && e.end !== e.start ? ` to ${fmtD(e.end)}` : ''}</td>
                  <td className="font-semibold text-sm">{plain(e.title)}</td>
                  <td className="text-sm">{e.status}</td>
                  <td className="text-sm">{actionFor(e.title)}{e.note ? ` ${plain(e.note)}` : ''}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {facts.length > 0 && (
        <section className="mt-10" aria-labelledby="cp-cycle">
          <h2 id="cp-cycle" className="text-2xl font-extrabold">{lc.year ?? cal.cycle} cycle at a glance</h2>
          <dl className="card p-5 mt-3 text-sm grid sm:grid-cols-[11rem_1fr] gap-x-4 gap-y-2">
            {facts.map(([k, v]) => (
              <div key={k} className="contents"><dt className="font-bold">{k}</dt><dd>{v}</dd></div>
            ))}
          </dl>
          <p className="text-xs faint mt-2">These lines are the facts recorded in our exam data as last verified on {fmtD(exam.lastVerified)}. Dates can change by notice.</p>
        </section>
      )}

      {past.length > 0 && (
        <section className="mt-10" aria-labelledby="cp-past">
          <h2 id="cp-past" className="text-2xl font-extrabold">How earlier {n} cycles ran</h2>
          <p className="text-sm muted mt-2 max-w-3xl">Looking at earlier cycles shows how long each gap typically lasted between notification, exam and result. Use it for planning only: the schedule of the cycle you are in is the one in the table above.</p>
          <div className="space-y-3 mt-3">
            {past.map((t, i) => (
              <div key={i} className="card p-4">
                <div className="font-bold text-sm">{t.year}</div>
                <ul className="text-sm mt-1 space-y-0.5 list-disc pl-5">
                  {Object.entries(t).filter(([k, v]) => k !== 'year' && v !== null && v !== undefined && v !== '' && typeof v !== 'object').map(([k, v]) => <li key={k}><b>{human(k)}:</b> {plain(v)}</li>)}
                </ul>
              </div>
            ))}
          </div>
        </section>
      )}

      <section className="mt-10" aria-labelledby="cp-docs">
        <h2 id="cp-docs" className="text-2xl font-extrabold">Documents and checks to keep ready</h2>
        {exam.documents && <Md className="card p-5 mt-3 text-sm max-w-3xl">{String(exam.documents)}</Md>}
        <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9 max-w-3xl">
          <li>Scan your photograph and signature in the size and format the notice specifies, and keep the same files for every stage.</li>
          <li>Make sure the name, date of birth and parent names match across your ID, certificates and application. A mismatch is the most common cause of trouble at verification.</li>
          <li>Keep an email address and phone number you check daily; notices and e-call letters can arrive there first.</li>
          <li>Keep a dated note of every date you add to your calendar, with the notice number it came from.</li>
        </ul>
      </section>

      <section className="mt-10" aria-labelledby="cp-where">
        <h2 id="cp-where" className="text-2xl font-extrabold">Where official {n} notices appear</h2>
        <div className="max-w-3xl text-sm space-y-3 mt-3">
          <p>The only reliable source for any {n} date is {info.basics.conductingBody} itself. For this exam the portal we track is <b>{portal}</b>. Look for the notice, the schedule and any corrigendum or date-change notice there, and treat dates that appear only on coaching sites or social media as unconfirmed until they appear on the official site.</p>
          <p>Dates shown as expected on this page are estimates made from earlier cycles and tentative schedules. Revisit the official site a few days before each expected date, and again after any large-scale event that could move a schedule.</p>
          <p>If you register for a reminder with the calendar button above, you still need to check the portal, because reminders carry the date we recorded and not any later change.</p>
        </div>
      </section>

      <RelatedCards id="cp-related" heading={`Next steps for ${n}`} cards={relatedFor(id, ['calendar'])} />
    </div>
  );
}

// ------------------------------------------------------------------ admit card checklist
export function AdmitCardChecklist({ id }: { id: string }): ReactNode {
  const info = getExamInfo(id);
  const pr = getProcess(id);
  const exam = getExam(id);
  if (!info || !pr || !exam) return null;
  const n = info.name;
  const main = (exam.stages ?? []).find((s: any) => s.durationMin) ?? null;
  return (
    <section className="mt-10" aria-labelledby="ac-check">
      <h2 id="ac-check" className="text-2xl font-extrabold">Admit card checklist before exam day</h2>
      <div className="max-w-3xl text-sm space-y-3 mt-3">
        <p>Download the admit card as soon as {info.basics.conductingBody} releases it on {pr.portal} and do not wait for the last day, when the portal is usually busy. Print it clearly and keep a digital copy as a backup. The checks below are the ones that most often decide whether a candidate is allowed in smoothly.</p>
      </div>
      <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9 max-w-3xl">
        <li>Check that your name, photograph, signature, date of birth, category and roll number are correct. If anything is wrong, contact the helpline named in the notice before exam day.</li>
        <li>Read the reporting time, gate-closing time and shift timing. {main?.durationMin ? `Plan so that you are seated well before the ${main.durationMin}-minute test begins.` : 'Plan to reach early.'}</li>
        <li>Visit or map the centre address a day ahead if possible, and confirm the route, travel time and local transport timings.</li>
        <li>Pack the documents listed above ({pr.admitCard.carry.length} items for {n}) in one folder, with the printed admit card on top.</li>
        <li>Read the instructions on the admit card about prohibited items, dress rules and biometric or photo checks, and follow them exactly.</li>
        <li>After the exam, keep the admit card until the final result. It is required again at later stages and for any query to the board.</li>
      </ul>
    </section>
  );
}
