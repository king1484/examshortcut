import Link from 'next/link';
import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import { notFound } from 'next/navigation';
import { Md } from '@/components/Md';
import { DatePhases } from '@/components/DatePhases';
import { SECTION_META, getCutoffs, listTopics } from '@/lib/content';
import { getExamInfo } from '@/lib/exams';
import {
  computeSeries, getCalendar, getExpectedSpec, getProcess, getSyllabus, hasPage, pagesFor,
  type PageKind,
} from '@/lib/examPages';
import { VerifiedChip, hubPath, loadExamPage, plain, type Faq } from '@/components/exam-subpages/common';
import { ExamEvents } from './ExamEvents';

/* eslint-disable @typescript-eslint/no-explicit-any */
/* Generic info pages for every exam except SSC CGL (which keeps hand-written ones):
   syllabus, admit card / answer key / result, calendar, expected cut-off.
   Facts come from content/exams/<id>/{exam,process,syllabus,expected-cutoff,cutoffs}.json. */

export const pagePath = (id: string, kind: PageKind) => `/exams/${id}/${kind}/`;

const LABEL: Record<PageKind, string> = {
  syllabus: 'Syllabus',
  'admit-card': 'Admit card, answer key & result',
  calendar: 'Important dates',
  'expected-cutoff': 'Expected cut-off',
};
const BLURB: Record<PageKind, string> = {
  syllabus: 'Section-wise topics for every stage',
  'admit-card': 'How to download, check the key, read the result',
  calendar: 'Notification to result, with reminders',
  'expected-cutoff': 'Trend from past years, clearly marked as an estimate',
};
const EMOJI: Record<PageKind, string> = { syllabus: '📚', 'admit-card': '🎫', calendar: '🗓️', 'expected-cutoff': '🎯' };

const fmtDate = (iso: string) => new Date(`${iso}T00:00:00+05:30`).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'Asia/Kolkata' });
const fmtNum = (n: number) => (Number.isInteger(n) ? String(n) : n.toFixed(2).replace(/0$/, ''));

// ------------------------------------------------------------------ metadata
export function infoMeta(id: string, kind: PageKind): Metadata {
  const page = loadExamPage(id);
  if (!page || !hasPage(id, kind)) return {};
  const n = page.info.name;
  const y = page.year;
  let title = '';
  let description = '';
  if (kind === 'syllabus') {
    title = `${n} ${y} Syllabus: Section-wise Topics for Every Stage`;
    description = `${n} syllabus listed section by section for each stage, with the subjects, topic areas and links to notes and practice. Verified against the official notice pattern.`;
  } else if (kind === 'admit-card') {
    title = `${n} ${y} Admit Card, Answer Key and Result: How to Download and Check`;
    description = `${n} admit card, answer key and result explained step by step: where to sign in, when each is released, how the answer key objection works and how to read the scorecard.`;
  } else if (kind === 'calendar') {
    title = `${n} ${y} Important Dates: Notification, Exam, Result`;
    description = `${n} ${y} dates in one table, marked done, confirmed or expected, with a last verified date and one-click calendar reminders.`;
  } else {
    title = `${n} Expected Cut Off ${y}: Trend From Past Years`;
    description = `${n} previous cut-off trend by year and a rough range for the next cycle, clearly marked as an estimate and not an official figure.`;
  }
  return {
    title: { absolute: title },
    description,
    alternates: { canonical: pagePath(id, kind) },
    openGraph: { title, description },
    twitter: { card: 'summary_large_image', title, description },
  };
}

// ------------------------------------------------------------------ frame
function Frame({ id, kind, h1, intro, faqs, children }: {
  id: string; kind: PageKind; h1: string; intro: ReactNode; faqs: Faq[]; children: ReactNode;
}) {
  const info = getExamInfo(id)!;
  const crumbLd = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://examshortcut.in/' },
      { '@type': 'ListItem', position: 2, name: 'Exams', item: 'https://examshortcut.in/exams/' },
      { '@type': 'ListItem', position: 3, name: info.name, item: `https://examshortcut.in${hubPath(id)}` },
      { '@type': 'ListItem', position: 4, name: LABEL[kind], item: `https://examshortcut.in${pagePath(id, kind)}` },
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
  const siblings = pagesFor(id);
  return (
    <article className="max-w-4xl mx-auto">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />
      <nav aria-label="Breadcrumb" className="text-xs faint">
        <Link href="/exams/" className="underline decoration-dotted">Exams</Link> / <Link href={hubPath(id)} className="underline decoration-dotted">{info.name}</Link> / {LABEL[kind]}
      </nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-2">{h1}</h1>
      <div className="mt-3 text-[15px] muted space-y-3">{intro}</div>
      <nav aria-label={`${info.name} guide pages`} className="flex flex-wrap gap-2 mt-4 text-sm">
        <Link href={hubPath(id)} className="chip hover:underline">← {info.name} guide</Link>
        {siblings.map((k) => k === kind
          ? <span key={k} className="chip chip-brand" aria-current="page">{LABEL[k]}</span>
          : <Link key={k} href={pagePath(id, k)} className="chip hover:underline">{LABEL[k]}</Link>)}
      </nav>
      {children}
      {faqs.length > 0 && (
        <section aria-labelledby="faqs">
          <h2 id="faqs" className="text-2xl font-extrabold mt-10">{info.name} {LABEL[kind].toLowerCase()}: FAQs</h2>
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
      <section className="mt-10" aria-labelledby="keep-going">
        <h2 id="keep-going" className="text-xl font-extrabold">Keep preparing for {info.name}</h2>
        <nav className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-3">
          {[
            [hubPath(id), `${info.name} complete guide`, 'Status, pattern, eligibility, FAQs'],
            [`/exams/${id}/exam-pattern/`, `${info.name} exam pattern`, 'Stages, marks, negative marking'],
            ...(getCutoffs(id) ? [[`/exams/${id}/cutoffs/`, `${info.name} cutoffs`, 'Official, category-wise']] : []),
            ['/daily-quiz/', 'Daily quiz', 'A fresh mix every day'],
            ['/current-affairs/', 'Current affairs', 'Exam-relevant, month-wise'],
          ].map(([href, t, s]) => (
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

/** Block for the exam hubs: links to whichever of the four pages exist for that exam. */
export function ExamGuideLinks({ id }: { id: string }) {
  const info = getExamInfo(id);
  const kinds = pagesFor(id);
  if (!info || kinds.length === 0) return null;
  return (
    <section className="mt-6" aria-labelledby={`dates-${id}`}>
      <h2 id={`dates-${id}`} className="text-lg font-extrabold">Dates, syllabus and results for {info.name}</h2>
      <div className="grid sm:grid-cols-2 gap-3 mt-3">
        {kinds.map((k) => (
          <Link key={k} href={pagePath(id, k)} className="card p-4 hover:-translate-y-0.5 transition-transform">
            <div className="font-bold text-sm">{EMOJI[k]} {info.name} {LABEL[k].toLowerCase()}</div>
            <div className="text-xs faint mt-0.5">{BLURB[k]}</div>
          </Link>
        ))}
      </div>
    </section>
  );
}

// ------------------------------------------------------------------ syllabus
export function SyllabusInfoPage({ id }: { id: string }) {
  const page = loadExamPage(id);
  const syl = getSyllabus(id);
  if (!page || !syl || !hasPage(id, 'syllabus')) notFound();
  const { info, year } = page;
  const faqs: Faq[] = [
    { q: `What is the ${info.name} syllabus?`, a: `${syl.sections.map((s) => `${s.name} (${s.stage})`).join('; ')}. ${syl.intro}` },
    { q: `Where is the official ${info.name} syllabus published?`, a: `The conducting body is ${info.basics.conductingBody}. The syllabus and pattern are given in the official notification for each cycle, so check that notice before you finalise your plan.` },
  ];
  return (
    <Frame id={id} kind="syllabus" h1={`${info.name} ${year} syllabus: section-wise topics for every stage`} faqs={faqs}
      intro={<>
        <p>{syl.intro}</p>
        <p><VerifiedChip exam={{ lastVerified: syl.lastVerified }} /></p>
      </>}>
      {syl.note && <p className="text-sm muted mt-4">{syl.note}</p>}
      <div className="space-y-4 mt-6">
        {syl.sections.map((s) => {
          const hasNotes = s.sectionId && info.sections.includes(s.sectionId);
          const label = s.sectionId ? (info.sectionLabels?.[s.sectionId] ?? SECTION_META[s.sectionId].name) : s.name;
          return (
            <section key={s.name} className="card p-5" style={s.sectionId ? { borderTop: `3px solid ${SECTION_META[s.sectionId].color}` } : undefined}>
              <div className="flex items-baseline justify-between gap-2 flex-wrap">
                <h2 className="text-lg font-extrabold">{s.name}</h2>
                <span className="chip">{s.stage}</span>
              </div>
              <ul className="mt-3 space-y-1.5 text-sm list-disc pl-5">
                {s.topics.map((t) => <li key={t}>{t}</li>)}
              </ul>
              {s.tip && <p className="text-sm muted mt-3"><b>Tip:</b> {s.tip}</p>}
              {hasNotes && (
                <p className="text-sm mt-3">
                  <Link href={`/${s.sectionId}/`} className="underline underline-offset-2 font-semibold">{label} notes and practice</Link>
                  <span className="faint"> · {listTopics(s.sectionId!).length} topics</span>
                </p>
              )}
            </section>
          );
        })}
      </div>
      <p className="text-sm muted mt-6">
        For the number of questions, marks, timing and negative marking of each stage, see the <Link className="underline" href={`/exams/${id}/exam-pattern/`}>{info.name} exam pattern</Link>.
      </p>
    </Frame>
  );
}

// ------------------------------------------------------------------ admit card, answer key, result
const BUILT_AT = 0;
void BUILT_AT;

export function AdmitCardInfoPage({ id }: { id: string }) {
  const page = loadExamPage(id);
  const pr = getProcess(id);
  if (!page || !pr || !hasPage(id, 'admit-card')) notFound();
  const { info, exam, year } = page;
  const lc = exam.latestCycle ?? {};
  const phases = lc.status
    ? [{ node: <Md>{lc.status}</Md> }, ...(lc.statusPhases ?? []).map((ph: { from: string; status: string }) => ({ from: ph.from, node: <Md>{ph.status}</Md> }))]
    : [];
  const faqs: Faq[] = [
    { q: `Where do I download the ${info.name} admit card?`, a: `${pr.admitCard.where}. ${pr.admitCard.when}.` },
    pr.answerKey.released
      ? { q: `Is the ${info.name} answer key released, and can I challenge it?`, a: `${pr.answerKey.summary} ${pr.answerKey.fee}` }
      : { q: `Does ${info.name} release an answer key?`, a: pr.answerKey.summary },
    { q: `How do I check the ${info.name} result?`, a: `${pr.result.summary} ${pr.result.scorecard}` },
  ];
  return (
    <Frame id={id} kind="admit-card" h1={`${info.name} ${year}: admit card, answer key and result`} faqs={faqs}
      intro={<>
        <p>This page explains how the admit card, the answer key and the result work for {info.name}, which is conducted by {info.basics.conductingBody}. The official portal is <b>{pr.portal}</b>, and everything here should be checked against the notice for your cycle.</p>
        <p><VerifiedChip exam={{ lastVerified: pr.lastVerified }} /></p>
      </>}>
      {phases.length > 0 && (
        <div className="card p-5 mt-6">
          <h2 className="text-lg font-extrabold">Where the {lc.year ?? year} cycle stands</h2>
          <div className="status-callout"><span className="status-kicker">Latest</span><div className="mt-1.5"><DatePhases phases={phases} /></div></div>
          <p className="text-xs faint mt-2">Status as last verified on {fmtDate(exam.lastVerified)}. See the <Link className="underline" href={pagePath(id, 'calendar')}>important dates</Link> for the full list.</p>
        </div>
      )}

      <h2 className="text-2xl font-extrabold mt-10">Admit card</h2>
      <div className="card p-5 mt-3 text-sm">
        <p><b>Where:</b> {pr.admitCard.where}.</p>
        <p className="mt-1"><b>When:</b> {pr.admitCard.when}.</p>
        <ol className="mt-3 space-y-2">
          {pr.admitCard.steps.map((s, i) => (
            <li key={i} className="flex gap-3">
              <span className="shrink-0 w-6 h-6 rounded-full text-xs font-bold flex items-center justify-center" style={{ background: 'var(--brand-soft)', color: 'var(--brand-text)' }}>{i + 1}</span>
              <span>{s}</span>
            </li>
          ))}
        </ol>
        <h3 className="font-bold mt-4">What to carry</h3>
        <ul className="mt-1 space-y-1 list-disc pl-5">{pr.admitCard.carry.map((c) => <li key={c}>{c}</li>)}</ul>
        {pr.admitCard.note && <p className="mt-3 muted">{pr.admitCard.note}</p>}
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Answer key</h2>
      <div className="card p-5 mt-3 text-sm">
        <p>{pr.answerKey.summary}</p>
        {pr.answerKey.steps.length > 0 && (
          <ol className="mt-3 space-y-2 list-decimal pl-5">{pr.answerKey.steps.map((s) => <li key={s}>{s}</li>)}</ol>
        )}
        {pr.answerKey.released && <p className="mt-3"><b>Objection fee:</b> {pr.answerKey.fee}</p>}
        {pr.answerKey.note && <p className="mt-3 muted">{pr.answerKey.note}</p>}
      </div>

      <h2 className="text-2xl font-extrabold mt-10">Result and scorecard</h2>
      <div className="card p-5 mt-3 text-sm">
        <p>{pr.result.summary}</p>
        <div className="tbl-wrap mt-3">
          <table className="tbl">
            <thead><tr><th>Stage</th><th>What the result means</th></tr></thead>
            <tbody>{pr.result.stages.map((s) => <tr key={s.stage}><td className="font-semibold whitespace-nowrap">{s.stage}</td><td>{s.what}</td></tr>)}</tbody>
          </table>
        </div>
        <p className="mt-3"><b>Scorecard:</b> {pr.result.scorecard}</p>
        {getCutoffs(id) && <p className="mt-3">Once the result is out, compare your score with the <Link className="underline" href={`/exams/${id}/cutoffs/`}>official cutoffs</Link>.</p>}
      </div>
      <p className="text-xs faint mt-6">Source basis: {pr.sources.join('; ')}. Always follow the notice and the official website for your cycle.</p>
    </Frame>
  );
}

// ------------------------------------------------------------------ calendar
export function CalendarInfoPage({ id }: { id: string }) {
  const page = loadExamPage(id);
  const cal = getCalendar(id);
  if (!page || !cal || !hasPage(id, 'calendar')) notFound();
  const { info, exam, year } = page;
  const pr = getProcess(id);
  const portal = pr?.portal ?? 'the official website';
  const events = [...cal.events].sort((a, b) => a.start.localeCompare(b.start));
  const st = { done: 'done', confirmed: 'confirmed', expected: 'expected' } as const;
  const faqs: Faq[] = [
    {
      q: `What are the important dates for ${info.name} ${cal.cycle}?`,
      a: events.map((e) => `${e.title}: ${fmtDate(e.start)}${e.end && e.end !== e.start ? ` to ${fmtDate(e.end)}` : ''} (${st[e.status]})`).join('. ') + '.',
    },
    { q: `Which ${info.name} dates are confirmed and which are only expected?`, a: `Dates marked confirmed come from an official notice. Dates marked expected are estimates based on how earlier cycles ran, and they can move. Check ${portal} for the official notice.` },
  ];
  return (
    <Frame id={id} kind="calendar" h1={`${info.name} ${cal.cycle} important dates`} faqs={faqs}
      intro={<>
        <p>Every date we track for {info.name} in one place, from notification to the final stage. Each row is marked <b>done</b>, <b>confirmed</b> (from an official notice) or <b>expected</b> (an estimate).</p>
        <p><VerifiedChip exam={exam} /></p>
      </>}>
      <ExamEvents name={info.name} slug={info.id} portal={portal} events={events} />
      {cal.note && <p className="text-xs faint mt-3">{cal.note.replaceAll('*', '')}</p>}
      <p className="text-sm muted mt-4">
        Expected dates can move, and the exam body announces changes only on its own website ({portal}). Add reminders for the confirmed dates and look at the official site again a few days before each one. For the {year} cycle summary, see the <Link className="underline" href={hubPath(id)}>{info.name} guide</Link>.
      </p>
    </Frame>
  );
}

// ------------------------------------------------------------------ expected cut-off
export function ExpectedCutoffInfoPage({ id }: { id: string }) {
  const page = loadExamPage(id);
  const spec = getExpectedSpec(id);
  if (!page || !spec || !hasPage(id, 'expected-cutoff')) notFound();
  const { info, year } = page;
  const series = computeSeries(id);
  const first = series[0];
  const faqs: Faq[] = [
    { q: `What was the last ${info.name} cutoff?`, a: series.map((s) => `${s.label}: ${fmtNum(s.last.value)} in ${s.last.year}`).join('. ') + '.' },
    { q: `Is this ${info.name} expected cutoff official?`, a: `No. The past figures come from official result notices, but the range for the next cycle is our own rough estimate from the year-to-year change. The conducting body publishes the real cutoff only after the result.` },
    { q: `What marks should I aim for in ${info.name}?`, a: spec.target },
  ];
  return (
    <Frame id={id} kind="expected-cutoff" h1={`${info.name} expected cut-off ${year}: what past years suggest`} faqs={faqs}
      intro={<>
        <p>{spec.intro}</p>
        <p><VerifiedChip exam={{ lastVerified: spec.lastVerified }} /></p>
      </>}>
      <div className="callout callout-warn mt-5 text-sm">
        <b>This is an estimate, not an official cutoff.</b> The past figures are official. The range is simply the last cutoff plus or minus the average year-to-year change, so use it to set a target and not to predict a result.
      </div>
      {first && (
        <p className="text-sm muted mt-4">{spec.caveat}</p>
      )}
      <div className="space-y-5 mt-6">
        {series.map((s) => (
          <section key={s.id} className="card p-5">
            <h2 className="text-lg font-extrabold">{s.label}</h2>
            <div className="tbl-wrap mt-3">
              <table className="tbl">
                <thead><tr><th>Year</th><th>Cutoff</th>{s.maxMarks && <th>Share of {s.maxMarks}</th>}</tr></thead>
                <tbody>
                  {s.points.slice().reverse().map((p) => (
                    <tr key={p.year}>
                      <td className="font-bold">{p.year}</td>
                      <td>{fmtNum(p.value)}</td>
                      {s.maxMarks && <td>{Math.round((p.value / s.maxMarks) * 1000) / 10}%</td>}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="grid sm:grid-cols-3 gap-3 mt-4 text-sm">
              <div className="rounded-lg p-3" style={{ background: 'var(--surface-2)' }}>
                <div className="text-xs faint">Latest ({s.last.year})</div>
                <div className="font-extrabold text-lg">{fmtNum(s.last.value)}</div>
              </div>
              <div className="rounded-lg p-3" style={{ background: 'var(--surface-2)' }}>
                <div className="text-xs faint">Average change per year</div>
                <div className="font-extrabold text-lg">{fmtNum(s.swing)}</div>
              </div>
              <div className="rounded-lg p-3" style={{ background: 'var(--brand-soft)' }}>
                <div className="text-xs faint">Rough range for next cycle (estimate)</div>
                <div className="font-extrabold text-lg">{fmtNum(s.low)} to {fmtNum(s.high)}</div>
              </div>
            </div>
            {s.scaled && (
              <p className="text-sm muted mt-3">
                On a paper out of {s.scaled.to}, the same share of marks would be about {fmtNum(s.scaled.low)} to {fmtNum(s.scaled.high)}. The pattern has changed, so treat this only as a loose guide.
              </p>
            )}
          </section>
        ))}
      </div>

      <h2 className="text-2xl font-extrabold mt-10">What moves the cutoff</h2>
      <ul className="card p-5 mt-3 text-sm space-y-2 list-disc pl-9">
        {spec.factors.map((f) => <li key={f}>{f}</li>)}
      </ul>

      <h2 className="text-2xl font-extrabold mt-10">What to aim for</h2>
      <p className="card p-5 mt-3 text-sm">{spec.target}</p>
      <p className="text-sm muted mt-4">
        Full category-wise tables are on the <Link className="underline" href={`/exams/${id}/cutoffs/`}>{info.name} cutoffs page</Link>.
      </p>
    </Frame>
  );
}
