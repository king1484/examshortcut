import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { MOCK_DEFS, getMock } from '@/lib/content';
import { MockCBT } from '@/components/MockCBT';
import { MockAccessGate } from '@/components/MockAccessGate';
import { MockSeoSection } from '@/components/exam-pages/MockSeoSection';
import Link from 'next/link';

export const dynamic = 'force-static';

export function generateStaticParams() {
  return MOCK_DEFS.map((m) => ({ id: m.id }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params;
  const m = MOCK_DEFS.find((x) => x.id === id);
  return m ? { title: m.title, description: `${m.title}. ${m.blurb}`, alternates: { canonical: `/exams/${m.exam ?? 'ssc-cgl'}/mocks/${id}/` }, robots: m.reviewHold || (m.exam && m.exam !== 'ssc-cgl') ? { index: false, follow: true } : undefined } : {};
}

export default async function MockPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const def = MOCK_DEFS.find(m => m.id === id);
  if (def?.exam && def.exam !== 'ssc-cgl') return <div><h1 className="text-2xl font-bold">{def.title}</h1><p className="mt-4">This test belongs to a different exam.</p><Link className="btn btn-brand mt-4" href={`/exams/${def.exam}/mocks/${id}/`}>Open the correct test page</Link></div>;
  const mock = getMock(id);
  if (!mock) notFound();
  return (
    <>
      <MockAccessGate open={mock.open} title={mock.title}>
        <MockCBT mock={mock} />
      </MockAccessGate>
      <MockSeoSection mock={mock} />
    </>
  );
}
