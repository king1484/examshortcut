import Link from 'next/link';
import type { Topic } from '@/lib/types';
import { SECTION_META, type SectionId } from '@/lib/sections';
import { MathText } from '@/components/MathText';
import { Md, Figure, isSvg } from '@/components/Md';
import {
  LETTERS, budgetSeconds, difficultyMix, exampleLines, joinList, leadLine, patternLabel, patternsWithExample, plural, withPassages,
} from '@/lib/topicInsights';
import { EXAMPLE_HABIT } from './copy';

const DIFF_CHIP: Record<string, string> = { easy: 'chip-low', medium: 'chip-medium', hard: 'chip-high' };

/** Server-rendered depth for /[section]/[topic]/examples/: an index of the solved examples and the
    full worked solutions as plain HTML (the interactive cards above hide them until clicked). */
export function TopicExamplesGuide({ topic: t }: { topic: Topic }) {
  const exs = withPassages(t.solvedExamples ?? []);
  if (!exs.length) return null;
  const meta = SECTION_META[t.sectionId as SectionId];
  const base = `/${t.sectionId}/${t.id}`;
  const subTitle = Object.fromEntries(t.subtopics.map((s) => [s.id, s.title]));
  const mix = difficultyMix(exs);
  const mins = Math.max(1, Math.round(budgetSeconds(exs) / 60));
  const diffParts = ([['easy', mix.easy], ['medium', mix.medium], ['hard', mix.hard]] as const).filter(([, n]) => n > 0).map(([d, n]) => `${n} ${d}`);
  const subs = [...new Set(exs.map((q) => q.subtopic).filter((x): x is string => !!x && !!subTitle[x]))];
  const labels = [...new Set(exs.map((q) => patternLabel(q.pattern)).filter((x): x is string => !!x))];
  const withShortcut = exs.filter((q) => typeof q.shortcut === 'string' && q.shortcut).length;
  const habit = EXAMPLE_HABIT[t.sectionId as SectionId];
  const nPractice = t.practice?.length ?? 0;

  // One more worked case per subtopic, taken from the lessons' question-type catalogue.
  const lessonCases = t.subtopics
    .map((s) => ({ s, p: patternsWithExample(s, false)[0] }))
    .filter((x) => x.p?.example)
    .slice(0, 8);

  return (
    <div className="mt-10">
      <section aria-labelledby="eg-about">
        <h2 id="eg-about" className="text-2xl font-extrabold">About these {t.title} examples</h2>
        <p className="mt-2 text-[15px] muted">
          There {exs.length === 1 ? 'is' : 'are'} {plural(exs.length, 'solved example')} for {t.title}
          {diffParts.length > 0 && <> ({joinList(diffParts)})</>}, with an exam time budget of about {mins} {mins === 1 ? 'minute' : 'minutes'} in all.
          {subs.length > 0 && <> They draw on {joinList(subs.map((id) => subTitle[id]))}.</>}
          {labels.length > 0 && <> Question types represented: {joinList(labels.slice(0, 6))}.</>}
          {withShortcut > 0 && <> {withShortcut === exs.length ? 'Each' : `${withShortcut} of them`} also shows a quicker exam route next to the standard method.</>}
          {' '}The interactive cards above let you attempt each one first. The index and full solutions below are the same questions in plain text, so you can scan them, print the page, or revise without clicking anything.
        </p>
      </section>

      <section className="mt-9" aria-labelledby="eg-index">
        <h2 id="eg-index" className="text-2xl font-extrabold">Index of examples</h2>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead>
              <tr><th>#</th><th>Question (first line)</th><th>Level</th><th>Type</th><th>Subtopic</th><th>Time</th></tr>
            </thead>
            <tbody>
              {exs.map((q, i) => {
                const stmt = leadLine(q.q) ?? (q.passage ? leadLine(q.passage) : null);
                const label = patternLabel(q.pattern);
                return (
                  <tr key={q.id}>
                    <td><a className="underline decoration-dotted" href={`#ex-${i + 1}`}>{i + 1}</a></td>
                    <td className="text-sm">{stmt ? <MathText text={stmt} max={140} /> : <span className="faint">Figure-based question</span>}</td>
                    <td>{q.difficulty ? <span className={`chip ${DIFF_CHIP[q.difficulty] ?? ''}`}>{q.difficulty}</span> : null}</td>
                    <td className="text-xs">{label ?? ''}</td>
                    <td className="text-xs">{q.subtopic && subTitle[q.subtopic] ? <Link className="underline decoration-dotted" href={`${base}/learn/${q.subtopic}/`}>{subTitle[q.subtopic]}</Link> : ''}</td>
                    <td className="text-xs">{q.timeSec ? `${q.timeSec}s` : ''}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </section>

      <section className="mt-9" aria-labelledby="eg-full">
        <h2 id="eg-full" className="text-2xl font-extrabold">Solutions in full</h2>
        <div className="mt-3 space-y-3">
          {exs.map((q, i) => {
            const right = q.options[q.answer];
            const label = patternLabel(q.pattern);
            return (
              <article key={q.id} id={`ex-${i + 1}`} className="card p-4 sm:p-5">
                <div className="flex gap-2 items-center flex-wrap text-xs">
                  <h3 className="font-extrabold text-sm">Example {i + 1}</h3>
                  {q.difficulty && <span className={`chip ${DIFF_CHIP[q.difficulty] ?? ''}`}>{q.difficulty}</span>}
                  {label && <span className="chip">{label}</span>}
                  {q.timeSec ? <span className="faint">{q.timeSec}s exam budget</span> : null}
                </div>
                {q.passage && (
                  <div className="mt-3 rounded-xl px-3 py-2.5 text-sm" style={{ background: 'var(--surface-2)' }}>
                    <div className="faint text-xs font-semibold uppercase tracking-wide">Passage</div>
                    <Md>{q.passage}</Md>
                  </div>
                )}
                <div className="mt-3"><Md>{q.q}</Md></div>
                <Figure svg={q.figure} />
                {q.options.length > 0 && (
                  <ol className="mt-3 grid gap-1.5 list-none p-0">
                    {q.options.map((o, k) => (
                      <li key={k} className="flex gap-2.5 items-start text-sm">
                        <span className="shrink-0 font-bold w-5">{LETTERS[k]}.</span>
                        <span className="min-w-0 flex-1"><Md inline>{o}</Md></span>
                      </li>
                    ))}
                  </ol>
                )}
                {q.options.length > 0 && (
                  <div className="mt-3 text-sm font-bold flex gap-1.5 items-baseline flex-wrap" style={{ color: 'var(--ok)' }}>
                    <span>Correct answer: option {LETTERS[q.answer]}</span>
                    {right && !isSvg(right) ? <><span aria-hidden>—</span><span className="min-w-0"><Md inline>{right}</Md></span></> : null}
                  </div>
                )}
                <h4 className="mt-3 text-xs font-bold uppercase tracking-wide faint">Standard method</h4>
                <Md className="text-sm">{q.solution}</Md>
                {typeof q.shortcut === 'string' && q.shortcut && (
                  <>
                    <h4 className="mt-3 text-xs font-bold uppercase tracking-wide faint">Shortcut route</h4>
                    <Md className="text-sm">{q.shortcut}</Md>
                  </>
                )}
              </article>
            );
          })}
        </div>
      </section>

      <section className="mt-9" aria-labelledby="eg-read">
        <h2 id="eg-read" className="text-2xl font-extrabold">How to get the most from a solved example</h2>
        <p className="text-[15px] mt-2">{habit}</p>
        <p className="text-[15px] mt-2 muted">
          After the {exs.length} {exs.length === 1 ? 'example' : 'examples'} here, move on to fresh questions of the same kinds rather than rereading: understanding a worked solution and producing one unaided are different skills.
        </p>
      </section>

      {lessonCases.length > 0 && (
        <section className="mt-9" aria-labelledby="eg-more">
          <h2 id="eg-more" className="text-2xl font-extrabold">More worked cases from the {t.title} lessons</h2>
          <p className="text-sm muted mt-1">One further question type from each lesson, with the answer. The lesson shows the full method.</p>
          <ul className="mt-3 grid gap-2.5 list-none p-0">
            {lessonCases.map(({ s, p }) => {
              const lines = exampleLines(p!.example!);
              return (
                <li key={s.id} className="card p-3.5 text-sm">
                  <div className="font-bold">{s.title}: {p!.name}</div>
                  <div className="mt-1"><Md>{p!.example!.q}</Md></div>
                  {(p!.example!.answer || lines.length > 0) && (
                    <p className="mt-1.5"><b style={{ color: 'var(--ok)' }}>Answer:</b> <MathText text={p!.example!.answer ?? lines[lines.length - 1]} max={220} /></p>
                  )}
                  <p className="text-xs mt-1.5"><Link className="underline decoration-dotted" href={`${base}/learn/${s.id}/`}>Method in the lesson →</Link></p>
                </li>
              );
            })}
          </ul>
        </section>
      )}

      <section className="mt-9">
        <p className="text-sm muted">
          {meta.short} · {t.title}: next, {nPractice > 0 ? <>test yourself with the <Link className="underline" href={`${base}/practice/`}>{nPractice}-question practice set</Link></> : 'revisit the lessons'}
          {(t.subtopics.some((s) => (s.formulas?.length ?? 0) > 0)) && <>, keep the <Link className="underline" href={`${base}/formulas/`}>formula sheet</Link> handy</>}
          {' '}or return to the <Link className="underline" href={`${base}/learn/`}>lessons</Link>.
        </p>
      </section>
    </div>
  );
}
