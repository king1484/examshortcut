import type { Metadata } from 'next';
import { Search } from '@/components/Search';

export const metadata: Metadata = {
  title: 'Search — topics, formulas, tricks, mocks',
  description: 'Instantly search every SSC CGL topic, formula, shortcut trick, common mistake and mock test on ExamShortcut.',
  robots: { index: false, follow: true },
};

export default function SearchPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <h1 className="text-3xl font-extrabold">Search</h1>
      <p className="muted mt-1 mb-1 text-sm">Every topic, formula, shortcut and mock — one box.</p>
      <Search />
    </div>
  );
}
