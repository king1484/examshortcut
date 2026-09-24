import Link from 'next/link';
import type { Metadata } from 'next';
import { DEST_PASSAGES } from '@/lib/destPassages';
import { DestTyping } from '@/components/DestTyping';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL typing test (DEST) practice — free, with SSC-style error marking',
  description: 'Free SSC CGL DEST practice: type a 2000-key-depression passage in 15 minutes with paste and spell-check disabled. Each full and half mistake is marked on the passage, and you get your error % against the UR, OBC and SC/ST limits.',
};

export default function TypingTestPage() {
  return (
    <div className="max-w-4xl mx-auto">
      <nav className="text-xs faint"><Link href="/exams/ssc-cgl/" className="underline decoration-dotted">SSC CGL</Link> / Typing test (DEST)</nav>
      <h1 className="text-3xl sm:text-4xl font-extrabold mt-2">SSC CGL typing test (DEST) practice</h1>
      <p className="muted mt-3 text-[15px]">
        The Data Entry Speed Test is part of Tier 2 (Paper 1, Section III, Module II). You type an English passage of about <b>2000 key depressions in 15 minutes</b>. It is qualifying only, but you must clear it for posts such as Tax Assistant, CSS ASO and Inspector. This simulator uses the same rules: no copy-paste, no spell-check, and every mistake is marked the way SSC marks it.
      </p>
      <div className="mt-6"><DestTyping passages={DEST_PASSAGES} /></div>

      <h2 className="text-2xl font-extrabold mt-10">How DEST is evaluated</h2>
      <div className="grid sm:grid-cols-2 gap-3 mt-3 text-sm">
        <div className="card p-4"><b style={{ color: 'var(--bad)' }}>Full mistakes (1 each)</b>
          <ul className="list-disc ml-5 mt-2 space-y-1 muted"><li>Leaving out a word or figure</li><li>Adding a word that isn&apos;t in the passage</li><li>Typing a wrong word, or misspelling one</li><li>Repeating a word</li></ul>
        </div>
        <div className="card p-4"><b style={{ color: 'var(--warn)' }}>Half mistakes (½ each)</b>
          <ul className="list-disc ml-5 mt-2 space-y-1 muted"><li>Spacing errors, e.g. &quot;Ihope&quot; for &quot;I hope&quot;</li><li>Wrong capitalisation</li><li>Wrong or missing punctuation</li><li>Two words swapped</li></ul>
        </div>
      </div>
      <div className="card p-4 mt-3 text-sm space-y-2">
        <p><b>Allowed errors:</b> up to 20% for UR, 25% for OBC/EWS and 30% for SC/ST and other reserved categories, as reported for recent cycles. Check your notification, because SSC can revise these.</p>
        <p><b>Speed target:</b> 2000 key depressions in 15 minutes is about 133 characters a minute, or roughly 27 words a minute. If you can type 35 wpm with good accuracy you have a comfortable margin.</p>
        <p><b>Tips:</b> accuracy beats speed, since a missed word costs twice as much as a comma. Don&apos;t go back to fix small typos in words you&apos;ve already finished. Keep your eyes on the passage, not the keyboard. Practise on a desktop keyboard; laptop and phone practice doesn&apos;t carry over well.</p>
      </div>
    </div>
  );
}
