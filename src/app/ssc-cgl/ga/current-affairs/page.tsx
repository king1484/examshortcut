import type { Metadata } from 'next';
import { getTopic } from '@/lib/content';
import { Md } from '@/components/Md';
import { TopicQuiz } from '@/components/TopicQuiz';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Current affairs for SSC CGL — Apr–Sep 2026, exam-relevant only',
  description: 'Month-wise current affairs compiled for SSC CGL and other govt exams: appointments, awards, sports, schemes, summits, reports, defence, science and economy — with a free quiz.',
};

export default function CurrentAffairsPage() {
  const t = getTopic('ga', 'current-affairs');

  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">Current affairs for SSC CGL</h1>
      <p className="muted mt-2">The 6-month window SSC actually asks (Apr–Sep 2026), grouped by month, exam-relevance only — no news dump.</p>
      {!t ? (
        <div className="card p-6 mt-6 text-center muted">Being compiled — the current-affairs desk is still verifying items. Check back shortly.</div>
      ) : (
        <>
          {t.subtopics.map((s, i) => (
            <section key={s.id} className="mt-8">
              <h2 className="text-2xl font-extrabold">{s.title}</h2>
              <Md className="mt-2 text-[15px]">{s.concept}</Md>
              {s.tricks?.map((k, j) => (
                <div key={j} className="mt-3 rounded-xl p-3.5" style={{ background: 'var(--surface-2)' }}>
                  <p className="text-sm font-bold">🧠 {k.title}</p>
                  <Md className="mt-1 text-sm">{k.body}</Md>
                </div>
              ))}
              {i === t.subtopics.length - 1 && t.practice && t.practice.length > 0 && (
                <div className="mt-8">
                  <h2 className="text-2xl font-extrabold">Current affairs quiz</h2>
                  <div className="mt-3"><TopicQuiz questions={t.practice} storageKey="ga/current-affairs" href="/ssc-cgl/ga/current-affairs/" section="ga" title="Current affairs" /></div>
                </div>
              )}
            </section>
          ))}
        </>
      )}
    </div>
  );
}
