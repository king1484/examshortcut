import Link from 'next/link';
import type { Metadata } from 'next';
import { allFormulas, SECTION_META } from '@/lib/content';
import { LazyTex } from '@/components/LazyTex';
import { PrintButton } from '@/components/PrintButton';

export const dynamic = 'force-static';
export const metadata: Metadata = {
  title: 'SSC CGL formula sheet PDF — all Quant formulas & shortcuts, free',
  description: 'Free SSC CGL formula sheet (save as PDF): every Quant formula, reasoning rule, English grammar rule and GA mnemonic on one page, with shortcut tricks for last-minute revision.',
};

/** 220-char trick preview as plain text + browser-rendered inline math. Full
    markdown/KaTeX for 851 snippets was ~2 MB of the page on its own. */
function TrickSnippet({ body }: { body: string }) {
  // \$ in data = a literal dollar (Md escape): park it so the $…$ splitter can't mispair
  const D = '\u0001';
  let text = body.replace(/\\\$/g, D).replace(/\\([#*+_~\-])/g, '$1');
  text = text.length > 220 ? text.slice(0, 220) : text;
  // A cut through a $…$ span would leave an unbalanced delimiter: drop the tail
  if ((text.match(/\$/g)?.length ?? 0) % 2) text = text.slice(0, text.lastIndexOf('$'));
  const parts = text.split(/\$([^$]+)\$/);
  return (
    <span className="muted">
      {parts.map((p, i) => (i % 2 ? <LazyTex key={i} tex={p} /> : p.replace(/\*\*|__|`/g, '').split(D).join('$')))}
      {body.length > text.length && '…'}
    </span>
  );
}

export default function FormulaSheetPage() {
  const sections = allFormulas();

  return (
    <div className="max-w-4xl mx-auto">
      <div className="flex items-start justify-between gap-4 flex-wrap no-print">
        <div>
          <h1 className="text-3xl sm:text-4xl font-extrabold">SSC CGL formula sheet</h1>
          <p className="muted mt-2 max-w-2xl">Every formula and shortcut trick from the notes, on one page. Tap “Download PDF” (or press Ctrl/Cmd + P) and choose “Save as PDF” — it's formatted for paper.</p>
        </div>
        <PrintButton />
      </div>

      {sections.map((sec) => (
        <section key={sec.sectionId} className="mt-10">
          <h2 className="text-2xl font-extrabold pb-1 border-b-2" style={{ color: SECTION_META[sec.sectionId].color, borderColor: SECTION_META[sec.sectionId].color }}>
            {SECTION_META[sec.sectionId].name}
          </h2>
          {sec.topics.map((t) => (
            <div key={t.id} className="mt-5">
              <h3 className="font-extrabold text-lg">{t.title}</h3>
              <div className="grid sm:grid-cols-2 gap-2.5 mt-2">
                {t.subtopics.map((s) => (
                  <div key={s.id} className="card p-3.5">
                    <div className="text-sm font-bold">{s.title}</div>
                    {s.formulas.map((f, i) => (
                      <div key={i} className="mt-2">
                        <div className="text-xs font-semibold faint">{f.name}</div>
                        <div className="overflow-x-auto overflow-y-hidden py-0.5"><LazyTex tex={f.tex} /></div>
                        {f.note && <div className="text-[11px] muted">{f.note}</div>}
                      </div>
                    ))}
                    {s.tricks.map((k, i) => (
                      <div key={`t${i}`} className="mt-2 text-xs">
                        <span className="font-bold">⚡ {k.title}.</span> <TrickSnippet body={k.body} />
                      </div>
                    ))}
                  </div>
                ))}
              </div>
            </div>
          ))}
        </section>
      ))}
      {sections.every((s) => s.topics.length === 0) && <p className="card p-6 mt-8 text-center muted">Formulas are being compiled — check back shortly.</p>}

      <aside className="card p-4 mt-10 text-sm no-print">
        <div className="font-bold">More ways to revise</div>
        <p className="muted mt-1">
          <Link href="/quant-formulas/" className="underline decoration-dotted">Quant formulas by topic</Link> (with per-topic links) ·{' '}
          <Link href="/shortcut-tricks/" className="underline decoration-dotted">All shortcut tricks</Link> ·{' '}
          <Link href="/data-interpretation/" className="underline decoration-dotted">Data interpretation formulas &amp; tricks</Link> ·{' '}
          <Link href="/exams/ssc-cgl/mocks/" className="underline decoration-dotted">Mock tests</Link> ·{' '}
          <Link href="/daily-quiz/" className="underline decoration-dotted">Daily quiz</Link>
        </p>
      </aside>
    </div>
  );
}
