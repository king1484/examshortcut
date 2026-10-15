import Link from 'next/link';
import type { Mock } from '@/lib/types';
import { analyseMock, siblingMocks, type MockSeoData, type MockTopicCount } from '@/lib/mockSeo';
import { hasPage } from '@/lib/examPages';
import { Md, Figure } from '@/components/Md';

/* Crawlable, server-rendered companion to the client-side CBT: everything below is computed
   from the paper's own questions (see src/lib/mockSeo.ts), so the text differs for every paper. */

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
const num = (n: number, d = 2) => String(Number(n.toFixed(d)));
const pct = (n: number) => `${Math.round(n)}%`;
const plural = (n: number, one: string, many = `${one}s`) => `${n} ${n === 1 ? one : many}`;
const hash = (s: string) => [...s].reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 7);
const joinList = (xs: string[]) => (xs.length <= 1 ? xs.join('') : `${xs.slice(0, -1).join(', ')} and ${xs[xs.length - 1]}`);

const KIND_LABEL: Record<Mock['kind'], string> = {
  full: 'a full-length practice mock',
  'pyq-pattern': 'a practice paper modelled on the previous-year pattern',
  'real-pyq': 'a previous-year paper',
};

function TopicLink({ t }: { t: MockTopicCount }) {
  const text = `${t.label} (${t.count})`;
  return t.link ? <Link className="underline decoration-dotted underline-offset-2" href={`/${t.link.section}/${t.link.id}/`}>{text}</Link> : <>{text}</>;
}

function penaltyText(d: MockSeoData, plus: number): string {
  const [main, ...rest] = d.penalties;
  if (!main) return '';
  if (!rest.length) {
    return main.value > 0
      ? `Each correct answer earns ${num(plus)} and each wrong answer costs ${num(main.value)}; unattempted questions lose nothing.`
      : `Each correct answer earns ${num(plus)} and this paper has no negative marking.`;
  }
  const parts = d.penalties.map((p) => `${plural(p.count, 'question')} ${p.value > 0 ? `with a ${num(p.value)}-mark penalty` : 'with no penalty'}`);
  return `Each correct answer earns ${num(plus)}, but the penalty for a wrong answer depends on the question: ${joinList(parts)}.`;
}

export function MockSeoSection({ mock }: { mock: Mock }) {
  const d = analyseMock(mock);
  if (!d.total) return null;
  const sibs = siblingMocks(mock);
  const h = hash(mock.id);
  const examBase = `/exams/${d.examId}`;
  const names = d.sections.map((s) => s.name);
  const mainPenalty = d.penalties[0]?.value ?? 0;
  const singlePenalty = d.penalties.length === 1;
  const byCount = [...d.sections].sort((a, b) => b.count - a.count || a.name.localeCompare(b.name));
  const biggest = byCount[0];
  const smallest = byCount[byCount.length - 1];
  const haveEst = d.sections.every((s) => s.avgTimeSec !== null);
  const sectionHref = (sid: string, name: string) => (name === 'General Hindi' ? null : `/${sid}/`);
  const linkedTopics = d.topics.filter((t) => t.link).slice(0, 6);
  const hasSyllabus = d.examId === 'ssc-cgl' || d.examId === 'cat' || hasPage(d.examId, 'syllabus');

  // time budget per section: proportional to our time estimates when every question has one, otherwise to question count
  const weightOf = (s: MockSeoData['sections'][number]) => (haveEst ? (s.estSec as number) : s.count);
  const weightSum = d.sections.reduce((n, s) => n + weightOf(s), 0) || 1;
  const budget = (s: MockSeoData['sections'][number]) => Math.max(1, Math.round((d.durationMin * weightOf(s)) / weightSum));

  const fastest = haveEst ? [...d.sections].sort((a, b) => (a.avgTimeSec as number) - (b.avgTimeSec as number))[0] : null;
  const slowest = haveEst ? [...d.sections].sort((a, b) => (b.avgTimeSec as number) - (a.avgTimeSec as number))[0] : null;

  // guessing arithmetic for the dominant penalty
  const k = d.optionCount;
  const ev = k && mainPenalty > 0 ? (mock.plus - mainPenalty * (k - 1)) / k : null;
  const breakEven = mainPenalty > 0 ? (mainPenalty / (mock.plus + mainPenalty)) * 100 : null;
  const tryN = Math.round(d.total * 0.8), rightN = Math.round(tryN * 0.85), wrongN = tryN - rightN;
  const tryScore = rightN * mock.plus - wrongN * mainPenalty;

  const hardest = d.sections
    .filter((s) => s.difficulty)
    .map((s) => { const t = s.difficulty!.easy + s.difficulty!.medium + s.difficulty!.hard; return { s, share: t ? (s.difficulty!.hard / t) * 100 : 0, t }; })
    .sort((a, b) => b.share - a.share)[0];

  const opener = ['This page is', 'On this page you will find', 'You are looking at'][h % 3];

  return (
    <section className="max-w-3xl mx-auto mt-12 space-y-10" aria-labelledby="mock-about">
      <div>
        <h2 id="mock-about" className="text-xl sm:text-2xl font-extrabold">About this {d.examName} paper</h2>
        <p className="mt-3 muted">
          {opener} {KIND_LABEL[mock.kind]} for {d.examName}{d.dateLabel ? `, dated ${d.dateLabel}` : ''}{d.shiftLabel ? ` (${d.shiftLabel})` : ''}.
          It has {plural(d.total, 'question')} in {plural(d.sections.length, 'section')} ({joinList(names)}), worth {num(d.maxMarks)} marks in total,
          to be solved in {d.durationMin} minutes. {penaltyText(d, mock.plus)} Once you submit, the review mode shows the correct option and a full explanation for every
          question{d.shortcutQs > 0 ? `, and ${d.shortcutQs} of them also carry a shortcut method` : ''}. Your score is saved on this device.
        </p>
        <p className="mt-3 muted"><b>Source note:</b> {mock.blurb}</p>
        <div className="tbl-wrap mt-4">
          <table className="tbl">
            <tbody>
              <tr><th scope="row">Exam</th><td>{d.examName}</td></tr>
              {(d.dateLabel || d.shiftLabel) && <tr><th scope="row">Date / shift</th><td>{[d.dateLabel, d.shiftLabel].filter(Boolean).join(' · ')}</td></tr>}
              <tr><th scope="row">Questions</th><td>{d.total}</td></tr>
              <tr><th scope="row">Total marks</th><td>{num(d.maxMarks)} (+{num(mock.plus)} per correct answer)</td></tr>
              <tr><th scope="row">Duration</th><td>{d.durationMin} minutes ({num(d.secPerQuestion, 0)} seconds per question on average)</td></tr>
              <tr><th scope="row">Negative marking</th><td>{d.penalties.length === 1 ? (mainPenalty > 0 ? `−${num(mainPenalty)} per wrong answer` : 'None') : d.penalties.map((p) => `${p.value > 0 ? `−${num(p.value)}` : 'none'} on ${p.count}`).join('; ')}</td></tr>
              <tr><th scope="row">Sections</th><td>{d.sections.length}: {names.join(', ')}</td></tr>
              {d.optionCount && <tr><th scope="row">Answer format</th><td>{d.optionCount} options per question{d.numericQs > 0 ? `; ${d.numericQs} type-in answers` : ''}</td></tr>}
              {d.answerSpread.length > 1 && <tr><th scope="row">Answer key spread</th><td>{d.answerSpread.map((a) => `${a.letter} ${a.count}`).join(' · ')}</td></tr>}
            </tbody>
          </table>
        </div>
      </div>

      <div>
        <h2 className="text-xl sm:text-2xl font-extrabold">Section-wise breakdown</h2>
        <div className="tbl-wrap mt-4">
          <table className="tbl">
            <thead>
              <tr>
                <th>Section</th><th>Questions</th><th>Share</th><th>Marks</th>{haveEst && <th>Est. time / question</th>}<th>Topics covered</th>
              </tr>
            </thead>
            <tbody>
              {d.sections.map((s) => {
                const more = s.distinctTopics - s.topics.length;
                return (
                  <tr key={s.sectionId}>
                    <td className="font-semibold">{s.name}</td>
                    <td>{s.count}</td>
                    <td>{pct(s.sharePct)}</td>
                    <td>{num(s.marks)}</td>
                    {haveEst && <td>{num(s.avgTimeSec as number, 0)} s</td>}
                    <td>
                      {s.topics.length ? (
                        <>
                          {s.topics.map((t, i) => <span key={t.label}>{i > 0 && ', '}<TopicLink t={t} /></span>)}
                          {more > 0 && ` and ${plural(more, 'more topic')}`}
                          {s.taggedCount < s.count && <span className="faint"> · {s.count - s.taggedCount} not tagged</span>}
                        </>
                      ) : <span className="faint">No topic tags for this section</span>}
                    </td>
                  </tr>
                );
              })}
              <tr>
                <td className="font-bold">Total</td><td className="font-bold">{d.total}</td><td className="font-bold">100%</td><td className="font-bold">{num(d.maxMarks)}</td>{haveEst && <td />}<td />
              </tr>
            </tbody>
          </table>
        </div>
        <div className="mt-4 space-y-3 muted">
          <p>
            {d.sections.length > 1 && biggest.count !== smallest.count
              ? <>{biggest.name} is the heaviest block with {plural(biggest.count, 'question')} ({pct(biggest.sharePct)} of the paper, {num(biggest.marks)} marks), while {smallest.name} is the lightest with {smallest.count} ({pct(smallest.sharePct)}).</>
              : <>The {d.sections.length > 1 ? 'sections are evenly sized, ' : 'paper is a single section, '}with {biggest.count} questions {d.sections.length > 1 ? 'each' : ''} worth {num(biggest.marks)} marks.</>}
            {' '}{d.passageQs > 0 && <>{plural(d.passageQs, 'question')} belong to shared passages or sets. </>}
            {d.figureQs > 0 && <>{plural(d.figureQs, 'question')} come with a diagram. </>}
          </p>
          {d.taggedTotal > 0 ? (
            <p>
              {d.taggedTotal === d.total ? `All ${d.total}` : `${d.taggedTotal} of the ${d.total}`} questions carry a topic tag in our data, spread over {plural(d.distinctTopics, 'distinct topic')}.
              The most frequent are{' '}
              {d.topics.slice(0, 5).map((t, i, arr) => <span key={t.label}>{i > 0 && (i === arr.length - 1 ? ' and ' : ', ')}<TopicLink t={t} /></span>)}.
            </p>
          ) : (
            <p>The source of this paper does not tag individual topics, so the breakdown above is by section only.</p>
          )}
          {d.difficulty && (
            <p>
              Difficulty tags in our data put {d.difficulty.easy} questions at easy, {d.difficulty.medium} at medium and {d.difficulty.hard} at hard.
              {hardest && hardest.share > 0 && d.sections.length > 1 && <> {hardest.s.name} has the largest hard share, at {pct(hardest.share)} of its tagged questions.</>}
            </p>
          )}
        </div>
      </div>

      <div>
        <h2 className="text-xl sm:text-2xl font-extrabold">How to attempt this paper</h2>
        <div className="mt-3 space-y-3 muted">
          <p>
            The clock allows {d.durationMin} minutes for {plural(d.total, 'question')}, which is {d.secPerQuestion >= 90 ? `${num(d.durationMin / d.total, 1)} minutes` : `${num(d.secPerQuestion, 0)} seconds`} each.
            {d.estMinutes !== null && (d.estMinutes <= d.durationMin
              ? <> Our own per-question time estimates for this paper add up to about {num(d.estMinutes, 0)} minutes, so a solver working at that pace has roughly {num(d.durationMin - d.estMinutes, 0)} minutes left for review.</>
              : <> Our own per-question time estimates add up to about {num(d.estMinutes, 0)} minutes, which is {num(d.estMinutes - d.durationMin, 0)} minutes more than the clock allows, so some questions have to be skipped or answered on instinct.</>)}
          </p>
          <p>A workable split of the {d.durationMin} minutes, {haveEst ? 'weighted by the time estimates in our data' : 'weighted by the number of questions'}, is:</p>
          <ul className="list-disc pl-5 space-y-1">
            {d.sections.map((s) => (
              <li key={s.sectionId}>
                <b>{s.name}</b>: about {budget(s)} minutes for {plural(s.count, 'question')}
                {s.avgTimeSec !== null ? ` (around ${num(s.avgTimeSec, 0)} seconds each)` : ''}
              </li>
            ))}
          </ul>
          {fastest && slowest && fastest.sectionId !== slowest.sectionId ? (
            <p>
              Since {fastest.name} has the shortest estimated time per question ({num(fastest.avgTimeSec as number, 0)} s) and {slowest.name} the longest ({num(slowest.avgTimeSec as number, 0)} s),
              clearing {fastest.name} first banks marks quickly, and {slowest.name} is best kept for the last stretch when you know exactly how much time remains.
            </p>
          ) : (
            <p>
              The biggest block is {biggest.name} with {pct(biggest.sharePct)} of the marks, so a slow start there costs the most. Open with the section where your accuracy is highest,
              then move to {d.sections.length > 1 ? biggest.name : 'the harder questions'} while you still have most of the clock left.
            </p>
          )}
          {d.sections.filter((s) => s.passageQs > 0).map((s) => (
            <p key={s.sectionId}>
              In {s.name}, {s.passageQs === s.count ? `all ${s.count}` : `${s.passageQs} of the ${s.count}`} questions sit on shared passages or sets. Read each passage or set once and clear all its questions together instead of coming back to it.
            </p>
          ))}
          {mainPenalty > 0 && breakEven !== null ? (
            <p>
              {singlePenalty ? 'A wrong answer' : 'Most wrong answers'} costs {num(mainPenalty)} against {num(mock.plus)} for a right one, so you should attempt a question only when you judge your chance of being right to be above about {num(breakEven, 0)}%.
              {ev !== null && k && (Math.abs(ev) <= mock.plus * 0.01
                ? <> A blind guess among {k} options is worth about {num(ev, 3)} marks on average, which is break-even, so guess only after eliminating at least one option.</>
                : ev > 0
                  ? <> A blind guess among {k} options is worth {num(ev, 3)} marks on average, so an informed guess is always worthwhile.</>
                  : <> A blind guess among {k} options is worth {num(ev, 3)} marks on average, so leave a question blank unless you can cut the options down.</>)}
              {singlePenalty && <> As arithmetic, not a prediction: attempting {tryN} questions and getting {rightN} right leaves {wrongN} wrong, for {num(rightN * mock.plus)} − {num(wrongN * mainPenalty)} = {num(tryScore)} out of {num(d.maxMarks)}.</>}
            </p>
          ) : mainPenalty === 0 && singlePenalty ? (
            <p>There is no negative marking here, so every question is worth attempting: an unanswered question can only lose you marks you could have gained, so mark an answer for everything before the timer ends.</p>
          ) : null}
        </div>
      </div>

      {d.samples.length > 0 && (
        <div>
          <h2 className="text-xl sm:text-2xl font-extrabold">Sample questions with solutions</h2>
          <p className="mt-3 muted">
            {plural(d.samples.length, 'question')} from this paper ({joinList([...new Set(d.samples.map((x) => x.sectionName))])}), shown with the correct answer{d.samples.some((s) => s.showSolution) ? ' and the worked solution' : ''}.
            If you want to attempt the paper fresh, skip this part until you have finished the test.
          </p>
          <div className="mt-4 space-y-6">
            {d.samples.map((s, i) => {
              const q = s.q;
              const numeric = q.type === 'numeric' || !q.options?.length;
              const level = d.difficulty && q.difficulty ? q.difficulty : null;
              return (
                <article key={q.id} className="card p-4 sm:p-5">
                  <h3 className="font-bold">Sample {i + 1}: {s.sectionName}, question {s.number}{level ? <span className="chip ml-2 align-middle">{level}</span> : null}</h3>
                  <div className="mt-3"><Md>{q.q}</Md></div>
                  <Figure svg={q.figure} />
                  {!numeric && (
                    <ol className="mt-3 space-y-1.5 list-none p-0">
                      {q.options.map((o, oi) => (
                        <li key={oi} className="flex gap-2"><span className="font-bold shrink-0">{LETTERS[oi]}.</span><div className="min-w-0"><Md inline>{o}</Md></div></li>
                      ))}
                    </ol>
                  )}
                  <div className="mt-4 rounded-xl border p-4" style={{ borderColor: 'var(--line)', background: 'var(--surface-2)' }}>
                    <p className="font-bold text-sm">
                      Correct answer: {numeric ? String(q.answer) : <>{LETTERS[q.answer]}</>}
                    </p>
                    {s.showSolution && <div className="mt-2"><Md>{q.solution}</Md></div>}
                    {s.showSolution && q.shortcut && (
                      <div className="mt-3 text-sm"><b>Shortcut:</b> <Md inline>{q.shortcut}</Md></div>
                    )}
                  </div>
                </article>
              );
            })}
          </div>
        </div>
      )}

      <nav aria-labelledby="mock-related">
        <h2 id="mock-related" className="text-xl sm:text-2xl font-extrabold">Related practice</h2>
        <ul className="mt-3 space-y-2 list-disc pl-5">
          <li><Link className="underline" href={`${examBase}/`}>{d.examName} exam hub</Link>: pattern, cut-offs, mocks and tools in one place.</li>
          <li><Link className="underline" href={`${examBase}/exam-pattern/`}>{d.examName} exam pattern</Link>: how many questions, marks and minutes the real exam gives each section.</li>
          {hasSyllabus && <li><Link className="underline" href={`${examBase}/syllabus/`}>{d.examName} syllabus</Link>: the topic list this paper is drawn from.</li>}
          <li><Link className="underline" href={`${examBase}/cutoffs/`}>{d.examName} cut-offs</Link>: compare your score on this paper with past cut-offs.</li>
          <li><Link className="underline" href={`${examBase}/mocks/`}>All {d.examName} mock tests</Link>.</li>
          {d.sections.map((s) => {
            const href = sectionHref(s.sectionId, s.name);
            return href ? <li key={s.sectionId}><Link className="underline" href={href}>{s.name} notes and topic tests</Link></li> : null;
          })}
        </ul>
        {linkedTopics.length > 0 && (
          <>
            <h3 className="font-bold mt-5">Topics that appear most often in this paper</h3>
            <ul className="mt-2 space-y-1.5 list-disc pl-5">
              {linkedTopics.map((t) => (
                <li key={`${t.link!.section}/${t.link!.id}`}>
                  <Link className="underline" href={`/${t.link!.section}/${t.link!.id}/`}>{t.label}</Link> ({plural(t.count, 'question')} here) ·{' '}
                  <Link className="underline" href={`/${t.link!.section}/${t.link!.id}/practice/`}>topic practice test</Link>
                </li>
              ))}
            </ul>
          </>
        )}
        {sibs.length > 0 && (
          <>
            <h3 className="font-bold mt-5">More {d.examName} papers</h3>
            <ul className="mt-2 space-y-1.5 list-disc pl-5">
              {sibs.map((m) => <li key={m.id}><Link className="underline" href={`${examBase}/mocks/${m.id}/`}>{m.title}</Link></li>)}
            </ul>
          </>
        )}
      </nav>
    </section>
  );
}
