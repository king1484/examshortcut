import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getExamInfo } from '@/lib/exams';
import { MOCK_DEFS, getMock } from '@/lib/content';
import { MockCBT } from '@/components/MockCBT';
import { MockAccessGate } from '@/components/MockAccessGate';
import Link from 'next/link';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** Only mocks that belong to a non-CGL exam AND have their content parts on disk. */
export function generateStaticParams(): { exam: string; id: string }[] {
  return MOCK_DEFS.filter((m) => m.exam && m.exam !== 'ssc-cgl' && getMock(m.id))
    .map((m) => ({ exam: m.exam as string, id: m.id }));
}

type Params = Promise<{ exam: string; id: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam, id } = await params;
  const m = MOCK_DEFS.find((x) => x.id === id && x.exam === exam);
  return m ? { title: m.title, description: `${m.title}. ${m.blurb}`, alternates: { canonical: `/exams/${exam}/mocks/${id}/` }, robots: m.reviewHold ? { index: false, follow: true } : undefined } : {};
}

export default async function MockPage({ params }: { params: Params }) {
  const { exam, id } = await params;
  const info = getExamInfo(exam);
  const def = MOCK_DEFS.find((x) => x.id === id && x.exam === exam);
  if (!info || !def) notFound();
  if (def.reviewHold) return <div className="max-w-3xl mx-auto"><h1 className="text-3xl font-bold">{def.title}</h1><p className="card p-5 mt-5">{def.reviewHold}</p><p className="mt-4">A question that refers to a missing passage or puzzle cannot be used for a meaningful timed score.</p><p className="mt-4"><Link className="underline" href="/learn/">Study the topic notes</Link> or <Link className="underline" href={`/exams/${exam}/mocks/`}>choose an available test</Link>.</p></div>;
  const mock = getMock(id);
  if (!mock) notFound();
  return (
    <MockAccessGate open={mock.open} title={mock.title}>
      <MockCBT mock={mock} />
    </MockAccessGate>
  );
}
