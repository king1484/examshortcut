import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { EXAMS } from '@/lib/exams';
import { SalaryPage } from '@/components/exam-subpages/SalaryPage';
import { metaFor } from '@/components/exam-subpages/common';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** ssc-cgl keeps its own hand-built folder under /exams/ssc-cgl/ (same components, see there). */
export function generateStaticParams() {
  return EXAMS.filter((e) => e.id !== 'ssc-cgl').map((e) => ({ exam: e.id }));
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam } = await params;
  return metaFor(exam, 'salary-and-posts');
}

export default async function Page({ params }: { params: Params }) {
  const { exam } = await params;
  if (exam === 'ssc-cgl') notFound();
  return <SalaryPage id={exam} />;
}
