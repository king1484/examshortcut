import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getTopic } from '@/lib/content';
import { SolvedExample } from '@/components/SolvedExample';

export const dynamic = 'force-static';
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ section: string; topic: string }> }): Promise<Metadata> {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) return {};
  return {
    title: `${t.title} — solved examples · SSC CGL`,
    description: `${t.solvedExamples?.length ?? 0} exam-level ${t.title} questions solved step by step, with the shortcut route marked where one exists.`,
  };
}

export default async function ExamplesPage({ params }: { params: Promise<{ section: string; topic: string }> }) {
  const { section, topic } = await params;
  const t = getTopic(section as never, topic);
  if (!t) notFound();

  return (
    <div>
      <p className="muted text-sm mt-4">Exam-level questions worked step by step. Try each one yourself first — then expand the solution and compare routes.</p>
      <div className="mt-4 space-y-3">
        {(t.solvedExamples ?? []).map((q, k) => <SolvedExample key={q.id} q={q} n={k + 1} />)}
        {(t.solvedExamples ?? []).length === 0 && <p className="card p-6 mt-4 text-center muted">Solved examples are being written — check back shortly.</p>}
      </div>
      {(t.practice?.length ?? 0) > 0 && (
        <Link href={`/ssc-cgl/${t.sectionId}/${t.id}/practice/`} className="btn btn-brand mt-6 inline-block">Ready? Take the {t.practice!.length}-question test →</Link>
      )}
    </div>
  );
}
