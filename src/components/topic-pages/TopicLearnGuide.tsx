import Link from 'next/link';
import type { Topic } from '@/lib/types';
import { SECTION_META, type SectionId } from '@/lib/sections';
import { MathText } from '@/components/MathText';
import { readMinutes } from '@/components/Lesson';
import { firstParagraph, joinList, plural, trapList } from '@/lib/topicInsights';
import { PRACTICE_HABIT } from './copy';

/** Server-rendered depth for /[section]/[topic]/learn/: what the learning path covers, a short
    summary of every subtopic (taken from its own lesson), the traps that run through the topic and
    how to work through it. Every figure is derived from the topic's data. */
export function TopicLearnGuide({ topic: t }: { topic: Topic }) {
  const meta = SECTION_META[t.sectionId as SectionId];
  const base = `/${t.sectionId}/${t.id}`;
  const subs = t.subtopics;
  const practice = t.practice ?? [];
  const nTypes = subs.reduce((n, s) => n + (s.patterns?.length ?? 0), 0);
  const nFormulas = subs.reduce((n, s) => n + (s.formulas?.length ?? 0), 0);
  const nTricks = subs.reduce((n, s) => n + (s.tricks?.length ?? 0), 0);
  const nExamples = t.solvedExamples?.length ?? 0;
  const minutes = subs.reduce((n, s) => n + readMinutes(s.concept, s.notes, ...(s.patterns ?? []).map((p) => `${p.logic ?? ''} ${(p.steps ?? []).join(' ')} ${p.example?.q ?? ''}`)), 0);
  const traps = trapList(subs, 6);
  const habit = PRACTICE_HABIT[t.sectionId as SectionId];
  const facts = [
    nTypes > 0 && plural(nTypes, 'question type'),
    nFormulas > 0 && plural(nFormulas, 'formula'),
    nTricks > 0 && plural(nTricks, 'shortcut trick'),
    practice.length > 0 && `${practice.length} practice questions`,
  ].filter((x): x is string => !!x);

  return (
    <div className="mt-10">
      <section aria-labelledby="lg-about">
        <h2 id="lg-about" className="text-2xl font-extrabold">What the {t.title} lessons cover</h2>
        <p className="mt-2 text-[15px] muted">
          {t.title} is a {meta.short} topic taught here in {plural(subs.length, 'lesson')}, which add up to roughly {minutes} minutes of reading
          {facts.length > 0 && <>. Between them they hold {joinList(facts)}</>}.
          {' '}Each lesson opens with the idea in one minute, then goes through the question types you will meet, with a worked example for each, the shortcuts that save time, the mistakes that cost marks and a short revision list.
          {subs.length > 1 && <> Take them in the order listed above: later lessons assume the earlier ones.</>}
        </p>
      </section>

      <section className="mt-9" aria-labelledby="lg-subs">
        <h2 id="lg-subs" className="text-2xl font-extrabold">Lesson by lesson</h2>
        <div className="mt-3 grid gap-3">
          {subs.map((s, i) => {
            const lead = firstParagraph(s.concept);
            const types = (s.patterns ?? []).map((p) => p.name);
            const nQ = practice.filter((q) => q.subtopic === s.id).length;
            return (
              <div key={s.id} className="card p-4" id={`lesson-${s.id}`}>
                <div className="text-xs faint">Lesson {i + 1} of {subs.length}</div>
                <h3 className="font-extrabold">{s.title}</h3>
                {lead && <p className="text-sm muted mt-1.5"><MathText text={lead} max={320} /></p>}
                {types.length > 0 && (
                  <p className="text-sm mt-2"><b>Question types:</b> {joinList(types.slice(0, 5))}{types.length > 5 ? ` and ${types.length - 5} more` : ''}.</p>
                )}
                <p className="text-xs faint mt-2">
                  {[
                    (s.formulas?.length ?? 0) > 0 && plural(s.formulas!.length, 'formula'),
                    (s.tricks?.length ?? 0) > 0 && plural(s.tricks!.length, 'shortcut'),
                    nQ > 0 && `${nQ}-question quiz`,
                  ].filter(Boolean).join(' · ')}
                </p>
                <p className="text-xs mt-2"><Link className="underline decoration-dotted" href={`${base}/learn/${s.id}/`}>Open the lesson: {s.title} →</Link></p>
              </div>
            );
          })}
        </div>
      </section>

      {traps.length > 0 && (
        <section className="mt-9" aria-labelledby="lg-traps">
          <h2 id="lg-traps" className="text-2xl font-extrabold">Mistakes to watch for across {t.title}</h2>
          <ul className="mt-3 grid gap-2.5 list-none p-0">
            {traps.map((tr, i) => (
              <li key={i} className="card p-3.5 text-sm">
                <div className="text-xs faint">{tr.sub.title}</div>
                {tr.right ? (
                  <>
                    <p className="mt-1"><b style={{ color: 'var(--bad)' }}>Common slip:</b> <MathText text={tr.wrong} /></p>
                    <p className="mt-1"><b style={{ color: 'var(--ok)' }}>Instead:</b> <MathText text={tr.right} /></p>
                  </>
                ) : <p className="mt-1"><MathText text={tr.wrong} /></p>}
              </li>
            ))}
          </ul>
        </section>
      )}

      <section className="mt-9" aria-labelledby="lg-how">
        <h2 id="lg-how" className="text-2xl font-extrabold">How to work through {t.title}</h2>
        <p className="text-[15px] mt-2">{habit.attempt}</p>
        <p className="text-[15px] mt-2 muted">{habit.review}</p>
        <p className="text-sm muted mt-3">
          When a lesson is done, mark it as studied with the tick beside it, then test yourself:
          {practice.length > 0 && <> the <Link className="underline" href={`${base}/practice/`}>{practice.length}-question practice test</Link></>}
          {nExamples > 0 && <>{practice.length > 0 ? ', the ' : ' the '}<Link className="underline" href={`${base}/examples/`}>{plural(nExamples, 'solved example')}</Link></>}
          {nFormulas > 0 && <>{practice.length > 0 || nExamples > 0 ? ' and the ' : ' the '}<Link className="underline" href={`${base}/formulas/`}>formula sheet</Link></>}
          .
        </p>
      </section>
    </div>
  );
}
