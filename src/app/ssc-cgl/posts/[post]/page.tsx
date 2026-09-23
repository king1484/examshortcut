import Link from 'next/link';
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getExam } from '@/lib/content';
import { POST_DETAILS, salaryRows } from '@/lib/postDetails';
import type { PlannerPost } from '@/components/PostPlanner';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return ((getExam()?.posts ?? []) as PlannerPost[]).map((p) => ({ post: p.id }));
}

function getPost(id: string): PlannerPost | null {
  return ((getExam()?.posts ?? []) as PlannerPost[]).find((p) => p.id === id) ?? null;
}

export async function generateMetadata({ params }: { params: Promise<{ post: string }> }): Promise<Metadata> {
  const { post: id } = await params;
  const post = getPost(id);
  const d = POST_DETAILS[id];
  if (!post) return {};
  const short = post.name.replace(/ \(.*\)/, '');
  return {
    title: `SSC CGL ${short}: salary, job profile, promotion & age limit`,
    description: d?.tagline ?? post.special ?? `${post.name} in SSC CGL: ${post.payLevel}, in-hand ${post.inHandApprox}, age ${post.ageMin}–${post.ageMax}.`,
  };
}

export default async function PostPage({ params }: { params: Promise<{ post: string }> }) {
  const { post: id } = await params;
  const post = getPost(id);
  const d = POST_DETAILS[id];
  if (!post || !d) notFound();

  const level = parseInt(post.payLevel.match(/Level (\d)/)?.[1] ?? '0', 10);
  const short = post.name.replace(/ \(.*\)/, '');
  const others = ((getExam()?.posts ?? []) as PlannerPost[]).filter((p) => p.id !== id);

  const jsonLd = {
    '@context': 'https://schema.org', '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'SSC CGL', item: '/ssc-cgl/' },
      { '@type': 'ListItem', position: 2, name: 'Posts', item: '/ssc-cgl/posts/' },
      { '@type': 'ListItem', position: 3, name: post.name },
    ],
  };

  return (
    <div className="max-w-3xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <nav className="text-xs faint"><Link href="/ssc-cgl/" className="underline decoration-dotted">SSC CGL</Link> / <Link href="/ssc-cgl/posts/" className="underline decoration-dotted">Posts</Link> / {short}</nav>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-2">SSC CGL {short}: salary, job profile &amp; promotion</h1>
      <p className="muted mt-3 text-[15px]">{d.tagline}</p>

      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-6 text-sm">
        <div className="card p-3"><div className="text-xs faint">Pay level</div><b>{post.payLevel.split('·')[0].trim()}</b><div className="text-xs faint">{post.payLevel.split('·')[1]?.trim()}</div></div>
        <div className="card p-3"><div className="text-xs faint">In-hand (approx.)</div><b>{post.inHandApprox}</b><div className="text-xs faint">X-city, before tax</div></div>
        <div className="card p-3"><div className="text-xs faint">Age limit</div><b>{post.ageMin}–{post.ageMax}</b><div className="text-xs faint">+ relaxation by category</div></div>
        <div className="card p-3"><div className="text-xs faint">Group</div><b>{post.group === 'B' ? 'Group B' : 'Group C'}</b>{post.paper2 && <div className="text-xs faint">Paper 2 (Statistics)</div>}</div>
      </div>

      <h2 className="text-2xl font-extrabold mt-8">What the job actually is</h2>
      <p className="muted mt-2 text-[15px]">{d.about}</p>
      <ul className="list-disc ml-5 mt-3 space-y-1.5 text-[15px]">
        {d.profile.map((x) => <li key={x.slice(0, 32)}>{x}</li>)}
      </ul>

      <h2 className="text-2xl font-extrabold mt-8">Salary: how the in-hand figure is built</h2>
      <div className="tbl-wrap mt-3">
        <table className="tbl"><tbody>
          {salaryRows(level).map(([k, v]) => (
            <tr key={k} className={k.startsWith('Gross') || k.startsWith('Basic') ? 'font-semibold' : ''}><td>{k}</td><td className="text-right">{v}</td></tr>
          ))}
        </tbody></table>
      </div>
      <p className="text-xs faint mt-2">Indicative for 2026. DA revises twice a year, HRA depends on your posting city (X/Y/Z class) and stops if you take a government quarter, and TA varies by city and level. Where this differs from your office&apos;s first pay slip, the pay slip is right.</p>

      <h2 className="text-2xl font-extrabold mt-8">Career ladder</h2>
      <ol className="mt-3 space-y-2">
        {d.growth.map(([role, t]) => (
          <li key={role} className="card p-3 flex flex-wrap gap-x-3 items-baseline text-sm">
            <b>{role}</b><span className="text-xs muted ml-auto">{t}</span>
          </li>
        ))}
      </ol>
      <p className="text-xs faint mt-2">Times are typical ranges seen in recent years; cadre strength, zone and DPC regularity move them a lot.</p>

      <div className="grid sm:grid-cols-2 gap-3 mt-8">
        <div className="card p-4" style={{ borderColor: 'var(--ok)', borderWidth: 1 }}>
          <div className="font-extrabold text-sm" style={{ color: 'var(--ok)' }}>Choose it if</div>
          <p className="text-sm mt-1">{d.goodFor}</p>
        </div>
        <div className="card p-4" style={{ borderColor: 'var(--warn)', borderWidth: 1 }}>
          <div className="font-extrabold text-sm" style={{ color: 'var(--warn)' }}>Watch out for</div>
          <ul className="list-disc ml-5 mt-1 text-sm space-y-1">{d.watchOut.map((x) => <li key={x.slice(0, 32)}>{x}</li>)}</ul>
        </div>
      </div>
      {post.special && <p className="text-xs muted mt-3">Note from the notification summary: {post.special}</p>}

      <h2 className="text-2xl font-extrabold mt-10">Check yourself before you prefer it</h2>
      <div className="grid sm:grid-cols-2 gap-3 mt-3">
        <Link href="/ssc-cgl/posts/" className="card p-4"><div className="font-bold text-sm">🏛️ Age &amp; eligibility checker</div><div className="text-xs faint mt-1">Enter DOB + category, build your preference order</div></Link>
        <Link href="/ssc-cgl/score-calculator/" className="card p-4"><div className="font-bold text-sm">🧮 Score vs cut-off estimator</div><div className="text-xs faint mt-1">What rank this post usually needs</div></Link>
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Other posts</h2>
      <div className="flex flex-wrap gap-2 mt-3">
        {others.map((p) => (
          <Link key={p.id} href={`/ssc-cgl/posts/${p.id}/`} className="chip hover:opacity-80">{p.name.replace(/ \(.*\)/, '')}</Link>
        ))}
      </div>
    </div>
  );
}
