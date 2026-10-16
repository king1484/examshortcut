// Issued by the verified ExamShortcut Vignette zone on 16 October 2026.
export const MONETAG_VIGNETTE_ZONE = '12047445';
export const MONETAG_VIGNETTE_SRC = 'https://n6wxm.com/vignette.min.js';

export const monetagBootstrap = `
(function () {
  if (!['examshortcut.in', 'www.examshortcut.in'].includes(location.hostname)) return;
  if (document.getElementById('monetag-vignette-sdk')) return;
  var script = document.createElement('script');
  script.id = 'monetag-vignette-sdk';
  script.dataset.zone = '${MONETAG_VIGNETTE_ZONE}';
  script.async = true;
  script.src = '${MONETAG_VIGNETTE_SRC}';
  (document.body || document.documentElement).appendChild(script);
})();`;
