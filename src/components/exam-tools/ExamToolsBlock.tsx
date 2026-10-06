import Link from 'next/link';
import { getExamInfo } from '@/lib/exams';
import { TOOL_META, toolPath, toolsFor } from '@/lib/examTools';

/** "Calculators and tools" block for the exam hubs. Renders nothing for exams without generic tools (CGL and CAT have their own). */
export function ExamToolsBlock({ id }: { id: string }) {
  const info = getExamInfo(id);
  const kinds = toolsFor(id);
  if (!info || kinds.length === 0) return null;
  return (
    <section className="mt-6" aria-labelledby={`tools-${id}`}>
      <h2 id={`tools-${id}`} className="text-lg font-extrabold">{info.name} calculators</h2>
      <div className="grid sm:grid-cols-2 gap-3 mt-3">
        {kinds.map((k) => (
          <Link key={k} href={toolPath(id, k)} className="card p-4 hover:-translate-y-0.5 transition-transform">
            <div className="font-bold text-sm">{TOOL_META[k].emoji} {info.name} {TOOL_META[k].label.toLowerCase()}</div>
            <div className="text-xs faint mt-0.5">{TOOL_META[k].blurb}</div>
          </Link>
        ))}
      </div>
    </section>
  );
}
