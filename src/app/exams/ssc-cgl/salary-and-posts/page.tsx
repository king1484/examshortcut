import type { Metadata } from 'next';
import { SalaryPage } from '@/components/exam-subpages/SalaryPage';
import { metaFor } from '@/components/exam-subpages/common';

export const dynamic = 'force-static';

export const generateMetadata = (): Metadata => metaFor('ssc-cgl', 'salary-and-posts');

export default function Page() {
  return <SalaryPage id="ssc-cgl" />;
}
