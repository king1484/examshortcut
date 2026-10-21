import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { SECTION_META } from '@/lib/sections';
import { Md } from '@/components/Md';
import {
  allShiftParams, dayLabel, daySlug, difficultyColor, getShiftExam, hasAnalysis, listShiftDays, resolveSlug, shiftLabel, shiftSlug,
  type Shift, type ShiftDay, type ShiftExam,
} from '@/lib/shifts';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return allShiftParams();
}

type Params = { params: Promise<{ exam: string; slug: string }> };
const BASE = 'https://examshortcut.in';

function titleFor(exam: ShiftExam, day: ShiftDay, shift: Shift | null) {
  return shift
    ? `${exam.short} ${dayLabel(day.date)} Shift ${shift.shift} Analysis — Difficulty, Questions Asked`
    : `${exam.short} Exam Analysis ${dayLabel(day.date)} — All Shifts, Difficulty, Good Attempts`;
}
function descFor(exam: ShiftExam, day: ShiftDay, shift: Shift | null) {
  if (shift) {
    if (shift.status === 'pending') return `${exam.name} ${dayLabel(day.date)} Shift ${shift.shift} (${shift.time}): no usable analysis has been published yet. Reports are added when sufficient candidate feedback is available.`;
    if (shift.status === 'not-held') {
      const held = day.shifts.filter(hasAnalysis);
      return `No ${exam.short} exam was held in Shift ${shift.shift} (${shift.time}) on ${dayLabel(day.date)}. ${held.length ? `The first shift conducted was Shift ${held[0].shift} (${held[0].time}) — ${held[0].overall}, good attempts ${held[0].goodAttempts ?? '—'}.` : ''}`.trim();
    }
    return `${exam.name} ${dayLabel(day.date)} Shift ${shift.shift} (${shift.time}) review: overall ${shift.overall ?? 'difficulty'}, good attempts ${shift.goodAttempts ?? '—'}, section-wise difficulty and topics/questions asked, compiled from candidate reports.`;
  }
  const done = day.shifts.filter(hasAnalysis);
  return `${exam.name} ${dayLabel(day.date)} exam analysis, shift by shift: ${done.map((s) => `Shift ${s.shift} ${s.overall}`).join(', ') || 'updated shift by shift'} — good attempts, section-wise difficulty and questions asked.`;
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { exam: examSlug, slug } = await params;
  const exam = getShiftExam(examSlug);
  const r = resolveSlug(examSlug, slug);
  if (!exam || !r) return {};
  const title = titleFor(exam, r.day, r.shift);
  const description = descFor(exam, r.day, r.shift);
  /* A shift page is indexable once it has usable analysis; pending shifts stay
     noindex. A day page needs at least two usable shifts, and if every usable
     shift is only partial we wait for at least one complete analysis. */
  const analysed = r.day.shifts.filter(hasAnalysis);
  const thinDay = !r.shift && (
    analysed.length < 2 ||
    (r.day.shifts.some((s) => s.status === 'pending' || s.status === 'partial') && !analysed.some((s) => s.status === 'reported'))
  );
  return {
    title: { absolute: title },
    description,
    robots: r.shift?.status === 'pending' || thinDay ? { index: false, follow: true } : undefined,
    openGraph: { title, description, type: 'article', url: `${BASE}/exam-analysis/${examSlug}/${slug}/`, modifiedTime: r.day.updatedAt, images: ['/og.png'] },
    twitter: { card: 'summary_large_image', title, description, images: ['/og.png'] },
  };
}

const istTime = (iso: string) =>
  new Date(iso).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', day: 'numeric', month: 'short', hour: 'numeric', minute: '2-digit' }) + ' IST';

function DiffChip({ label }: { label?: string }) {
  const text = label && label !== 'Not reliably reported' ? label : 'Not reported';
  const unknown = /not reported|not held|awaiting|coming soon/i.test(text);
  const c = unknown ? 'var(--ink-2)' : difficultyColor(text);
  return <span className="analysis-label" style={{ color: c, borderColor: unknown ? 'var(--line)' : c }}>{text}</span>;
}

function StatusLabel({ shift }: { shift: Shift }) {
  return <span className={`analysis-status analysis-status-${shift.status}`}>{shift.status === 'reported' ? 'Reported' : shift.status === 'partial' ? 'Partial coverage' : shift.status === 'not-held' ? 'Not held' : 'Awaiting sources'}</span>;
}

function attempts(value?: string) {
  return !value || value === 'Not reliably reported' ? 'Not reported' : value.replace(/\s+overall$/i, '');
}

function Stat({ k, v, color }: { k: string; v: React.ReactNode; color?: string }) {
  return (
    <div className="analysis-stat" style={color ? { borderTop: `3px solid ${color}` } : undefined}>
      <div className="text-xs uppercase tracking-wide faint font-bold">{k}</div>
      <div className="text-lg font-extrabold mt-1">{v}</div>
    </div>
  );
}

function autoFaqs(exam: ShiftExam, day: ShiftDay, shift: Shift) {
  const when = `${dayLabel(day.date)} Shift ${shift.shift}`;
  const f: { q: string; a: string }[] = [];
  if (shift.status === 'not-held') {
    const held = day.shifts.filter(hasAnalysis);
    f.push({ q: `Was there an ${exam.short} exam in ${when}?`, a: `${shift.note ?? `No — the ${shift.time} slot was not conducted.`}${held.length ? ` The exam ran in ${held.map((s) => `Shift ${s.shift} (${s.time})`).join(' and ')}.` : ''}` });
    return f;
  }
  if (shift.overall) f.push({ q: `How was the ${exam.short} ${when} paper?`, a: `Candidates rated the ${when} paper ${shift.overall} overall.${shift.summary ? ' ' + shift.summary : ''}` });
  if (shift.goodAttempts && shift.goodAttempts !== 'Not reliably reported') f.push({ q: `What attempt range was reported for ${exam.short} ${when}?`, a: `${shift.goodAttempts} out of 100 questions, according to the linked reviews. This is an unofficial reported range, not a recommended attempt count or safe-score prediction.` });
  for (const s of shift.sections ?? []) {
    if (s.topics?.length) f.push({ q: `Which ${s.name} topics were asked in ${exam.short} ${when}?`, a: `${s.name} was ${s.difficulty}. Topics reported: ${s.topics.map((t) => t.topic + (t.count ? ` (${t.count})` : '')).join(', ')}.` });
  }
  return f;
}

function ShiftView({ exam, day, shift }: { exam: ShiftExam; day: ShiftDay; shift: Shift }) {
  const others = day.shifts.filter((s) => s.shift !== shift.shift);
  const bySection = (shift.asked ?? []).reduce<Record<string, typeof shift.asked>>((acc, q) => {
    (acc[q.section] ??= []).push(q); return acc;
  }, {});
  return (
    <>
      {shift.alsoCalled && <p className="text-sm muted mt-4">{shift.alsoCalled}</p>}
      {shift.status === 'not-held' ? (
        <div className="card p-5 mt-6" style={{ borderLeft: '3px solid var(--line)' }}>
          <h2 className="font-extrabold">No exam in this shift</h2>
          {shift.note && <p className="text-sm muted mt-1">{shift.note}</p>}
          {others.some(hasAnalysis) && (
            <div className="flex gap-2 flex-wrap mt-3 text-sm">
              {others.filter(hasAnalysis).map((s) => (
                <Link key={s.shift} className="btn btn-brand" href={`/exam-analysis/${exam.slug}/${shiftSlug(day.date, s.shift)}/`}>Shift {s.shift} ({s.time}) analysis →</Link>
              ))}
            </div>
          )}
        </div>
      ) : shift.status === 'pending' ? (
        <div className="card p-5 mt-6" style={{ borderLeft: '3px solid var(--warn)' }}>
          <h2 className="font-extrabold">Analysis not yet available</h2>
          <p className="text-sm muted mt-1">No usable report is available for this slot ({shift.time}). We will add analysis when sources support it. A missing report does not confirm that a shift was cancelled.</p>
        </div>
      ) : (
        <>
          <div className="analysis-stats mt-6">
            <Stat k="Overall difficulty" v={shift.overall ?? '—'} color={difficultyColor(shift.overall)} />
            <Stat k="Reported attempts" v={attempts(shift.goodAttempts) === 'Not reported' ? 'Not reported' : `${attempts(shift.goodAttempts)} / 100`} />
            <Stat k="Shift timing" v={<span className="text-base">{shift.time}</span>} />
          </div>
          {shift.status === 'partial' && <p className="text-xs mt-3" style={{ color: 'var(--warn)' }}>Partial coverage. Some figures may be withheld; read the source and correction notes below.</p>}
          {shift.summary && <p className="mt-5 text-[15px] leading-relaxed">{shift.summary}</p>}

          {!!shift.sections?.length && (
            <section className="mt-8 analysis-anchor" id="sections">
              <h2 className="text-xl font-extrabold">Section overview</h2>
              <div className="analysis-section-grid mt-3">
                {shift.sections.map((s) => <article key={s.id} className="analysis-section-card" style={{ borderTopColor: SECTION_META[s.id]?.color ?? 'var(--line)' }}>
                  <h3 className="font-bold text-sm">{s.name}</h3>
                  <p className="text-xs muted mt-1">{s.questions} questions · {s.marks} marks</p>
                  <dl className="analysis-section-facts">
                    <div><dt>Difficulty</dt><dd><DiffChip label={s.difficulty} /></dd></div>
                    <div><dt>Reported attempts</dt><dd>{attempts(s.goodAttempts)}</dd></div>
                  </dl>
                </article>)}
              </div>
            </section>
          )}

          {shift.sections?.some((s) => s.topics?.length || s.notes) && (
            <section className="mt-8 analysis-anchor" id="topics">
              <h2 className="text-xl font-extrabold">Topics asked, section by section</h2>
              <div className="space-y-3 mt-3">
                {shift.sections.filter((s) => s.topics?.length || s.notes).map((s) => (
                  <article key={s.id} className="card p-4" style={{ borderLeft: `3px solid ${SECTION_META[s.id]?.color ?? 'var(--line)'}` }}>
                    <div className="flex items-center justify-between gap-2 flex-wrap">
                      <h3 className="font-bold">{s.name}</h3><DiffChip label={s.difficulty} />
                    </div>
                    {s.notes && <p className="text-sm muted mt-1.5">{s.notes}</p>}
                    {!!s.topics?.length && (
                      <ul className="analysis-topic-list mt-3 text-sm">
                        {s.topics.map((t, i) => (
                          <li key={i}>
                            {t.link
                              ? <Link href={`/${t.link}/`} title={`Revise ${t.topic}`}>{t.topic}{t.count ? ` · ${t.count}` : ''} <span aria-hidden="true">→</span></Link>
                              : <span>{t.topic}{t.count ? ` · ${t.count}` : ''}</span>}
                          </li>
                        ))}
                      </ul>
                    )}
                  </article>
                ))}
              </div>
              <p className="text-xs faint mt-2">Topics with an arrow link to our free notes and practice questions for that topic.</p>
            </section>
          )}

          {!!shift.asked?.length && (
            <section className="mt-8 analysis-anchor" id="questions">
              <h2 className="text-xl font-extrabold">Questions asked (memory-based)</h2>
              <p className="text-sm muted mt-1">What candidates recalled after the shift, reworded. Exact wording and options may differ from the real paper.</p>
              <div className="space-y-4 mt-3">
                {Object.entries(bySection).map(([sid, qs]) => (
                  <div key={sid}>
                    <h3 className="font-bold text-sm">{SECTION_META[sid as keyof typeof SECTION_META]?.name ?? sid}</h3>
                    <ol className="analysis-question-list mt-3 text-[15px]">
                      {qs!.map((q, i) => (
                        <li key={i}><span className="analysis-question-number">{i + 1}</span><div className="min-w-0"><Md>{q.q}</Md>{q.a && <details className="analysis-answer text-sm"><summary>Show reported answer</summary><Md>{q.a}</Md></details>}</div></li>
                      ))}
                    </ol>
                  </div>
                ))}
              </div>
            </section>
          )}

          {!!shift.observations?.length && (
            <section className="mt-8">
              <h2 className="text-xl font-extrabold">What candidates noticed</h2>
              <ul className="mt-2 space-y-1.5 text-[15px] list-disc pl-5">{shift.observations.map((o, i) => <li key={i}>{o}</li>)}</ul>
            </section>
          )}
          {!!shift.disagreements?.length && (
            <section className="mt-6 card p-4" style={{ borderLeft: '3px solid var(--warn)' }}>
              <h2 className="font-extrabold">Where reviews disagree</h2>
              <ul className="mt-1.5 space-y-1 text-sm muted list-disc pl-5">{shift.disagreements.map((o, i) => <li key={i}>{o}</li>)}</ul>
            </section>
          )}
        </>
      )}

      {others.length > 0 && (
        <section className="mt-10">
          <h2 className="text-lg font-extrabold">Other shifts on {dayLabel(day.date, false)}</h2>
          <div className="grid sm:grid-cols-3 gap-3 mt-3">
            {others.map((s) => (
              <Link key={s.shift} href={`/exam-analysis/${exam.slug}/${shiftSlug(day.date, s.shift)}/`} className="card p-4 hover:-translate-y-0.5 transition-transform">
                <div className="font-bold">Shift {s.shift}</div>
                <div className="text-xs faint mt-0.5">{s.time}</div>
                <div className="mt-2"><DiffChip label={shiftLabel(s)} /></div>
              </Link>
            ))}
          </div>
        </section>
      )}
      <Sources shift={shift} />
    </>
  );
}

function Sources({ shift }: { shift: Shift }) {
  if (!shift.sources?.length && !shift.qualityNotes?.length) return null;
  return (
    <section className="mt-10 text-sm analysis-anchor analysis-sources" id="sources">
      <h2 className="font-extrabold">Sources</h2>
      <p className="faint text-xs mt-1">{shift.auto ? 'Automatically compiled from the linked reviews. Source agreement does not guarantee accuracy; this is not a manually verified paper.' : 'Compiled from the linked candidate reviews and coaching-institute analyses.'} Difficulty and attempt figures are unofficial.</p>
      {shift.qualityNotes?.length ? <ul className="mt-2 space-y-1">{shift.qualityNotes.map(n => <li key={n}>{n}</li>)}</ul> : null}
      <p className="mt-2"><Link className="underline" href="/editorial-policy/">How we use sources and correct errors</Link></p>
      <ul className="mt-3 space-y-2">
        {shift.sources?.map((s, i) => <li key={i}><a href={s.url} rel="nofollow noopener" target="_blank" className="underline decoration-dotted">{s.name}</a></li>)}
      </ul>
    </section>
  );
}

function DayView({ exam, day }: { exam: ShiftExam; day: ShiftDay }) {
  return (
    <>
      {day.intro && <p className="mt-4 text-[15px] leading-relaxed">{day.intro}</p>}
      {day.correctionNote && <p className="card p-3 mt-3 text-sm">{day.correctionNote}</p>}
      <section className="mt-6 space-y-4" aria-label="Shifts for this date">
        {day.shifts.map(s => <article key={s.shift} className="analysis-day-card">
          <div className="analysis-card-heading"><div><h2 className="text-xl font-extrabold">Shift {s.shift}</h2><p className="text-sm muted mt-1">{s.time}</p></div><StatusLabel shift={s} /></div>
          {hasAnalysis(s) && <dl className="analysis-day-facts"><div><dt>Overall difficulty</dt><dd><DiffChip label={s.overall} /></dd></div><div><dt>Reported attempts</dt><dd className="font-bold">{attempts(s.goodAttempts)}</dd></div><div><dt>Sources</dt><dd>{s.sources?.length ?? 0} linked review{(s.sources?.length ?? 0) === 1 ? '' : 's'}</dd></div></dl>}
          {s.summary && <p className="text-sm muted mt-4 leading-relaxed">{s.summary}</p>}
          {s.status === 'pending' && <p className="text-sm muted mt-3">No usable report has been published for this slot. We show it here so you can see the coverage gap.</p>}
          {s.status === 'not-held' && <p className="text-sm muted mt-3">{s.note ?? 'This shift was not held according to the linked sources.'}</p>}
          <Link className={`btn mt-4 ${hasAnalysis(s) ? 'btn-brand' : ''}`} href={`/exam-analysis/${exam.slug}/${shiftSlug(day.date, s.shift)}/`}>{hasAnalysis(s) ? `Read Shift ${s.shift} analysis` : `View Shift ${s.shift} details`} <span aria-hidden="true">→</span></Link>
        </article>)}
      </section>
    </>
  );
}

export default async function ShiftAnalysisPage({ params }: Params) {
  const { exam: examSlug, slug } = await params;
  const exam = getShiftExam(examSlug);
  const r = resolveSlug(examSlug, slug);
  if (!exam || !r) notFound();
  const { day, shift } = r;
  const chronologicalDays = listShiftDays(examSlug).reverse();
  const dayIndex = chronologicalDays.findIndex(entry => entry.date === day.date);
  const previousDay = chronologicalDays[dayIndex - 1];
  const nextDay = chronologicalDays[dayIndex + 1];
  const url = `${BASE}/exam-analysis/${examSlug}/${slug}/`;
  const h1 = shift
    ? `${exam.short} Exam Analysis ${dayLabel(day.date)} — Shift ${shift.shift}`
    : `${exam.short} Exam Analysis ${dayLabel(day.date)} — All Shifts`;
  const faqs = shift ? [...autoFaqs(exam, day, shift), ...(day.faqs ?? [])] : day.faqs ?? [];

  const crumbs = [
    { name: 'Exam analysis', url: `${BASE}/exam-analysis/` },
    { name: exam.name, url: `${BASE}/exam-analysis/${examSlug}/` },
    { name: dayLabel(day.date), url: `${BASE}/exam-analysis/${examSlug}/${daySlug(day.date)}/` },
    ...(shift ? [{ name: `Shift ${shift.shift}`, url }] : []),
  ];
  const ld = [
    {
      '@context': 'https://schema.org', '@type': 'Article', headline: h1, description: descFor(exam, day, shift),
      datePublished: `${day.date}T12:00:00+05:30`, dateModified: day.updatedAt, mainEntityOfPage: url,
      author: { '@type': 'Organization', name: 'ExamShortcut', url: BASE },
      publisher: { '@type': 'Organization', name: 'ExamShortcut', logo: { '@type': 'ImageObject', url: `${BASE}/icon-512.png` } },
      image: `${BASE}/og.png`,
    },
    { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: crumbs.map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: c.name, item: c.url })) },
    ...(faqs.length ? [{ '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: faqs.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })) }] : []),
  ];

  return (
    <article className="max-w-4xl mx-auto analysis-page">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />
      <nav className="text-xs faint mt-4">
        <Link href="/exam-analysis/" className="underline decoration-dotted">Exam analysis</Link> /{' '}
        <Link href={`/exam-analysis/${examSlug}/`} className="underline decoration-dotted">{exam.short}</Link> /{' '}
        {shift ? <><Link href={`/exam-analysis/${examSlug}/${daySlug(day.date)}/`} className="underline decoration-dotted">{dayLabel(day.date, false)}</Link> / Shift {shift.shift}</> : dayLabel(day.date, false)}
      </nav>
      <h1 className="text-2xl sm:text-4xl font-extrabold mt-1">{h1}</h1>
      <p className="text-xs faint mt-2">
        {exam.name}{shift ? ` · ${shift.time}` : ''} · Updated {istTime(day.updatedAt)}
      </p>
      <nav className="analysis-day-navigation" aria-label="Browse report dates">
        {previousDay ? <Link href={`/exam-analysis/${examSlug}/${daySlug(previousDay.date)}/`}>← {dayLabel(previousDay.date, false)}</Link> : <span>First report</span>}
        <Link href={`/exam-analysis/${examSlug}/`}>All dates</Link>
        {nextDay ? <Link href={`/exam-analysis/${examSlug}/${daySlug(nextDay.date)}/`}>{dayLabel(nextDay.date, false)} →</Link> : <span>Latest report</span>}
      </nav>
      <nav className="analysis-shift-navigation" aria-label="Choose a shift">
        <Link href={`/exam-analysis/${examSlug}/${daySlug(day.date)}/`} aria-current={!shift ? 'page' : undefined}>Day overview</Link>
        {day.shifts.map(entry => <Link key={entry.shift} href={`/exam-analysis/${examSlug}/${shiftSlug(day.date, entry.shift)}/`} aria-current={shift?.shift === entry.shift ? 'page' : undefined}>Shift {entry.shift}</Link>)}
      </nav>
      {shift && <div className="analysis-card-heading mt-5"><StatusLabel shift={shift} /><span className="text-xs muted">{shift.sources?.length ?? 0} linked source{shift.sources?.length === 1 ? '' : 's'} · unofficial candidate reports</span></div>}
      {shift && hasAnalysis(shift) && <nav className="analysis-jump-links" aria-label="On this shift page">
        {!!shift.sections?.length && <a href="#sections">Section overview</a>}
        {shift.sections?.some(section => section.topics?.length || section.notes) && <a href="#topics">Topics asked</a>}
        {!!shift.asked?.length && <a href="#questions">Recalled questions</a>}
        {!!shift.sources?.length && <a href="#sources">Sources</a>}
      </nav>}
      {shift && day.correctionNote && <p className="card p-3 mt-3 text-sm">{day.correctionNote}</p>}

      {shift ? <ShiftView exam={exam} day={day} shift={shift} /> : <DayView exam={exam} day={day} />}

      <section className="card p-5 mt-10" style={{ borderTop: '3px solid var(--brand)' }}>
        <h2 className="font-extrabold">Your shift is still ahead?</h2>
        <p className="text-sm muted mt-1">Take a free full-length mock in the real CBT interface, then check where you stand.</p>
        <div className="flex gap-2 flex-wrap mt-3 text-sm">
          <Link className="btn btn-brand" href="/exams/ssc-cgl/mocks/">Free mock tests</Link>
          <Link className="btn" href="/exams/ssc-cgl/score-calculator/">Score calculator</Link>
          <Link className="btn" href="/exams/ssc-cgl/cutoffs/">Previous cutoffs</Link>
          <Link className="btn" href="/formula-sheet/">Formula sheet</Link>
        </div>
      </section>

      {faqs.length > 0 && (
        <section className="mt-10">
          <h2 className="text-xl font-extrabold">FAQs</h2>
          <div className="space-y-2 mt-3">
            {faqs.map((f, i) => (
              <details key={i} className="card p-4"><summary className="font-semibold cursor-pointer">{f.q}</summary><p className="text-sm muted mt-2">{f.a}</p></details>
            ))}
          </div>
        </section>
      )}
    </article>
  );
}
