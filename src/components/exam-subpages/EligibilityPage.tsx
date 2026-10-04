import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Md } from '@/components/Md';
import { AgeCalculator } from './AgeCalculator';
import { buildAgeModel, fmtDate } from './ageModel';
import { SubpageFrame, VerifiedChip, loadExamPage, pickFaqs, plain, type Faq } from './common';

/* eslint-disable @typescript-eslint/no-explicit-any */
export function EligibilityPage({ id }: { id: string }) {
  const page = loadExamPage(id);
  if (!page) notFound();
  const { info, exam, year } = page;
  const el = exam.eligibility ?? {};
  const ages: { posts: string; range: string }[] = el.age ?? [];
  const edu: { posts: string; requirement: string }[] = el.education ?? [];
  const relax: { category: string; years: string }[] = el.ageRelaxation ?? [];
  const model = buildAgeModel(exam);
  const cutoff: string = model?.cutoff ?? '';

  const faqs: Faq[] = [];
  if (ages.length) {
    faqs.push({
      q: `What is the age limit for ${info.name}?`,
      a: `${ages.map((a) => `${a.posts}: ${a.range}`).join('; ')}.${cutoff ? ` Age is counted as on ${fmtDate(cutoff)} in this data.` : ''} The official notification's own age table is final.`,
    });
  }
  if (edu.length) {
    faqs.push({
      q: `What educational qualification is required for ${info.name}?`,
      a: edu.map((e) => `${e.posts}: ${plain(e.requirement)}`).join('; ') + '.',
    });
  }
  if (relax.length) {
    faqs.push({
      q: `How much age relaxation is given in ${info.name}?`,
      a: `${relax.map((r) => `${r.category}: ${r.years}`).join('; ')}. Relaxation is added to the upper age limit; see the notes below the table for the rules that apply to this exam.`,
    });
  }
  faqs.push(...pickFaqs(exam, /eligib|educational qualification|what qualification|attempt|final-year|who can apply|apply to both|apply for any/i, /age limit/i, 5));

  return (
    <SubpageFrame
      id={id}
      kind="eligibility"
      h1={`${info.name} ${year} eligibility — age limit, qualification, relaxation`}
      faqs={faqs}
      intro={
        <>
          <p>
            This page collects who can apply for <b>{info.name}</b> ({exam.fullName}), conducted by {info.basics.conductingBody}: the age limit for each group of posts, the educational qualification, nationality rules and the age relaxation for each category. It is built from the same verified data as the <Link className="underline" href={`/exams/${id}/`}>{info.name} guide</Link>, which also carries the {year} cycle status and dates.
          </p>
          <p>
            In one line: the basic educational requirement is <b>{info.basics.eligibility}</b>{ages.length > 0 && <>, and the age limit is {ages.length === 1 ? <b>{ages[0].range}</b> : <>set per post group ({ages.map((a) => a.range.match(/\d{1,2}\s*[–-]\s*\d{1,2}\s*years/)?.[0] ?? a.range).join(', ')})</>}</>}.
            {cutoff && <> Age is counted as on <b>{fmtDate(cutoff)}</b> in the data below.</>} Use the calculator to see your own eligible date-of-birth window.
          </p>
          <p><VerifiedChip exam={exam} /></p>
        </>
      }
    >
      {model && <AgeCalculator model={model} examName={info.name} />}

      {ages.length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Age limit</h2>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Posts</th><th>Age limit</th></tr></thead>
              <tbody>{ages.map((a, i) => <tr key={i}><td className="font-semibold">{a.posts}</td><td>{a.range}</td></tr>)}</tbody>
            </table>
          </div>
        </>
      )}

      {relax.length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Age relaxation by category</h2>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Category</th><th>Relaxation</th></tr></thead>
              <tbody>{relax.map((r, i) => <tr key={i}><td className="font-semibold">{r.category}</td><td>{r.years}</td></tr>)}</tbody>
            </table>
          </div>
        </>
      )}

      {edu.length > 0 && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Educational qualification</h2>
          <div className="tbl-wrap mt-3">
            <table className="tbl">
              <thead><tr><th>Posts / situation</th><th>Requirement</th></tr></thead>
              <tbody>{edu.map((e, i) => <tr key={i}><td className="font-semibold">{e.posts}</td><td><Md inline>{e.requirement}</Md></td></tr>)}</tbody>
            </table>
          </div>
        </>
      )}

      {el.nationality && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Nationality</h2>
          <Md className="mt-2 text-sm">{el.nationality}</Md>
        </>
      )}

      {el.notes && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Important notes on eligibility</h2>
          <div className="card p-5 mt-3"><Md className="text-sm">{el.notes}</Md></div>
        </>
      )}

      <h2 className="text-2xl font-extrabold mt-10">How to read these eligibility rules</h2>
      <div className="card p-5 mt-3 text-sm space-y-3">
        <p><b>The cut-off date decides your age.</b> Your age is not measured on the day you apply or the day of the exam. It is measured on one fixed date written in the notification{cutoff ? <> (<b>{fmtDate(cutoff)}</b> in the data used for this page)</> : null}.</p>
        <p><b>Relaxation is added to the upper limit only.</b> A category relaxation raises the maximum age, not the minimum. The calculator adds the number of years for the category you pick and shows the resulting birth-date window per post group.</p>
        <p><b>Your date of birth is taken from your certificate.</b> Age is checked against the date of birth on your Class 10 / matriculation certificate, so use that date rather than the one on any other document.</p>
        <p><b>Education is checked separately.</b> Meeting the age limit does not make you eligible on its own. Check the qualification table above for your post, including any row about final-year students or candidates who are still waiting for a result.</p>
        <p><b>The notification always wins.</b> Where the official notification differs from this page, follow the notification.</p>
      </div>

      {exam.documents && (
        <>
          <h2 className="text-2xl font-extrabold mt-10">Documents that prove age and qualification</h2>
          <Md className="mt-2 text-sm">{exam.documents}</Md>
        </>
      )}
    </SubpageFrame>
  );
}
