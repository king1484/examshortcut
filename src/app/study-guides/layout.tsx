import { DisplayBanner } from '@/components/DisplayBanner';

export default function StudyGuidesLayout({ children }: { children: React.ReactNode }) {
  return <>{children}<DisplayBanner /></>;
}
