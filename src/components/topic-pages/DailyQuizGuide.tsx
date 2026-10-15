import fs from 'node:fs';
import path from 'node:path';
import Link from 'next/link';
import type { Question } from '@/lib/types';
import { SECTION_META, SECTION_ORDER, availableSections, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { plural } from '@/lib/topicInsights';
import { SampleQuestion } from './SampleQuestion';

interface DailyQ extends Question { topic?: string }
interface Bucket { n: number; sections: { section: string; name: string; questions: DailyQ[] }[] }

/** Set 1 of the 30 rotating sets, read at build time from the generated public/data/daily files.
    Returns null when the file is missing so the page still renders without the sample. */
function readSampleSet(): Bucket | null {
  try {
    const raw = fs.readFileSync(path.join(process.cwd(), 'public', 'data', 'daily', '0.json'), 'utf8');
    const b = JSON.parse(raw) as Bucket;
    return Array.isArray(b.sections) ? b : null;
  } catch {
    return null;
  }
}

const plainEnough = (q: DailyQ) =>
  !q.figure && !q.passage && q.options.length >= 2 && q.type !== 'numeric'
  && !q.q.trimStart().startsWith('<') && !q.options.some((o) => o.trimStart().startsWith('<svg'))
  && q.solution.length <= 1000 && q.q.length <= 420;

/** Server-rendered explanation of the daily quiz (the quiz itself is client-side because it depends on
    the visitor's date, exam and saved scores), plus a worked sample from one of its 30 sets. */
export function DailyQuizGuide() {
  const secs = availableSections();
  const pools = secs.map((s) => {
    const topics = listTopics(s);
    return { id: s, topics: topics.length, questions: topics.reduce((n, t) => n + (t.practice?.length ?? 0), 0) };
  });
  const order = SECTION_ORDER as readonly string[];
  const ordered = [...pools].sort((a, b) => order.indexOf(a.id) - order.indexOf(b.id));
  const sample = readSampleSet();
  const samples = (sample?.sections ?? [])
    .map((s) => ({ s, q: s.questions.find(plainEnough) }))
    .filter((x): x is { s: Bucket['sections'][number]; q: DailyQ } => !!x.q)
    .sort((a, b) => order.indexOf(a.s.section) - order.indexOf(b.s.section));

  return (
    <div className="mt-12">
      <section aria-labelledby="dq-how">
        <h2 id="dq-how" className="text-2xl font-extrabold">How the daily quiz works</h2>
        <p className="mt-2 text-[15px]">
          Each day the quiz shows a mixed set of up to 20 questions: four from each of the five subject areas (Quantitative Aptitude, Reasoning, English, General Awareness and Computer). You work through one subject at a time on its own tab, and every question comes with its explanation and, where one exists, a one-line exam shortcut.
        </p>
        <ul className="mt-3 list-disc pl-5 space-y-2 text-[15px]">
          <li><b>Tuned to your exam.</b> The quiz hides subjects that your selected exam does not test, so the set shrinks accordingly rather than padding it with irrelevant questions. Changing your selected exam changes the mix.</li>
          <li><b>Thirty rotating sets.</b> The questions are prepared in advance as 30 fixed sets and the set for today is chosen from the date, so the quiz cycles about once a month. The date is counted in UTC, which means the set changes at 5:30 am IST.</li>
          <li><b>A day counts when you finish a section.</b> Completing the mini-test for any one subject marks the day as done. Your streak is the number of consecutive days marked done; if you have not finished today yet, it counts up to yesterday instead of resetting.</li>
          <li><b>Practice and test behaviour.</b> The mini-tests work like the topic tests: you can learn from each explanation as you go, or use the timed mode, where every question has its own time budget.</li>
        </ul>
      </section>

      <section className="mt-9" aria-labelledby="dq-picked">
        <h2 id="dq-picked" className="text-2xl font-extrabold">Where the questions come from</h2>
        <p className="mt-2 text-[15px]">
          Daily questions are not a separate bank. They are drawn from the same practice sets as the topic pages: for each subject, all of its topic questions are shuffled once in a fixed order and the daily sets take the next four in turn. A question you meet here therefore also has a home on a topic page, where you can practise its neighbours.
        </p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Subject</th><th>Topics</th><th>Practice questions in the pool</th><th>Questions per day</th></tr></thead>
            <tbody>
              {ordered.map((p) => (
                <tr key={p.id}>
                  <td><Link className="underline decoration-dotted" href={`/${p.id}/`}>{SECTION_META[p.id as SectionId]?.name ?? p.id}</Link></td>
                  <td>{p.topics}</td>
                  <td>{p.questions.toLocaleString('en-IN')}</td>
                  <td>4</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="text-xs faint mt-2">Pool sizes are counted from the topic files on this site at the time the pages were built.</p>
      </section>

      <section className="mt-9" aria-labelledby="dq-review">
        <h2 id="dq-review" className="text-2xl font-extrabold">How to review a daily set</h2>
        <ol className="mt-3 list-decimal pl-5 space-y-2 text-[15px]">
          <li><b>Commit to an answer before the explanation.</b> If you were unsure, count it as unsure even if the guess was right.</li>
          <li><b>Sort each miss by cause.</b> A reading slip, a missing fact, a wrong method and an arithmetic error need different repairs. Write the cause in one line.</li>
          <li><b>Follow the question to its topic.</b> Each question belongs to a topic; open that topic page and attempt a few of its neighbours the same day.</li>
          <li><b>Come back later.</b> When you are logged in, wrong answers are saved to <Link className="underline" href="/revision/">My revision</Link>. Retry them after a gap, and schedule the repeats with the <Link className="underline" href="/revision-planner/">revision planner</Link>.</li>
        </ol>
        <p className="text-sm muted mt-3">
          For the habit behind this, see the guides on the <Link className="underline" href="/study-guides/error-notebook-for-exam-preparation/">error notebook</Link> and on <Link className="underline" href="/study-guides/revision-without-forgetting/">revising without forgetting</Link>.
        </p>
      </section>

      {samples.length > 0 && (
        <section className="mt-9" aria-labelledby="dq-sample">
          <h2 id="dq-sample" className="text-2xl font-extrabold">A sample from set 1 of 30</h2>
          <p className="text-sm muted mt-1">
            One question from each subject in the first of the 30 sets, with the full solution, so you can see the level and the explanation style before you start. Today&apos;s set above is different unless the rotation happens to be on set 1.
          </p>
          <div className="mt-3 space-y-3">
            {samples.map(({ s, q }, i) => {
              const topicId = q.id.includes('/') ? q.id.split('/')[0] : null;
              return (
                <SampleQuestion key={q.id} q={q} label={`${s.name}`} id={`dq-sample-${i + 1}`}
                  tags={topicId && q.topic ? <Link className="chip" href={`/${s.section}/${topicId}/practice/`}>{q.topic}</Link> : null} />
              );
            })}
          </div>
        </section>
      )}

      <section className="mt-9" aria-labelledby="dq-faq">
        <h2 id="dq-faq" className="text-2xl font-extrabold">Questions about the daily quiz</h2>
        <dl className="mt-3 space-y-4 text-[15px]">
          <div>
            <dt className="font-bold">Why do I see fewer than 20 questions?</dt>
            <dd className="muted mt-1">Your selected exam does not test every subject, and the quiz only shows the subjects it does. Switch exam to see a different mix.</dd>
          </div>
          <div>
            <dt className="font-bold">Will I get the same questions again?</dt>
            <dd className="muted mt-1">Yes, after the cycle of 30 sets repeats. The repeat is useful: attempt it as a check on whether last month&apos;s mistakes are fixed.</dd>
          </div>
          <div>
            <dt className="font-bold">Is the quiz enough on its own?</dt>
            <dd className="muted mt-1">No. Four questions per subject is a daily habit and a diagnostic, not full preparation. Use it to find weak topics, then work on those with the {plural(pools.reduce((n, p) => n + p.topics, 0), 'topic')} on the site, each with lessons, solved examples and a practice test.</dd>
          </div>
          <div>
            <dt className="font-bold">I missed a day. What happens to my streak?</dt>
            <dd className="muted mt-1">The streak counts consecutive finished days, so a missed day ends it. Start again the next day; the earlier sets are still there in the cycle.</dd>
          </div>
        </dl>
      </section>
    </div>
  );
}
