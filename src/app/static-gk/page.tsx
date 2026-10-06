import type { Metadata } from 'next';
import { StaticGk } from '@/components/StaticGk';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC static GK — dances, national parks, dams, important days, books & UNESCO sites',
  description: 'SSC CGL static GK quick reference: classical and folk dances, festivals, national parks, dams and rivers, important days, books and authors, sports trophies, firsts in India, HQs, state capitals and UNESCO World Heritage Sites.',
};

export default function StaticGkPage() {
  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-2xl sm:text-4xl font-extrabold">SSC static GK quick reference</h1>
      <p className="muted mt-2 max-w-2xl">
        The static GK tables SSC repeats, on one searchable page. Type a name to filter every table at once.
      </p>
      <StaticGk />
    </div>
  );
}
