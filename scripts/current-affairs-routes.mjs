/** Submit only months whose published content changed, plus their parent hubs. */
export function changedCurrentAffairsRoutes(current, previous = { months: [] }) {
  const before = new Map(previous.months.map(month => [month.month, JSON.stringify(month)]));
  const changed = current.months.filter(month => month.items?.length && before.get(month.month) !== JSON.stringify(month));
  if (!changed.length) return [];
  return ['/current-affairs/', `/current-affairs/${current.year}/`, ...changed.map(month => `/current-affairs/${current.year}/${month.month.slice(5)}/`)];
}
