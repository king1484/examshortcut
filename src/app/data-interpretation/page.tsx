import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getTopic, listMocks } from '@/lib/content';
import { LazyTex } from '@/components/LazyTex';
import { MathText } from '@/components/MathText';
import { BarGraph } from '@/components/di/BarGraph';
import { LineGraph } from '@/components/di/LineGraph';
import { PieGraph } from '@/components/di/PieGraph';
import { CasletTable } from '@/components/di/CasletTable';

export const dynamic = 'force-static';

const PAGE_URL = 'https://examshortcut.in/data-interpretation/';
const BASE = '/quant/data-interpretation';

export function generateMetadata(): Metadata {
  const t = getTopic('quant', 'data-interpretation');
  const nF = t?.subtopics.reduce((n, s) => n + (s.formulas?.length ?? 0), 0) ?? 0;
  return {
    title: 'Data interpretation formulas & tricks for SSC CGL',
    description: `Data interpretation (DI) for SSC CGL: ${nF} formulas for tables, percentage change, pie charts, averages and growth, how to approach bar, line, pie and caselet sets, common traps and time-saving calculation tricks.`,
    alternates: { canonical: '/data-interpretation/' },
  };
}

/* Standard reciprocals worth knowing cold; all exact or rounded to two decimals. */
const RECIPROCALS: [string, string][] = [
  ['1/2', '50%'], ['1/3', '33.33%'], ['1/4', '25%'], ['1/5', '20%'], ['1/6', '16.67%'], ['1/7', '14.29%'],
  ['1/8', '12.5%'], ['1/9', '11.11%'], ['1/10', '10%'], ['1/11', '9.09%'], ['1/12', '8.33%'], ['1/16', '6.25%'],
];

export default function DataInterpretationPage() {
  const t = getTopic('quant', 'data-interpretation');
  if (!t) notFound();
  const mocks = listMocks().filter((m) => m.available);
  const q1 = t.avgQuestions?.tier1, q2 = t.avgQuestions?.tier2;
  const fSubs = t.subtopics.filter((s) => s.formulas?.length);
  const nFormulas = fSubs.reduce((n, s) => n + s.formulas!.length, 0);
  const tricks = t.subtopics.flatMap((s) => (s.tricks ?? []).map((k) => ({ s, k })));
  const patterns = t.subtopics.flatMap((s) => (s.patterns ?? []).map((p) => ({ s, p })));
  const traps = t.subtopics.map((s) => ({ s, items: (s.mistakes ?? []).slice(0, 2) })).filter((x) => x.items.length);

  const ld = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
      { '@type': 'ListItem', position: 2, name: 'Quantitative Aptitude', item: 'https://examshortcut.in/quant/' },
      { '@type': 'ListItem', position: 3, name: 'Data interpretation', item: PAGE_URL },
    ],
  };

  return (
    <div className="max-w-4xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />

      <p className="text-xs font-bold uppercase tracking-wide" style={{ color: 'var(--c-quant)' }}>Quant · Data interpretation</p>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-1">Data interpretation formulas &amp; tricks for SSC CGL</h1>
      <div className="flex gap-2 mt-3 flex-wrap text-sm">
        <span className="chip chip-brand">{nFormulas} formulas</span>
        <span className="chip">{tricks.length} tricks</span>
        <span className="chip">{t.practice?.length ?? 0} practice questions</span>
        {t.importance && <span className="chip">{t.importance} priority</span>}
      </div>

      <p className="mt-4 text-[15px] muted">
        Data interpretation (DI) means reading numbers off a table, bar graph, line graph or pie chart and answering a few
        questions about them. {t.summary}
        {q1 != null || q2 != null ? (
          <> Our topic notes put DI at about {q1 ?? '–'} question{q1 === 1 ? '' : 's'} in a Tier 1 paper and about {q2 ?? '–'} in Tier 2, so it is a smaller block than Percentage or Algebra, but it is among the most predictable.</>
        ) : null}
      </p>
      <p className="mt-3 text-[15px] muted">
        The good news is that DI needs very few formulas. Almost everything is a total, an average, a ratio, a percentage
        or a percentage change. What decides your score is reading the question carefully (which row, which year, which
        unit, percent of what) and keeping the arithmetic light. The sections below give you the formulas from our notes,
        a method for each chart type, the traps that cost marks, and the calculation habits that save time. Jump straight to
        what you need.
      </p>

      <nav aria-label="On this page" className="card p-3.5 mt-6 flex flex-wrap gap-2 items-center text-sm">
        <span className="font-bold">On this page:</span>
        <a href="#formulas" className="chip">Formulas</a>
        <a href="#approach" className="chip">How to approach each chart</a>
        <a href="#graphs" className="chip">Try the graphs</a>
        <a href="#tricks" className="chip">Time-saving tricks</a>
        <a href="#traps" className="chip">Common traps</a>
        <a href="#types" className="chip">Question types</a>
        <a href="#practice" className="chip">Practice</a>
      </nav>

      <section id="formulas" className="mt-10 scroll-mt-24">
        <h2 className="text-2xl font-extrabold">Data interpretation formulas</h2>
        <p className="text-sm muted mt-1 max-w-3xl">
          Grouped by the kind of question they answer. Each group links to its full subtopic page with notes, question
          types and practice.
        </p>
        {fSubs.map((s) => (
          <div key={s.id} className="mt-6">
            <div className="flex items-baseline justify-between gap-2 flex-wrap">
              <h3 className="font-extrabold text-lg">{s.title}</h3>
              <Link href={`${BASE}/learn/${s.id}/`} className="text-xs underline decoration-dotted">Full notes →</Link>
            </div>
            <p className="text-sm muted mt-0.5"><MathText text={s.concept} /></p>
            <div className="grid sm:grid-cols-2 gap-2.5 mt-2.5">
              {s.formulas!.map((f, i) => (
                <div key={i} className="card p-3.5">
                  <div className="text-sm font-bold">{f.name}</div>
                  <div className="my-1.5 overflow-x-auto overflow-y-hidden py-0.5"><LazyTex tex={f.tex} display /></div>
                  {f.note && <p className="text-xs muted">{f.note}</p>}
                </div>
              ))}
            </div>
          </div>
        ))}
        <p className="text-sm muted mt-5 max-w-3xl">
          Every percentage question reduces to <span className="font-semibold">part ÷ whole × 100</span> or{' '}
          <span className="font-semibold">change ÷ original × 100</span>. If you can name the part and the whole, or the
          change and the original, before you start computing, you will rarely pick the wrong formula.
        </p>
      </section>

      <section id="approach" className="mt-12 scroll-mt-24">
        <h2 className="text-2xl font-extrabold">How to approach each type of DI set</h2>
        <div className="grid gap-3 mt-3">
          <article className="card p-4">
            <h3 className="font-extrabold">Tables</h3>
            <p className="text-sm muted mt-1">
              Read the title and the unit line first (thousands, lakhs, crores, percent), then the row and column headings.
              Most questions touch one row or one column, so add or compare only that strip and ignore the rest. For
              count-style questions (how many years was a value above a figure) sweep the strip once and tick as you go.
              Questions that use several columns at once often reward writing a small helper row, such as a total or a
              ratio, once and reusing it.
            </p>
          </article>
          <article className="card p-4">
            <h3 className="font-extrabold">Bar graphs</h3>
            <p className="text-sm muted mt-1">
              A bar graph is a table drawn as bars, so first turn the bars you need into numbers and jot them down. Check
              the axis scale and where it starts before you compare heights by eye; a bar that looks twice as tall may not
              be twice the value. With grouped or stacked bars, read the legend to know which colour is which series, and
              remember that in a stacked bar a segment&apos;s value is its own length, not the top of the stack.
            </p>
          </article>
          <article className="card p-4">
            <h3 className="font-extrabold">Line graphs</h3>
            <p className="text-sm muted mt-1">
              Line graphs are about change over time, so most questions ask for a rise, a fall or a percentage change
              between two points. Read the two values off the axis, then use change ÷ original × 100 with the earlier value
              as the original. For &quot;in which year was the increase highest&quot; questions, compare the differences
              between neighbouring points. The steepest segment is a good first guess, but confirm with numbers when
              percent change is asked, because the largest absolute rise is not always the largest percentage rise.
            </p>
          </article>
          <article className="card p-4">
            <h3 className="font-extrabold">Pie charts</h3>
            <p className="text-sm muted mt-1">
              A pie divides a total into slices measured in degrees or percentages. With degrees, 360° is the whole, so
              value = angle ÷ 360 × total and percent = angle ÷ 3.6. If only one slice has a known value, find the value of
              1° (or 1%) once and price every other slice from it. When two pies are compared, convert each slice to an
              actual value using its own pie&apos;s total before comparing; equal percentages on pies with different totals
              are not equal amounts.
            </p>
          </article>
          <article className="card p-4">
            <h3 className="font-extrabold">Caselets and mixed sets</h3>
            <p className="text-sm muted mt-1">
              A caselet gives the data in a paragraph, and a mixed set combines, say, a table and a pie. Do not start
              answering. Spend a minute converting the caselet into a small table with labelled rows and columns, filling
              the unknowns from the given ratios or totals. For mixed sets, work out which chart gives the total and which
              gives the split, then connect them. The setup time is repaid across the several questions that follow the same data.
            </p>
          </article>
        </div>
      </section>

      <section id="graphs" className="mt-12 scroll-mt-24">
        <h2 className="text-2xl font-extrabold">Try it: DI graphs with questions</h2>
        <p className="text-sm muted mt-1 max-w-3xl">
          One worked set for each chart type. Read the chart, try each question yourself, then tap Show answer to see the
          answer and the shortcut. Every figure, answer and solution below is computed from the same data, so they always agree.
        </p>
        <div className="grid gap-4 mt-4 min-w-0">
          <BarGraph />
          <LineGraph />
          <PieGraph />
          <CasletTable />
        </div>
      </section>

      <section id="tricks" className="mt-12 scroll-mt-24">
        <h2 className="text-2xl font-extrabold">Time-saving calculation tricks</h2>
        <p className="text-sm muted mt-1 max-w-3xl">
          DI options are usually far apart, so exact long division is rarely needed. These tricks keep you fast without
          losing accuracy.
        </p>
        <div className="grid sm:grid-cols-2 gap-2.5 mt-3">
          {tricks.map(({ s, k }) => (
            <div key={`${s.id}-${k.title}`} className="card p-3.5 text-sm">
              <div className="font-bold">⚡ {k.title}</div>
              <p className="muted mt-1"><MathText text={k.body} /></p>
              <Link href={`${BASE}/learn/${s.id}/`} className="text-xs underline decoration-dotted mt-1.5 inline-block">{s.title} →</Link>
            </div>
          ))}
        </div>

        <h3 className="font-extrabold text-lg mt-7">Fractions worth knowing as percentages</h3>
        <p className="text-sm muted mt-1 max-w-3xl">
          Turning a percentage into a fraction (or the reverse) is the quickest DI shortcut. To find 12.5% of 480, think
          one-eighth of 480, which is 60. To find what percentage 35 is of 280, notice 35 is one-eighth of 280, so 12.5%.
          Learn this short table until it is automatic. Values are rounded to two decimals where they do not terminate.
        </p>
        <div className="card p-3.5 mt-3 overflow-x-auto">
          <table className="text-sm w-full text-left">
            <thead>
              <tr className="faint text-xs">
                <th className="py-1 pr-4">Fraction</th><th className="py-1 pr-6">Percent</th>
                <th className="py-1 pr-4 hidden sm:table-cell">Fraction</th><th className="py-1 hidden sm:table-cell">Percent</th>
              </tr>
            </thead>
            <tbody>
              {Array.from({ length: RECIPROCALS.length / 2 }, (_, i) => (
                <tr key={i} className="border-t" style={{ borderColor: 'var(--line)' }}>
                  <td className="py-1 pr-4 font-semibold">{RECIPROCALS[i][0]}</td><td className="py-1 pr-6">{RECIPROCALS[i][1]}</td>
                  <td className="py-1 pr-4 font-semibold hidden sm:table-cell">{RECIPROCALS[i + RECIPROCALS.length / 2][0]}</td>
                  <td className="py-1 hidden sm:table-cell">{RECIPROCALS[i + RECIPROCALS.length / 2][1]}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <p className="text-xs faint mt-2 sm:hidden">
            Also: {RECIPROCALS.slice(RECIPROCALS.length / 2).map(([a, b]) => `${a} = ${b}`).join(', ')}.
          </p>
        </div>

        <h3 className="font-extrabold text-lg mt-7">Three habits that save the most time</h3>
        <ul className="list-disc pl-5 text-sm muted mt-2 space-y-1.5 max-w-3xl">
          <li><span className="font-semibold">Compare before you calculate.</span> If a question asks which of two ratios is larger, cross-multiply or compare roughly; you rarely need the actual values.</li>
          <li><span className="font-semibold">Approximate late.</span> Keep exact numbers until the final step, then round only to separate the options. Rounding early compounds across steps.</li>
          <li><span className="font-semibold">Reuse a derived value.</span> If several questions need the same total or the same per-degree value, compute it once and write it beside the data.</li>
        </ul>
      </section>

      <section id="traps" className="mt-12 scroll-mt-24">
        <h2 className="text-2xl font-extrabold">Common DI traps</h2>
        <p className="text-sm muted mt-1 max-w-3xl">
          Examiners build wrong options out of predictable slips. Most DI errors are reading errors, not arithmetic errors.
        </p>
        <ul className="list-disc pl-5 text-sm muted mt-3 space-y-1.5 max-w-3xl">
          <li><span className="font-semibold">Wrong unit.</span> A table in thousands or crores with an option written in full rupees. Check the unit line before you pick an answer.</li>
          <li><span className="font-semibold">Wrong base.</span> &quot;A is what percent of B&quot; divides by B; &quot;B is what percent more than A&quot; divides by A. Underline the word after &quot;of&quot; or &quot;than&quot;.</li>
          <li><span className="font-semibold">Percentage points versus percent.</span> A rise from 20% to 25% is 5 percentage points, but a 25% increase in the rate.</li>
          <li><span className="font-semibold">Misreading the axis or legend.</span> Axes that do not start at zero and series with similar colours produce wrong readings.</li>
        </ul>
        <div className="grid sm:grid-cols-2 gap-2.5 mt-4">
          {traps.map(({ s, items }) => (
            <div key={s.id} className="card p-3.5 text-sm">
              <div className="font-bold">{s.title}</div>
              <ul className="mt-1.5 space-y-2 text-xs">
                {items.map((m, i) =>
                  typeof m === 'string' ? (
                    <li key={i} className="muted"><MathText text={m} /></li>
                  ) : (
                    <li key={i}>
                      <div style={{ color: 'var(--bad)' }}>✗ <MathText text={m.wrong} /></div>
                      <div style={{ color: 'var(--ok)' }}>✓ <MathText text={m.right} /></div>
                    </li>
                  ),
                )}
              </ul>
            </div>
          ))}
        </div>
      </section>

      {patterns.length > 0 && (
        <section id="types" className="mt-12 scroll-mt-24">
          <h2 className="text-2xl font-extrabold">Question types you will see</h2>
          <p className="text-sm muted mt-1 max-w-3xl">
            The recurring DI question types in our notes, with how to spot each one. Open the subtopic for the formula, the
            steps and a worked example.
          </p>
          <div className="grid sm:grid-cols-2 gap-2.5 mt-3">
            {patterns.map(({ s, p }) => (
              <Link key={p.id} href={`${BASE}/learn/${s.id}/`} className="card p-3.5 text-sm hover:-translate-y-0.5 transition-transform">
                <div className="flex items-center gap-2">
                  <span className="font-bold">{p.name}</span>
                  {p.frequency && <span className="chip ml-auto">{p.frequency}</span>}
                </div>
                {p.howToSpot && <p className="text-xs muted mt-1"><MathText text={p.howToSpot} /></p>}
                <span className="text-xs faint mt-1.5 inline-block">{s.title}</span>
              </Link>
            ))}
          </div>
        </section>
      )}

      <section id="practice" className="card p-5 mt-12 scroll-mt-24">
        <h2 className="text-xl font-extrabold">Practise data interpretation</h2>
        <p className="text-sm muted mt-2 max-w-3xl">
          Learn the five subtopics in order (tables, percentage, pie charts, averages, growth), then take the topic test
          under a timer. Afterwards, attempt a full mock and look at how long you spent on the DI block compared with the
          rest of the paper. Set a target per question and train to it.
        </p>
        <div className="flex gap-2 mt-3 flex-wrap">
          <Link href={`${BASE}/learn/${t.subtopics[0].id}/`} className="btn btn-brand">Start learning DI →</Link>
          <Link href={`${BASE}/practice/`} className="btn">{t.practice?.length ?? 0} practice questions</Link>
          <Link href={`${BASE}/examples/`} className="btn">{t.solvedExamples?.length ?? 0} solved examples</Link>
          <Link href="/exams/ssc-cgl/mocks/" className="btn">Mock tests{mocks.length ? ` (${mocks.length})` : ''}</Link>
          <Link href="/daily-quiz/" className="btn">Daily quiz</Link>
        </div>
        <p className="text-xs faint mt-4">
          Related: <Link href={BASE + '/'} className="underline decoration-dotted">Data interpretation topic page</Link> ·{' '}
          <Link href="/quant/percentage/" className="underline decoration-dotted">Percentage</Link> ·{' '}
          <Link href="/quant/average/" className="underline decoration-dotted">Average</Link> ·{' '}
          <Link href="/quant/ratio-proportion/" className="underline decoration-dotted">Ratio &amp; proportion</Link> ·{' '}
          <Link href="/quant-formulas/" className="underline decoration-dotted">All Quant formulas</Link> ·{' '}
          <Link href="/shortcut-tricks/" className="underline decoration-dotted">All shortcut tricks</Link> ·{' '}
          <Link href="/formula-sheet/" className="underline decoration-dotted">Formula sheet</Link>
        </p>
      </section>

      <aside className="mt-8 text-sm muted max-w-3xl">
        <h2 className="font-extrabold text-base" style={{ color: 'var(--ink)' }}>Practice yourself</h2>
        <p className="mt-1">
          The graphs above use illustrative data, so treat them as warm-up. For exam-style sets, attempt the{' '}
          <Link href="/daily-quiz/" className="underline decoration-dotted font-semibold">daily quiz</Link> to keep your
          calculation speed up, then time yourself on a full{' '}
          <Link href="/exams/ssc-cgl/mocks/" className="underline decoration-dotted font-semibold">SSC CGL mock test</Link>.        </p>
      </aside>
    </div>
  );
}
