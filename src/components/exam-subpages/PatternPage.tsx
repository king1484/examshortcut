import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Md } from '@/components/Md';
import { SECTION_META, listTopics, type SectionId } from '@/lib/content';
import { SubpageFrame, VerifiedChip, loadExamPage, pickFaqs, subPath, type Faq } from './common';

/* eslint-disable @typescript-eslint/no-explicit-any */

/* General preparation advice per subject. Process advice only — no exam facts or numbers;
   the question counts and marks shown next to it come from the exam data. */
const APPROACH: Record<SectionId, string> = {
  quant: 'Learn the formula and the shortcut for each topic first, then drill timed sets so that routine calculation questions take seconds. In the exam, take the questions you can do quickly and leave the long, multi-step ones for the end. Topic tests after every chapter show which topics still cost you time.',
  reasoning: 'Reasoning rewards pattern recognition, so practise each question type until you recognise it on sight: series, coding-decoding, analogy, classification, syllogism, direction and blood-relation questions, and non-verbal figures. Work in rough on paper rather than in your head, and skip any puzzle that is not settling within a minute or so.',
  english: 'Build the basics in grammar (error spotting, fill in the blanks, sentence improvement) and add a little vocabulary every day: idioms, one-word substitutions, synonyms and spellings. For comprehension, read the questions before the passage and answer from the text, not from outside knowledge.',
  ga: 'General awareness is memory work, so revise in short, regular rounds instead of cramming. Combine static GK tables with the last several months of current affairs, and use the daily quiz to keep facts fresh. Decide in advance how much time you will give it.',
  computer: 'Computer questions are fact-based: hardware and software, operating systems, MS Office shortcuts, networking and internet basics, and security terms. Read through the notes a few times and revise with quick quizzes rather than long practice sessions.',
};

export function PatternPage({ id }: { id: string }) {
  const page = loadExamPage(id);
  if (!page) notFound();
  const { info, exam, year } = page;
  const stages: any[] = exam.stages ?? [];
  const scored = stages.filter((s) => (s.sections ?? []).length > 0);

  // subjects that have a notes section on the site, in order of first appearance
  const sectionIds: SectionId[] = [];
  for (const st of stages) for (const s of st.sections ?? []) {
    if (s.sectionId && info.sections.includes(s.sectionId) && !sectionIds.includes(s.sectionId)) sectionIds.push(s.sectionId);
  }

  const stageFacts = (st: any) => [
    st.totalQuestions != null && `${st.totalQuestions} questions`,
    st.totalMarks != null && `${st.totalMarks} marks`,
    st.durationMin != null && `${st.durationMin} minutes`,
    st.negative && String(st.negative),
  ].filter(Boolean) as string[];

  const faqs: Faq[] = [];
  faqs.push({ q: `What is the selection process for ${info.name}?`, a: `${info.basics.stages}.` });
  for (const st of scored.slice(0, 3)) {
    const facts = stageFacts(st);
    faqs.push({
      q: `What is the ${st.name} pattern in ${info.name}?`,
      a: `${facts.length ? facts.join(', ') + '. ' : ''}Sections: ${(st.sections ?? []).map((s: any) => `${s.name} (${s.questions} questions, ${s.marks} marks)`).join('; ')}.`,
    });
  }
  faqs.push(...pickFaqs(exam, /negative|marking|normali|sectional|qualifying|count|interview|waiting|session|both|cbat|typing|language|hindi/i, /\bpattern\b/i, 6));
  const uniqueFaqs = faqs.filter((f, i) => faqs.findIndex((g) => g.q === f.q) === i);

  return (
    <SubpageFrame
      id={id}
      kind="exam-pattern"
      h1={`${info.name} ${year} exam pattern — sections, marks, negative marking`}
      faqs={uniqueFaqs}
      intro={
        <>
          <p>
            <b>{info.name}</b> ({exam.fullName}) is conducted by {info.basics.conductingBody}. The stages are: <b>{info.basics.stages}</b>. This page sets out each stage with its sections, questions, marks, duration and negative marking, explains how the final selection is made, and shows how to approach each subject. For dates and the current status of the {year} cycle, see the <Link className="underline" href={`/exams/${id}/`}>{info.name} guide</Link>.
          </p>
          {scored.length > 0 && (
            <p>
              {scored.map((st, i) => (
                <span key={st.id}>{i > 0 && ' '}<b>{st.name}:</b> {stageFacts(st).join(', ')}.</span>
              ))}
            </p>
          )}
          <p><VerifiedChip exam={exam} /></p>
        </>
      }
    >
      <h2 className="text-2xl font-extrabold mt-8">Stage-wise exam pattern</h2>
      {stages.map((st) => (
        <div key={st.id} className="mt-5">
          <h3 className="font-bold">{st.name} {st.nature && <span className="chip ml-1">{st.nature}</span>}</h3>
          {(st.mode || st.durationMin != null || st.negative) && (
            <p className="text-xs faint mt-1">{[st.mode, st.durationMin != null && `${st.durationMin} min`, st.negative].filter(Boolean).join(' · ')}</p>
          )}
          {(st.sections ?? []).length > 0 && (
            <div className="tbl-wrap mt-2">
              <table className="tbl">
                <thead><tr><th>Section</th><th>Questions</th><th>Marks</th></tr></thead>
                <tbody>
                  {st.sections.map((s: any) => (
                    <tr key={s.name}>
                      <td>
                        {s.sectionId && info.sections.includes(s.sectionId)
                          ? <Link className="underline decoration-dotted" href={`/${s.sectionId}/`}>{s.name}</Link>
                          : s.name}
                      </td>
                      <td>{s.questions}</td><td>{s.marks}</td>
                    </tr>
                  ))}
                  {st.totalQuestions != null && (
                    <tr><td className="font-bold">Total</td><td className="font-bold">{st.totalQuestions}</td><td className="font-bold">{st.totalMarks}</td></tr>
                  )}
                </tbody>
              </table>
            </div>
          )}
          {st.notes && <Md className="mt-2 text-sm muted">{st.notes}</Md>}
        </div>
      ))}

      {exam.selectionProcess && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Selection process</h2>
          <Md className="mt-2">{exam.selectionProcess}</Md>
        </>
      )}

      {exam.normalization && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Normalisation: why your raw score is not your final score</h2>
          <Md className="mt-2 text-sm muted">{exam.normalization}</Md>
        </>
      )}

      <h2 className="text-2xl font-extrabold mt-10">How to read this pattern</h2>
      <div className="card p-5 mt-3 text-sm space-y-3">
        <p>Each stage carries a tag that tells you what it is for.{stages.some((s) => s.nature) && <> In this exam: {stages.filter((s) => s.nature).map((s) => `${s.name} is “${s.nature}”`).join('; ')}.</>} Read each stage's tag and notes to see whether its marks count towards the final merit or only decide who moves to the next stage, because that changes how much risk is worth taking on a single question.</p>
        <p>Always check the negative marking line before you decide how freely to guess. Where there is a penalty, a wrong answer costs marks; where the data says there is none, leaving a question blank only loses the chance to score.</p>
        <p>Question counts per section are the best guide to how much time and practice each subject deserves. Use the tables above to split your preparation in proportion to the marks on offer, and revisit the split after each mock or topic test.</p>
      </div>

      {sectionIds.length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">How to approach each section</h2>
          <p className="text-sm muted mt-2">Each subject below links to the full notes on ExamShortcut. Topics are listed as high importance where our topic data flags them; the question counts come from the pattern above.</p>
          <div className="space-y-4 mt-4">
            {sectionIds.map((sid) => {
              const meta = SECTION_META[sid];
              const topics = listTopics(sid);
              const key = topics.filter((t) => t.importance === 'high').slice(0, 6);
              const shown = key.length ? key : topics.slice(0, 6);
              const appears = stages.flatMap((st) => (st.sections ?? []).filter((s: any) => s.sectionId === sid).map((s: any) => `${st.name}: ${s.questions} questions, ${s.marks} marks`));
              return (
                <section key={sid} className="card p-5" style={{ borderTop: `3px solid ${meta.color}` }}>
                  <div className="flex items-baseline justify-between gap-2 flex-wrap">
                    <h3 className="font-bold text-lg">{meta.name}</h3>
                    <Link href={`/${sid}/`} className="text-sm underline decoration-dotted">All {topics.length} topics →</Link>
                  </div>
                  {appears.length > 0 && <p className="text-xs faint mt-1">{appears.join(' · ')}</p>}
                  <p className="text-sm mt-2">{APPROACH[sid]}</p>
                  {shown.length > 0 && (
                    <p className="text-sm mt-3">
                      <b>{key.length ? 'High-importance topics' : 'Start with'}:</b>{' '}
                      {shown.map((t, i) => (
                        <span key={t.id}>{i > 0 && ', '}<Link className="underline decoration-dotted" href={`/${sid}/${t.id}/`}>{t.title}</Link></span>
                      ))}
                    </p>
                  )}
                </section>
              );
            })}
          </div>
        </>
      )}

      <p className="text-sm muted mt-8">
        Next, check who can apply on the <Link className="underline" href={subPath(id, 'eligibility')}>{info.name} eligibility page</Link> and compare posts and pay on the <Link className="underline" href={subPath(id, 'salary-and-posts')}>{info.name} salary and posts page</Link>.
      </p>
    </SubpageFrame>
  );
}
