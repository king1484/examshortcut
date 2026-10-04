import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getCutoffs } from '@/lib/content';
import { EXAMS, getExamInfo } from '@/lib/exams';
import { Md } from '@/components/Md';
import { ExamCutoffs } from '@/components/ExamCutoffs';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** ssc-cgl keeps its own hand-built cutoffs page with trend charts. */
export function generateStaticParams() {
  return EXAMS.filter((e) => e.id !== 'ssc-cgl').map((e) => ({ exam: e.id }));
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam: id } = await params;
  const info = getExamInfo(id);
  if (!info) return {};
  return {
    title: `${info.name} cutoffs — official, category-wise`,
    description: `${info.name} cutoffs: official qualifying marks and typical shortlist levels, category-wise, with honest notes on what each row means.`,
    alternates: { canonical: `/exams/${id}/cutoffs/` },
  };
}

export default async function CutoffsPage({ params }: { params: Params }) {
  const { exam: id } = await params;
  const info = getExamInfo(id);
  if (!info || id === 'ssc-cgl') notFound();
  const data = getCutoffs(id) as Record<string, unknown> | null;
  if (!data) notFound();

  // the raw source lists are long and not shown, so don't ship them to the client
  const { sources: _sources, ...shown } = data;
  void _sources;

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-3xl sm:text-4xl font-extrabold">{info.name} cutoffs</h1>
      {typeof data.notes === 'string' && <Md className="muted mt-2 max-w-3xl text-[15px]">{data.notes}</Md>}
      <ExamCutoffs data={shown} />
      <p className="faint text-xs mt-8">
        Cutoff rows are compiled from official result notices and reputable reproductions — see the notes above for what each row means.
        Always confirm on the official website.
      </p>
    </div>
  );
}
