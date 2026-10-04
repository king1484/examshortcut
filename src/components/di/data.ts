/*
 * Illustrative data for practice. Every number shown in the DI graphs, tables,
 * questions, answers and solutions on /data-interpretation/ is derived from the
 * constants in this file, so nothing can drift out of sync.
 */

export const DATA_LABEL = 'Illustrative data for practice';

export type QA = { q: string; a: string; sol: string };

/* ---------- number helpers ---------- */

export function fmt(n: number, dp = 2): string {
  const r = Number(n.toFixed(dp));
  return r.toLocaleString('en-IN', { maximumFractionDigits: dp });
}

const sum = (xs: number[]) => xs.reduce((s, x) => s + x, 0);
const gcd = (a: number, b: number): number => (b === 0 ? a : gcd(b, a % b));
const pctChange = (from: number, to: number) => ((to - from) / from) * 100;

/* ---------- 1. Multi-series bar graph ---------- */

export const BAR = {
  title: 'Cars produced by three plants (in thousands)',
  unit: 'thousand cars',
  years: ['2020', '2021', '2022', '2023', '2024'],
  series: [
    { name: 'Plant A', color: 'var(--brand)', values: [40, 55, 45, 60, 70] },
    { name: 'Plant B', color: 'var(--info)', values: [50, 45, 60, 55, 65] },
    { name: 'Plant C', color: 'var(--ok)', values: [30, 35, 50, 45, 55] },
  ],
};

export function barQuestions(): QA[] {
  const { years, series } = BAR;
  const [A, B, C] = series;
  const yi = years.indexOf('2023');
  const col = series.map((s) => s.values[yi]);
  const total = sum(col);

  const a0 = A.values[0], a1 = A.values[A.values.length - 1];
  const rise = a1 - a0;
  const pct = pctChange(a0, a1);

  const cTotal = sum(C.values);
  const cAvg = cTotal / C.values.length;

  return [
    {
      q: `What was the total production of all three plants together in ${years[yi]}?`,
      a: `${fmt(total)} thousand cars`,
      sol: `Read one column only: ${col.map(fmt).join(' + ')} = ${fmt(total)} thousand.`,
    },
    {
      q: `By what percentage did Plant A's production rise from ${years[0]} to ${years[years.length - 1]}?`,
      a: `${fmt(pct)}%`,
      sol: `Change ÷ original × 100. Change = ${fmt(a1)} − ${fmt(a0)} = ${fmt(rise)}; original is the earlier year, ${fmt(a0)}. So ${fmt(rise)}/${fmt(a0)} × 100 = ${fmt(pct)}%.`,
    },
    {
      q: `What was Plant C's average annual production over the five years?`,
      a: `${fmt(cAvg)} thousand cars`,
      sol: `Average = sum ÷ count. ${C.values.map(fmt).join(' + ')} = ${fmt(cTotal)}; ${fmt(cTotal)} ÷ ${C.values.length} = ${fmt(cAvg)}. (Plant B reads ${fmt(B.values[yi])} in ${years[yi]}, so do not mix up the colours.)`,
    },
  ];
}

/* ---------- 2. Line graph with two lines ---------- */

export const LINE = {
  title: 'Revenue and expenditure of a company (₹ lakh)',
  unit: '₹ lakh',
  periods: ['2019', '2020', '2021', '2022', '2023', '2024'],
  revenue: { name: 'Revenue', color: 'var(--brand)', values: [120, 135, 128, 150, 165, 180] },
  spend: { name: 'Expenditure', color: 'var(--info)', values: [90, 100, 110, 115, 125, 130] },
};

export function lineQuestions(): QA[] {
  const { periods, revenue, spend } = LINE;
  const profit = revenue.values.map((r, i) => r - spend.values[i]);

  const minGap = Math.min(...profit);
  const minI = profit.indexOf(minGap);

  // the one period in which revenue fell versus the previous period
  let dropI = 1;
  for (let i = 1; i < revenue.values.length; i++) {
    if (revenue.values[i] - revenue.values[i - 1] < revenue.values[dropI] - revenue.values[dropI - 1]) dropI = i;
  }
  const dFrom = revenue.values[dropI - 1], dTo = revenue.values[dropI];
  const dPct = Math.abs(pctChange(dFrom, dTo));

  const last = periods.length - 1;
  const lastProfit = profit[last];
  const lastPct = (lastProfit / spend.values[last]) * 100;

  return [
    {
      q: `In which year was the gap between revenue and expenditure (the profit) the smallest, and what was it?`,
      a: `${periods[minI]}, ${fmt(minGap)} lakh`,
      sol: `Profit = revenue − expenditure each year: ${periods.map((p, i) => `${p}: ${fmt(profit[i])}`).join(', ')}. The smallest is ${periods[minI]}, where the lines are closest.`,
    },
    {
      q: `Revenue fell in one year compared with the year before. What was the percentage fall?`,
      a: `${fmt(dPct)}% (${periods[dropI - 1]} to ${periods[dropI]})`,
      sol: `Find the dip: revenue went from ${fmt(dFrom)} to ${fmt(dTo)}. Fall = ${fmt(dFrom - dTo)}; base is the earlier year, so ${fmt(dFrom - dTo)}/${fmt(dFrom)} × 100 = ${fmt(dPct)}%.`,
    },
    {
      q: `In ${periods[last]}, profit was what percentage of expenditure?`,
      a: `${fmt(lastPct)}%`,
      sol: `Profit = ${fmt(revenue.values[last])} − ${fmt(spend.values[last])} = ${fmt(lastProfit)}. "Percentage of expenditure" puts expenditure in the denominator: ${fmt(lastProfit)}/${fmt(spend.values[last])} × 100 = ${fmt(lastPct)}%.`,
    },
  ];
}

/* ---------- 3. Pie chart (angles in degrees) ---------- */

export const PIE = {
  title: 'How a family spends its monthly income',
  income: 36000,
  slices: [
    { name: 'Rent', color: 'var(--brand)', deg: 90 },
    { name: 'Food', color: 'var(--info)', deg: 108 },
    { name: 'Education', color: 'var(--ok)', deg: 54 },
    { name: 'Savings', color: 'var(--c-reasoning)', deg: 72 },
    { name: 'Others', color: 'var(--warn)', deg: 36 },
  ],
};

export function pieQuestions(): QA[] {
  const { income, slices } = PIE;
  const get = (n: string) => slices.find((s) => s.name === n)!;
  const food = get('Food'), sav = get('Savings'), edu = get('Education');

  const foodAmt = (food.deg / 360) * income;
  const savPct = sav.deg / 3.6;
  const newEdu = 12000;
  const newDeg = (newEdu / income) * 360;
  const perDeg = income / 360;

  return [
    {
      q: `The monthly income is ₹${fmt(income)}. How much is spent on Food?`,
      a: `₹${fmt(foodAmt)}`,
      sol: `Value = angle ÷ 360 × total = ${food.deg}/360 × ${fmt(income)}. Shortcut: 1° = ₹${fmt(perDeg)}, so ${food.deg} × ${fmt(perDeg)} = ₹${fmt(foodAmt)}.`,
    },
    {
      q: `What percentage of the income goes to Savings?`,
      a: `${fmt(savPct)}%`,
      sol: `Percent = angle ÷ 3.6 (because 360° = 100%). ${sav.deg} ÷ 3.6 = ${fmt(savPct)}%.`,
    },
    {
      q: `Education currently takes ${edu.deg}°. If its spending were instead ₹${fmt(newEdu)} out of the same income, what central angle would its sector need?`,
      a: `${fmt(newDeg)}°`,
      sol: `Angle = value ÷ total × 360 = ${fmt(newEdu)}/${fmt(income)} × 360 = ${fmt(newDeg)}°. Check with 1° = ₹${fmt(perDeg)}: ${fmt(newEdu)} ÷ ${fmt(perDeg)} = ${fmt(newDeg)}°.`,
    },
  ];
}

/* ---------- 4. Caselet to table ---------- */

export const CASELET = {
  title: 'A coaching institute and its batches',
  total: 800,
  batches: [
    { name: 'Morning', part: 5, girlsPct: 40 },
    { name: 'Evening', part: 3, girlsPct: 50 },
    { name: 'Weekend', part: 2, girlsPct: 25 },
  ],
};

export function casletRows() {
  const { total, batches } = CASELET;
  const parts = sum(batches.map((b) => b.part));
  return batches.map((b) => {
    const size = (total * b.part) / parts;
    const girls = (size * b.girlsPct) / 100;
    return { name: b.name, part: b.part, girlsPct: b.girlsPct, size, girls, boys: size - girls };
  });
}

export function casletText(): string {
  const { total, batches } = CASELET;
  const names = batches.map((b) => b.name);
  const ratio = batches.map((b) => b.part).join(' : ');
  const girls = batches.map((b, i) => `${b.girlsPct}% of the ${names[i]} batch`);
  return `A coaching institute has ${fmt(total)} students spread over three batches, ${names[0]}, ${names[1]} and ${names[2]}, in the ratio ${ratio}. The girls are ${girls[0]}, ${girls[1]} and ${girls[2]}. The rest of each batch are boys.`;
}

export function casletQuestions(): QA[] {
  const rows = casletRows();
  const total = CASELET.total;
  const girls = sum(rows.map((r) => r.girls));
  const boys = sum(rows.map((r) => r.boys));
  const g = gcd(girls, boys);
  const wk = rows[rows.length - 1];
  const wkPct = (wk.boys / boys) * 100;
  const parts = sum(rows.map((r) => r.part));
  const unit = total / parts;

  return [
    {
      q: `How many girls are there in the institute altogether?`,
      a: fmt(girls),
      sol: `Make the table first. One ratio part = ${fmt(total)}/${parts} = ${fmt(unit)} students, so batches are ${rows.map((r) => `${r.name} ${fmt(r.size)}`).join(', ')}. Girls = ${rows.map((r) => `${r.girlsPct}% of ${fmt(r.size)} = ${fmt(r.girls)}`).join('; ')}. Total ${fmt(girls)}.`,
    },
    {
      q: `What is the ratio of girls to boys in the whole institute?`,
      a: `${fmt(girls / g)} : ${fmt(boys / g)}`,
      sol: `Girls = ${fmt(girls)}, boys = ${fmt(total)} − ${fmt(girls)} = ${fmt(boys)}. Divide both by their HCF ${fmt(g)}: ${fmt(girls / g)} : ${fmt(boys / g)}.`,
    },
    {
      q: `The ${wk.name} batch's boys are what percentage of all boys in the institute?`,
      a: `${fmt(wkPct)}%`,
      sol: `${wk.name} boys = ${fmt(wk.size)} − ${fmt(wk.girls)} = ${fmt(wk.boys)}. Base is all boys (${fmt(boys)}), so ${fmt(wk.boys)}/${fmt(boys)} × 100 = ${fmt(wkPct)}%.`,
    },
  ];
}
