import type { Metadata } from 'next';
import { idsWithPage } from '@/lib/examPages';
import { ExpectedCutoffInfoPage, infoMeta } from '@/components/exam-pages/ExamInfoPages';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return idsWithPage('expected-cutoff');
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam } = await params;
  return infoMeta(exam, 'expected-cutoff');
}

export default async function Page({ params }: { params: Params }) {
  const { exam } = await params;
  return <ExpectedCutoffInfoPage id={exam} />;
}
