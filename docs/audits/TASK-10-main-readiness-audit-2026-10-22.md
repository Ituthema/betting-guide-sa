# TASK-10 — Main-branch readiness audit

**Audit date:** 2026-10-22  
**Repository:** `Ituthema/betting-guide-sa`  
**Audited ref:** `main` (content snapshot SHA: `72aff34e4cd70401bd2c3970250c96a5afa403e4`)  
**Purpose:** Establish an evidence-based content, affiliate, legal-review and release-readiness baseline. This is an audit report only; it does not certify legal compliance or mark any content verified.

## Executive summary

**Release status: NOT READY for a fully promoted affiliate launch.** The static build and existing automated checks have passed in the latest recorded main/PR validation, but technical success is not evidence that operator facts, current offers, licensing, privacy practices or legal obligations have been independently verified.

The inspected `content/pages.json` contains **77 records**:
- **55** `editorial-review`
- **19** `needs-verification`
- **3** `legal-review-required`
- **0** `verified`
- **3 of 77** records have at least one source entry; **74 of 77** have none.
- **77 of 77** records have `lastVerified: null`.
- The three sourced records are `/guides/responsible-gambling/`, `/bookmakers/licensing-checklist/`, and `/guides/risk/self-exclusion/`. Their listed source check date is 2026-10-19.
- The three `legal-review-required` records are `/legal/privacy/`, `/legal/terms/`, and `/affiliate-disclosure/`.

These counts describe metadata in the audited file. They do not mean every unsourced educational statement is false; they mean the repository does not currently attach source evidence to those records.

## Scope and method

Read the current `main` versions of:
- `content/pages.json`
- `README.md`
- `WORKFLOW.md`
- `scripts/build.py`
- `scripts/validate.py`
- `scripts/check-banned-claims.sh`
- `.github/workflows/pages.yml`

This is a repository snapshot review, not a complete legal opinion, live review of every operator website, or live verification of all deployed routes. No operator has been upgraded to `verified`.

## Findings

### P0 — Resolve legal/editorial launch gates before publishing promotional claims

1. **Casino content needs an explicit legal disposition.** The repository's own `WORKFLOW.md` flags casino content as a major legal exposure and says legal-labelled items require qualified South African legal review. The content set includes `/casino/`, `/casino/slots/`, and `/casino/live-casino/`. Do not treat the existence of these pages or a passing build as permission to publish or promote them. Obtain qualified legal advice on the exact products, wording, audience and affiliate activity; restrict or remove content if advised.
2. **Privacy and terms are not cleared.** `/legal/privacy/` and `/legal/terms/` are marked `legal-review-required`. Review the actual deployed behaviour—hosting, logs, analytics, cookies, search, forms, third-party requests and any data collection—before writing final policies. The policy must describe what the site actually does.
3. **Affiliate disclosure is not cleared.** `/affiliate-disclosure/` is marked `legal-review-required`. Before commercial links go live, have the disclosure and placement reviewed, and ensure it accurately explains paid links, commission relationships and editorial independence where applicable.

### P1 — Build a source-backed evidence record for each factual page

4. **74 records have no attached source entries.** Add direct, authoritative source URLs to factual claims, especially current operator details, product availability, payment methods, withdrawal limits/timing, promotions and rules. Prefer the operator's current terms for operator-specific claims and relevant regulator sources for licensing/legal claims. Do not rely solely on an operator's marketing page to establish licensing.
5. **No page has a verification date.** After a human actually checks the sources, record a real `lastVerified` date and source-level `checkedAt` dates. Never backdate or set these fields simply to satisfy the build.
6. **19 operator review records remain `needs-verification`.** These are:
   - `/bookmakers/betway/`
   - `/bookmakers/hollywoodbets/`
   - `/bookmakers/easybet/`
   - `/bookmakers/lulabet/`
   - `/bookmakers/jackpot-city/`
   - `/bookmakers/supabets/`
   - `/bookmakers/betfred/`
   - `/bookmakers/sunbet/`
   - `/bookmakers/10bet/`
   - `/bookmakers/gbets/`
   - `/bookmakers/lucky-fish/`
   - `/bookmakers/betshezi/`
   - `/bookmakers/world-sports-betting/`
   - `/bookmakers/sportingbet/`
   - `/bookmakers/yesplay/`
   - `/bookmakers/bet-co-za/`
   - `/bookmakers/playabets/`
   - `/bookmakers/interbet/`
   - `/bookmakers/fafabet/`

   Verify the operator identity, official domain, relevant provincial licensing evidence, terms, payment and withdrawal statements, product availability, and any offer details before changing an operator record's status.

### P1 — Confirm actual affiliate readiness

7. **No structured affiliate/offer URL fields are present in the 77 content records.** A scan of the records found only the three NGB source URLs, and no `affiliateUrl`, `outboundLinks`, `offerUrl` or `trackingUrl` fields. This is evidence that affiliate links are not represented in the content data model as inspected; it does not prove that no links exist elsewhere in the repository or in a third-party system.
8. Before adding affiliate links, define and document how links are approved, tagged, disclosed, tested and retired. Confirm the affiliate programme's actual terms, permitted traffic sources, geographic restrictions, tracking behaviour and required disclosure. Never fabricate tracking URLs, offer amounts, promo codes or partner relationships.

### P2 — Keep technical and content QA distinct

9. **Existing automated checks are useful but limited.** `scripts/validate.py` checks built HTML metadata, one H1 and local links/assets. `scripts/check-banned-claims.sh` scans for selected high-risk promotional claims. Neither check independently verifies factual accuracy, licensing, live offer terms, affiliate tracking, legal compliance or the accessibility of the deployed site.
10. **Build guard is narrower than the full content policy.** `scripts/build.py` rejects a record marked `verified` when its verification date or sources are missing. It does not require every `editorial-review` or `needs-verification` record to have sources, so the current build can pass while 74 records remain unsourced.
11. **Deployment gate is appropriately separated from PR validation.** In `.github/workflows/pages.yml`, the deploy job is gated to non-PR events on `main`; PR runs build and validate but do not deploy. Preserve this guard.

## Evidence and known limits

- The most recent recorded validation for this project reported 78 content pages built, 79 HTML documents / 78 direct index routes validated, the banned-claims check passing, and a Pages artifact uploaded. That was a PR validation run; production deployment was skipped. Re-run or inspect the latest main-branch run before treating that result as current.
- Repository URLs:
  - [Content records](https://github.com/Ituthema/betting-guide-sa/blob/main/content/pages.json)
  - [Build script](https://github.com/Ituthema/betting-guide-sa/blob/main/scripts/build.py)
  - [HTML validator](https://github.com/Ituthema/betting-guide-sa/blob/main/scripts/validate.py)
  - [Promotional-claims checker](https://github.com/Ituthema/betting-guide-sa/blob/main/scripts/check-banned-claims.sh)
  - [Pages workflow](https://github.com/Ituthema/betting-guide-sa/blob/main/.github/workflows/pages.yml)
  - [Research workflow / legal-review notes](https://github.com/Ituthema/betting-guide-sa/blob/main/WORKFLOW.md)
- This report does not claim that an operator is licensed or unlicensed, that any offer is currently available, or that the website complies with South African law. Those require fresh evidence and, for legal conclusions, qualified counsel.

## Prioritized next tasks

| Priority | Task | Completion evidence |
|---|---|---|
| 1 | **TASK-11: Legal/content scope decision for casino pages and affiliate model** | Written decision from qualified South African counsel; affected routes and promotion rules explicitly listed. |
| 2 | **TASK-12: Finalize affiliate disclosure, privacy and terms review** | Approved text reflects real data flows and affiliate relationships; legal reviewer/date recorded. |
| 3 | **TASK-13: Operator verification batch 1** | A small batch (recommend 3–5 operators) has official source URLs, licensing evidence, checked dates, and human review; no unsupported claims. |
| 4 | **TASK-14: Add content evidence completeness reporting** | A report/check lists every page missing sources/date; it warns rather than falsely auto-verifying content. |
| 5 | **TASK-15: Affiliate link inventory and redirect/tracking QA** | Approved-link register, disclosure placement, test results, and documented link retirement procedure. |
| 6 | **TASK-16: Deployed release QA** | Live route checks, mobile/accessibility review, policy links, error/404 behaviour, security headers and latest main workflow evidence. |

## Acceptance decision

Do not mark this audit as a launch approval. Keep current content statuses unchanged until the evidence exists. Start with TASK-11 and TASK-12 before introducing or promoting casino-related content or affiliate offers. Work in isolated branches and pull requests; do not commit audit-driven bulk content changes directly to `main`.
