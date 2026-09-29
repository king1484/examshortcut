import type { Metadata } from 'next';

// The revision page is a client component, so its metadata lives here. It shows the visitor's own
// mistakes and bookmarks — nothing for a search engine to index.
export const metadata: Metadata = {
  title: 'My revision — mistakes, bookmarks and progress',
  description: 'Your wrong answers, bookmarked questions and topic progress in one place, to revise before the exam.',
  robots: { index: false, follow: true },
};

export default function RevisionLayout({ children }: { children: React.ReactNode }) {
  return children;
}
