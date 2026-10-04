import Link from 'next/link';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { listMocks } from '@/lib/content';
import { EXAMS, getExamInfo } from '@/lib/exams';
import { MockList } from '@/components/MockList';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** ssc-cgl keeps its own hand-built mocks page under /exams/ssc-cgl/mocks/. */
export function generateStaticParams() {
  return EXAMS.filter((e) => e.id !== 'ssc-cgl').map((e) => ({ exam: e.id }));
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam: id } = await params;
  const info = getExamInfo(id);
  if (!info) return {};
  return {
    title: `${info.name} mock tests — real exam interface, full analysis`,
    description: `${info.name} mock tests and previous-year papers in the exact exam interface: question palette, mark for review, auto-submit, section-wise analysis and per-question timing.`,
    alternates: { canonical: `/exams/${id}/mocks/` },
  };
}

export default async function MocksPage({ params }: { params: Params }) {
  const { exam: id } = await params;
  const info = getExamInfo(id);
  if (!info || id === 'ssc-cgl') notFound();
  const mocks = listMocks(id);
  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">{info.name} mock tests</h1>
      <p className="muted mt-2 max-w-3xl">
        Same interface as the real exam — palette, Save &amp; Next, Mark for Review, auto-submit at 00:00.
        After submitting you get section-wise scores, accuracy, <b>time spent per question</b>, and the topics to fix first.
        Wrong answers go straight into your <Link className="underline" href="/revision/">mistake notebook</Link>.
      </p>
      <MockList mocks={mocks.map((m) => ({ id: m.id, title: m.title, blurb: m.blurb, available: m.available, questionCount: m.questionCount, durationMin: m.durationMin, tier: m.tier }))} />
    </div>
  );
}
