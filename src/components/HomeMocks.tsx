'use client';
import Link from 'next/link';
import { getExamInfo } from '@/lib/exams';
import { useSelectedExam } from '@/lib/useExam';

export interface HomeMock { id: string; title: string; blurb: string; tier: 1 | 2; exam: string; available: boolean }

const MAX_SELECTED = 6;

function MockCard({ m, showTier }: { m: HomeMock; showTier: boolean }) {
  return (
    <Link href={`/exams/${m.exam}/mocks/${m.id}/`} className="card p-5 flex flex-col">
      <span className="flex gap-2 flex-wrap">
        <span className={`chip ${m.available ? 'chip-low' : 'chip-medium'}`}>{m.available ? 'Ready' : 'Coming up'}</span>
        {showTier && <span className="chip">Tier {m.tier}</span>}
        <span className="chip">Free</span>
      </span>
      <h3 className="font-bold mt-2">{m.title}</h3>
      <p className="text-sm muted mt-1 flex-1 line-clamp-4">{m.blurb}</p>
    </Link>
  );
}

/** Home-page mock section. With an exam chosen it lists that exam's mocks; otherwise it shows one
 *  entry per exam so no single exam dominates the page. */
export function HomeMocks({ mocks }: { mocks: HomeMock[] }) {
  const selected = useSelectedExam();
  const byExam = new Map<string, HomeMock[]>();
  for (const m of mocks) byExam.set(m.exam, [...(byExam.get(m.exam) ?? []), m]);

  const own = selected ? byExam.get(selected.id) : undefined;
  if (selected && own?.length) {
    const shown = own.slice(0, MAX_SELECTED);
    return (
      <section className="mt-10">
        <div className="flex items-baseline justify-between flex-wrap gap-2">
          <h2 className="text-xl font-extrabold">Mock tests <span className="text-sm font-semibold faint">· {selected.name}</span></h2>
          <Link href={`/exams/${selected.id}/mocks/`} className="text-sm font-semibold underline">All {own.length} {selected.name} mocks →</Link>
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-3">
          {shown.map((m) => <MockCard key={m.id} m={m} showTier={selected.id.startsWith('ssc-')} />)}
        </div>
      </section>
    );
  }

  const exams = [...byExam.entries()];
  return (
    <section className="mt-10">
      <h2 className="text-xl font-extrabold">Mock tests <span className="text-sm font-semibold faint">· every exam</span></h2>
      <p className="text-sm muted mt-1">Real exam interface with full analysis. Pick your exam above to see only its mocks.</p>
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-3">
        {exams.map(([examId, list]) => {
          const info = getExamInfo(examId);
          if (!info) return null;
          const first = list[0];
          return (
            <Link key={examId} href={`/exams/${examId}/mocks/`} className="card p-5 flex flex-col hover:-translate-y-0.5 transition-transform">
              <span className="flex gap-2 flex-wrap">
                <span className="chip chip-low">{list.length} mock{list.length === 1 ? '' : 's'}</span>
                <span className="chip">Free</span>
              </span>
              <h3 className="font-bold mt-2">{info.name} mock tests</h3>
              <p className="text-sm muted mt-1 flex-1">Latest: {first.title}</p>
              <span className="text-sm font-semibold mt-3" style={{ color: 'var(--brand)' }}>Open {info.short} mocks →</span>
            </Link>
          );
        })}
      </div>
    </section>
  );
}
