import Link from 'next/link';
import type { Metadata } from 'next';
import { listMocks } from '@/lib/content';
import { MockList } from '@/components/MockList';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL mock tests — real CBT interface, full analysis',
  description: 'SSC CGL Tier 1 and Tier 2 mock tests in the exact exam interface: question palette, mark for review, auto-submit, section-wise analysis, per-question timing and a PYQ-pattern paper modelled on CGL 2025.',
};

export default function MocksPage() {
  const mocks = listMocks();
  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">SSC CGL mock tests</h1>
      <p className="muted mt-2 max-w-3xl">
        Same interface as the real SSC CBT, with a full analysis after you submit.
      </p>
      <MockList mocks={mocks.map((m) => ({ id: m.id, title: m.title, blurb: m.blurb, available: m.available, questionCount: m.questionCount, durationMin: m.durationMin, tier: m.tier }))} />

      <h2 className="text-2xl font-extrabold mt-10">What you get</h2>
      <div className="card p-5 mt-3 text-sm muted space-y-2">
        <p><b>Real interface:</b> palette, Save &amp; Next, Mark for Review, auto-submit at 00:00.</p>
        <p><b>Analysis:</b> section-wise scores, accuracy, <b>time spent per question</b>, and the topics to fix first.</p>
        <p>Wrong answers go straight into your <Link className="underline" href="/revision/">mistake notebook</Link>.</p>
      </div>
    </div>
  );
}
