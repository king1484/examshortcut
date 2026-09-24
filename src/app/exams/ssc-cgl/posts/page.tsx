import Link from 'next/link';
import type { Metadata } from 'next';
import { getExam } from '@/lib/content';
import { Md } from '@/components/Md';
import { PostPlanner, type PlannerPost } from '@/components/PostPlanner';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL posts, salary & age limit checker — build your post preference',
  description: 'Every SSC CGL post with pay level, approximate in-hand salary and post-wise age limit. Enter your date of birth and category to see which posts you are eligible for, then order your post preference.',
};

export default function PostsPage() {
  const exam = getExam();
  const posts = (exam?.posts ?? []) as PlannerPost[];
  const cutoff: string = exam?.eligibility?.ageCutoffDate ?? '2026-01-01';

  return (
    <div className="max-w-3xl mx-auto">
      <nav className="text-xs faint"><Link href="/exams/ssc-cgl/" className="underline decoration-dotted">SSC CGL</Link> / Posts & eligibility</nav>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-2">SSC CGL posts, salary & age-limit checker</h1>
      <p className="muted mt-3 text-[15px]">
        CGL fills {posts.length}+ kinds of Group B and Group C posts. They differ in pay level, age limit, field vs desk work and where you get posted. Check which ones you can apply for, then rank them. You&apos;ll need this order when you fill the option form, and it decides which post you actually get.
      </p>

      <div className="mt-6"><PostPlanner posts={posts} cutoffDate={cutoff} /></div>

      <h2 className="text-2xl font-extrabold mt-10">Age relaxation</h2>
      <div className="tbl-wrap mt-3">
        <table className="tbl"><tbody>
          {(exam?.eligibility?.ageRelaxation ?? []).map((r: { category: string; years: string }) => (
            <tr key={r.category}><td className="font-semibold">{r.category}</td><td>{r.years}</td></tr>
          ))}
        </tbody></table>
      </div>
      {exam?.eligibility?.notes && <Md className="mt-2 text-sm muted">{exam.eligibility.notes}</Md>}

      <h2 className="text-2xl font-extrabold mt-10">How to choose</h2>
      <div className="card p-5 mt-3 text-sm space-y-2">
        <p><b>Pay first, then lifestyle.</b> AAO is Level 8. ASO, Inspectors and SI CBI are Level 7. JSO is Level 6. Auditor and Accountant are Level 5. Tax Assistant is Level 4. Within the same level, the day-to-day job is very different.</p>
        <p><b>Field or desk.</b> CBIC Preventive Officer, Examiner and Inspector jobs involve customs, excise or anti-evasion field work, often at ports and airports. CSS ASO is desk work in Delhi ministries with good promotion prospects. Income Tax Inspector is a mix of both.</p>
        <p><b>Posting.</b> CSS ASO is mostly Delhi. Income Tax and CBIC posts are zone-wise, so you stay in your region for longer. MEA ASO includes foreign postings.</p>
        <p><b>Extra hurdles.</b> JSO needs Statistics in your degree and a pass in Paper 2. SI CBI has physical and medical standards. Choose these only if you meet them.</p>
      </div>
      <p className="text-xs faint mt-4">In-hand figures are rough monthly estimates for an X-class city (7th CPC pay plus DA and HRA, before tax). Always confirm the age table and post list in the official notification on <a className="underline" href="https://ssc.gov.in" target="_blank" rel="noopener noreferrer">ssc.gov.in</a>. Where it differs from this page, the notification is correct.</p>
    </div>
  );
}
