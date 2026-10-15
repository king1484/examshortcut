import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { SalaryCalculator } from '@/components/exam-tools/SalaryCalculator';
import { ToolPageFrame } from '@/components/exam-tools/ToolPageFrame';
import { VerifiedChip, loadExamPage, type Faq } from '@/components/exam-subpages/common';
import { CENTRAL, examsWith, hasTool } from '@/lib/examTools';
import { bankPay, salaryPosts, statePay } from '@/lib/examToolsServer';

export const dynamic = 'force-static';
export const dynamicParams = false;

export function generateStaticParams() {
  return examsWith('salary-calculator').map((exam) => ({ exam }));
}

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam: id } = await params;
  const page = hasTool(id, 'salary-calculator') ? loadExamPage(id) : null;
  if (!page) return {};
  return {
    title: `${page.info.name} salary calculator: in-hand pay by post`,
    description: `Estimate monthly in-hand salary for ${page.info.name} posts from pay level or basic pay, DA, HRA by city class and deductions. Free, runs in your browser.`,
    alternates: { canonical: `/exams/${id}/salary-calculator/` },
  };
}

export default async function SalaryCalculatorPage({ params }: { params: Params }) {
  const { exam: id } = await params;
  const page = hasTool(id, 'salary-calculator') ? loadExamPage(id) : null;
  if (!page) notFound();
  const { info, exam } = page;
  const bank = /^(ibps|sbi)/.test(id);
  // UP Police is a state government force: central 7th CPC allowance rules would be wrong, so it gets the blank-allowance form.
  const state = id === 'up-police';
  const posts = bank || state ? [] : salaryPosts(exam);
  const banks = bank ? bankPay(exam) : state ? statePay(exam) : [];
  if (bank || state ? banks.length === 0 : posts.length === 0) notFound();

  const faqs: Faq[] = state
    ? [
        { q: `What is the starting pay for ${info.name}?`, a: `Pay Level 3, which our exam page gives as ${'₹' + banks[0].basic.toLocaleString('en-IN')}${banks[0].scaleMax ? ` to ${'₹' + banks[0].scaleMax.toLocaleString('en-IN')}` : ''} a month before allowances. This comes from the recruitment notice.` },
        { q: 'Why are DA and HRA left blank?', a: 'UP government employees get DA and HRA by state government order, and we could not confirm the current official values. The central government rates do not apply, so enter the numbers from the latest order or your appointment letter.' },
        { q: 'Is the in-hand figure exact?', a: 'No. It is an estimate from the numbers you enter. Income tax, uniform and ration allowances and any other deductions are not included, so your payslip will differ.' },
      ]
    : bank
    ? [
        { q: `What is the starting basic pay for ${info.name}?`, a: `${banks.map((b) => `${b.name}: basic ${'₹' + b.basic.toLocaleString('en-IN')}${b.scaleMax ? ` on a scale up to ${'₹' + b.scaleMax.toLocaleString('en-IN')}` : ''}`).join('; ')}. These come from the recruitment notice.` },
        { q: 'Why are DA and HRA left blank?', a: 'Banks revise DA by circular and HRA depends on the centre, and we could not confirm current official values. Enter the numbers from your bank\'s latest circular or offer letter.' },
        { q: 'Is the in-hand figure exact?', a: 'No. It is an estimate from the numbers you enter. Income tax, perquisites and bank-specific allowances are not included, so your payslip will differ.' },
      ]
    : [
        { q: 'What DA rate does the calculator use?', a: `${CENTRAL.da}% of basic pay, the rate in force from ${CENTRAL.daAsOf}. The government revises DA twice a year, so the field is editable. Update it when a new rate is notified.` },
        { q: 'How is HRA worked out?', a: `HRA is a percentage of basic pay by city class: ${CENTRAL.hra.X}% for X, ${CENTRAL.hra.Y}% for Y and ${CENTRAL.hra.Z}% for Z cities, since DA crossed 50%.` },
        { q: 'What deductions are counted?', a: 'NPS at 10% of basic plus DA by default, the health scheme contribution for your pay level, and any other deductions you enter. Income tax is not included.' },
        { q: 'Why does my payslip differ?', a: 'Post-specific allowances such as risk, ration, uniform or night duty, the exact city list for transport allowance, and your tax slab are not modelled. Treat the result as an estimate.' },
      ];

  return (
    <ToolPageFrame
      id={id}
      kind="salary-calculator"
      h1={`${info.name} salary calculator`}
      faqs={faqs}
      intro={
        state ? (
          <>
            <p>Pick the post, then enter DA, HRA and other allowances from the latest UP government order. The calculator adds them to the starting pay and subtracts deductions to give an approximate monthly in-hand figure.</p>
            <p>The starting pay comes from the recruitment notice. State allowances change by order and we could not confirm current official values, so they start blank. Check the government order and the official notice.</p>
            <p><VerifiedChip exam={exam} /></p>
          </>
        ) : bank ? (
          <>
            <p>Pick the post, then enter DA, HRA and other allowances from your bank&apos;s latest circular. The calculator adds them to basic pay and subtracts deductions to give an approximate monthly in-hand figure.</p>
            <p>Basic pay comes from the recruitment notice. Bank allowances change often and we could not confirm current official values, so they start blank. Check your bank&apos;s circular and the official notice.</p>
            <p><VerifiedChip exam={exam} /></p>
          </>
        ) : (
          <>
            <p>Pick a {info.name} post to start from its pay level, choose the city class for HRA, and see an approximate monthly in-hand salary. Pay levels come from the {info.name} notice, and the allowance rules follow the 7th Pay Commission for central government staff.</p>
            <p>DA, NPS and the health scheme amount are editable, so you can update them when the rates change. Income tax and post-specific allowances are not included.</p>
            <p><VerifiedChip exam={exam} /></p>
          </>
        )
      }
    >
      <SalaryCalculator mode={state ? 'state' : bank ? 'bank' : 'central'} posts={posts} bank={banks} />
    </ToolPageFrame>
  );
}
