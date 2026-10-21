import type { Metadata } from 'next';
import { ExamPreparationLinks } from '@/components/ExamPreparationLinks';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getExamUpdate, listExamUpdates } from '@/lib/examUpdates';
import { isOfficialUpdateUrl, UPDATE_LABELS, updateDate } from '@/lib/examUpdateRules';
import { getExamInfo } from '@/lib/exams';
import { ExamUpdateCards } from '@/components/ExamUpdateCards';

export const dynamic = 'force-static';
export const dynamicParams = false;
export function generateStaticParams() { return listExamUpdates().map(item => ({ slug: item.slug })); }
type Props = { params: Promise<{ slug: string }> };
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const item = getExamUpdate((await params).slug);
  if (!item) return {};
  return { title: { absolute: `${item.title} · ExamShortcut` }, description: item.summary,
    alternates: { canonical: `/exam-updates/${item.slug}/` },
    openGraph: { type: 'article', title: item.title, description: item.summary, publishedTime: item.publishedAt, modifiedTime: item.updatedAt, authors: ['ExamShortcut'], images: ['/og.png'] },
  };
}
export default async function ExamUpdatePage({ params }: Props) {
  const item = getExamUpdate((await params).slug);
  if (!item) notFound();
  const exam = getExamInfo(item.examId);
  const sources = item.sources.filter(source => isOfficialUpdateUrl(source.url));
  const url = `https://examshortcut.in/exam-updates/${item.slug}/`;
  const schema = [{ '@context': 'https://schema.org', '@type': 'NewsArticle', headline: item.title, description: item.summary, mainEntityOfPage: url,
    datePublished: item.publishedAt, dateModified: item.updatedAt, inLanguage: 'en-IN', image: ['https://examshortcut.in/og.png'],
    author: { '@type': 'Organization', name: 'ExamShortcut', url: 'https://examshortcut.in/about/' },
    publisher: { '@id': 'https://examshortcut.in/#org' }, citation: sources.map(s => s.url),
  }, { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
    { '@type': 'ListItem', position: 2, name: 'Exam updates', item: 'https://examshortcut.in/exam-updates/' },
    { '@type': 'ListItem', position: 3, name: item.title, item: url },
  ] }];
  const related = listExamUpdates().filter(other => other.slug !== item.slug && (other.examId === item.examId || other.kind === item.kind)).slice(0, 3);
  return <article className="max-w-4xl mx-auto exam-updates">
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(schema).replace(/</g, '\\u003c') }} />
    <nav aria-label="Breadcrumb" className="text-sm muted mb-5"><Link href="/exam-updates/" className="underline">Exam updates</Link> / <Link href={`/exams/${item.examId}/`} className="underline">{exam?.name}</Link></nav>
    <div className="flex flex-wrap gap-2"><span className="chip chip-brand">{UPDATE_LABELS[item.kind]}</span><span className="chip">{item.status}</span></div>
    <h1 className="text-3xl sm:text-4xl font-extrabold mt-4 leading-tight">{item.title}</h1>
    <p className="mt-4 text-lg muted">{item.summary}</p>
    <div className="text-xs muted mt-4 flex flex-wrap gap-x-4 gap-y-2"><span>By <Link href="/about/" className="underline">ExamShortcut</Link></span><span>Published <time dateTime={item.publishedAt}>{updateDate(item.publishedAt)}</time></span><span>Updated <time dateTime={item.updatedAt}>{updateDate(item.updatedAt)}</time></span><span>Source checked {updateDate(item.verifiedAt)}</span></div>
    <section className="card p-5 mt-6" aria-labelledby="official-notices">
      <h2 id="official-notices" className="text-lg font-extrabold">Open the official notice</h2>
      <p className="text-sm muted mt-1">{item.cycle}{item.noticeDate ? ` · Notice dated ${updateDate(item.noticeDate)}` : ' · Notice publication date not established in this review'}</p>
      <div className="flex flex-wrap gap-3 mt-4">{sources.map((source, index) => <a className={`btn ${index === 0 ? 'exam-update-primary' : ''}`} href={source.url} target="_blank" rel="noopener noreferrer" key={source.url}>{source.label} <span aria-hidden="true">↗</span><span className="sr-only"> (opens in a new tab)</span></a>)}</div>
      <p className="text-xs muted mt-3">This is an independent explanation. The recruiting body&apos;s notice and candidate portal decide your status.</p>
      {sources.some(source => source.url.startsWith('https://rrb.indianrailways.gov.in/')) && <p className="text-xs muted mt-2">If a direct PDF does not open, use the linked RRB notice table and select the document&apos;s English version.</p>}
    </section>
    <dl className="exam-update-facts mt-5">{item.facts.map(fact => <div className="card p-4" key={fact.label}><dt className="text-xs font-bold uppercase muted">{fact.label}</dt><dd className="font-semibold mt-1">{fact.value}</dd></div>)}</dl>
    {item.sections.map(section => <section key={section.title} className="mt-8"><h2 className="text-xl font-extrabold">{section.title}</h2><p className="muted mt-3 leading-relaxed">{section.body}</p></section>)}
    <section className="card p-5 mt-8"><h2 className="text-xl font-extrabold">What to do next</h2><ol className="list-decimal pl-5 space-y-3 mt-4">{item.nextSteps.map(step => <li key={step}>{step}</li>)}</ol></section>
    <nav className="flex flex-wrap gap-3 mt-6" aria-label="Continue with this exam"><Link className="btn" href={`/exams/${item.examId}/`}>{exam?.name} guide</Link><Link className="btn" href={`/exams/${item.examId}/calendar/`}>Important dates</Link><Link className="btn" href={`/exams/${item.examId}/admit-card/`}>Result and admit-card guide</Link></nav>
    <p className="text-sm muted mt-6">Compiled from the official sources linked above. <Link href="/editorial-policy/" className="underline">Source and corrections policy</Link> · <Link href="/feedback/" className="underline">Report a correction</Link>.</p>
    <ExamPreparationLinks examId={item.examId} />
    {related.length > 0 && <section className="mt-10"><h2 className="font-extrabold text-2xl mb-4">Related updates</h2><ExamUpdateCards items={related} /></section>}
  </article>;
}
