import type { Metadata, Viewport } from 'next';
import { Plus_Jakarta_Sans } from 'next/font/google';
import 'katex/dist/katex.min.css';
import './globals.css';
import { SiteHeader } from '@/components/SiteHeader';
import { SwRegister } from '@/components/SwRegister';
import { NavLoader } from '@/components/NavLoader';
import Link from 'next/link';
import { AuthProvider } from '@/components/Auth';

const sans = Plus_Jakarta_Sans({ subsets: ['latin'], variable: '--font-sans', display: 'swap' });

export const metadata: Metadata = {
  metadataBase: new URL('https://examshortcut.in'),
  title: { default: 'ExamShortcut — Government & entrance exam preparation: notes, shortcuts, mocks', template: '%s · ExamShortcut' },
  description:
    'Preparation for SSC, Railway, teaching and entrance exams: detailed topic notes, every question type with formulas and shortcuts, practice sets, daily quiz, full mocks, cutoffs and 5 years of current affairs.',
  manifest: '/manifest.webmanifest',
  icons: { icon: '/icon.svg', apple: '/icon-192.png' },
  openGraph: { siteName: 'ExamShortcut', type: 'website', locale: 'en_IN' },
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: '#f7f5f0' },
    { media: '(prefers-color-scheme: dark)', color: '#111318' },
  ],
};

const themeScript = `try{var t=localStorage.getItem('es-theme');if(t==='light'||t==='dark')document.documentElement.dataset.theme=t}catch(e){}`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-IN" className={sans.variable} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body className="min-h-screen flex flex-col">
        <AuthProvider>
        <SiteHeader />
        <main className="flex-1 w-full max-w-6xl mx-auto px-4 sm:px-6 py-6 sm:py-8">{children}</main>
        <footer className="border-t mt-10" style={{ borderColor: 'var(--line)' }}>
          <div className="max-w-6xl mx-auto px-4 sm:px-6 py-8 text-sm faint space-y-3">
            <div className="flex flex-wrap gap-x-5 gap-y-2">
              <Link href="/exams/">All exams</Link>
              <Link href="/learn/">Subjects &amp; notes</Link>
              <Link href="/quant/">Quantitative Aptitude</Link>
              <Link href="/reasoning/">Reasoning</Link>
              <Link href="/english/">English</Link>
              <Link href="/ga/">General Awareness</Link>
              <Link href="/computer/">Computer</Link>
              <Link href="/daily-quiz/">Daily quiz</Link>
              <Link href="/current-affairs/">Current affairs</Link>
              <Link href="/exams/ssc-cgl/">SSC CGL</Link>
              <Link href="/exams/ssc-cgl/mocks/">Mock tests</Link>
              <Link href="/formula-sheet/">Formula sheet</Link>
              <Link href="/vocab/">Vocab bank</Link>
              <Link href="/static-gk/">Static GK</Link>
              <Link href="/exams/ssc-cgl/cutoffs/">Cutoffs</Link>
              <Link href="/exams/ssc-cgl/score-calculator/">Score calculator</Link>
              <Link href="/dashboard/">My progress</Link>
              <Link href="/revision/">My revision</Link>
              <Link href="/about/">About</Link>
              <Link href="/privacy/">Privacy</Link>
              <Link href="/contact/">Contact</Link>
            </div>
            <p>© {new Date().getFullYear()} ExamShortcut</p>
          </div>
        </footer>
        <NavLoader />
        <SwRegister />
        </AuthProvider>
      </body>
    </html>
  );
}
