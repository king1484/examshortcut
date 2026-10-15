import Link from 'next/link';
import { Md } from '@/components/Md';
import { SECTION_META, getCutoffs, getExam, getWeightage } from '@/lib/content';
import { plain } from '@/components/exam-subpages/common';
import { RelatedCards, StagesTable, peerCards, relatedFor, show } from './ExamDepth';

/* eslint-disable @typescript-eslint/no-explicit-any */
/* Server-rendered depth for the SSC CGL cutoff pages (index, per-year, final merit, expected 2026).
   Every number is computed from content/exams/ssc-cgl/{cutoffs,exam,weightage}.json at build time. The
   guidance text is general advice that points back to the official SSC notice. Additive: these blocks sit
   below the existing tables. */

interface CutoffList { year: number; list: string; maxMarks: number; cutoffs: Record<string, number> }

const MAIN_LIST = 'all posts except AAO/JSO';
const CAT_ORDER = ['UR', 'EWS', 'OBC', 'SC', 'ST'];
const cats = (c: Record<string, number>) => [...CAT_ORDER.filter((k) => k in c), ...Object.keys(c).filter((k) => !CAT_ORDER.includes(k))];
const signed = (n: number) => (n > 0 ? '+' : n < 0 ? '−' : '') + show(Math.abs(n));
const pct = (n: number, of: number) => `${show((n / of) * 100)} percent`;

function load() {
  const d = getCutoffs('ssc-cgl') as any;
  const tier1 = ((d?.tier1 ?? []) as CutoffList[]).filter((l) => l.cutoffs);
  const final = ((d?.final ?? []) as CutoffList[]).filter((l) => l.cutoffs);
  const main = tier1.filter((l) => l.list.includes(MAIN_LIST)).sort((a, b) => a.year - b.year);
  return { tier1, final, main };
}

/** Marks per correct and per wrong answer, read from the stage record (marks / questions, and the negative-marking line). */
function marking(stageId: string) {
  const exam = getExam('ssc-cgl');
  const s = (exam?.stages ?? []).find((x: any) => x.id === stageId);
  const plus = s?.totalQuestions && s?.totalMarks ? s.totalMarks / s.totalQuestions : 2;
  const m = String(s?.negative ?? '').match(/[−-]\s*([\d.]+)/);
  const minus = m ? Number(m[1]) : 0.5;
  return { plus, minus, questions: (s?.totalQuestions ?? 100) as number, marks: (s?.totalMarks ?? 200) as number, stage: s };
}

/** Raw marks reached with `a` attempts at accuracy `acc`. */
const rawMarks = (a: number, acc: number, plus: number, minus: number) => a * acc * plus - a * (1 - acc) * minus;
/** Attempts needed at a given accuracy to reach `target` raw marks. */
const attemptsFor = (target: number, acc: number, plus: number, minus: number) => Math.ceil(target / (acc * plus - (1 - acc) * minus));

const listTag = (l: CutoffList) => (l.list.includes(MAIN_LIST) ? 'Main list' : l.list.match(/—\s*([A-Za-z]+)/)?.[1] ?? 'Premier list');
const timelineFor = (year: number) => ((getExam('ssc-cgl')?.timeline ?? []) as any[]).find((t) => t.year === year);

// ------------------------------------------------------------------ shared blocks
function AttemptsTable({ target, label }: { target: number; label: string }) {
  const { plus, minus, questions } = marking('tier1');
  const accs = [1, 0.95, 0.9, 0.85, 0.8];
  const attempts = [60, 70, 80, 90, 100].filter((a) => a <= questions);
  return (
    <>
      <p className="text-sm muted mt-2 max-w-3xl">
        Tier 1 gives +{show(plus)} for a correct answer and −{show(minus)} for a wrong one, out of {questions} questions. The table shows the raw marks you reach for a number of attempts at a given accuracy. Cells at or above {label} ({show(target)}) are in bold. These are raw marks before normalisation, so use them to plan your attempts, not to predict a final score.
      </p>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>Attempts</th>{accs.map((a) => <th key={a} className="text-right">{show(a * 100)}% accuracy</th>)}</tr></thead>
          <tbody>
            {attempts.map((n) => (
              <tr key={n}>
                <td className="font-semibold">{n}</td>
                {accs.map((a) => {
                  const v = rawMarks(n, a, plus, minus);
                  return <td key={a} className={`text-right ${v >= target ? 'font-bold' : ''}`}>{show(v)}</td>;
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="text-sm muted mt-3 max-w-3xl">
        Read across a row to see what accuracy costs you. For example, to reach {show(target)} you need at least {attemptsFor(target, 1, plus, minus)} attempts even if every answer is right, {attemptsFor(target, 0.9, plus, minus)} attempts at 90 percent accuracy and {attemptsFor(target, 0.85, plus, minus)} attempts at 85 percent accuracy. Each wrong answer removes {show(plus + minus)} marks compared with getting it right, so guessing blindly is rarely worth it.
      </p>
    </>
  );
}

function Floors({ latest }: { latest: CutoffList }) {
  const { marks } = marking('tier1');
  const floors: [string, string, number][] = [['UR', 'UR', 0.3], ['OBC / EWS', 'OBC', 0.25], ['SC / ST / others', 'SC', 0.2]];
  return (
    <>
      <p className="text-sm muted mt-2 max-w-3xl">
        Our cutoff data records the minimum qualifying marks for Tier 1 as 30 percent for UR, 25 percent for OBC and EWS, and 20 percent for SC, ST and others. These floors only make you eligible to be considered. The cutoffs actually declared sit far above them, as the table shows for the {latest.year} main list.
      </p>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead><tr><th>Group</th><th className="text-right">Floor</th><th className="text-right">Floor in marks (of {marks})</th><th className="text-right">{latest.year} cutoff</th><th className="text-right">Cutoff above floor</th></tr></thead>
          <tbody>
            {floors.map(([label, key, f]) => {
              const floor = marks * f;
              const c = latest.cutoffs[key];
              return (
                <tr key={label}>
                  <td className="font-semibold">{label}</td>
                  <td className="text-right">{show(f * 100)}%</td>
                  <td className="text-right">{show(floor)}</td>
                  <td className="text-right">{c != null ? show(c) : '—'}</td>
                  <td className="text-right font-bold">{c != null ? `${signed(c - floor)} marks` : '—'}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </>
  );
}

function CategoryGuide({ list }: { list: CutoffList }) {
  const c = list.cutoffs;
  const ur = c.UR;
  const line = (k: string) => (k in c && k !== 'UR' && ur != null ? `${show(c[k])}, which is ${show(Math.abs(ur - c[k]))} marks ${c[k] <= ur ? 'below' : 'above'} UR` : null);
  const text: Record<string, string> = {
    UR: 'The open-merit line. It is the highest figure in most years and the one most coaching comparisons quote, but it is only the right target if you are in the unreserved group.',
    EWS: 'Declared separately from OBC and the figure can sit above or below the OBC line in a given year, so look at your own certificate category and not at the order of the rows.',
    OBC: 'The OBC line depends on the central OBC (non-creamy layer) list. If your certificate is not in the central format, the category can be changed at verification, so check the certificate rules in the notice well before the result.',
    SC: 'The SC line is declared on its own merit list. A comfortable margin over it matters less than clearing it with Tier 2 in mind, because Tier 1 only screens.',
    ST: 'The ST line is usually the lowest of the five in our data. It is still a normalised score, so a raw score a few marks below it can still clear and a raw score a few marks above it can still miss.',
  };
  return (
    <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9 max-w-3xl">
      {cats(c).map((k) => (
        <li key={k}><b>{k}:</b> {text[k] ?? 'Declared as its own line in the result notice.'} {k !== 'UR' && line(k) ? `In ${list.year} the figure was ${line(k)}.` : k === 'UR' ? `In ${list.year} it was ${show(c[k])} out of ${list.maxMarks}, which is ${pct(c[k], list.maxMarks)} of the maximum.` : ''}</li>
      ))}
    </ul>
  );
}

function CrossYearTable({ rows, highlight }: { rows: CutoffList[]; highlight?: number }) {
  const all = [...new Set(rows.flatMap((r) => cats(r.cutoffs)))];
  return (
    <div className="tbl-wrap mt-3">
      <table className="tbl">
        <thead>
          <tr>
            <th>Category</th>
            {rows.map((r) => <th key={r.year} className="text-right">{r.year}{highlight === r.year ? ' (this page)' : ''}</th>)}
            {rows.slice(1).map((r, i) => <th key={`d${r.year}`} className="text-right">{r.year} vs {rows[i].year}</th>)}
            <th className="text-right">Low – high</th>
          </tr>
        </thead>
        <tbody>
          {all.map((k) => {
            const vals = rows.map((r) => r.cutoffs[k]).filter((v) => v != null);
            return (
              <tr key={k}>
                <td className="font-semibold">{k}</td>
                {rows.map((r) => <td key={r.year} className={`text-right ${highlight === r.year ? 'font-bold' : ''}`}>{r.cutoffs[k] != null ? show(r.cutoffs[k]) : '—'}</td>)}
                {rows.slice(1).map((r, i) => {
                  const a = rows[i].cutoffs[k], b = r.cutoffs[k];
                  return <td key={`d${r.year}`} className="text-right">{a != null && b != null ? signed(b - a) : '—'}</td>;
                })}
                <td className="text-right">{vals.length ? `${show(Math.min(...vals))} – ${show(Math.max(...vals))}` : '—'}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

function TrendBullets({ rows }: { rows: CutoffList[] }) {
  if (rows.length < 2) return null;
  const first = rows[0], last = rows[rows.length - 1];
  const bullets: string[] = [];
  const ur = rows.map((r) => ({ y: r.year, v: r.cutoffs.UR })).filter((x) => x.v != null);
  if (ur.length >= 2) {
    const hi = ur.reduce((a, b) => (b.v > a.v ? b : a)), lo = ur.reduce((a, b) => (b.v < a.v ? b : a));
    bullets.push(`The UR line moved from ${show(first.cutoffs.UR)} in ${first.year} to ${show(last.cutoffs.UR)} in ${last.year}. The highest UR figure in this window is ${show(hi.v)} (${hi.y}) and the lowest is ${show(lo.v)} (${lo.y}), a spread of ${show(hi.v - lo.v)} marks within three cycles.`);
  }
  const cs = cats(last.cutoffs).filter((k) => first.cutoffs[k] != null && last.cutoffs[k] != null);
  if (cs.length) {
    const moves = cs.map((k) => ({ k, d: last.cutoffs[k] - first.cutoffs[k] }));
    const big = moves.reduce((a, b) => (Math.abs(b.d) > Math.abs(a.d) ? b : a));
    const small = moves.reduce((a, b) => (Math.abs(b.d) < Math.abs(a.d) ? b : a));
    bullets.push(`Between ${first.year} and ${last.year} the largest change was in ${big.k} (${signed(big.d)} marks) and the smallest in ${small.k} (${signed(small.d)} marks). Categories do not move together, so a fall in the UR line does not mean every line fell by the same amount.`);
  }
  const spreads = rows.filter((r) => r.cutoffs.UR != null && r.cutoffs.ST != null).map((r) => `${r.year}: ${show(r.cutoffs.UR - r.cutoffs.ST)}`);
  if (spreads.length) bullets.push(`The gap between the UR and ST lines (marks) was ${spreads.join(', ')}. A reserved-category target is not simply the UR target minus a fixed amount.`);
  const order = rows.filter((r) => r.cutoffs.OBC != null && r.cutoffs.EWS != null).map((r) => `${r.year}: ${r.cutoffs.OBC > r.cutoffs.EWS ? 'OBC above EWS' : r.cutoffs.OBC < r.cutoffs.EWS ? 'EWS above OBC' : 'OBC equal to EWS'} by ${show(Math.abs(r.cutoffs.OBC - r.cutoffs.EWS))}`);
  if (order.length) bullets.push(`The OBC and EWS lines swapped order across these cycles (${order.join('; ')}), which shows that the order of reserved lines is not fixed.`);
  return (
    <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9 max-w-3xl">
      {bullets.map((b, i) => <li key={i}>{b}</li>)}
    </ul>
  );
}

function Normalisation() {
  const exam = getExam('ssc-cgl');
  const tier1 = (exam?.stages ?? []).find((s: any) => s.id === 'tier1');
  return (
    <section className="mt-10" aria-labelledby="cd-norm">
      <h2 id="cd-norm" className="text-2xl font-extrabold">Normalisation and sectional cutoffs</h2>
      {exam?.normalization && <Md className="card p-5 mt-3 text-sm max-w-3xl">{String(exam.normalization)}</Md>}
      {tier1?.notes && <Md className="text-sm muted mt-3 max-w-3xl">{String(tier1.notes)}</Md>}
      <p className="text-sm muted mt-3 max-w-3xl">
        In plain terms, the number you see on your response sheet is a raw score, and the number SSC compares is a normalised score. Two candidates with the same raw score in different shifts can end up with different normalised scores. This is why a cutoff quoted in marks cannot be matched to your raw score one to one, and why mock scores should be read as ranges.
      </p>
    </section>
  );
}

// ------------------------------------------------------------------ index page
export function CglCutoffIndexDepth() {
  const { final, main, tier1 } = load();
  if (!main.length) return null;
  const latest = main[main.length - 1];
  const exam = getExam('ssc-cgl');
  const wt = getWeightage('ssc-cgl');
  const good = wt?.analysis?.goodAttempts as Record<string, string> | undefined;
  const premier = tier1.filter((l) => !l.list.includes(MAIN_LIST));
  const mainBy = (y: number) => main.find((m) => m.year === y);
  return (
    <div className="mt-12">
      <section aria-labelledby="cd-trend">
        <h2 id="cd-trend" className="text-2xl font-extrabold">Tier 1 cutoff trend, {main[0].year} to {latest.year}</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          The table puts the main post list (all posts except AAO and JSO) for {main.map((m) => m.year).join(', ')} side by side, out of {latest.maxMarks} marks after normalisation. The change columns show how each category moved from one cycle to the next, so you can see which direction the line is heading rather than relying on a single year.
        </p>
        <CrossYearTable rows={main} />
        <TrendBullets rows={main} />
      </section>

      <section className="mt-10" aria-labelledby="cd-read">
        <h2 id="cd-read" className="text-2xl font-extrabold">How to read these numbers</h2>
        <div className="max-w-3xl text-sm space-y-3 mt-3">
          <p>
            <b>A cutoff is a result, not a rule.</b> SSC does not fix a pass mark in advance. After the exam it ranks normalised scores within each category and each post list, and the last score that gets a Tier 2 call becomes that list’s cutoff. That is why every cycle has a different number and why the same cycle has many numbers.
          </p>
          <p>
            <b>Lists matter.</b> Our data shows the largest, most quoted list for each year, which covers all posts except AAO and JSO, plus the AAO and JSO lists for the one cycle where we have them. If your preference is a post with its own list, the main-list figure is a baseline, not your number. {premier.length > 0 && premier[0] ? `For ${premier[0].year}, the premier-post lists are higher than the main list, as the next table shows.` : ''}
          </p>
          <p>
            <b>Tier 1 only screens.</b> The exam record for CGL says Tier 1 is a qualifying-in stage that shortlists for Tier 2 and that its marks do not carry into final merit. The merit list is drawn from Tier 2 Paper 1. So the right question is not how high your Tier 1 score was but whether it was safely above the line for your category and list.
          </p>
        </div>
        <StagesTable id="ssc-cgl" caption="Stages of SSC CGL, from the exam record" />
      </section>

      {premier.length > 0 && (
        <section className="mt-10" aria-labelledby="cd-premier">
          <h2 id="cd-premier" className="text-2xl font-extrabold">Premier-post lists compared with the main list</h2>
          <p className="text-sm muted mt-2 max-w-3xl">Some posts are shortlisted from their own, higher lists. The table compares those lists with the main list of the same year, category by category.</p>
          {(() => {
            const y = premier[0].year;
            const base = mainBy(y);
            if (!base) return null;
            const lists = [base, ...premier.filter((p) => p.year === y)];
            const all = cats(base.cutoffs);
            return (
              <div className="tbl-wrap mt-3">
                <table className="tbl">
                  <thead><tr><th>Category</th>{lists.map((l) => <th key={l.list} className="text-right">{listTag(l)}</th>)}{lists.slice(1).map((l) => <th key={`d${l.list}`} className="text-right">{listTag(l)} vs main</th>)}</tr></thead>
                  <tbody>
                    {all.map((k) => (
                      <tr key={k}>
                        <td className="font-semibold">{k}</td>
                        {lists.map((l) => <td key={l.list} className="text-right">{l.cutoffs[k] != null ? show(l.cutoffs[k]) : '—'}</td>)}
                        {lists.slice(1).map((l) => <td key={`d${l.list}`} className="text-right">{l.cutoffs[k] != null && base.cutoffs[k] != null ? signed(l.cutoffs[k] - base.cutoffs[k]) : '—'}</td>)}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            );
          })()}
          <p className="text-xs faint mt-2">Premier lists: {premier.map((p) => `${p.year} ${p.list.replace(/^Tier 1 → Tier 2\s*—?\s*/, '')}`).join('; ')}.</p>
        </section>
      )}

      <section className="mt-10" aria-labelledby="cd-floor">
        <h2 id="cd-floor" className="text-2xl font-extrabold">Qualifying floor versus cutoff</h2>
        <Floors latest={latest} />
      </section>

      <Normalisation />

      <section className="mt-10" aria-labelledby="cd-cat">
        <h2 id="cd-cat" className="text-2xl font-extrabold">Category-wise reading guide</h2>
        <p className="text-sm muted mt-2 max-w-3xl">Each category has its own line. This is how to think about yours, using the {latest.year} main list.</p>
        <CategoryGuide list={latest} />
      </section>

      <section className="mt-10" aria-labelledby="cd-safe">
        <h2 id="cd-safe" className="text-2xl font-extrabold">Safe score versus cutoff</h2>
        <div className="max-w-3xl text-sm space-y-3 mt-3">
          <p>
            Because the line moves every year, a score exactly at last year’s cutoff is not safe. A practical way to set a target is to take the highest figure for your category across the cycles in the table above, which is {show(Math.max(...main.map((m) => m.cutoffs.UR).filter((v) => v != null)))} for UR in this data, and aim to score above it consistently in mocks taken at exam timing. Mock scores are raw scores, so a margin is more important than the exact number.
          </p>
          {good && Object.keys(good).length > 0 && (
            <p>
              Shift analyses compiled on this site describe what a good attempt looked like: {Object.entries(good).sort(([a], [b]) => a.localeCompare(b)).map(([y, v]) => `${y} — ${plain(v)}`).join('; ')}. They are compiled from candidate memory-based papers, so treat them as indicative. Our <Link className="underline" href="/exams/ssc-cgl/weightage/">weightage page</Link> shows the per-shift topic counts behind them.
            </p>
          )}
        </div>
        <AttemptsTable target={Math.max(...main.map((m) => m.cutoffs.UR).filter((v) => v != null))} label="the highest UR cutoff in the trend table" />
      </section>

      {final.length > 0 && (
        <section className="mt-10" aria-labelledby="cd-final">
          <h2 id="cd-final" className="text-2xl font-extrabold">From Tier 1 to the final merit list</h2>
          <div className="max-w-3xl text-sm space-y-3 mt-3">
            <p>
              The final lists in our data are out of {final[0].maxMarks} marks and belong to Tier 2 Paper 1, not Tier 1. For {final[0].year} they show UR at {final.map((f) => `${show(f.cutoffs.UR)} for ${plain(f.list).replace(/^Final merit —\s*/, '').replace(/\s*\(.*$/, '')}`).join(' and ')}. That is a different exam with a different scale, so none of the Tier 1 numbers above are comparable to it. Read the <Link className="underline" href="/exams/ssc-cgl/cutoffs/final-merit/">final merit cutoff page</Link> for the post-wise breakdown.
            </p>
            {exam?.selectionProcess && <Md className="card p-5">{String(exam.selectionProcess)}</Md>}
          </div>
        </section>
      )}

      <section className="mt-10" aria-labelledby="cd-use">
        <h2 id="cd-use" className="text-2xl font-extrabold">How to use cutoffs in your preparation</h2>
        <ol className="card p-5 mt-3 text-sm space-y-2 list-decimal pl-9 max-w-3xl">
          <li>Find your category line in the trend table and note the highest value, not only the latest.</li>
          <li>Convert that target into attempts and accuracy using the table above, then check whether your mock accuracy can support it.</li>
          <li>Take full-length mocks at exam timing and record attempts, accuracy and score, not just the score. A rising score with falling accuracy is a warning.</li>
          <li>Use the <Link className="underline" href="/exams/ssc-cgl/score-calculator/">score calculator</Link> and <Link className="underline" href="/exams/ssc-cgl/rank-estimator/">rank estimator</Link> to place a mock result against the lines, and remember that they work on raw numbers.</li>
          <li>Keep Tier 2 in view from the start. The topics behind Geometry, Algebra, Cloze Test and Comprehension decide Tier 1 and Tier 2 alike, so see the <Link className="underline" href="/exams/ssc-cgl/guides/tier-2-strategy/">Tier 2 strategy guide</Link>.</li>
        </ol>
      </section>

      <RelatedCards id="cd-related" heading="More on SSC CGL" cards={relatedFor('ssc-cgl', ['cutoffs'])} />
      <RelatedCards id="cd-peers" heading="Compare with similar exams" cards={peerCards('ssc-cgl', 'cutoffs', 4)} />
    </div>
  );
}

// ------------------------------------------------------------------ per-year pages
export function CglYearDepth({ year }: { year: number }) {
  const { main, tier1 } = load();
  const here = main.find((m) => m.year === year);
  if (!here) return null;
  const { plus, minus, marks } = marking('tier1');
  const tl = timelineFor(year);
  const wt = getWeightage('ssc-cgl');
  const diff = wt?.analysis?.difficulty?.[String(year)] as Record<string, string> | undefined;
  const good = wt?.analysis?.goodAttempts?.[String(year)] as string | undefined;
  const sorted = [...main].sort((a, b) => b.cutoffs.UR - a.cutoffs.UR);
  const rank = sorted.findIndex((m) => m.year === year) + 1;
  const prev = [...main].reverse().find((m) => m.year < year);
  const others = main.filter((m) => m.year !== year);
  const otherLists = tier1.filter((l) => l.year === year && !l.list.includes(MAIN_LIST));
  const cs = cats(here.cutoffs);
  const ordinal = ['highest', 'middle', 'lowest'];
  return (
    <div className="mt-12">
      <section aria-labelledby="yd-compare">
        <h2 id="yd-compare" className="text-2xl font-extrabold">How the {year} cutoff compares with other cycles</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          The table shows the main list for every cycle in our data, with {year} in bold. UR in {year} was {show(here.cutoffs.UR)}, which ranks {rank} of {main.length} cycles by UR ({main.length === 3 ? ordinal[rank - 1] : `rank ${rank}`}).
          {prev ? ` Compared with ${prev.year}, the UR line changed by ${signed(here.cutoffs.UR - prev.cutoffs.UR)} marks.` : ' It is the earliest cycle in our data, so there is no earlier cycle to compare with.'}
          {others.length ? ` Across the other cycles the UR line ranged from ${show(Math.min(...others.map((o) => o.cutoffs.UR)))} to ${show(Math.max(...others.map((o) => o.cutoffs.UR)))}.` : ''}
        </p>
        <CrossYearTable rows={main} highlight={year} />
        <TrendBullets rows={main} />
      </section>

      <section className="mt-10" aria-labelledby="yd-cycle">
        <h2 id="yd-cycle" className="text-2xl font-extrabold">The {year} cycle in our records</h2>
        {tl ? (
          <ul className="card p-5 mt-3 text-sm space-y-1.5 list-disc pl-9 max-w-3xl">
            {tl.vacancies != null && <li><b>Vacancies recorded:</b> {Number(tl.vacancies).toLocaleString('en-IN')}. The number of posts is one of the factors that decides how many candidates are called for Tier 2, but it does not move the cutoff in a fixed way.</li>}
            {tl.notification && <li><b>Notification:</b> {plain(tl.notification)}</li>}
            {tl.tier1 && <li><b>Tier 1 window:</b> {plain(tl.tier1)}</li>}
            {tl.tier2 && <li><b>Tier 2:</b> {plain(tl.tier2)}</li>}
            {tl.finalResult && <li><b>Final result:</b> {plain(tl.finalResult)}</li>}
          </ul>
        ) : <p className="text-sm muted mt-2 max-w-3xl">The timeline for this cycle is not recorded in our exam data, so only the cutoff figures are shown on this page.</p>}
        {diff && (
          <>
            <p className="text-sm muted mt-4 max-w-3xl">Shift analyses compiled on this site rate the difficulty of each section for {year} as follows. They are compiled from candidate recollections, so use them as a rough guide to why the line moved.</p>
            <div className="tbl-wrap mt-3">
              <table className="tbl">
                <thead><tr><th>Section</th><th>Reported difficulty</th></tr></thead>
                <tbody>
                  {Object.entries(diff).map(([sid, d]) => (
                    <tr key={sid}><td className="font-semibold">{(SECTION_META as any)[sid]?.name ?? sid}</td><td>{plain(d)}</td></tr>
                  ))}
                </tbody>
              </table>
            </div>
            {good && <p className="text-sm muted mt-3 max-w-3xl">A good attempt in {year} was described as: {plain(good)}.</p>}
          </>
        )}
      </section>

      <section className="mt-10" aria-labelledby="yd-cat">
        <h2 id="yd-cat" className="text-2xl font-extrabold">Category-wise reading guide for {year}</h2>
        <p className="text-sm muted mt-2 max-w-3xl">Each category is ranked in its own list. This is how to read your line.</p>
        <CategoryGuide list={here} />
      </section>

      <section className="mt-10" aria-labelledby="yd-attempts">
        <h2 id="yd-attempts" className="text-2xl font-extrabold">What the {year} lines mean in attempts</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          With +{show(plus)} for a correct answer and −{show(minus)} for a wrong one, a cutoff can be turned into the number of questions you must attempt. The table shows the attempts needed for each category at three accuracy levels. The numbers are raw marks before normalisation, so add a margin.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Category</th><th className="text-right">Cutoff</th><th className="text-right">Share of {marks}</th><th className="text-right">Attempts at 100%</th><th className="text-right">At 90%</th><th className="text-right">At 85%</th><th className="text-right">At 80%</th></tr></thead>
            <tbody>
              {cs.map((k) => {
                const v = here.cutoffs[k];
                return (
                  <tr key={k}>
                    <td className="font-semibold">{k}</td>
                    <td className="text-right font-bold">{show(v)}</td>
                    <td className="text-right">{pct(v, here.maxMarks)}</td>
                    {[1, 0.9, 0.85, 0.8].map((a) => <td key={a} className="text-right">{attemptsFor(v, a, plus, minus)}</td>)}
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
        <p className="text-sm muted mt-3 max-w-3xl">Tier 1 has 100 questions, so any figure above 100 attempts in the table means that accuracy level cannot reach that line on its own. In that case you need higher accuracy.</p>
      </section>

      <section className="mt-10" aria-labelledby="yd-floor">
        <h2 id="yd-floor" className="text-2xl font-extrabold">Qualifying floor versus the {year} cutoff</h2>
        <Floors latest={here} />
      </section>

      <Normalisation />

      <section className="mt-10" aria-labelledby="yd-limits">
        <h2 id="yd-limits" className="text-2xl font-extrabold">What this page does not tell you</h2>
        <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9 max-w-3xl">
          <li>It shows the main post list{otherLists.length ? ` and ${otherLists.length} premier list${otherLists.length > 1 ? 's' : ''} for ${year}` : ''}. Other post lists have their own lines in the SSC result notice.</li>
          <li>It shows normalised Tier 1 marks. Your final merit position comes from Tier 2 Paper 1, so a Tier 1 score above the line does not rank you for the final list.</li>
          <li>Decimals can differ slightly between reproductions of the SSC notice. The official PDF is the final word.</li>
          <li>Cutoffs describe the past. They cannot tell you where the next line will fall, which is why the <Link className="underline" href="/exams/ssc-cgl/cutoffs/expected-2026/">expected 2026 band</Link> is presented as an estimate.</li>
        </ul>
      </section>

      <RelatedCards id="yd-related" heading="Keep going" cards={relatedFor('ssc-cgl', ['cutoffs'])} />
    </div>
  );
}

// ------------------------------------------------------------------ final merit page
export function CglFinalDepth() {
  const { final, main } = load();
  if (!final.length) return null;
  const exam = getExam('ssc-cgl');
  const t2 = (exam?.stages ?? []).find((s: any) => s.id === 'tier2');
  const { plus, minus } = marking('tier2');
  const secs: any[] = t2?.sections ?? [];
  const merit = secs.filter((s) => !/qualifying/i.test(String(s.name)));
  const meritQ = merit.reduce((a, s) => a + (s.questions ?? 0), 0);
  const meritM = merit.reduce((a, s) => a + (s.marks ?? 0), 0);
  const maxMarks = final[0].maxMarks;
  const latestT1 = main[main.length - 1];
  return (
    <div className="mt-12">
      <section aria-labelledby="fd-posts">
        <h2 id="fd-posts" className="text-2xl font-extrabold">What the final merit figures mean</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          The lists below are out of {maxMarks} marks and come from Tier 2 Paper 1. The table converts each figure into a share of the maximum and into the minimum number of correct answers it implies, assuming no wrong answers. Paper 1 gives +{show(plus)} for a correct answer and −{show(minus)} for a wrong one, so every wrong answer costs {show(plus + minus)} marks relative to a right one and a real attempt needs more correct answers than the minimum shown.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>List</th><th>Category</th><th className="text-right">Cutoff</th><th className="text-right">Share of {maxMarks}</th><th className="text-right">Min. correct of {meritQ || '—'}</th><th className="text-right">Below UR</th></tr></thead>
            <tbody>
              {final.flatMap((l) => cats(l.cutoffs).map((k) => (
                <tr key={`${l.list}-${k}`}>
                  <td className="text-sm">{plain(l.list).replace(/^Final merit —\s*/, '').replace(/\s*\(.*$/, '')}</td>
                  <td className="font-semibold">{k}</td>
                  <td className="text-right font-bold">{show(l.cutoffs[k])}</td>
                  <td className="text-right">{pct(l.cutoffs[k], l.maxMarks)}</td>
                  <td className="text-right">{Math.ceil(l.cutoffs[k] / plus)}</td>
                  <td className="text-right">{k === 'UR' ? '—' : show(l.cutoffs.UR - l.cutoffs[k])}</td>
                </tr>
              )))}
            </tbody>
          </table>
        </div>
        {final.length > 1 && (
          <p className="text-sm muted mt-3 max-w-3xl">
            Comparing the two lists, the {plain(final[0].list).replace(/^Final merit —\s*/, '').replace(/\s*\(.*$/, '')} UR line was {show(Math.abs(final[0].cutoffs.UR - final[1].cutoffs.UR))} marks {final[0].cutoffs.UR >= final[1].cutoffs.UR ? 'above' : 'below'} the {plain(final[1].list).replace(/^Final merit —\s*/, '').replace(/\s*\(.*$/, '')} UR line. Posts are ranked on their own lists, so the line for the post you want is the one to chase.
          </p>
        )}
      </section>

      {secs.length > 0 && (
        <section className="mt-10" aria-labelledby="fd-struct">
          <h2 id="fd-struct" className="text-2xl font-extrabold">How the {maxMarks} marks are built</h2>
          <p className="text-sm muted mt-2 max-w-3xl">
            Tier 2 Paper 1 has {t2?.totalQuestions} questions over {t2?.durationMin} minutes in two sessions. The merit questions are the first four modules, which carry {meritQ} questions and {meritM} marks. The Computer Knowledge module is qualifying only, and the data entry speed test is qualifying too. Our exam record states that merit is drawn from Paper 1 out of {maxMarks} marks.
          </p>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Module</th><th className="text-right">Questions</th><th className="text-right">Marks</th><th className="text-right">Share of merit marks</th><th>Counts for merit</th></tr></thead>
              <tbody>
                {secs.map((s) => {
                  const q = !/qualifying/i.test(String(s.name));
                  return (
                    <tr key={s.name}>
                      <td className="text-sm">{plain(s.name)}</td>
                      <td className="text-right">{s.questions}</td>
                      <td className="text-right">{s.marks}</td>
                      <td className="text-right">{q && meritM ? pct(s.marks, meritM) : '—'}</td>
                      <td>{q ? 'Yes' : 'Qualifying only'}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
          {t2?.notes && <Md className="text-sm muted mt-3 max-w-3xl">{String(t2.notes)}</Md>}
          <p className="text-sm muted mt-3 max-w-3xl">
            The module sizes show where Tier 2 effort pays off most: the English module is the heaviest, and Mathematical Abilities and Reasoning follow. The record also notes that section-wise qualifying minimums apply in Paper 1, so a lopsided score can fail even if the total looks high. The notice states the exact minimums.
          </p>
        </section>
      )}

      <section className="mt-10" aria-labelledby="fd-t1">
        <h2 id="fd-t1" className="text-2xl font-extrabold">How Tier 1 and the final list relate</h2>
        <div className="max-w-3xl text-sm space-y-3 mt-3">
          <p>
            Tier 1 only decides who is called for Tier 2. The latest Tier 1 main-list UR line in our data is {show(latestT1.cutoffs.UR)} out of {latestT1.maxMarks} ({latestT1.year}), while the final lists above are out of {maxMarks}. They are different exams on different scales, so a Tier 1 score cannot be converted into a final merit score. See the <Link className="underline" href="/exams/ssc-cgl/cutoffs/">Tier 1 cutoff explorer</Link> for the screening lines.
          </p>
          <p>
            Many aspirants stop at Tier 1 level preparation and lose ground in Tier 2. The topics that decide Tier 2 marks are the same syllabus taken deeper, with a larger share for English. Use the <Link className="underline" href="/exams/ssc-cgl/guides/tier-2-strategy/">Tier 2 strategy guide</Link> and the <Link className="underline" href="/exams/ssc-cgl/weightage/">weightage page</Link> to plan the extra months between the two tiers.
          </p>
        </div>
      </section>

      <section className="mt-10" aria-labelledby="fd-use">
        <h2 id="fd-use" className="text-2xl font-extrabold">How to use these figures</h2>
        <ol className="card p-5 mt-3 text-sm space-y-2 list-decimal pl-9 max-w-3xl">
          <li>Choose the post you actually want and read its list, not the average of both.</li>
          <li>Translate the line into correct answers and wrong-answer budget using the table, then check what that means for your accuracy on {meritQ || 'the'} merit questions.</li>
          <li>Practise in two blocks of timed modules, as in the real paper, and track the section-wise minimums, not only the total.</li>
          <li>Treat the printed numbers as past results. Normalisation and post preference change the line from one cycle to the next.</li>
        </ol>
      </section>

      <RelatedCards id="fd-related" heading="Keep going" cards={relatedFor('ssc-cgl', ['cutoffs'])} />
    </div>
  );
}

// ------------------------------------------------------------------ expected 2026
export function CglExpectedDepth() {
  const { main } = load();
  if (main.length < 2) return null;
  const latest = main[main.length - 1];
  const nextYear = getExam('ssc-cgl')?.latestCycle?.year ?? latest.year + 1;
  const all = cats(latest.cutoffs);
  const wt = getWeightage('ssc-cgl');
  const good = wt?.analysis?.goodAttempts as Record<string, string> | undefined;
  const timeline = (getExam('ssc-cgl')?.timeline ?? []) as any[];
  const stats = all.map((k) => {
    const v = main.map((m) => m.cutoffs[k]).filter((x) => x != null);
    return { k, lo: Math.min(...v), hi: Math.max(...v), mean: v.reduce((a, b) => a + b, 0) / v.length, last: latest.cutoffs[k] };
  });
  const urStat = stats.find((s) => s.k === 'UR') ?? stats[0];
  return (
    <div className="mt-12">
      <section aria-labelledby="ed-stats">
        <h2 id="ed-stats" className="text-2xl font-extrabold">The band in numbers</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          The band is built only from the {main.length} official cycles in our data ({main.map((m) => m.year).join(', ')}), so it reflects a small sample and is not a forecast. The table adds the average of the cycles and the width of the band, which tells you how much the line has moved for each category.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Category</th><th className="text-right">Low</th><th className="text-right">Average</th><th className="text-right">High</th><th className="text-right">Band width</th><th className="text-right">{latest.year} vs average</th></tr></thead>
            <tbody>
              {stats.map((s) => (
                <tr key={s.k}>
                  <td className="font-semibold">{s.k}</td>
                  <td className="text-right">{show(s.lo)}</td>
                  <td className="text-right">{show(s.mean)}</td>
                  <td className="text-right font-bold">{show(s.hi)}</td>
                  <td className="text-right">{show(s.hi - s.lo)}</td>
                  <td className="text-right">{signed(s.last - s.mean)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <TrendBullets rows={main} />
      </section>

      <section className="mt-10" aria-labelledby="ed-zones">
        <h2 id="ed-zones" className="text-2xl font-extrabold">What your mock score means for {nextYear}</h2>
        <p className="text-sm muted mt-2 max-w-3xl">Use the UR band as a worked example; for any other category read your own row above. These zones are a planning aid for raw mock scores, not a promise about the {nextYear} result.</p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Mock score (UR example)</th><th>Zone</th><th>What to do</th></tr></thead>
            <tbody>
              <tr><td className="whitespace-nowrap">Below {show(urStat.lo)}</td><td className="font-semibold">Under the band</td><td className="text-sm">Below every cutoff in the sample. Fix accuracy first, then speed, and do not rely on the paper being easy.</td></tr>
              <tr><td className="whitespace-nowrap">{show(urStat.lo)} to {show(urStat.mean)}</td><td className="font-semibold">Lower half</td><td className="text-sm">Clears the lowest cycle in the sample but not the average. A harder cycle might let you through; a standard one probably will not.</td></tr>
              <tr><td className="whitespace-nowrap">{show(urStat.mean)} to {show(urStat.hi)}</td><td className="font-semibold">Upper half</td><td className="text-sm">Above the average line but below the strictest cycle. Work on consistency so that one bad mock does not decide the outcome.</td></tr>
              <tr><td className="whitespace-nowrap">Above {show(urStat.hi)}</td><td className="font-semibold">Above the band</td><td className="text-sm">Higher than any line in the sample. Keep scoring there across several mocks and shift attention to Tier 2.</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <section className="mt-10" aria-labelledby="ed-attempts">
        <h2 id="ed-attempts" className="text-2xl font-extrabold">Turning the high end of the band into attempts</h2>
        <AttemptsTable target={urStat.hi} label="the high end of the UR band" />
        {good && Object.keys(good).length > 0 && (
          <p className="text-sm muted mt-3 max-w-3xl">
            For comparison, compiled shift analyses describe a good Tier 1 attempt as {Object.entries(good).sort(([a], [b]) => a.localeCompare(b)).map(([y, v]) => `${plain(v).replace(/^Tier 1:\s*/, '')} (${y})`).join(' and ')}.
          </p>
        )}
      </section>

      <section className="mt-10" aria-labelledby="ed-vac">
        <h2 id="ed-vac" className="text-2xl font-extrabold">Vacancies and the cutoff, side by side</h2>
        <p className="text-sm muted mt-2 max-w-3xl">The table shows the vacancy figure recorded in our exam data next to the main-list UR line for each cycle. It is there for context only. Four or five data points cannot establish a rule, and other factors such as difficulty and the size of the candidate pool also act on the line.</p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Cycle</th><th className="text-right">Vacancies recorded</th><th className="text-right">Main-list UR cutoff</th><th>Tier 1 window</th></tr></thead>
            <tbody>
              {[...timeline].filter((t) => t.year >= main[0].year).sort((a, b) => a.year - b.year).map((t) => {
                const row = main.find((m) => m.year === t.year);
                return (
                  <tr key={t.year}>
                    <td className="font-semibold">{t.year}</td>
                    <td className="text-right">{t.vacancies != null ? Number(t.vacancies).toLocaleString('en-IN') : '—'}</td>
                    <td className="text-right">{row ? show(row.cutoffs.UR) : 'Not yet declared'}</td>
                    <td className="text-sm">{t.tier1 ? plain(t.tier1) : '—'}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </section>

      <Normalisation />

      <RelatedCards id="ed-related" heading="Keep going" cards={relatedFor('ssc-cgl', ['cutoffs'])} />
    </div>
  );
}
