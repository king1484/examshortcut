import Link from 'next/link';
import type { ReactNode } from 'react';
import { listMocks } from '@/lib/content';
import { getExamInfo } from '@/lib/exams';
import { TOOL_META, toolPath, toolsFor, type ToolKind } from '@/lib/examTools';
import { hubPath, subPath, type Faq } from '@/components/exam-subpages/common';

/* Page frame for the generic exam tools: breadcrumb, JSON-LD, heading, sibling-tool nav, the tool, FAQs
   and onward links. FAQ answers are plain text so the on-page copy and the FAQPage markup say the same thing. */

const SITE = 'https://examshortcut.in';

export function ToolPageFrame({ id, kind, h1, intro, faqs, children }: {
  id: string; kind: ToolKind; h1: string; intro: ReactNode; faqs: Faq[]; children: ReactNode;
}) {
  const info = getExamInfo(id)!;
  const meta = TOOL_META[kind];
  const url = `${SITE}${toolPath(id, kind)}`;
  const ld: object[] = [
    {
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: `${SITE}/` },
        { '@type': 'ListItem', position: 2, name: 'Exams', item: `${SITE}/exams/` },
        { '@type': 'ListItem', position: 3, name: info.name, item: `${SITE}${hubPath(id)}` },
        { '@type': 'ListItem', position: 4, name: meta.label, item: url },
      ],
    },
    {
      '@context': 'https://schema.org',
      '@type': 'SoftwareApplication',
      name: `${info.name} ${meta.label.toLowerCase()}`,
      url,
      applicationCategory: 'EducationalApplication',
      operatingSystem: 'Any (web browser)',
      isAccessibleForFree: true,
      offers: { '@type': 'Offer', price: '0', priceCurrency: 'INR' },
    },
  ];
  if (faqs.length) {
    ld.push({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: faqs.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })),
    });
  }

  const siblings = toolsFor(id).filter((k) => k !== kind);
  const hasMocks = listMocks(id).some((m) => m.available);
  const links: [string, string, string][] = [
    [hubPath(id), `${info.name} complete guide`, 'Status, dates, pattern, eligibility, FAQs'],
    [`/exams/${id}/cutoffs/`, `${info.name} cutoffs`, 'Past cut-offs, category-wise'],
    [subPath(id, 'exam-pattern'), `${info.name} exam pattern`, 'Sections, marks and timing'],
    [subPath(id, 'salary-and-posts'), `${info.name} salary and posts`, 'Pay levels and post list'],
    ...(hasMocks ? [[`/exams/${id}/mocks/`, 'Mock tests', 'Real CBT interface and analysis'] as [string, string, string]] : []),
  ];

  return (
    <article className="max-w-4xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />
      <nav aria-label="Breadcrumb" className="text-xs faint">
        <Link href="/exams/" className="underline decoration-dotted">Exams</Link> / <Link href={hubPath(id)} className="underline decoration-dotted">{info.name}</Link> / {meta.label}
      </nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-2">{h1}</h1>
      <div className="mt-3 text-[15px] muted space-y-3">{intro}</div>

      {siblings.length > 0 && (
        <nav aria-label={`More ${info.name} tools`} className="flex gap-2 flex-wrap mt-4">
          {siblings.map((k) => (
            <Link key={k} href={toolPath(id, k)} className="chip">{TOOL_META[k].emoji} {TOOL_META[k].label}</Link>
          ))}
        </nav>
      )}

      {children}

      {faqs.length > 0 && (
        <section aria-labelledby="faqs">
          <h2 id="faqs" className="text-2xl font-extrabold mt-10">{info.name} {meta.label.toLowerCase()}: FAQs</h2>
          <div className="mt-3 space-y-2">
            {faqs.map((f, i) => (
              <details key={i} className="card p-4">
                <summary className="font-semibold cursor-pointer text-sm">{f.q}</summary>
                <p className="mt-2 text-sm">{f.a}</p>
              </details>
            ))}
          </div>
        </section>
      )}

      <section className="mt-10" aria-labelledby="keep-going">
        <h2 id="keep-going" className="text-xl font-extrabold">Keep preparing for {info.name}</h2>
        <nav className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-3">
          {links.map(([href, t, s]) => (
            <Link key={href} href={href} className="card p-4 hover:-translate-y-0.5 transition-transform">
              <div className="font-bold text-sm">{t}</div>
              <div className="text-xs faint mt-0.5">{s}</div>
            </Link>
          ))}
        </nav>
      </section>
    </article>
  );
}
