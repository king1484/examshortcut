import Link from 'next/link';
import type { Metadata } from 'next';
import { Children, Fragment, isValidElement, type ReactNode } from 'react';
import { getExam, listMocks } from '@/lib/content';
import { getExamInfo, type ExamInfo } from '@/lib/exams';
import { listShiftExams } from '@/lib/shifts';
import { Md } from '@/components/Md';
import { fmtDate } from './ageModel';

/* Shared building blocks for the three search-intent sub-pages under /exams/<exam>/
   (eligibility, salary-and-posts, exam-pattern). Every fact comes from
   content/exams/<exam>/exam.json; nothing here invents dates, numbers or cut-offs. */

/* eslint-disable @typescript-eslint/no-explicit-any */
export type SubKind = 'eligibility' | 'salary-and-posts' | 'exam-pattern';
export interface Faq { q: string; a: string }

export const SUB_KINDS: SubKind[] = ['eligibility', 'salary-and-posts', 'exam-pattern'];
export const SUB_META: Record<SubKind, { label: string; blurb: string; emoji: string }> = {
  eligibility: { label: 'Eligibility', blurb: 'Age limit, qualification, relaxation + age calculator', emoji: '✅' },
  'salary-and-posts': { label: 'Salary & posts', blurb: 'Posts, pay level, in-hand pay explained', emoji: '💰' },
  'exam-pattern': { label: 'Exam pattern', blurb: 'Stages, marks, negative marking, selection', emoji: '📝' },
};

/** Per-exam label for a sub-page: MBA entrance exams have programs, not posts or pay levels. */
export function subMeta(id: string, kind: SubKind) {
  if (kind === 'salary-and-posts' && getExamInfo(id)?.category === 'MBA') {
    return { label: 'Institutes & programs', blurb: 'IIMs, FMS and CAP programs, shortlist weights', emoji: '🏛️' };
  }
  return SUB_META[kind];
}

export const hubPath = (id: string) => `/exams/${id}/`;
export const subPath = (id: string, kind: SubKind) => `/exams/${id}/${kind}/`;

/** The SSC MTS hub and its sub-pages still describe the 2025 cycle. */
export const isSscMtsArchive = (id: string) => id === 'ssc-mts';

export function SscMtsArchiveNote({ id, self = false }: { id: string; self?: boolean }) {
  if (!isSscMtsArchive(id)) return null;
  return (
    <div className="card p-3 mt-4 text-sm" style={{ borderLeft: '3px solid var(--warn)' }}>
      <strong>2025 cycle archive.</strong>{' '}
      This page documents the SSC MTS 2025 cycle, whose CBT was held in February 2026. The next cycle has not been verified as notified.{' '}
      {self
        ? <a href="#status" className="underline decoration-dotted">Jump to the latest cycle status →</a>
        : <Link href={hubPath(id)} className="underline decoration-dotted">Read the main SSC MTS guide for the latest status →</Link>}
    </div>
  );
}

export function loadExamPage(id: string): { info: ExamInfo; exam: any; year: number | string } | null {
  const info = getExamInfo(id);
  const exam = getExam(id);
  if (!info || !exam) return null;
  return { info, exam, year: exam.latestCycle?.year ?? new Date().getFullYear() };
}

/** Plain text for JSON-LD answers (markdown and math markers removed). */
export const plain = (s: unknown) => String(s ?? '').replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/[#*`$>]/g, '').replace(/\s+/g, ' ').trim();

/** Existing hand-written FAQs from the JSON whose question matches `re` (skipping those matching `skip`). */
export function pickFaqs(exam: any, re: RegExp, skip?: RegExp, cap = 5): Faq[] {
  return ((exam.faqs ?? []) as Faq[])
    .filter((f) => f?.q && f?.a && re.test(f.q) && !(skip && skip.test(f.q)))
    .slice(0, cap);
}

function cap(text: string, max: number) {
  const clean = text.replace(/\s+/g, ' ').trim();
  if (clean.length <= max) return clean;
  const cut = clean.slice(0, max - 1);
  const at = cut.lastIndexOf(' ');
  const base = at > Math.floor(max * 0.5) ? cut.slice(0, at) : cut;
  return `${base.replace(/[\s,;:·—–-]+$/, '')}…`;
}

export function metaFor(id: string, kind: SubKind): Metadata {
  const page = loadExamPage(id);
  if (!page) return {};
  const { info, exam, year } = page;
  const n = info.name;
  let title = '';
  let description = '';
  if (kind === 'eligibility') {
    title = `${n} ${year} Eligibility — Age Limit, Qualification, Relaxation`;
    const cutoff = exam.eligibility?.ageCutoffDate;
    description = `${n} eligibility: age limit by post, educational qualification, nationality and category-wise age relaxation, with a free age calculator${cutoff ? ` pre-set to the ${fmtDate(cutoff)} cut-off date` : ''}.`;
  } else if (kind === 'salary-and-posts' && info.category === 'MBA') {
    title = `${n} ${year} Institutes & Programs — IIMs, FMS, Shortlist Criteria`;
    description = `${n} participating institutes and programs: ${(exam.posts ?? []).length} listed with programme type, duration and how each shortlists, plus links to the exam pattern and eligibility.`;
  } else if (kind === 'salary-and-posts') {
    title = `${n} ${year} Salary & Posts — Pay Level, In-Hand, Department`;
    description = `${n} posts with department, group, pay level and what in-hand salary means: ${(exam.posts ?? []).length} posts listed, special requirements, and links to the exam pattern and eligibility.`;
  } else {
    title = `${n} ${year} Exam Pattern — Sections, Marks, Negative Marking`;
    description = `${n} exam pattern: stage-wise questions, marks, duration and negative marking, selection process, normalisation, and how to approach each section with topic links.`;
  }
  if (isSscMtsArchive(id)) {
    description = `Archive of the SSC MTS 2025 cycle. ${description}`;
  }
  title = cap(title, 60);
  description = cap(description, 160);
  return {
    title: { absolute: title },
    description,
    alternates: { canonical: subPath(id, kind) },
    openGraph: { title, description, images: ['/og.png'] },
    twitter: { card: 'summary_large_image', title, description, images: ['/og.png'] },
  };
}

function SiblingNav({ id, current }: { id: string; current: SubKind }) {
  const info = getExamInfo(id)!;
  return (
    <nav aria-label={`${info.name} guide pages`} className="flex flex-wrap gap-2 mt-4 text-sm">
      <Link href={hubPath(id)} className="chip hover:underline">← {info.name} guide</Link>
      {SUB_KINDS.map((k) =>
        k === current
          ? <span key={k} className="chip chip-brand" aria-current="page">{subMeta(id, k).label}</span>
          : <Link key={k} href={subPath(id, k)} className="chip hover:underline">{subMeta(id, k).label}</Link>)}
    </nav>
  );
}

/** "More on this exam" block for the exam hubs. */
export function MoreOnExam({ id }: { id: string }) {
  const info = getExamInfo(id);
  if (!info) return null;
  return (
    <section className="mt-6" aria-labelledby={`more-${id}`}>
      <h2 id={`more-${id}`} className="text-lg font-extrabold">More on {info.name}</h2>
      <div className="grid sm:grid-cols-3 gap-3 mt-3">
        {SUB_KINDS.map((k) => (
          <Link key={k} href={subPath(id, k)} className="card p-4 hover:-translate-y-0.5 transition-transform">
            <div className="font-bold text-sm">{subMeta(id, k).emoji} {info.name} {subMeta(id, k).label.toLowerCase()}</div>
            <div className="text-xs faint mt-0.5">{subMeta(id, k).blurb}</div>
          </Link>
        ))}
      </div>
    </section>
  );
}

export function RelatedLinks({ id, current }: { id: string; current: SubKind }) {
  const info = getExamInfo(id)!;
  const hasMocks = listMocks(id).some((m) => m.available);
  const analysis = listShiftExams().find((e) => e.guide === hubPath(id));
  const links: [string, string, string][] = [
    [hubPath(id), `${info.name} complete guide`, 'Status, dates, pattern, eligibility, FAQs'],
    ...SUB_KINDS.filter((k) => k !== current).map((k) => [subPath(id, k), `${info.name} ${subMeta(id, k).label.toLowerCase()}`, subMeta(id, k).blurb] as [string, string, string]),
    ...(hasMocks ? [[`/exams/${id}/mocks/`, 'Mock tests', 'Real CBT interface + analysis'] as [string, string, string]] : []),
    ['/daily-quiz/', 'Daily quiz', 'A fresh mix every day'],
    [analysis ? `/exam-analysis/${analysis.slug}/` : '/exam-analysis/', analysis ? `${analysis.name} analysis` : 'Exam analysis', 'Shift-wise difficulty and questions asked'],
    ['/learn/', 'Syllabus & topic notes', 'Formulas, shortcuts, topic tests'],
    ...(id === 'ssc-cgl' ? [
      ['/exams/ssc-cgl/syllabus/', 'CGL syllabus', 'Topic by topic'] as [string, string, string],
      ['/exams/ssc-cgl/cutoffs/', 'CGL cutoffs', 'Year × category official cutoffs'] as [string, string, string],
      ['/exams/ssc-cgl/posts/', 'Posts & preference builder', 'Rank posts by your eligibility'] as [string, string, string],
    ] : []),
    ['/current-affairs/', 'Current affairs', 'Exam-relevant, month-wise'],
  ];
  return (
    <section className="mt-10" aria-labelledby="related-links">
      <h2 id="related-links" className="text-xl font-extrabold">Keep preparing for {info.name}</h2>
      <nav className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-3">
        {links.map(([href, t, s]) => (
          <Link key={href} href={href} className="card p-4 hover:-translate-y-0.5 transition-transform">
            <div className="font-bold text-sm">{t}</div>
            <div className="text-xs faint mt-0.5">{s}</div>
          </Link>
        ))}
      </nav>
    </section>
  );
}

/** Page frame: breadcrumb + JSON-LD + heading + sibling nav + body + FAQ + related links. */
export function SubpageFrame({ id, kind, h1, intro, faqs, children }: {
  id: string; kind: SubKind; h1: string; intro: ReactNode; faqs: Faq[]; children: ReactNode;
}) {
  const info = getExamInfo(id)!;
  const label = subMeta(id, kind).label;
  // Keep the intro short: first paragraph (and the trailing verified chip) stay under the heading, the rest moves below.
  const introNodes = isValidElement(intro) && intro.type === Fragment
    ? Children.toArray((intro.props as { children?: ReactNode }).children)
    : [intro];
  const lead = introNodes.length > 2 ? [introNodes[0], introNodes[introNodes.length - 1]] : introNodes;
  const more = introNodes.length > 2 ? introNodes.slice(1, -1) : [];
  const crumbLd = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
      { '@type': 'ListItem', position: 2, name: 'Exams', item: 'https://examshortcut.in/exams/' },
      { '@type': 'ListItem', position: 3, name: info.name, item: `https://examshortcut.in${hubPath(id)}` },
      { '@type': 'ListItem', position: 4, name: label, item: `https://examshortcut.in${subPath(id, kind)}` },
    ],
  };
  const ld: object[] = [crumbLd];
  if (faqs.length) {
    ld.push({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: faqs.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: plain(f.a) } })),
    });
  }
  return (
    <article className="max-w-4xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />
      <nav aria-label="Breadcrumb" className="text-xs faint">
        <Link href="/exams/" className="underline decoration-dotted">Exams</Link> / <Link href={hubPath(id)} className="underline decoration-dotted">{info.name}</Link> / {label}
      </nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-2">{h1}</h1>
      <SscMtsArchiveNote id={id} />
      <div className="mt-3 text-[15px] muted space-y-3">{lead}</div>
      <SiblingNav id={id} current={kind} />
      {children}
      {more.length > 0 && (
        <section aria-labelledby="overview">
          <h2 id="overview" className="text-2xl font-extrabold mt-10">{info.name} {label.toLowerCase()} — overview</h2>
          <div className="card p-5 mt-3 text-sm muted space-y-3">{more}</div>
        </section>
      )}
      {faqs.length > 0 && (
        <section aria-labelledby="faqs">
          <h2 id="faqs" className="text-2xl font-extrabold mt-10">{info.name} {label.toLowerCase()} — FAQs</h2>
          <div className="mt-3 space-y-2">
            {faqs.map((f, i) => (
              <details key={i} className="card p-4">
                <summary className="font-semibold cursor-pointer text-sm">{f.q}</summary>
                <Md className="mt-2 text-sm">{f.a}</Md>
              </details>
            ))}
          </div>
        </section>
      )}
      <RelatedLinks id={id} current={kind} />
    </article>
  );
}

export function VerifiedChip({ exam }: { exam: any }) {
  if (!exam.lastVerified) return null;
  return (
    <span className="chip">✓ Data verified {new Date(`${exam.lastVerified}T00:00:00+05:30`).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'Asia/Kolkata' })}</span>
  );
}
