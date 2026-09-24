import type { Metadata } from 'next';
import { LoginForm } from '@/components/LoginForm';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'Log in — save your progress',
  description: 'Free ExamShortcut account to save your revision list, studied topics, daily-quiz streak and mock scores across devices.',
  robots: { index: false, follow: true },
};

export default function LoginPage() {
  return (
    <div className="max-w-md mx-auto">
      <LoginForm />
    </div>
  );
}
