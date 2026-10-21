# Security policy

## Reporting a vulnerability

Please do not disclose credentials, student records, or exploitable details in a public issue. Use this repository's **Security → Report a vulnerability** option when available, or contact the maintainer using the address on [examshortcut.in/contact](https://examshortcut.in/contact/). There is no guaranteed response time or paid bounty program.

Include affected files or routes, reproduction steps using synthetic data, the potential impact, and a suggested fix if you have one. Do not access another person's records or test against the live site without the maintainer's permission.

## Supported code

Security fixes target the current default branch. No older release series is supported at present.

## Sensitive information

Do not commit `.env.local`, `.dev.vars`, provider tokens, service-account keys, proxy credentials, feedback exports, or student data. Firebase `NEXT_PUBLIC_*` web configuration is intentionally browser-visible; Auth and Firestore rules enforce access control. A public configuration identifier is not a substitute for secure rules.

Public ad-placement identifiers and the published IndexNow ownership-verification key may resemble secrets to scanners. Review findings in context; never disable a secret rule across the repository to hide an unexplained result. If a private credential is exposed, revoke it before considering history cleanup.

## Repository checks

The contributor workflow has read-only repository permissions and does not receive production secrets or deploy. The scheduled analysis/deployment workflow is separate and maintainer-controlled. Do not add privileged `pull_request_target` execution for untrusted pull requests.
