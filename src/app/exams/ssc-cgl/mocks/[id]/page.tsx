import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { MOCK_DEFS, getMock } from '@/lib/content';
import { MockCBT } from '@/components/MockCBT';
import { MockAccessGate } from '@/components/MockAccessGate';

export const dynamic = 'force-static';

export function generateStaticParams() {
  return MOCK_DEFS.map((m) => ({ id: m.id }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params;
  const m = MOCK_DEFS.find((x) => x.id === id);
  return m ? { title: m.title, description: m.blurb } : {};
}

export default async function MockPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const mock = getMock(id);
  if (!mock) notFound();
  return (
    <MockAccessGate open={mock.open} title={mock.title}>
      <MockCBT mock={mock} />
    </MockAccessGate>
  );
}
