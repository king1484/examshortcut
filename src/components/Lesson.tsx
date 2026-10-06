import { Md } from '@/components/Md';
import type { Mistake, WorkedExample } from '@/lib/types';

/* Helpers that turn a subtopic's long markdown into separate, numbered lesson sections.
   Older content packs traps and a recap inside the notes; those are lifted out so the
   page shows each thing once, in its own block. */

export interface NoteSection { id: string; title: string; body: string }

const TRAPS = /\b(trap|traps|mistake|mistakes|pitfall|errors? to avoid)\b/i;
const RECAP = /\b(quick revision|revision|recap|summary|in short|key takeaways?)\b/i;

const slug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 48);

function bullets(md: string): string[] {
  return md.split('\n').map((l) => l.match(/^\s*(?:[-*]|\d+[.)])\s+(.*)$/)?.[1]?.trim()).filter((x): x is string => !!x);
}

export function splitNotes(notes: string | undefined) {
  const sections: NoteSection[] = [];
  let traps: string[] = [];
  let recap: string[] = [];
  if (!notes) return { sections, traps, recap };
  const parts = notes.split(/^###\s+/m);
  const lead = parts.shift()?.trim();
  if (lead) sections.push({ id: 'intro', title: 'Overview', body: lead });
  for (const p of parts) {
    const nl = p.indexOf('\n');
    const title = (nl < 0 ? p : p.slice(0, nl)).trim();
    const body = nl < 0 ? '' : p.slice(nl + 1).trim();
    if (TRAPS.test(title) && bullets(body).length) { traps = bullets(body); continue; }
    if (RECAP.test(title) && bullets(body).length) { recap = bullets(body); continue; }
    sections.push({ id: slug(title) || `part-${sections.length + 1}`, title, body });
  }
  return { sections, traps, recap };
}

/** Legacy `logic` is "1. … 2. … Why: …"; split it into intro text, steps and a reason. */
export function splitLogic(logic: string | undefined) {
  const steps: string[] = [];
  const rest: string[] = [];
  let why = '';
  for (const line of (logic ?? '').split('\n')) {
    const step = line.match(/^\s*\d+[.)]\s+(.*)$/);
    if (step) steps.push(step[1].trim());
    else if (/^\s*why\s*:/i.test(line)) why = line.replace(/^\s*why\s*:\s*/i, '').trim();
    else if (line.trim()) rest.push(line);
  }
  return { steps, why, rest: rest.join('\n') };
}

export const pad2 = (n: number) => String(n).padStart(2, '0');

export function readMinutes(...texts: (string | undefined)[]) {
  const words = texts.join(' ').replace(/\$[^$]*\$/g, ' x ').split(/\s+/).filter(Boolean).length;
  return Math.max(2, Math.round(words / 180));
}

export function Steps({ steps }: { steps: string[] }) {
  return (
    <ol className="steps">
      {steps.map((st, i) => <li key={i}><Md inline>{st}</Md></li>)}
    </ol>
  );
}

/** Question first; the working stays folded until the reader has tried it. */
export function Example({ ex, label = 'Try this' }: { ex: WorkedExample; label?: string }) {
  const lines = ex.steps?.length ? ex.steps : (ex.solution ?? '').split('\n').map((l) => l.trim()).filter(Boolean);
  return (
    <div className="example">
      <div className="example-kicker">{label}</div>
      <Md className="mt-1 font-semibold text-[15px]">{ex.q}</Md>
      <details className="mt-2.5 group">
        <summary className="solution-toggle">
          <span className="group-open:hidden">Show solution</span>
          <span className="hidden group-open:inline">Hide solution</span>
        </summary>
        <div className="mt-2.5">
          {lines.length > 1 ? <Steps steps={lines} /> : <Md className="text-[15px]">{lines[0]}</Md>}
          {ex.answer && <div className="answer-pill"><span>Answer</span> <Md inline>{ex.answer}</Md></div>}
        </div>
      </details>
    </div>
  );
}

export function MistakeCard({ m, i }: { m: string | Mistake; i: number }) {
  return (
    <div className="card p-4">
      <div className="text-xs font-extrabold tracking-wider uppercase" style={{ color: 'var(--bad)' }}>Mistake {pad2(i + 1)}</div>
      {typeof m === 'string' ? (
        <Md className="mt-1.5 text-[15px]">{m}</Md>
      ) : (
        <div className="mt-1.5 space-y-1.5 text-[15px]">
          <div className="flex gap-2"><span aria-hidden style={{ color: 'var(--bad)' }}>✗</span><Md inline>{m.wrong}</Md></div>
          <div className="flex gap-2"><span aria-hidden style={{ color: 'var(--ok)' }}>✓</span><Md inline>{m.right}</Md></div>
        </div>
      )}
    </div>
  );
}

export function SectionHead({ n, title, sub }: { n: number; title: string; sub?: string }) {
  return (
    <div>
      <div className="flex items-baseline gap-3">
        <span className="sec-num">{pad2(n)}</span>
        <h3 className="text-xl sm:text-[22px] font-extrabold leading-snug">{title}</h3>
      </div>
      {sub && <p className="text-sm muted mt-1.5">{sub}</p>}
    </div>
  );
}
