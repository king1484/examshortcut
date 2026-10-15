import Link from 'next/link';
import { listShiftDays, listShiftExams } from '@/lib/shifts';

/* Server-rendered explanation for /exam-analysis/ : how many days and shifts are covered, what the
   labels mean and how the figures should be read. Counts come from the shift-analysis data. */

export function ExamAnalysisGuide() {
  const exams = listShiftExams().map((e) => {
    const days = listShiftDays(e.slug);
    const shifts = days.flatMap((d) => d.shifts);
    const n = (s: string) => shifts.filter((x) => x.status === s).length;
    return { e, days: days.length, shifts: shifts.length, reported: n('reported'), partial: n('partial'), pending: n('pending') };
  });
  if (!exams.length) return null;
  return (
    <div className="mt-10">
      <section aria-labelledby="ea-cover">
        <h2 id="ea-cover" className="text-2xl font-extrabold">What is covered so far</h2>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Exam</th><th className="text-right">Days</th><th className="text-right">Shifts</th><th className="text-right">Reported</th><th className="text-right">Partial</th><th className="text-right">Pending</th></tr></thead>
            <tbody>
              {exams.map(({ e, days, shifts, reported, partial, pending }) => (
                <tr key={e.slug}>
                  <td><Link className="underline decoration-dotted" href={`/exam-analysis/${e.slug}/`}>{e.name}</Link></td>
                  <td className="text-right">{days}</td><td className="text-right">{shifts}</td>
                  <td className="text-right">{reported}</td><td className="text-right">{partial}</td><td className="text-right">{pending}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="mt-9" aria-labelledby="ea-read">
        <h2 id="ea-read" className="text-2xl font-extrabold">How to read a shift analysis</h2>
        <ul className="mt-3 space-y-2.5 text-[15px] list-disc pl-5">
          <li><b>Reported</b> means enough usable candidate reports were found for that shift. It describes how much source coverage there is, not whether the figures are official.</li>
          <li><b>Partial</b> means coverage is limited, or a figure was withheld because it failed a sanity check, for example an attempt count larger than the section size. Read the notes on the page before relying on it.</li>
          <li><b>Pending</b> means no usable report has been published yet. It does not mean the shift was cancelled.</li>
          <li><b>Difficulty</b> is what candidates reported and is subjective. A paper described as moderate can feel hard to a candidate who is weak in that section.</li>
          <li><b>Good attempts</b> is the range reports mention for a candidate who scored well. It is not a recommended number of attempts and it is not a safe score.</li>
          <li><b>Recalled questions</b> are remembered by candidates after the exam, so wording can differ from the paper and some will be wrong.</li>
        </ul>
        <p className="text-sm muted mt-3">
          Marks are normalised across shifts, so a harder shift does not mean a lower final score. The pages are meant for judging the style of the paper, not for predicting a result. The collection and checking process is described in the <Link className="underline" href="/editorial-policy/">content policy</Link>, and any error can be reported on the <Link className="underline" href="/feedback/">feedback page</Link>.
        </p>
      </section>

      <section className="mt-9" aria-labelledby="ea-use">
        <h2 id="ea-use" className="text-2xl font-extrabold">Using the analysis in your preparation</h2>
        <div className="mt-2 space-y-3 text-[15px]">
          <p>If you have not yet written the exam, read the section-wise topic lists for the shifts so far and check them against your plan: topics that appear in several shifts deserve a timed set, and topics that appear once are worth a revision pass.</p>
          <p>If you have written it, compare your own attempts with the good-attempt range and the section difficulty, then check <Link className="underline" href="/exams/ssc-cgl/score-calculator/">your score</Link> and where it sits against <Link className="underline" href="/exams/ssc-cgl/cutoffs/">past cutoffs</Link>.</p>
        </div>
      </section>
    </div>
  );
}
