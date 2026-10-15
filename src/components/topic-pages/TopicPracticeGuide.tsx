import Link from 'next/link';
import type { Topic } from '@/lib/types';
import { SECTION_META, type SectionId } from '@/lib/sections';
import { MathText } from '@/components/MathText';
import {
  FREQ_CHIP, budgetSeconds, difficultyMix, joinList, leadLine, patternLabel, pickSamples, plural,
  questionTypes, subtopicCounts, timeRange, trapList,
} from '@/lib/topicInsights';
import { SampleQuestion } from './SampleQuestion';
import { PRACTICE_HABIT } from './copy';

/** Server-rendered companion to the interactive test on /[section]/[topic]/practice/: what the
    question set contains, the traps it sets, worked sample questions and a practice routine.
    Everything is computed from the topic's own data. */
export function TopicPracticeGuide({ topic: t }: { topic: Topic }) {
  const qs = t.practice ?? [];
  if (!qs.length) return null;
  const meta = SECTION_META[t.sectionId as SectionId];
  const base = `/${t.sectionId}/${t.id}`;
  const mix = difficultyMix(qs);
  const budget = budgetSeconds(qs);
  const range = timeRange(qs);
  const perSub = subtopicCounts(t);
  const types = questionTypes(t);
  const shortcutN = qs.filter((q) => typeof q.shortcut === 'string' && q.shortcut).length;
  const traps = trapList(t.subtopics, 6);
  const samples = pickSamples(t.id, qs, 4);
  const subTitle = Object.fromEntries(t.subtopics.map((s) => [s.id, s.title]));
  const habit = PRACTICE_HABIT[t.sectionId as SectionId];
  const nFormulas = t.subtopics.reduce((n, s) => n + (s.formulas?.length ?? 0), 0);
  const minutes = Math.max(1, Math.round(budget / 60));
  const diffParts = ([['easy', mix.easy], ['medium', mix.medium], ['hard', mix.hard]] as const).filter(([, n]) => n > 0).map(([d, n]) => `${n} ${d}`);
  const tier1 = t.avgQuestions?.tier1;
  const tier2 = t.avgQuestions?.tier2;
  const biggest = perSub[0];

  return (
    <div className="mt-10">
      <section aria-labelledby="pg-covers">
        <h2 id="pg-covers" className="text-2xl font-extrabold">What this {t.title} test covers</h2>
        <p className="mt-2 text-[15px] muted">
          This is the full {meta.short} topic set for {t.title}: {plural(qs.length, 'question')} spread over {plural(perSub.length || t.subtopics.length, 'subtopic')}
          {perSub.length > 0 && <> ({joinList(perSub.slice(0, 4).map((x) => `${x.sub.title}: ${x.n}`))}{perSub.length > 4 ? `, plus ${perSub.length - 4} more` : ''})</>}.
          {diffParts.length > 0 && <> The difficulty mix is {joinList(diffParts)}.</>}
          {' '}The timed test budgets about {minutes} {minutes === 1 ? 'minute' : 'minutes'} in total
          {range ? <>, using a per-question allowance that runs from {range.min} to {range.max} seconds depending on the question</> : null}.
          {shortcutN > 0 && <> {shortcutN} of the {qs.length} questions also come with a faster exam-style route in addition to the full solution.</>}
        </p>
        {(tier1 || tier2 || t.importance) && (
          <p className="mt-2 text-[15px] muted">
            In the syllabus data on this site {t.title} is rated {t.importance ?? 'a regular'}{t.importance ? ' importance' : ' topic'}
            {tier1 ? <>, with about {tier1} {tier1 === 1 ? 'question' : 'questions'} in a Tier 1 paper</> : null}
            {tier2 ? <>{tier1 ? ' and' : ', with'} about {tier2} in Tier 2</> : null}.
            {' '}The questions here are written in the style of the recurring previous-year patterns for this topic, with fresh numbers and wording.
          </p>
        )}
      </section>

      {types.length > 0 && (
        <section className="mt-9" aria-labelledby="pg-types">
          <h2 id="pg-types" className="text-2xl font-extrabold">Question types in this set</h2>
          <p className="text-sm muted mt-1">
            The set is built from {plural(types.length, 'recurring question type')}. The ones below appear most often here; each links to the lesson where the method is taught.
          </p>
          <ul className="mt-3 grid gap-2.5 list-none p-0">
            {types.slice(0, 8).map((ty) => {
              const lead = ty.ref?.pattern.howToSpot ?? null;
              const stmt = leadLine(ty.sample.q);
              const freq = ty.ref?.pattern.frequency;
              return (
                <li key={ty.key} className="card p-3.5">
                  <div className="flex items-center gap-2 flex-wrap">
                    <h3 className="font-bold text-sm">{ty.label}</h3>
                    <span className="chip">{ty.n} {ty.n === 1 ? 'question' : 'questions'}</span>
                    {freq && <span className={`chip ${FREQ_CHIP[freq] ?? ''}`}>{freq}</span>}
                  </div>
                  {lead && <p className="text-sm muted mt-1.5"><b>How to spot it:</b> <MathText text={lead} max={240} /></p>}
                  {stmt && <p className="text-xs faint mt-1.5">Example from this set: <MathText text={stmt} max={150} /></p>}
                  {ty.sub && <p className="text-xs mt-1.5"><Link className="underline decoration-dotted" href={`${base}/learn/${ty.sub.id}/`}>Learn this in “{ty.sub.title}” →</Link></p>}
                </li>
              );
            })}
          </ul>
          {types.length > 8 && <p className="text-xs faint mt-2">…plus {types.length - 8} less frequent types, each covered by one or two questions.</p>}
        </section>
      )}

      {traps.length > 0 && (
        <section className="mt-9" aria-labelledby="pg-traps">
          <h2 id="pg-traps" className="text-2xl font-extrabold">Traps to watch for in {t.title}</h2>
          <p className="text-sm muted mt-1">These are the slips the lessons flag for this topic, one or two from each subtopic. A quick scan before you start is worth the minute.</p>
          <ul className="mt-3 grid gap-2.5 list-none p-0">
            {traps.map((tr, i) => (
              <li key={i} className="card p-3.5 text-sm">
                <div className="text-xs faint">{tr.sub.title}</div>
                {tr.right ? (
                  <>
                    <p className="mt-1"><b style={{ color: 'var(--bad)' }}>Common slip:</b> <MathText text={tr.wrong} /></p>
                    <p className="mt-1"><b style={{ color: 'var(--ok)' }}>Instead:</b> <MathText text={tr.right} /></p>
                  </>
                ) : (
                  <p className="mt-1"><MathText text={tr.wrong} /></p>
                )}
              </li>
            ))}
          </ul>
        </section>
      )}

      {samples.length > 0 && (
        <section className="mt-9" aria-labelledby="pg-samples">
          <h2 id="pg-samples" className="text-2xl font-extrabold">{samples.length} sample questions with full solutions</h2>
          <p className="text-sm muted mt-1">
            A cross-section of the set, from easier to harder and from different subtopics. Try each one before reading the solution; the interactive test above gives you the rest.
          </p>
          <div className="mt-3 space-y-3">
            {samples.map((q, i) => {
              const label = patternLabel(q.pattern);
              return (
                <SampleQuestion key={q.id} q={q} id={`sample-${i + 1}`} label={`Sample ${i + 1}`}
                  tags={<>
                    {q.subtopic && subTitle[q.subtopic] && <Link className="chip" href={`${base}/learn/${q.subtopic}/`}>{subTitle[q.subtopic]}</Link>}
                    {label && <span className="chip" title="Recurring question pattern">{label}</span>}
                  </>} />
              );
            })}
          </div>
        </section>
      )}

      <section className="mt-9" aria-labelledby="pg-routine">
        <h2 id="pg-routine" className="text-2xl font-extrabold">How to practise {t.title}</h2>
        <ol className="mt-3 space-y-3 list-decimal pl-5 text-[15px]">
          <li>
            <b>Learn the method first.</b> {t.subtopics[0] ? <>Start with <Link className="underline" href={`${base}/learn/${t.subtopics[0].id}/`}>{t.subtopics[0].title}</Link> and work through the {plural(t.subtopics.length, 'subtopic')} in order</> : 'Work through the lessons in order'}
            {nFormulas > 0 ? <>; keep the <Link className="underline" href={`${base}/formulas/`}>{nFormulas}-formula sheet</Link> open the first time</> : null}.
          </li>
          <li>
            <b>Go subtopic by subtopic in practice mode.</b>{' '}
            {biggest ? <>The largest block is {biggest.sub.title} ({plural(biggest.n, 'question')}); start there, because it carries the most weight in this set. </> : null}
            {habit.attempt}
          </li>
          <li>
            <b>Then take the full set as a timed test.</b> Allow {minutes} {minutes === 1 ? 'minute' : 'minutes'} and do not pause. Afterwards compare your time with the target for each question: a correct answer that took three times the budget is still a weak spot.
          </li>
          <li>
            <b>Review the misses, then repeat after a gap.</b> {habit.review} When you are logged in, wrong answers are saved to <Link className="underline" href="/revision/">My revision</Link> so you can retry them later; use the <Link className="underline" href="/revision-planner/">revision planner</Link> to schedule the repeat.
          </li>
        </ol>
        {(t.solvedExamples?.length ?? 0) > 0 && (
          <p className="text-sm muted mt-3">
            Stuck before you start? Read the <Link className="underline" href={`${base}/examples/`}>{plural(t.solvedExamples!.length, 'solved example')}</Link> first; they are worked line by line.
          </p>
        )}
      </section>
    </div>
  );
}
