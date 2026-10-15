import Link from 'next/link';
import type { Subtopic, Topic, WorkedExample } from '@/lib/types';
import { SECTION_META, type SectionId } from '@/lib/sections';
import { MathText } from '@/components/MathText';
import { LazyTex } from '@/components/LazyTex';
import { Md } from '@/components/Md';
import { firstParagraph, exampleLines, joinList, patternsWithExample, plural, trapList } from '@/lib/topicInsights';
import { FORMULA_HABIT } from './copy';

function Worked({ ex }: { ex: WorkedExample }) {
  const lines = exampleLines(ex).slice(0, 6);
  return (
    <div className="mt-2 rounded-xl px-3 py-2.5 text-sm" style={{ background: 'var(--surface-2)' }}>
      <div className="faint text-xs font-semibold uppercase tracking-wide">Worked example</div>
      <div className="mt-1"><Md>{ex.q}</Md></div>
      {lines.length > 0 && (
        <ol className="mt-1.5 list-decimal pl-5 space-y-0.5">
          {lines.map((l, i) => <li key={i}><Md inline>{l}</Md></li>)}
        </ol>
      )}
      {ex.answer && <div className="mt-1.5 font-bold" style={{ color: 'var(--ok)' }}>Answer: <Md inline>{ex.answer}</Md></div>}
    </div>
  );
}

/** One subtopic's "in action" block: what it is, then up to two question types that use a formula,
    each with the formula, how to spot it and a worked example from our own lesson data. */
function ActionBlock({ s, base }: { s: Subtopic; base: string }) {
  const lead = firstParagraph(s.concept);
  let pats = patternsWithExample(s, true).slice(0, 2);
  if (!pats.length) pats = patternsWithExample(s, false).slice(0, 1);
  const fallbackTrick = !pats.length ? (s.tricks ?? []).find((x) => x.example && (x.example.steps?.length || x.example.solution)) : undefined;
  const nF = s.formulas?.length ?? 0;
  return (
    <div className="card p-4" id={`use-${s.id}`}>
      <h3 className="font-extrabold">{s.title}</h3>
      {nF > 0 && <div className="text-xs faint">{plural(nF, 'formula')} on this page</div>}
      {lead && <p className="text-sm muted mt-1.5"><MathText text={lead} max={300} /></p>}
      {pats.map((p) => (
        <div key={p.id} className="mt-3">
          <h4 className="text-sm font-bold">{p.name}{p.frequency ? <span className="faint font-normal"> · asked {p.frequency === 'occasional' ? 'occasionally' : p.frequency}</span> : null}</h4>
          {p.howToSpot && <p className="text-sm muted mt-0.5"><b>Use it when:</b> <MathText text={p.howToSpot} max={260} /></p>}
          {p.formula && <div className="my-1.5 overflow-x-auto overflow-y-hidden py-0.5"><LazyTex tex={p.formula} display /></div>}
          {p.example && <Worked ex={p.example} />}
        </div>
      ))}
      {fallbackTrick?.example && (
        <div className="mt-3">
          <h4 className="text-sm font-bold">{fallbackTrick.title}</h4>
          <p className="text-sm muted mt-0.5"><MathText text={fallbackTrick.body} max={260} /></p>
          <Worked ex={fallbackTrick.example} />
        </div>
      )}
      <p className="text-xs mt-3"><Link className="underline decoration-dotted" href={`${base}/learn/${s.id}/`}>Full lesson: {s.title} →</Link></p>
    </div>
  );
}

/** Server-rendered depth for /[section]/[topic]/formulas/: how the formulas are used, worked
    examples from the lessons, the mistakes that go with them and a memorisation routine. */
export function TopicFormulaGuide({ topic: t }: { topic: Topic }) {
  const meta = SECTION_META[t.sectionId as SectionId];
  const base = `/${t.sectionId}/${t.id}`;
  const withF = t.subtopics.filter((s) => (s.formulas?.length ?? 0) > 0);
  const nF = withF.reduce((n, s) => n + s.formulas!.length, 0);
  const habit = FORMULA_HABIT[t.sectionId as SectionId];
  const traps = trapList(t.subtopics, 8);
  const types = t.subtopics.reduce((n, s) => n + (s.patterns?.length ?? 0), 0);
  const typesWithFormula = t.subtopics.reduce((n, s) => n + (s.patterns ?? []).filter((p) => p.formula).length, 0);
  const nExamples = t.solvedExamples?.length ?? 0;
  const nPractice = t.practice?.length ?? 0;

  /* ---- topics without a formula list: show the key rules instead ---- */
  if (nF === 0) {
    const rulesSubs = t.subtopics.filter((s) => (s.revision?.length ?? 0) > 0);
    return (
      <div className="mt-10">
        <section aria-labelledby="fg-rules">
          <h2 id="fg-rules" className="text-2xl font-extrabold">Key rules for {t.title}, subtopic by subtopic</h2>
          <p className="text-sm muted mt-1">
            {t.title} is a {meta.short} topic that is learned through rules and recognition rather than numeric formulas. These are the one-line takeaways from each of its {plural(t.subtopics.length, 'lesson')}; each links to the full lesson with examples.
          </p>
          <div className="mt-3 grid gap-3">
            {rulesSubs.map((s) => (
              <div key={s.id} className="card p-4" id={`rules-${s.id}`}>
                <h3 className="font-extrabold">{s.title}</h3>
                <ul className="mt-2 list-disc pl-5 space-y-1 text-sm">
                  {s.revision!.slice(0, 6).map((r, i) => <li key={i}><MathText text={r} max={260} /></li>)}
                </ul>
                {(s.tricks?.length ?? 0) > 0 && (
                  <div className="mt-3">
                    <h4 className="text-xs font-bold uppercase tracking-wide faint">Shortcuts in this lesson</h4>
                    <ul className="mt-1 list-disc pl-5 space-y-1 text-sm">
                      {s.tricks!.slice(0, 3).map((x, i) => <li key={i}><b>{x.title}.</b> <MathText text={x.body} max={240} /></li>)}
                    </ul>
                  </div>
                )}
                <p className="text-xs mt-2"><Link className="underline decoration-dotted" href={`${base}/learn/${s.id}/`}>Full lesson: {s.title} →</Link></p>
              </div>
            ))}
          </div>
        </section>

        {traps.length > 0 && (
          <section className="mt-9" aria-labelledby="fg-mistakes">
            <h2 id="fg-mistakes" className="text-2xl font-extrabold">Mistakes that cost marks in {t.title}</h2>
            <ul className="mt-3 grid gap-2.5 list-none p-0">
              {traps.map((tr, i) => (
                <li key={i} className="card p-3.5 text-sm">
                  <div className="text-xs faint">{tr.sub.title}</div>
                  {tr.right ? (
                    <>
                      <p className="mt-1"><b style={{ color: 'var(--bad)' }}>Common slip:</b> <MathText text={tr.wrong} /></p>
                      <p className="mt-1"><b style={{ color: 'var(--ok)' }}>Instead:</b> <MathText text={tr.right} /></p>
                    </>
                  ) : <p className="mt-1"><MathText text={tr.wrong} /></p>}
                </li>
              ))}
            </ul>
          </section>
        )}

        <section className="mt-9" aria-labelledby="fg-learn">
          <h2 id="fg-learn" className="text-2xl font-extrabold">How to hold these rules</h2>
          <p className="text-[15px] mt-2">{habit}</p>
          <p className="text-sm muted mt-3">
            Next steps for {t.title}: work through the <Link className="underline" href={`${base}/learn/`}>lessons</Link>
            {nExamples > 0 && <>, read the <Link className="underline" href={`${base}/examples/`}>{plural(nExamples, 'solved example')}</Link></>}
            {nPractice > 0 && <> and take the <Link className="underline" href={`${base}/practice/`}>{nPractice}-question practice test</Link></>}.
          </p>
        </section>
      </div>
    );
  }

  return (
    <div className="mt-10">
      <section aria-labelledby="fg-about">
        <h2 id="fg-about" className="text-2xl font-extrabold">How these {t.title} formulas are used</h2>
        <p className="mt-2 text-[15px] muted">
          The cards above hold {plural(nF, 'formula')} across {plural(withF.length, 'subtopic')}: {joinList(withF.map((s) => `${s.title} (${s.formulas!.length})`))}.
          {types > 0 && typesWithFormula > 0 && <> Of the {plural(types, 'recurring question type')} catalogued for this topic, {typesWithFormula} are solved directly from a formula; the rest need a method or a table rather than a single relation.</>}
          {' '}A formula sheet only helps when you know which words in a question call for which formula, so the section below pairs each subtopic with the question types that use its formulas, a worked case taken from the lessons, and a note on when to apply it.
        </p>
        <p className="mt-2 text-sm faint">Jump to: {withF.map((s, i) => <span key={s.id}>{i > 0 && ' · '}<a className="underline decoration-dotted" href={`#use-${s.id}`}>{s.title}</a></span>)}</p>
      </section>

      <section className="mt-9" aria-labelledby="fg-action">
        <h2 id="fg-action" className="text-2xl font-extrabold">Formulas in action</h2>
        <p className="text-sm muted mt-1">For each subtopic: what it deals with, when the formula applies, and a worked example from our lessons.</p>
        <div className="mt-3 grid gap-3">
          {withF.map((s) => <ActionBlock key={s.id} s={s} base={base} />)}
        </div>
      </section>

      {traps.length > 0 && (
        <section className="mt-9" aria-labelledby="fg-mistakes">
          <h2 id="fg-mistakes" className="text-2xl font-extrabold">Common mistakes when applying {t.title} formulas</h2>
          <p className="text-sm muted mt-1">Knowing a formula and applying it correctly are different skills. These are the slips flagged in the lessons.</p>
          <ul className="mt-3 grid gap-2.5 list-none p-0">
            {traps.map((tr, i) => (
              <li key={i} className="card p-3.5 text-sm">
                <div className="text-xs faint">{tr.sub.title}</div>
                {tr.right ? (
                  <>
                    <p className="mt-1"><b style={{ color: 'var(--bad)' }}>Common slip:</b> <MathText text={tr.wrong} /></p>
                    <p className="mt-1"><b style={{ color: 'var(--ok)' }}>Instead:</b> <MathText text={tr.right} /></p>
                  </>
                ) : <p className="mt-1"><MathText text={tr.wrong} /></p>}
              </li>
            ))}
          </ul>
        </section>
      )}

      <section className="mt-9" aria-labelledby="fg-learn">
        <h2 id="fg-learn" className="text-2xl font-extrabold">How to memorise this sheet</h2>
        <p className="text-[15px] mt-2">{habit}</p>
        <p className="text-[15px] mt-2 muted">
          With {nF} formulas, do not try to learn them in one sitting. Take one subtopic at a time, test yourself the next day, then again after a few days; the <Link className="underline" href="/revision-planner/">revision planner</Link> can schedule those repeats.
        </p>
        <p className="text-sm muted mt-3">
          Put them to use: read the <Link className="underline" href={`${base}/learn/`}>lessons</Link>
          {nExamples > 0 && <>, work through the <Link className="underline" href={`${base}/examples/`}>{plural(nExamples, 'solved example')}</Link></>}
          {nPractice > 0 && <> and then take the <Link className="underline" href={`${base}/practice/`}>{nPractice}-question practice test</Link></>}.
          {' '}The combined sheet for every topic is on the <Link className="underline" href="/formula-sheet/">all-topics formula sheet</Link>.
        </p>
      </section>
    </div>
  );
}
