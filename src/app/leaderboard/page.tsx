import type { Metadata } from 'next';
import { Leaderboard } from '@/components/Leaderboard';

export const metadata: Metadata = {
  title: 'Leaderboard',
  description: 'Earn points by studying and testing, and optionally join the leaderboard of ExamShortcut learners.',
  robots: { index: false, follow: true },
};

export default function LeaderboardPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <Leaderboard />
    </div>
  );
}
