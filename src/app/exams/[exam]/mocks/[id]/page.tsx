import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getExamInfo } from '@/lib/exams';
import { MOCK_DEFS, getMock } from '@/lib/content';
import { MockCBT } from '@/components/MockCBT';
import { MockAccessGate } from '@/components/MockAccessGate';

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
  return m ? { title: m.title, description: m.blurb } : {};
}

export default async function MockPage({ params }: { params: Params }) {
  const { exam, id } = await params;
  const info = getExamInfo(exam);
  const def = MOCK_DEFS.find((x) => x.id === id && x.exam === exam);
  if (!info || !def) notFound();
  const mock = getMock(id);
  if (!mock) notFound();
  return (
    <MockAccessGate open={mock.open} title={mock.title}>
      <MockCBT mock={mock} />
    </MockAccessGate>
  );
}
