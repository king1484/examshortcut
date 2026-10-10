import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { STUDY_GUIDES, GUIDE_DATE, getStudyGuide } from '@/lib/studyGuides';
import { Md } from '@/components/Md';
import { ShareResource } from '@/components/ShareResource';
import { PrintGuide } from '@/components/PrintGuide';

export const dynamic = 'force-static';
export const dynamicParams = false;
export const generateStaticParams = () => STUDY_GUIDES.map((g) => ({ slug: g.slug }));

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const g = getStudyGuide((await params).slug);
  if (!g) return {};
  const url = `/study-guides/${g.slug}/`;
  return { title: g.title, description: g.description, alternates: { canonical: url },
    openGraph: { title: g.title, description: g.description, url, type: 'article',
      images: [{ url: '/og.png', width: 1200, height: 630 }], publishedTime: g.published ?? GUIDE_DATE, modifiedTime: g.published ?? GUIDE_DATE },
    twitter: { card: 'summary_large_image', title: g.title, description: g.description, images: ['/og.png'] } };
}

export default async function StudyGuidePage({ params }: { params: Promise<{ slug: string }> }) {
  const g = getStudyGuide((await params).slug);
  if (!g) notFound();
  const url = `https://examshortcut.in/study-guides/${g.slug}/`;
  const ld = { '@context': 'https://schema.org', '@graph': [
    { '@type': 'Article', headline: g.title, description: g.description, url,
      datePublished: g.published ?? GUIDE_DATE, dateModified: g.published ?? GUIDE_DATE, inLanguage: 'en-IN',
      author: { '@type': 'Person', name: 'Vinay', url: 'https://examshortcut.in/about/' },
      publisher: { '@type': 'Organization', name: 'ExamShortcut', url: 'https://examshortcut.in/' },
      image: 'https://examshortcut.in/og.png', mainEntityOfPage: url },
    { '@type': 'BreadcrumbList', itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
      { '@type': 'ListItem', position: 2, name: 'Study guides', item: 'https://examshortcut.in/study-guides/' },
      { '@type': 'ListItem', position: 3, name: g.title, item: url },
    ] },
  ] };
  return (
    <article className="max-w-3xl mx-auto lesson study-guide">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld).replaceAll('<', '\\u003c') }} />
      <Link className="text-sm underline muted" href="/study-guides/">← All study guides</Link>
      <p className="kicker mt-4">{g.audience} · free</p>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-2 leading-tight">{g.title}</h1>
      <p className="text-xs faint mt-3">By <Link href="/about/" className="underline">Vinay</Link> · Published {new Date(g.published ?? GUIDE_DATE).toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Kolkata' })}</p>
      <p className="muted mt-4 text-base leading-relaxed">{g.intro}</p>
      <nav className="card p-4 mt-6" aria-label="On this page">
        <p className="kicker">On this page</p>
        <div className="toc mt-2">{g.sections.map((s, i) => <a key={s.id} href={`#${s.id}`}><b>{i + 1}</b><span>{s.title}</span></a>)}</div>
      </nav>
      {g.sections.map((s, i) => (
        <section key={s.id} id={s.id} className="lesson-sec">
          <h2 className="text-xl sm:text-2xl font-bold flex gap-3 items-start"><span className="sec-num mt-1">{i + 1}</span>{s.title}</h2>
          <Md className="mt-4">{s.body}</Md>
        </section>
      ))}
      <section className="lesson-sec">
        <h2 className="text-xl font-bold">Your next study session</h2>
        <ul className="check mt-4">{g.checklist.map((item) => <li key={item}>{item}</li>)}</ul>
        <div className="flex flex-wrap gap-3 mt-5 resource-actions">
          <Link href="/revision-planner/" className="btn btn-brand">Plan my revision</Link>
          <PrintGuide />
        </div>
      </section>
      <ShareResource title={g.title} path={`/study-guides/${g.slug}/`} />
      <section className="lesson-sec resource-related">
        <h2 className="text-xl font-bold">Keep learning</h2>
        <div className="grid sm:grid-cols-2 gap-3 mt-4">{g.related.map((slug) => {
          const related = getStudyGuide(slug);
          return related ? <Link className="card p-4 font-semibold" key={slug} href={`/study-guides/${slug}/`}>{related.title} →</Link> : null;
        })}</div>
        <p className="text-sm muted mt-5">Spot a mistake? <Link href="/contact/" className="underline">Send the page and the correction</Link>.</p>
      </section>
    </article>
  );
}
