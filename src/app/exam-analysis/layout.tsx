import { DisplayBanner } from '@/components/DisplayBanner';

export default function ExamAnalysisLayout({ children }: { children: React.ReactNode }) {
  return <>{children}<DisplayBanner /></>;
}
