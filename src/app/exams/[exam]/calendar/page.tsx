import type { Metadata } from 'next';
import { idsWithPage } from '@/lib/examPages';
import { CalendarInfoPage, infoMeta } from '@/components/exam-pages/ExamInfoPages';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return idsWithPage('calendar');
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam } = await params;
  return infoMeta(exam, 'calendar');
}

export default async function Page({ params }: { params: Params }) {
  const { exam } = await params;
  return <CalendarInfoPage id={exam} />;
}
