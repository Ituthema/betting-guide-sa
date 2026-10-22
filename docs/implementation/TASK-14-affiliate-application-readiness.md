# TASK-14 — Affiliate Application Readiness Plan

**Status:** IMPLEMENTATION CHECKLIST — NOT A LAUNCH OR COMPLIANCE CERTIFICATION  
**Prepared:** 2026-10-22  
**Repository:** `Ituthema/betting-guide-sa`  
**Purpose:** Turn the current static-site baseline into a credible, testable website to submit to bookmaker affiliate programmes once the owner is ready.

## 1. Scope and operating assumptions

- The owner reports that every bookmaker currently listed has been checked for South African registration/licensing. This document records that report; it does not independently re-audit those checks.
- The owner has not yet applied to affiliate programmes because prospective partners require a working website for review.
- This phase therefore prioritises a functioning, transparent editorial website and evidence-backed bookmaker pages. It does not invent affiliate links, partner approvals, commission arrangements, live bonuses, ratings, contact details or licence evidence.
- Do not treat the checklist as legal advice, regulator approval, affiliate approval or proof that a specific product or advertisement is permitted.
- Development of ordinary editorial, accessibility, navigation and quality-control features can continue. Keep any individual high-risk promotional placement on hold where its product, operator scope, terms or advertising treatment cannot yet be substantiated.

## 2. Baseline observed in repository on 2026-10-22

Source inspected: `content/pages.json`, `scripts/build.py`, `scripts/validate.py`, `README.md` on the repository default branch.

| Check | Observed baseline | Consequence |
|---|---|---|
| Content records | 77 | There is a substantial starter catalogue to review. |
| Editorial review | 55 records | Content needs editorial QA before being represented as final. |
| Needs verification | 19 records | These are the 19 individual bookmaker records; do not present them as independently verified reviews. |
| Legal review required | 3 records | Privacy, Terms and Affiliate Disclosure remain unfinished frameworks. |
| Records marked verified | 0 | No content record currently passes the site's verified status. |
| Records with at least one source | 3 | Evidence coverage is incomplete; 74 records have no source entry. |
| Records with a verification date | 0 | All `lastVerified` fields are null. |
| Contact workflow | README says no contact backend is selected and no fake-success contact form is included | Decide whether to publish a real monitored contact channel; do not add a form that silently discards messages. |
| Affiliate status | Owner reports no affiliate applications submitted yet | Do not imply partner approval, tracking links or earned commissions. |
| Production behaviour | Not established by this repository-only inspection | Test the actual deployed domain and its hosting configuration before applying. |

This is a source-code/content inventory, not a live-browser audit. Re-run it after significant content or implementation changes.

## 3. Definition of “ready to apply”

A website can be submitted for programme review when the following are true:

- [ ] The production domain is reachable over HTTPS and has no blocking deployment or certificate errors.
- [ ] Home, bookmaker directory, individual bookmaker pages, About, Contact (or a clearly published monitored alternative), Privacy, Terms, Affiliate Disclosure and Responsible Gambling pages work on mobile and desktop.
- [ ] Navigation, search, footer links, direct nested-route loading and 404 handling have been tested on the deployed domain.
- [ ] The site identifies its publisher/editorial purpose and provides a genuine contact route; no identity, address, company registration or contact detail is invented.
- [ ] Each bookmaker page clearly distinguishes known facts, owner-reported information, editorial explanation and fields that still need verification.
- [ ] Any specific licence claim intended for publication has a saved official source, exact legal entity, relevant provincial authority/jurisdiction and review date. Do not infer a licence scope for every product from a brand name alone.
- [ ] Current offers are not presented as live until their official terms and expiry/recheck date have been checked. No fake bonus amounts, invented ratings, unsupported payout-speed claims or fabricated user reviews.
- [ ] Affiliate disclosure copy accurately describes the current state. Before acceptance, it must not imply the site is an approved partner or already receives commission. After acceptance, update it to match the actual agreement and links.
- [ ] The privacy policy is aligned with the real implementation, including hosting, server logs, external fonts, any analytics, advertising, affiliate tracking, contact messages and third-party requests actually used. Do not claim a cookie or data practice that has not been checked.
- [ ] Age messaging and responsible-gambling information are visible and do not make gambling sound risk-free, guaranteed or a source of income.
- [ ] The build and validation scripts pass, and the deployed site has been checked for broken internal links, obvious mobile layout defects and console/runtime errors.
- [ ] A small evidence pack is saved for the application: live domain, representative screenshots, site description, publisher/contact details, editorial/disclosure pages, and a record of the programme's application terms/status.

A programme may have additional requirements. Record each programme's own current requirements instead of assuming one checklist fits all.

## 4. Implementation sequence

### TASK-14A — Live-site and route smoke test
1. Confirm the actual production domain and HTTPS.
2. Open the home page and a sample nested route directly in a fresh browser tab.
3. Test navigation, search queries, footer links, 404 behaviour and mobile widths.
4. Run the local build and validator; retain the exact output.
5. Record each failure with route, device/browser, expected result, actual result and screenshot where useful.

**Acceptance:** A dated smoke-test record exists, failures are fixed or explicitly tracked, and no claim is made that untested routes passed.

### TASK-14B — Publisher identity and contact route
1. Review `/about/` for accurate publisher/editorial purpose.
2. Choose a contact method the owner can actually monitor (for example, a dedicated email address or a real form provider).
3. Publish only the chosen, confirmed contact details.
4. If using a form, verify delivery, error handling, spam protection, data minimisation and what happens to submitted messages before launch.

**Acceptance:** A visitor can reach the publisher using a real, tested channel; no placeholder address or fake-success form remains.

### TASK-14C — Bookmaker evidence register
For each of the 19 individual bookmaker records, maintain these fields in the working review record:

- Brand and exact legal entity named in official terms
- Product scope being discussed (sports betting, casino, or other)
- Relevant provincial regulator/register and official source URL
- Date checked and reviewer
- Official terms URL and last checked date
- Payment/withdrawal facts only when supported by official terms
- Promotion name, full terms, eligibility, expiry/recheck date, or “not currently verified”
- Affiliate programme: not researched / application not submitted / applied / approved / rejected / terms accepted
- Tracking URL status: none / issued / tested
- Material uncertainty, conflicting evidence and next review date

Do not turn the owner's general statement that bookmakers were checked into 19 individual verified records without preserving the actual evidence for each record. Do not test payment claims by depositing money.

**Acceptance:** Every operator page has a traceable review record; unsupported claims are removed, qualified or held. A record is only marked `verified` when it meets the repository's verification rules.

### TASK-14D — Editorial and legal-page fact check
1. Confirm the real site owner/publisher and contact details.
2. Inspect actual deployment and third-party requests, including Google Fonts, hosting logs, analytics, advertising and affiliate tracking if later added.
3. Update Privacy, Terms and Affiliate Disclosure from the facts actually confirmed; preserve `legal-review-required` until the relevant implementation and factual checks are complete.
4. Keep affiliate disclosure truthful before and after programme acceptance.
5. Continue low-risk educational content and quality improvements while keeping only unresolved material-risk promotional elements on hold.

**Acceptance:** The pages describe the actual service and current relationships, not an imagined business model or data flow.

### TASK-14E — Affiliate application log
Create one row per programme and record:
- Programme name and official application URL
- Date requirements checked
- Site/content requirements
- Required audience, traffic or promotional-channel declarations
- Application date and status
- Programme terms and restrictions, once provided
- Approval date, permitted brands/products/territories, and tracking-link issuance
- Disclosure or placement obligations and re-review date

Do not submit misleading traffic figures or claim audiences, company details, approval, or commercial relationships that do not exist.

**Acceptance:** Every application and later relationship has a dated status and evidence. Links are added only after the programme issues them and their destination is tested.

## 5. Suggested order of work

1. **First:** TASK-14A, test the live domain and routes.
2. **Second:** TASK-14B, confirm publisher identity and a genuine contact method.
3. **Third:** TASK-14C, build evidence for the bookmaker pages, starting with the first operators intended for application.
4. **Fourth:** TASK-14D, fact-check the disclosure and privacy/terms frameworks against the real site.
5. **Fifth:** TASK-14E, apply to programmes whose requirements the finished site meets.
6. **After approval:** add only issued affiliate links, test them, update disclosures and retain each programme's rules.

Do not spend time polishing 19 operator pages to the same depth before the owner selects a first application shortlist. A small number of accurate, useful pages is better than a large catalogue of unsupported claims.

## 6. Out of scope for this phase

- No invented operator evidence or licence assertions.
- No affiliate tracking URLs or claim of approval before a programme issues/accepts them.
- No live bonus claims without current official terms.
- No casino/slots/live-casino affiliate CTAs where the specific product, advertising treatment and scope remain unresolved under the project's interim risk controls.
- No deployment, live content status changes or publication of final legal policies as part of this documentation-only task.

## 7. Validation and change boundary

This change adds a planning/evidence document only. It does not change public page content, content statuses, affiliate links, scripts, dependencies, workflow files or deployment settings.

When implementation work begins, run:

```bash
python3 scripts/build.py
python3 scripts/validate.py
bash scripts/check-banned-claims.sh
```

Then test the actual deployed site separately. Passing local checks does not prove production behaviour, content accuracy, affiliate approval or legal compliance.
