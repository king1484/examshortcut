import Link from 'next/link';
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getGuide, listGuides } from '@/lib/content';
import { Md } from '@/components/Md';
import { SectionHead, pad2 } from '@/components/Lesson';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return listGuides().map((g) => ({ slug: g.id }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const g = getGuide(slug);
  if (!g) return {};
  return { title: g.title, description: g.description, openGraph: { title: g.title, description: g.description } };
}

export default async function GuidePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const g = getGuide(slug);
  if (!g) notFound();
  const related = (g.related ?? []).map((id) => getGuide(id)).filter((x): x is NonNullable<typeof x> => !!x && x.id !== g.id);

  const faqLd = g.faqs?.length ? {
    '@context': 'https://schema.org', '@type': 'FAQPage',
    mainEntity: g.faqs.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })),
  } : null;

  return (
    <div className="max-w-3xl mx-auto lesson">
      {faqLd && <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqLd) }} />}
      <div className="text-xs faint mt-2">
        <Link href="/exams/ssc-cgl/guides/" className="underline decoration-dotted">SSC CGL guides</Link>
        {g.lastVerified && <span> · checked {g.lastVerified}</span>}
      </div>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-1 leading-tight">{g.title}</h1>
      <Md className="mt-3 text-[15px] muted">{g.intro}</Md>

      {g.sections.length > 2 && (
        <nav className="card p-3 sm:p-4 mt-5" aria-label="On this page">
          <div className="kicker px-2">On this page</div>
          <div className="toc mt-1.5 sm:grid-cols-2">
            {g.sections.map((s, i) => <a key={s.id} href={`#${s.id}`}><b>{pad2(i + 1)}</b><span>{s.title}</span></a>)}
          </div>
        </nav>
      )}

      {g.sections.map((s, i) => (
        <section key={s.id} id={s.id} className="lesson-sec">
          <SectionHead n={i + 1} title={s.title} />
          <Md className="mt-3">{s.body}</Md>
        </section>
      ))}

      {g.faqs && g.faqs.length > 0 && (
        <section className="lesson-sec">
          <SectionHead n={g.sections.length + 1} title="Frequently asked questions" />
          <div className="space-y-2 mt-4">
            {g.faqs.map((f) => (
              <details key={f.q} className="card p-4">
                <summary className="font-bold cursor-pointer">{f.q}</summary>
                <Md className="mt-2 text-[15px]">{f.a}</Md>
              </details>
            ))}
          </div>
        </section>
      )}

      {related.length > 0 && (
        <div className="lesson-sec">
          <div className="kicker">Keep reading</div>
          <div className="grid sm:grid-cols-2 gap-3 mt-2.5">
            {related.map((r) => (
              <Link key={r.id} href={`/exams/ssc-cgl/guides/${r.id}/`} className="card p-4 hover:-translate-y-0.5 transition-transform">
                <div className="font-bold">{r.title}</div>
                <p className="text-xs muted mt-1">{r.description}</p>
              </Link>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
