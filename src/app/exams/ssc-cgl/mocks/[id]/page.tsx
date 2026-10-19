import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { MOCK_DEFS, getMock } from '@/lib/content';
import { MockCBT } from '@/components/MockCBT';
import { MockAccessGate } from '@/components/MockAccessGate';
import { MockSeoSection } from '@/components/exam-pages/MockSeoSection';
import Link from 'next/link';

export const dynamic = 'force-static';

export function generateStaticParams() {
  // Only CGL mocks belong under this legacy path. Other exams have their own
  // /exams/<exam>/mocks/<id>/ route and must not create duplicate thin pages here.
  return MOCK_DEFS.filter((m) => !m.exam || m.exam === 'ssc-cgl').map((m) => ({ id: m.id }));
}
export const dynamicParams = false;

/** Trim to Google's display limits at a word boundary (local, so other templates stay untouched). */
function cap(text: string, max: number) {
  const clean = text.replace(/\s+/g, ' ').trim();
  if (clean.length <= max) return clean;
  const cut = clean.slice(0, max - 1);
  const at = cut.lastIndexOf(' ');
  const base = at > Math.floor(max * 0.5) ? cut.slice(0, at) : cut;
  return `${base.replace(/[\s,;:·—–-]+$/, '')}…`;
}

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params;
  const m = MOCK_DEFS.find((x) => x.id === id);
  if (!m) return {};
  return {
    title: { absolute: cap(m.title, 60) },
    description: cap(`${m.title}: ${m.blurb}`, 160),
    alternates: { canonical: `/exams/${m.exam ?? 'ssc-cgl'}/mocks/${id}/` },
    robots: m.reviewHold || (m.exam && m.exam !== 'ssc-cgl') ? { index: false, follow: true } : undefined,
  };
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
