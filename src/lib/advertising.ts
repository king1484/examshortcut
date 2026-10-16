export function isPublicAdPage(pathname: string): boolean {
  // Only public reading pages. Forms, personal progress, calculators and tests stay out.
  return pathname === '/'
    || /^\/(study-guides|exam-analysis|current-affairs)(\/|$)/.test(pathname)
    || /^\/(quant|reasoning|english|ga|computer)(\/[^/]+)?\/?$/.test(pathname)
    || /^\/exams(\/[^/]+)?\/?$/.test(pathname)
    || /^\/(learn|vocab|static-gk|shortcut-tricks)\/?$/.test(pathname);
}
