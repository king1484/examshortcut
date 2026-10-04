import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Md } from '@/components/Md';
import { SubpageFrame, VerifiedChip, loadExamPage, pickFaqs, subPath, type Faq } from './common';

/* eslint-disable @typescript-eslint/no-explicit-any */
const levelNum = (s: string) => Number(String(s).match(/Level\s*(\d+)/i)?.[1] ?? 0);

export function SalaryPage({ id }: { id: string }) {
  const page = loadExamPage(id);
  if (!page) notFound();
  const { info, exam, year } = page;
  const lc = exam.latestCycle ?? {};
  const posts: any[] = exam.posts ?? [];
  const hasInHand = posts.some((p) => p.inHandApprox);
  const departments = Array.from(new Set(posts.map((p) => p.department).filter(Boolean)));
  const groups = Array.from(new Set(posts.map((p) => p.group).filter(Boolean)));

  // group posts by their printed pay level, highest first
  const byLevel = new Map<string, any[]>();
  for (const p of posts) {
    const k = String(p.payLevel ?? '');
    if (!k) continue;
    byLevel.set(k, [...(byLevel.get(k) ?? []), p]);
  }
  const levels = Array.from(byLevel.entries()).sort((a, b) => levelNum(b[0]) - levelNum(a[0]));
  const allSameLevel = levels.length === 1;
  const withSpecial = posts.filter((p) => p.special);

  const faqs: Faq[] = [];
  if (posts.length) {
    faqs.push({
      q: `Which posts are covered in ${info.name} and what is the pay level of each?`,
      a: allSameLevel
        ? `All ${posts.length} posts sit at ${levels[0][0]}: ${posts.map((p) => p.name).join('; ')}.`
        : posts.map((p) => `${p.name}${p.payLevel ? ` — ${p.payLevel}` : ''}`).join('; ') + '.',
    });
  }
  if (levels.length > 1) {
    faqs.push({
      q: `Which ${info.name} post has the highest pay level?`,
      a: `${levels[0][1].map((p: any) => p.name).join(', ')} (${levels[0][0]}), going by the pay levels listed in the data on this page.`,
    });
  }
  if (hasInHand) {
    faqs.push({
      q: `What is the approximate in-hand salary in ${info.name}?`,
      a: posts.filter((p) => p.inHandApprox).map((p) => `${p.name}: ${p.inHandApprox}`).join('; ') + '. These are estimates; your actual take-home depends on the city you are posted in and your deductions.',
    });
  }
  faqs.push(...pickFaqs(exam, /salary|in-hand|pay\b|best|vacanc|which posts|choose which|which graduate post/i, /which posts does .* cover|which posts are covered/i, 5));

  const uniqueFaqs = faqs.filter((f, i) => faqs.findIndex((g) => g.q === f.q) === i);

  return (
    <SubpageFrame
      id={id}
      kind="salary-and-posts"
      h1={`${info.name} ${year} salary & posts — pay level, in-hand, department`}
      faqs={uniqueFaqs}
      intro={
        <>
          <p>
            <b>{info.name}</b> ({exam.fullName}) fills {posts.length} {posts.length === 1 ? 'post' : 'posts'}
            {departments.length > 0 && <> across {departments.length === 1 ? 'one department or service' : `${departments.length} departments or services`}</>}
            {groups.length > 0 && <> in {groups.length === 1 ? 'group' : 'groups'} {groups.join(', ')}</>}. The table below lists each post with its department, group and pay level{hasInHand ? ' and an approximate monthly in-hand figure' : ''}, taken from the same verified data as the <Link className="underline" href={`/exams/${id}/`}>{info.name} guide</Link>.
          </p>
          <p>
            {allSameLevel
              ? <>Every post listed here sits at the same pay level: <b>{levels[0][0]}</b>. That makes the choice between posts less about salary and more about the work, the employer and where you would be posted.</>
              : levels.length > 1
                ? <>Pay levels run from <b>{levels[levels.length - 1][0]}</b> up to <b>{levels[0][0]}</b>, so the post you finally get matters as much as clearing the exam.</>
                : null}
            {lc.vacancies && <> The {lc.year} cycle lists <b>{Number(lc.vacancies).toLocaleString('en-IN')}</b> vacancies{lc.fee ? <> and an application fee of <b>{lc.fee}</b></> : null}.</>}
          </p>
          <p><VerifiedChip exam={exam} /></p>
        </>
      }
    >
      <h2 className="text-2xl font-extrabold mt-8">Posts, department, group and pay level</h2>
      <div className="tbl-wrap mt-3">
        <table className="tbl">
          <thead>
            <tr><th>Post</th><th>Department</th><th>Group</th><th>Pay level</th>{hasInHand && <th>Approx. in-hand</th>}</tr>
          </thead>
          <tbody>
            {posts.map((p) => (
              <tr key={p.name}>
                <td className="font-semibold">{p.name}</td>
                <td>{p.department ?? '—'}</td>
                <td>{p.group ?? '—'}</td>
                <td>{p.payLevel ?? '—'}</td>
                {hasInHand && <td>{p.inHandApprox ?? '—'}</td>}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {levels.length > 1 && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Posts grouped by pay level</h2>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Pay level</th><th>Posts</th></tr></thead>
              <tbody>
                {levels.map(([lvl, ps]) => (
                  <tr key={lvl}><td className="font-semibold whitespace-nowrap">{lvl}</td><td>{ps.map((p) => p.name).join(' · ')}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}

      {withSpecial.length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Special requirements and notes by post</h2>
          <ul className="card p-5 mt-3 space-y-2 text-sm list-disc pl-9">
            {withSpecial.map((p) => <li key={p.name}><b>{p.name}:</b> <Md inline>{p.special}</Md></li>)}
          </ul>
        </>
      )}

      <h2 className="text-2xl font-extrabold mt-10">What pay level and in-hand salary mean</h2>
      <div className="card p-5 mt-3 text-sm space-y-3">
        <p><b>Pay level.</b> Central government posts are placed on a pay matrix. A line such as &quot;Level 2 · ₹19,900–63,200&quot; says which row of the matrix the post sits in, followed by the entry pay and the top of the pay band as printed in the notification. The entry figure is the <i>basic</i> pay you start on; it is not what reaches your bank account.</p>
        <p><b>Basic pay versus in-hand.</b> In-hand (take-home) salary is basic pay plus allowances such as dearness allowance, house rent allowance and travel allowance, minus deductions. Allowances such as house rent and travel vary with the class of city you are posted in, which is why the same post can pay differently in different places.</p>
        <p><b>{hasInHand ? 'Why the in-hand figures here are approximate.' : 'Why this page does not give a single in-hand figure.'}</b> {hasInHand ? 'The in-hand column is a rough monthly estimate, not a guarantee; where it is blank the data only gives the official pay level.' : 'The data for this exam gives the official pay level only. Because allowances depend on the posting city and deductions depend on the individual, any single take-home number would be a guess, so none is shown.'}</p>
        <p><b>Group.</b> The group letter or label is how the post is classified in the notification. Posts in the same group can still sit at different pay levels, so always read the pay level column, not the group alone.</p>
        <p><b>Always confirm with the notification.</b> Pay levels, vacancies and department lists can change between cycles. The official notification is the final word.</p>
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Choosing between posts</h2>
      <div className="card p-5 mt-3 text-sm space-y-3">
        <p>Look at pay level first, then at the department and the nature of the job (desk, field or physical). Check any special requirements listed above before you rank posts, because a post you do not qualify for cannot be a fallback.</p>
        <p>
          Before you decide, confirm that you meet the age and education rules on the <Link className="underline" href={subPath(id, 'eligibility')}>{info.name} eligibility page</Link>, and see how the stages are scored on the <Link className="underline" href={subPath(id, 'exam-pattern')}>{info.name} exam pattern page</Link>.
          {id === 'ssc-cgl' && <> The <Link className="underline" href="/exams/ssc-cgl/posts/">CGL posts and preference builder</Link> lets you rank posts for your own date of birth and category.</>}
        </p>
      </div>
    </SubpageFrame>
  );
}
