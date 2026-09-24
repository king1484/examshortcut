'use client';
import Link from 'next/link';
import { useEffect, useState } from 'react';
import { usePathname } from 'next/navigation';
import { ThemeToggle } from './ThemeToggle';
import { AccountButton } from './Auth';
import { useSelectedExam } from '@/lib/useExam';

const NAV = [
  { href: '/', label: 'Home', exact: true },
  { href: '/exams/', label: 'Exams' },
  { href: '/learn/', label: 'Subjects & Notes' },
  { href: '/daily-quiz/', label: 'Daily Quiz' },
  { href: '/exams/ssc-cgl/mocks/', label: 'Mock Tests' },
  { href: '/formula-sheet/', label: 'Formula Sheet' },
  { href: '/current-affairs/', label: 'Current Affairs' },
  { href: '/exams/ssc-cgl/cutoffs/', label: 'Cutoffs' },
  { href: '/dashboard/', label: 'My Progress', exact: true },
  { href: '/revision/', label: 'Revision' },
];

export function Logo() {
  return (
    <span className="flex items-center gap-2 font-extrabold tracking-tight text-lg">
      <svg width="28" height="28" viewBox="0 0 32 32" aria-hidden>
        <rect width="32" height="32" rx="8" fill="var(--brand)" />
        <path d="M9 17.5 14 22 23 10" stroke="var(--brand-ink)" strokeWidth="3.4" fill="none" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      <span>Exam<span style={{ color: 'var(--brand)' }}>Shortcut</span></span>
    </span>
  );
}

export function SiteHeader() {
  const path = usePathname() || '/';
  // Highlight the clicked tab immediately rather than when the route lands
  const [pendingHref, setPendingHref] = useState<string | null>(null);
  useEffect(() => { setPendingHref(null); }, [path]);
  const exam = useSelectedExam();
  // The CBT screen is full-focus; hide the site chrome there.
  if (/\/mocks\/[^/]+\/?$/.test(path) && path !== '/exams/ssc-cgl/mocks/') return null;
  return (
    <header className="sticky top-0 z-30 border-b backdrop-blur" style={{ borderColor: 'var(--line)', background: 'color-mix(in srgb, var(--bg) 88%, transparent)' }}>
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between gap-3">
        <Link href="/" aria-label="ExamShortcut home"><Logo /></Link>
        <div className="flex items-center gap-2">
          <Link href="/search/" aria-label="Search" className="btn" style={{ padding: '.4rem .7rem' }}>🔍<span className="hidden md:inline ml-1">Search</span></Link>
          <Link href="/exams/" className="btn hidden sm:inline-flex" style={{ padding: '.4rem .75rem' }} title="Change exam">
            🎯 {exam ? exam.short : 'Choose exam'}
          </Link>
          <ThemeToggle />
          <AccountButton />
        </div>
      </div>
      <nav className="max-w-6xl mx-auto px-2 sm:px-4 flex gap-1 overflow-x-auto text-sm font-semibold" style={{ scrollbarWidth: 'none' }}>
        {NAV.map((n) => {
          const active = pendingHref ? pendingHref === n.href
            : n.exact ? path === n.href || path === n.href.slice(0, -1) : path.startsWith(n.href);
          return (
            <Link key={n.href} href={n.href} onClick={() => setPendingHref(n.href)} className="px-3 py-2 whitespace-nowrap border-b-2 transition-colors"
              style={{ borderColor: active ? 'var(--brand)' : 'transparent', color: active ? 'var(--ink)' : 'var(--ink-2)' }}>
              {n.label}
            </Link>
          );
        })}
      </nav>
    </header>
  );
}
