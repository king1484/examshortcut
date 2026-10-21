import Link from 'next/link';
import type { Metadata } from 'next';
import { listGuides, type Guide } from '@/lib/content';
import { getExamInfo } from '@/lib/exams';
import { Md } from '@/components/Md';
import { GuideChecklist } from '@/components/GuideChecklist';
import { PrintGuide } from '@/components/PrintGuide';
import { ShareResource } from '@/components/ShareResource';
import { ExamUpdatesForExam } from '@/components/ExamUpdatesForExam';
import { isOfficialUpdateUrl, updateDate } from '@/lib/examUpdateRules';

export function examGuideMetadata(examId: string, guide: Guide): Metadata {
  const path = `/exams/${examId}/guides/${guide.id}/`;
  return { title: guide.title, description: guide.description, alternates: { canonical: path },
    openGraph: { type: 'article', title: guide.title, description: guide.description, url: path, images: ['/og.png'], publishedTime: guide.publishedAt, modifiedTime: guide.updatedAt ?? guide.publishedAt },
    twitter: { card: 'summary_large_image', title: guide.title, description: guide.description, images: ['/og.png'] } };
}

export function ExamGuideArticle({ examId, guide: g }: { examId: string; guide: Guide }) {
  const name = getExamInfo(examId)?.name ?? examId;
  const path = `/exams/${examId}/guides/${g.id}/`;
  const url = `https://examshortcut.in${path}`;
  const related = listGuides(examId).filter(guide => guide.id !== g.id).slice(0, 3);
  const graph = { '@context': 'https://schema.org', '@graph': [
    { '@type': 'Article', headline: g.title, description: g.description, url, mainEntityOfPage: url, inLanguage: 'en-IN',
      ...(g.publishedAt ? { datePublished: g.publishedAt, dateModified: g.updatedAt ?? g.publishedAt } : {}),
      author: { '@type': 'Organization', name: 'ExamShortcut', url: 'https://examshortcut.in/about/' },
      publisher: { '@type': 'Organization', name: 'ExamShortcut', url: 'https://examshortcut.in/' }, image: 'https://examshortcut.in/og.png' },
    { '@type': 'BreadcrumbList', itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Exams', item: 'https://examshortcut.in/exams/' },
      { '@type': 'ListItem', position: 2, name, item: `https://examshortcut.in/exams/${examId}/` },
      { '@type': 'ListItem', position: 3, name: 'Guides', item: `https://examshortcut.in/exams/${examId}/guides/` },
      { '@type': 'ListItem', position: 4, name: g.title, item: url },
    ] },
  ] };
  return <article className="max-w-3xl mx-auto lesson study-guide">
    <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(graph).replaceAll('<', '\\u003c') }} />
    <Link className="underline text-sm" href={`/exams/${examId}/guides/`}>← {name} guides</Link>
    <p className="kicker mt-5">Free preparation &amp; next steps</p>
    <h1 className="text-3xl sm:text-4xl font-extrabold mt-2 leading-tight">{g.title}</h1>
    <p className="text-sm muted mt-3">By <Link href="/about/" className="underline">ExamShortcut</Link>{g.publishedAt && <> · Published {updateDate(g.publishedAt)}</>}{g.lastVerified && <> · Checked {updateDate(g.lastVerified)}</>}</p>
    <Md className="mt-4 muted">{g.intro}</Md>
    <nav className="card p-4 mt-6" aria-label="On this page"><p className="kicker">In this guide</p><div className="toc mt-2">{g.sections.map((section, i) => <a key={section.id} href={`#${section.id}`}><b>{i + 1}</b><span>{section.title}</span></a>)}</div></nav>
    {g.sections.map((section, i) => <section key={section.id} id={section.id} className="lesson-sec"><h2 className="text-xl sm:text-2xl font-bold">{i + 1}. {section.title}</h2><Md className="mt-4">{section.body}</Md></section>)}
    {!!g.drills?.length && <section className="lesson-sec"><h2 className="text-2xl font-bold">Try it before opening the answer</h2><p className="muted mt-2">Original learning checks, not recalled exam questions or a prediction of your score.</p><div className="space-y-3 mt-4">{g.drills.map((drill, i) => <details key={drill.prompt} className="card p-4"><summary className="font-semibold cursor-pointer min-h-11">{i + 1}. {drill.prompt}</summary><p className="mt-3 font-bold">{drill.answer}</p><Md className="mt-2">{drill.explanation}</Md></details>)}</div></section>}
    {!!g.checklist?.length && <GuideChecklist guideKey={`${examId}:${g.id}`} items={g.checklist} />}
    {!!g.sources?.length && <section className="lesson-sec"><h2 className="text-xl font-bold">Official references</h2><p className="text-sm muted mt-2">Use the matching cycle’s notice and call letter for eligibility, dates and test rules. Study routines and examples above are our editorial suggestions.</p><ul className="space-y-3 mt-4">{g.sources.filter(source => isOfficialUpdateUrl(source.url)).map(source => <li key={source.url}><a className="underline underline-offset-4 break-words" href={source.url} target="_blank" rel="noopener noreferrer">{source.label} ↗<span className="sr-only"> (opens in a new tab)</span></a></li>)}</ul></section>}
    {!!g.faqs?.length && <section className="lesson-sec"><h2 className="text-xl font-bold">Common questions</h2><div className="space-y-3 mt-4">{g.faqs.map(faq => <details key={faq.q} className="card p-4"><summary className="font-semibold cursor-pointer">{faq.q}</summary><Md className="mt-3">{faq.a}</Md></details>)}</div></section>}
    <div className="flex flex-wrap gap-3 mt-8"><Link href={`/exams/${examId}/syllabus/`} className="btn">Check the syllabus</Link><Link href="/revision-planner/" className="btn btn-brand">Plan my revision</Link><PrintGuide /></div>
    <ShareResource title={g.title} path={path} />
    <ExamUpdatesForExam examId={examId} />
    {!!related.length && <section className="lesson-sec"><h2 className="text-xl font-bold">More {name} guides</h2><ul className="mt-3 space-y-3">{related.map(guide => <li key={guide.id}><Link className="underline" href={`/exams/${examId}/guides/${guide.id}/`}>{guide.title}</Link></li>)}</ul></section>}
    <p className="text-sm muted mt-7">Found an error? <Link className="underline" href="/contact/">Send the page and correction</Link>. <Link className="underline" href="/editorial-policy/">How we check content</Link>.</p>
  </article>;
}
