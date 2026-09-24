import type { Metadata, Viewport } from 'next';
import { Plus_Jakarta_Sans } from 'next/font/google';
import 'katex/dist/katex.min.css';
import './globals.css';
import { SiteHeader } from '@/components/SiteHeader';
import { SwRegister } from '@/components/SwRegister';
import Link from 'next/link';

const sans = Plus_Jakarta_Sans({ subsets: ['latin'], variable: '--font-sans', display: 'swap' });

export const metadata: Metadata = {
  metadataBase: new URL('https://examshortcut.in'),
  title: { default: 'ExamShortcut — Free SSC CGL preparation: syllabus, shortcuts, mocks, cutoffs', template: '%s · ExamShortcut' },
  description:
    'Everything for SSC CGL in one place, free: exam pattern, topic-wise notes, formulas & shortcut tricks, topic tests, full mocks in a real CBT interface, PYQ-pattern papers, cutoffs and current affairs.',
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

/* Static export navigates are full page loads (no SPA router), and the CDN
   round trip from India is ~0.7s. Prerender links on hover so Chrome renders
   the next page before the click — unsupported browsers ignore this. */
const speculationRules = JSON.stringify({
  prefetch: [{ source: 'document', where: { href_matches: '/*' }, eagerness: 'moderate' }],
  prerender: [{ source: 'document', where: { href_matches: '/*' }, eagerness: 'moderate' }],
});

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-IN" className={sans.variable} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
        <script type="speculationrules" dangerouslySetInnerHTML={{ __html: speculationRules }} />
      </head>
      <body className="min-h-screen flex flex-col">
        <SiteHeader />
        <main className="flex-1 w-full max-w-6xl mx-auto px-4 sm:px-6 py-6 sm:py-8">{children}</main>
        <footer className="border-t mt-10" style={{ borderColor: 'var(--line)' }}>
          <div className="max-w-6xl mx-auto px-4 sm:px-6 py-8 text-sm faint space-y-3">
            <div className="flex flex-wrap gap-x-5 gap-y-2">
              <Link href="/dashboard/">Dashboard</Link>
              <Link href="/ssc-cgl/">SSC CGL</Link>
              <Link href="/ssc-cgl/syllabus/">Syllabus</Link>
              <Link href="/ssc-cgl/weightage/">Weightage</Link>
              <Link href="/ssc-cgl/mocks/">Mock tests</Link>
              <Link href="/ssc-cgl/formula-sheet/">Formula sheet</Link>
              <Link href="/ssc-cgl/vocab/">Vocab bank</Link>
              <Link href="/ssc-cgl/static-gk/">Static GK</Link>
              <Link href="/ssc-cgl/cutoffs/">Cutoffs</Link>
              <Link href="/ssc-cgl/score-calculator/">Score calculator</Link>
              <Link href="/revision/">My revision</Link>
              <Link href="/about/">About &amp; disclaimer</Link>
              <Link href="/privacy/">Privacy</Link>
              <Link href="/contact/">Contact</Link>
            </div>
            <p>
              ExamShortcut is an independent learning platform. It is not affiliated with, endorsed by, or connected to the Staff Selection
              Commission or any Government body. Always confirm dates and rules on the official website{' '}
              <a className="underline" href="https://ssc.gov.in" target="_blank" rel="noopener noreferrer">ssc.gov.in</a>.
            </p>
            <p>© {new Date().getFullYear()} ExamShortcut · Free forever for core preparation · No login needed</p>
          </div>
        </footer>
        <SwRegister />
      </body>
    </html>
  );
}
