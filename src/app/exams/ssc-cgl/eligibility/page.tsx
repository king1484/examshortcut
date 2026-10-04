import type { Metadata } from 'next';
import { EligibilityPage } from '@/components/exam-subpages/EligibilityPage';
import { metaFor } from '@/components/exam-subpages/common';

export const dynamic = 'force-static';

export const generateMetadata = (): Metadata => metaFor('ssc-cgl', 'eligibility');

export default function Page() {
  return <EligibilityPage id="ssc-cgl" />;
}
