import type { Metadata } from 'next';
import { Dashboard } from '@/components/Dashboard';
import { AuthGate } from '@/components/Auth';

export const metadata: Metadata = {
  title: 'Dashboard — your preparation at a glance',
  description: 'Track syllabus coverage, topic-test accuracy, mock scores, streaks and your weakest topics — with a daily plan built from your own activity.',
};

export default function DashboardPage() {
  return (
    <div className="max-w-5xl mx-auto">
      <AuthGate what="see your dashboard">
        <Dashboard />
      </AuthGate>
    </div>
  );
}
