import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { SECTION_META } from '@/lib/sections';
import {
  allShiftParams, dayLabel, daySlug, difficultyColor, getShiftExam, hasAnalysis, resolveSlug, shiftLabel, shiftSlug,
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
    if (shift.status === 'pending') return `${exam.name} ${dayLabel(day.date)} Shift ${shift.shift} (${shift.time}) analysis: difficulty level, good attempts and questions asked — updated right after the shift ends.`;
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
  return {
    title: { absolute: title },
    description,
    openGraph: { title, description, type: 'article', url: `${BASE}/exam-analysis/${examSlug}/${slug}/`, modifiedTime: r.day.updatedAt },
    twitter: { card: 'summary_large_image', title, description },
  };
}

const istTime = (iso: string) =>
  new Date(iso).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', day: 'numeric', month: 'short', hour: 'numeric', minute: '2-digit' }) + ' IST';

function DiffChip({ label }: { label?: string }) {
  if (!label) return <span className="faint">—</span>;
  const c = difficultyColor(label);
  return <span className="chip font-semibold" style={{ color: c, borderColor: c }}>{label}</span>;
}

function Stat({ k, v, color }: { k: string; v: React.ReactNode; color?: string }) {
  return (
    <div className="card p-4 flex-1 min-w-[9rem]" style={color ? { borderTop: `3px solid ${color}` } : undefined}>
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
  if (shift.goodAttempts) f.push({ q: `What are good attempts for ${exam.short} ${when}?`, a: `Around ${shift.goodAttempts} out of 100 questions, going by candidate and coaching-institute reviews. Accuracy matters more than raw attempts because of the 0.50 negative marking.` });
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
          <h2 className="font-extrabold">Analysis coming after the shift</h2>
          <p className="text-sm muted mt-1">Shift {shift.shift} runs {shift.time}. We update this page with difficulty, good attempts and the questions candidates recall as soon as reviews come in — usually within an hour of the shift ending.</p>
        </div>
      ) : (
        <>
          <div className="flex gap-3 flex-wrap mt-6">
            <Stat k="Overall difficulty" v={shift.overall ?? '—'} color={difficultyColor(shift.overall)} />
            <Stat k="Good attempts" v={shift.goodAttempts ? `${shift.goodAttempts} / 100` : '—'} />
            <Stat k="Shift timing" v={<span className="text-base">{shift.time}</span>} />
          </div>
          {shift.status === 'partial' && <p className="text-xs mt-3" style={{ color: 'var(--warn)' }}>Early reviews — numbers may shift as more candidates report.</p>}
          {shift.summary && <p className="mt-5 text-[15px] leading-relaxed">{shift.summary}</p>}

          {!!shift.sections?.length && (
            <section className="mt-8">
              <h2 className="text-xl font-extrabold">Section-wise difficulty and good attempts</h2>
              <div className="card mt-3 overflow-x-auto">
                <table className="w-full text-sm">
                  <thead><tr className="text-left faint text-xs uppercase">
                    <th className="p-3">Section</th><th className="p-3">Qs</th><th className="p-3">Difficulty</th><th className="p-3">Good attempts</th>
                  </tr></thead>
                  <tbody>
                    {shift.sections.map((s) => (
                      <tr key={s.id} className="border-t" style={{ borderColor: 'var(--line)' }}>
                        <td className="p-3 font-semibold">{s.name}</td>
                        <td className="p-3">{s.questions}</td>
                        <td className="p-3"><DiffChip label={s.difficulty} /></td>
                        <td className="p-3">{s.goodAttempts ?? '—'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </section>
          )}

          {shift.sections?.some((s) => s.topics?.length || s.notes) && (
            <section className="mt-8">
              <h2 className="text-xl font-extrabold">Topics asked, section by section</h2>
              <div className="space-y-3 mt-3">
                {shift.sections.filter((s) => s.topics?.length || s.notes).map((s) => (
                  <article key={s.id} className="card p-4" style={{ borderLeft: `3px solid ${SECTION_META[s.id]?.color ?? 'var(--line)'}` }}>
                    <div className="flex items-center justify-between gap-2 flex-wrap">
                      <h3 className="font-bold">{s.name}</h3><DiffChip label={s.difficulty} />
                    </div>
                    {s.notes && <p className="text-sm muted mt-1.5">{s.notes}</p>}
                    {!!s.topics?.length && (
                      <ul className="mt-2 flex flex-wrap gap-1.5 text-sm">
                        {s.topics.map((t, i) => (
                          <li key={i}>
                            {t.link
                              ? <Link href={`/${t.link}/`} className="chip hover:underline" title={`Revise ${t.topic}`}>{t.topic}{t.count ? ` · ${t.count}` : ''} →</Link>
                              : <span className="chip">{t.topic}{t.count ? ` · ${t.count}` : ''}</span>}
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
            <section className="mt-8">
              <h2 className="text-xl font-extrabold">Questions asked (memory-based)</h2>
              <p className="text-sm muted mt-1">What candidates recalled after the shift, reworded. Exact wording and options may differ from the real paper.</p>
              <div className="space-y-4 mt-3">
                {Object.entries(bySection).map(([sid, qs]) => (
                  <div key={sid}>
                    <h3 className="font-bold text-sm">{SECTION_META[sid as keyof typeof SECTION_META]?.name ?? sid}</h3>
                    <ol className="list-decimal pl-5 mt-1.5 space-y-1.5 text-[15px]">
                      {qs!.map((q, i) => (
                        <li key={i}>{q.q}{q.a && <details className="inline-block ml-2 text-sm"><summary className="cursor-pointer faint">answer</summary><span style={{ color: 'var(--ok)' }}>{q.a}</span></details>}</li>
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
  if (!shift.sources?.length) return null;
  return (
    <section className="mt-10 text-sm">
      <h2 className="font-extrabold">Sources</h2>
      <p className="faint text-xs mt-1">Compiled and cross-checked from candidate reviews and coaching-institute analyses. Figures are unofficial until SSC releases the answer key.</p>
      <ul className="mt-2 space-y-0.5">
        {shift.sources.map((s, i) => <li key={i}><a href={s.url} rel="nofollow noopener" target="_blank" className="underline decoration-dotted">{s.name}</a></li>)}
      </ul>
    </section>
  );
}

function DayView({ exam, day }: { exam: ShiftExam; day: ShiftDay }) {
  return (
    <>
      {day.intro && <p className="mt-4 text-[15px] leading-relaxed">{day.intro}</p>}
      <div className="card mt-6 overflow-x-auto">
        <table className="w-full text-sm">
          <thead><tr className="text-left faint text-xs uppercase">
            <th className="p-3">Shift</th><th className="p-3">Timing</th><th className="p-3">Overall</th><th className="p-3">Good attempts</th><th className="p-3" />
          </tr></thead>
          <tbody>
            {day.shifts.map((s) => (
              <tr key={s.shift} className="border-t" style={{ borderColor: 'var(--line)' }}>
                <td className="p-3 font-semibold">Shift {s.shift}</td>
                <td className="p-3 whitespace-nowrap">{s.time}</td>
                <td className="p-3"><DiffChip label={shiftLabel(s)} /></td>
                <td className="p-3">{s.goodAttempts ?? '—'}</td>
                <td className="p-3"><Link className="underline decoration-dotted whitespace-nowrap" href={`/exam-analysis/${exam.slug}/${shiftSlug(day.date, s.shift)}/`}>Full analysis →</Link></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="space-y-3 mt-6">
        {day.shifts.filter((s) => hasAnalysis(s) && s.summary).map((s) => (
          <Link key={s.shift} href={`/exam-analysis/${exam.slug}/${shiftSlug(day.date, s.shift)}/`} className="card p-4 block hover:-translate-y-0.5 transition-transform" style={{ borderLeft: `3px solid ${difficultyColor(s.overall)}` }}>
            <h2 className="font-bold">Shift {s.shift} — {s.overall}</h2>
            <p className="text-sm muted mt-1">{s.summary}</p>
          </Link>
        ))}
      </div>
    </>
  );
}

export default async function ShiftAnalysisPage({ params }: Params) {
  const { exam: examSlug, slug } = await params;
  const exam = getShiftExam(examSlug);
  const r = resolveSlug(examSlug, slug);
  if (!exam || !r) notFound();
  const { day, shift } = r;
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
    <article className="max-w-3xl mx-auto">
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
