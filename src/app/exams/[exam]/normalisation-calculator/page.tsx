import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { NormalisationCalculator } from '@/components/exam-tools/NormalisationCalculator';
import { ToolPageFrame } from '@/components/exam-tools/ToolPageFrame';
import { loadExamPage, type Faq } from '@/components/exam-subpages/common';
import { NORMALISING, examsWith, hasTool } from '@/lib/examTools';

export const dynamic = 'force-static';
export const dynamicParams = false;

/** Only multi-shift SSC and RRB exams normalise. ssc-cgl keeps its own pages. */
export function generateStaticParams() {
  return examsWith('normalisation-calculator').map((exam) => ({ exam }));
}

const MAX: Record<string, number> = { 'ssc-chsl': 200, 'ssc-mts': 150, 'ssc-gd': 160, 'ssc-cpo': 100, 'rrb-ntpc': 100, 'rrb-group-d': 100 };

type Params = Promise<{ exam: string }>;

export async function generateMetadata({ params }: { params: Params }): Promise<Metadata> {
  const { exam: id } = await params;
  const page = hasTool(id, 'normalisation-calculator') ? loadExamPage(id) : null;
  if (!page) return {};
  return {
    title: `${page.info.name} normalisation calculator: estimate your normalised marks`,
    description: `How ${page.info.name} normalisation works and a free estimator for your normalised marks across shifts. Clearly an estimate, not the official score.`,
    alternates: { canonical: `/exams/${id}/normalisation-calculator/` },
  };
}

export default async function NormalisationPage({ params }: { params: Params }) {
  const { exam: id } = await params;
  const page = hasTool(id, 'normalisation-calculator') ? loadExamPage(id) : null;
  if (!page) notFound();
  const { info } = page;
  const family = NORMALISING[id];

  const faqs: Faq[] = family === 'ssc'
    ? [
        { q: 'Why does SSC normalise marks?', a: 'The exam runs in several shifts with different question papers. Normalisation adjusts for the difference in difficulty so that candidates are compared fairly.' },
        { q: 'Which method does SSC use now?', a: 'An SSC notice dated 2 June 2025 moved SSC exams to the equipercentile method, where your percentile within your own shift is matched to the same percentile in the other shifts. Check the official notice for the exact rules.' },
        { q: 'Can this tool give my exact normalised score?', a: 'No. SSC has not published a step-by-step worked formula, and the real calculation uses the score distribution of every shift. This tool gives an estimate only.' },
      ]
    : [
        { q: 'Why does RRB normalise marks?', a: 'CBTs run over many days and shifts with different papers. Normalisation puts every shift on a common scale before merit lists are made.' },
        { q: 'How does the RRB percentile method work?', a: 'Each candidate gets a percentile score within their own shift, meaning the share of candidates in that shift scoring at or below them. These are matched to marks in a base shift, using straight-line interpolation between neighbouring percentile points when an exact match is missing.' },
        { q: 'Can this tool give my exact normalised score?', a: 'No. It is an estimate. The board uses the full score data of every shift and has its own rules for choosing the base shift and breaking ties. Check the official methodology note.' },
      ];

  return (
    <ToolPageFrame
      id={id}
      kind="normalisation-calculator"
      h1={`${info.name} normalisation calculator`}
      faqs={faqs}
      intro={
        <>
          <p>{info.name} is held over several shifts, so raw marks are normalised before the merit list is made. Use this page to understand the idea and to get a rough estimate of what your raw score may become.</p>
          <p>It is an estimate, not the official score. The board does not publish a calculator, and the real result depends on score data from every shift that candidates cannot see.</p>
        </>
      }
    >
      <NormalisationCalculator family={family} maxDefault={MAX[id] ?? 100} />

      <section className="mt-10" aria-labelledby="how">
        <h2 id="how" className="text-2xl font-extrabold">How normalisation works</h2>
        <div className="card p-5 mt-3 text-sm muted space-y-3">
          {family === 'ssc' ? (
            <>
              <p>
                SSC announced in a notice dated 2 June 2025 that it would use the equipercentile method. In simple words: find your percentile within your own shift, then take the marks that the same percentile earns in the other shifts. The idea replaces the older mean and standard deviation approach.
              </p>
              <p>
                SSC has explained the concept but we could not find a step-by-step formula that anyone can reproduce, so the two modes above are approximations. The percentile table mode follows the equipercentile idea. The mean and SD mode is a quicker bell-curve shortcut that only works when scores are roughly bell-shaped.
              </p>
              <p>Always rely on the marks printed in the official result, and check the official notice for the current rules.</p>
            </>
          ) : (
            <>
              <p>
                RRB&apos;s methodology note describes a percentile-based method. The percentile score of a candidate is the share of candidates in their shift who scored at or below them, so the shift topper gets 100. A base shift is chosen using the shift averages and the number of candidates, and every shift is mapped onto it.
              </p>
              <p>
                If the base shift has a candidate at exactly your percentile, you get that candidate&apos;s marks. Otherwise the board interpolates between the two nearest percentile points of the base shift: normalised marks = Y1 + (Y2 − Y1) ÷ (X2 − X1) × (X − X1), where X is your percentile, X1 and X2 are the neighbouring percentiles and Y1 and Y2 are the base-shift marks at those points. There are separate rules for very low percentiles, and ties are broken by age and then name.
              </p>
              <p>
                Older RRB cycles used a mean and standard deviation formula instead, so you may still see that on older pages. We could not open the board&apos;s own methodology file while writing this, so the summary above comes from published explanations of it. Check the official methodology note before relying on any detail.
              </p>
            </>
          )}
        </div>
      </section>
    </ToolPageFrame>
  );
}
