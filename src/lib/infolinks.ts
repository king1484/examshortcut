// Issued by the Infolinks integration page for ExamShortcut on 16 October 2026.
export const INFOLINKS_PID = 3448714;
export const INFOLINKS_WSID = 0;

export function isInfolinksPage(pathname: string): boolean {
  // Only public reading pages. Forms, personal progress, calculators and tests stay out.
  return pathname === '/'
    || /^\/(study-guides|exam-analysis|current-affairs)(\/|$)/.test(pathname)
    || /^\/(quant|reasoning|english|ga|computer)(\/[^/]+)?\/?$/.test(pathname)
    || /^\/exams(\/[^/]+)?\/?$/.test(pathname)
    || /^\/(learn|vocab|static-gk|shortcut-tricks)\/?$/.test(pathname);
}

export const infolinksBootstrap = `
(function () {
  if (!['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;
  if (document.getElementById('infolinks-sdk')) return;
  window.infolinks_pid = ${INFOLINKS_PID};
  window.infolinks_wsid = ${INFOLINKS_WSID};
  var script = document.createElement('script');
  script.id = 'infolinks-sdk';
  script.async = true;
  script.src = 'https://resources.infolinks.com/js/infolinks_main.js';
  document.body.appendChild(script);
})();`;
