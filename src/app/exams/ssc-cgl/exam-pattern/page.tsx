import type { Metadata } from 'next';
import { PatternPage } from '@/components/exam-subpages/PatternPage';
import { metaFor } from '@/components/exam-subpages/common';

export const dynamic = 'force-static';

export const generateMetadata = (): Metadata => metaFor('ssc-cgl', 'exam-pattern');

export default function Page() {
  return <PatternPage id="ssc-cgl" />;
}
