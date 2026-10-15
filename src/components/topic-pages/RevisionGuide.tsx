import Link from 'next/link';
import { SECTION_META, availableSections, listTopics } from '@/lib/content';
import type { SectionId } from '@/lib/sections';
import { REVIEW_OFFSETS, reviewDates } from '@/lib/revisionSchedule';
import { MathText } from '@/components/MathText';

const WHAT_TO_DO = [
  'Close the notes and write down the method or the key facts from memory, including one worked example.',
  'Attempt a few fresh questions on the topic without looking anything up, then mark them.',
  'Redo any question you missed from a blank page, and note whether the gap was a fact, a method or care.',
  'Do a mixed check: a couple of questions on this topic placed among questions from other topics, as in the real paper.',
] as const;

const fmt = (iso: string) => new Date(`${iso}T00:00:00Z`).toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short', timeZone: 'UTC' });

/** A written guide to spaced revision that sits under the planner: the site's own 1/3/7/14 schedule as a
    table, a worked plan built from real topic titles, per-subject recall prompts from the lessons and FAQs. */
export function RevisionGuide() {
  const picks = availableSections()
    .map((s) => {
      const t = listTopics(s).find((x) => x.subtopics.some((st) => (st.revision?.length ?? 0) > 0));
      const sub = t?.subtopics.find((st) => (st.revision?.length ?? 0) > 0);
      return t && sub ? { section: s, t, sub } : null;
    })
    .filter((x): x is NonNullable<typeof x> => !!x);

  // Worked plan: three topics learned on three consecutive days from a fixed illustrative start.
  const START = '2026-03-02';
  const learned = picks.slice(0, 3).map((p, i) => {
    const d = new Date(`${START}T00:00:00Z`);
    d.setUTCDate(d.getUTCDate() + i);
    const iso = d.toISOString().slice(0, 10);
    return { title: p.t.title, iso, reviews: reviewDates(iso) };
  });
  const days = new Map<string, string[]>();
  for (const l of learned) {
    if (!days.has(l.iso)) days.set(l.iso, []);
    days.get(l.iso)!.push(`Learn ${l.title}`);
    l.reviews.forEach((r, i) => {
      if (!days.has(r)) days.set(r, []);
      days.get(r)!.push(`Review ${l.title} (${i + 1}/${REVIEW_OFFSETS.length})`);
    });
  }
  const timeline = [...days.entries()].sort(([a], [b]) => a.localeCompare(b));

  return (
    <div className="mt-10">
      <section aria-labelledby="rg-why">
        <h2 id="rg-why" className="text-2xl font-extrabold">Why spaced revision works</h2>
        <p className="mt-2 text-[15px]">
          Material you read once is mostly gone within days unless you meet it again. Spaced revision means meeting it again at growing gaps: soon after learning, then after a few days, then after a couple of weeks. Each time, the useful part is the effort of pulling the idea out of memory with the notes closed. Rereading feels productive but tests recognition, which is easier than recall.
        </p>
        <p className="mt-2 text-[15px] muted">
          The planner above gives every topic four reviews. This is a convenient starting routine, not a fixed law of memory: harder topics may need an extra early review, and well-known ones may need fewer. The aim is a routine you will actually follow.
        </p>
      </section>

      <section className="mt-9" aria-labelledby="rg-schedule">
        <h2 id="rg-schedule" className="text-2xl font-extrabold">The schedule, review by review</h2>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Review</th><th>When</th><th>What to do</th></tr></thead>
            <tbody>
              {REVIEW_OFFSETS.map((d, i) => (
                <tr key={d}>
                  <td>{i + 1} of {REVIEW_OFFSETS.length}</td>
                  <td>{d} {d === 1 ? 'day' : 'days'} after you studied it</td>
                  <td className="text-sm">{WHAT_TO_DO[i]}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="text-sm muted mt-2">Each review should be short, around ten to twenty minutes per topic. If a review shows the topic has not stuck, treat it as a fresh study session and restart the sequence from that day.</p>
      </section>

      {timeline.length > 0 && (
        <section className="mt-9" aria-labelledby="rg-example">
          <h2 id="rg-example" className="text-2xl font-extrabold">A worked plan: three topics, three days</h2>
          <p className="text-sm muted mt-1">
            Suppose you learn {learned.map((l) => l.title).join(', ').replace(/, ([^,]*)$/, ' and $1')} on three consecutive days, starting on {fmt(START)} {START.slice(0, 4)}. The planner builds this calendar for you; the dates below are only an illustration.
          </p>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Date</th><th>Tasks that day</th></tr></thead>
              <tbody>
                {timeline.map(([iso, tasks]) => (
                  <tr key={iso}><td className="whitespace-nowrap">{fmt(iso)}</td><td className="text-sm">{tasks.join('; ')}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="text-sm muted mt-2">Notice that reviews of earlier topics start landing on the same days as new learning. Keep reviews first and short, so that new material does not push them out.</p>
        </section>
      )}

      {picks.length > 0 && (
        <section className="mt-9" aria-labelledby="rg-prompts">
          <h2 id="rg-prompts" className="text-2xl font-extrabold">What a closed-book review looks like</h2>
          <p className="text-sm muted mt-1">
            One example per subject, taken from the one-line takeaways at the end of our lessons. At the review, try to state each line from memory, then check yourself against the lesson.
          </p>
          <div className="mt-3 grid gap-3">
            {picks.map(({ section, t, sub }) => (
              <div key={t.id} className="card p-4">
                <div className="text-xs faint">{SECTION_META[section as SectionId]?.name ?? section}</div>
                <h3 className="font-extrabold">{t.title}: {sub.title}</h3>
                <ul className="mt-2 list-disc pl-5 space-y-1 text-sm">
                  {sub.revision!.slice(0, 3).map((r, i) => <li key={i}><MathText text={r} max={220} /></li>)}
                </ul>
                <p className="text-xs mt-2"><Link className="underline decoration-dotted" href={`/${section}/${t.id}/learn/${sub.id}/`}>Open the lesson →</Link></p>
              </div>
            ))}
          </div>
        </section>
      )}

      <section className="mt-9" aria-labelledby="rg-faq">
        <h2 id="rg-faq" className="text-2xl font-extrabold">Questions about the planner</h2>
        <dl className="mt-3 space-y-4 text-[15px]">
          <div>
            <dt className="font-bold">What if I miss a review?</dt>
            <dd className="muted mt-1">Do it the next day rather than skipping it. Do not try to catch up on several missed reviews at once; do the oldest topic first and let the rest follow over the next days.</dd>
          </div>
          <div>
            <dt className="font-bold">How many topics should I add?</dt>
            <dd className="muted mt-1">Only as many as you can review. Four reviews per topic add up: ten topics in a week is about forty short reviews in the following two weeks. Add topics at the pace you finish them, not the whole syllabus at once.</dd>
          </div>
          <div>
            <dt className="font-bold">Can I use it for topics that are not on this site?</dt>
            <dd className="muted mt-1">Yes. The planner takes any topic name; the suggestions are only a convenience.</dd>
          </div>
          <div>
            <dt className="font-bold">Where is my list stored?</dt>
            <dd className="muted mt-1">In this browser on this device. It is separate from the progress in your account, so clearing site data or switching device starts the list again. Download the calendar file if you want a copy.</dd>
          </div>
          <div>
            <dt className="font-bold">What does the calendar file contain?</dt>
            <dd className="muted mt-1">All-day events named like &ldquo;Review Percentage (2/4)&rdquo;. Notifications depend on your calendar app, and importing the same file twice may create duplicates in some apps.</dd>
          </div>
        </dl>
        <p className="text-sm muted mt-4">
          Related: <Link className="underline" href="/study-guides/revision-without-forgetting/">revising without forgetting</Link>, the <Link className="underline" href="/study-guides/error-notebook-for-exam-preparation/">error notebook guide</Link>, your <Link className="underline" href="/revision/">saved mistakes</Link> and the <Link className="underline" href="/formula-sheet/">formula sheet</Link> for quick closed-book checks.
        </p>
      </section>
    </div>
  );
}
