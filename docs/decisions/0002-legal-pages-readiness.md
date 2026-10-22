# TASK-12 — Privacy, Terms and Affiliate Disclosure Readiness

**Status:** DRAFT FOR FACT-CHECKING AND QUALIFIED SOUTH AFRICAN LEGAL REVIEW  
**Prepared:** 2026-10-22  
**Repository:** `Ituthema/betting-guide-sa`  
**Scope:** Readiness review for `/legal/privacy/`, `/legal/terms/`, and `/affiliate-disclosure/`  
**Important:** This is an implementation and review brief, not legal advice, a POPIA compliance certification, or approval to publish final legal policies.

## 1. Executive decision

Do not mark any of the three legal pages `verified` or represent them as final. Their current content is explicitly framework/draft language, their `lastVerified` fields are null, and no source entries are recorded. The actual business identity, contact route, deployed domain, data flows, third-party services and affiliate agreement terms have not yet been evidenced in this task.

Keep the existing `legal-review-required` statuses unchanged. This task adds a documented checklist and a fact-gathering record; it does not assert that the site is compliant or that a specific cookie, analytics tool, form, tracking pixel, or affiliate programme is in use.

TASK-11's interim content-scope hold is a separate dependency. The privacy/terms/disclosure work must not be read as permission to publish casino promotion or affiliate links. The TASK-11 decision remains pending qualified South African gambling/advertising counsel.

## 2. Existing pages and observed gaps

The following is based on the current `content/pages.json` entries, not on a live-site crawl or a runtime inspection.

| Route | Current status | Observed issue / required action |
|---|---|---|
| `/legal/privacy/` | `legal-review-required` | Correctly says the final notice must reflect actual collection, purposes, lawful basis where applicable, retention, recipients, security, rights and contact route. Those implementation facts are not yet documented in the repository. |
| `/legal/terms/` | `legal-review-required` | Generic framework only. Owner identity, governing-law/jurisdiction wording, contact details, intellectual-property position, affiliate arrangements, actual site functionality and liability wording need owner decisions and legal review. |
| `/affiliate-disclosure/` | `legal-review-required` | Describes possible commissions conditionally, but the actual programmes, qualifying actions, link labels, compensation terms and placement on pages are not evidenced. |
| `/about/` | `editorial-review` | Mentions possible affiliate links and editorial standards. Align it with the final disclosure, but do not upgrade its status based only on this brief. |

Common issue: the three legal pages currently repeat generic “scope and implementation checks”, “corrections, contact and review”, and “commercial relationships and user protection” sections. These should eventually be replaced with page-specific, fact-checked wording rather than copied boilerplate.

## 3. Fact-finding record — answer before counsel review

Do not guess these values. Record the owner's confirmed answer and evidence in a restricted project record; only non-confidential conclusions should be committed to this public repository.

### A. Publisher identity and contact

- [ ] Legal name of the person/entity operating the website.
- [ ] Business/trading name, if different.
- [ ] Country and business/contact address where legally appropriate to disclose.
- [ ] A working privacy/contact email or contact form, with an owner responsible for monitoring it.
- [ ] Who is the POPIA responsible party and who acts as Information Officer, if applicable; confirm any registration/appointment duties with counsel.
- [ ] Hosting/deployment domain(s), including canonical domain, redirects, and any preview domains that collect visitor data.
- [ ] Who receives and responds to access, correction, objection, deletion, complaint and privacy requests, and the process for identity verification.

**Release gate:** never publish invented contact details, an unmonitored mailbox, an unconfirmed legal entity, or a claim that an officer is registered/appointed unless verified.

### B. Actual personal-information and technology inventory

Inspect the built site and repository configuration and confirm the production deployment. For each item, record **present / absent / unknown**, the purpose, data collected, provider, retention, sharing, transfer locations, and evidence.

- [ ] Web-server/hosting logs and security telemetry (including IP addresses, user agents, request logs and retention).
- [ ] Analytics or measurement tools.
- [ ] Advertising tags, pixels, remarketing, conversion tracking or ad networks.
- [ ] Affiliate redirect links, click identifiers, cookies, pixels, postbacks, and operator-side tracking.
- [ ] Cookies, local storage, session storage, service workers and other browser identifiers.
- [ ] Forms, newsletter signup, contact messages, account/login features, comments, surveys or user-submitted content.
- [ ] Embedded video, maps, social widgets, external fonts, or other third-party requests.
- [ ] Email, customer support, CRM, consent-management and anti-spam services.
- [ ] Backups, logs, exports and any local spreadsheets containing visitor or partner information.
- [ ] Whether any personal information is transferred outside South Africa or made accessible to overseas service providers.
- [ ] Security controls, access restrictions, breach-response process and deletion/retention schedules.

A static site can still generate server logs or load third-party resources. Do not assume “no accounts” means “no personal information”; equally, do not claim analytics, advertising cookies, forms or tracking are active without evidence.

### C. Affiliate/commercial relationships

- [ ] Names of actual affiliate networks and operator partners, if any.
- [ ] Agreements/terms governing commission triggers, attribution windows, tracking, reversals, payment, use of logos and required disclosures.
- [ ] Whether compensation depends on clicks, registrations, first deposits, betting activity, revenue share or another event.
- [ ] Whether any operator or network can pay for ranking, placement, review language, sponsored pages or editorial changes.
- [ ] Every page/template location with a commercial link, CTA, badge, comparison table or sponsored placement.
- [ ] Whether the site uses direct operator links, network redirects, URL parameters, shortened URLs or other tracking.
- [ ] Whether any “independent”, “best”, “top”, “recommended”, “licensed”, “verified” or “no extra cost” claim can be evidenced and is approved.
- [ ] Required age, responsible-gambling and promotion warnings and their placement, as determined by counsel.

Do not say the site “may earn commission” as though that is a current fact if there are no active affiliate links or agreements. Before commercial links go live, make the disclosure accurate to the actual arrangement and visible before or at the point where a reader may act.

## 4. Page-specific drafting requirements for counsel

These are required topics, not ready-to-publish legal copy.

### 4.1 Privacy Policy — `/legal/privacy/`

Prepare a plain-language notice based on the completed inventory above. Ask counsel to determine the required notices and wording under POPIA and any other applicable law. At minimum, review:

1. Publisher/responsible-party identity and a working privacy contact.
2. Each category of personal information actually processed, including information generated by site infrastructure or affiliate tracking.
3. Purposes for each processing activity and the applicable lawful justification; do not use a generic “consent” statement for every purpose without checking.
4. Whether information is collected directly or indirectly, and any required notice when information is obtained from another source.
5. Actual recipients/operators, affiliate networks, advertisers, hosting providers and other service providers.
6. Retention periods or objective criteria, including logs, support messages and tracking identifiers.
7. Security safeguards described at a level the operator can substantiate; do not promise absolute security.
8. Data-subject rights and a practical request process, including how to complain to the Information Regulator where appropriate.
9. Cross-border transfers and safeguards, if applicable.
10. Cookies and similar technologies: list actual technologies and purposes; link to a separate cookie notice/policy if needed.
11. Direct marketing and optional analytics/advertising choices, including what consent or objection controls are actually implemented.
12. Effective date, version/review date and a process to update the notice when processing changes.

**Implementation check:** test the deployed site in a clean browser session, inspect network requests and storage, and compare findings against the written inventory. A policy must not claim a consent banner or opt-out mechanism exists unless it works.

### 4.2 Terms of Use — `/legal/terms/`

Counsel and the owner should decide whether separate terms are appropriate for this informational affiliate site and confirm:

1. Correct publisher identity and contact route.
2. Permitted use, intellectual property, third-party marks and user-submitted material (if any).
3. Nature and limits of editorial information, update frequency and how corrections are handled.
4. Clear separation between general information and personalised advice, predictions, or guarantees; avoid using a disclaimer to excuse misleading claims.
5. External links and third-party operator terms, while not implying the publisher controls those services.
6. Affiliate and sponsored content relationship, with a cross-link to the disclosure.
7. Responsible-gambling, age and jurisdictional limitations consistent with the approved content scope.
8. Complaints, notices, amendments, effective date and contact process.
9. Governing law, dispute resolution and liability wording that counsel considers enforceable and fair under applicable South African law.
10. Accessibility and practical implications of any restriction or disclaimer.

Do not add an overbroad waiver, claim that visitors surrender statutory rights, or imply that external operators are endorsed or legally authorised merely because they are mentioned.

### 4.3 Affiliate Disclosure — `/affiliate-disclosure/`

The final disclosure should match actual commercial arrangements and be consistent across the site. Ask counsel to review:

1. Whether affiliate relationships currently exist and which categories of links are commercial.
2. What action may generate compensation, stated accurately without overstating certainty.
3. Whether compensation can affect ranking, placement, content, offers or review conclusions; explain the real editorial controls.
4. Where readers see a short disclosure before clicking, including in tables, comparison cards, review pages, promotional pages and mobile layouts.
5. How sponsored placements and paid advertising are labelled separately from ordinary editorial content.
6. How operator-specific claims, ratings and comparisons are sourced, verified, dated and corrected.
7. Whether required gambling warnings and age safeguards must accompany particular links or promotions.
8. How the disclosure is kept current when partner relationships begin, end or change.

**Suggested short-label pattern for design testing only (not legal approval):**

> **Affiliate link:** We may receive a commission if you use this link and the qualifying conditions are met. This commercial relationship does not prove an operator is licensed, safe, or suitable for you. Check the operator's current terms and applicable licensing information.

Use this only if it truthfully describes the actual arrangement. Counsel should approve the wording and required placement before launch. If the link is paid/sponsored but not affiliate-tracked, label it accurately rather than using this template.

## 5. Publication and UI checklist

- [ ] Privacy, Terms and Affiliate Disclosure pages are linked in a persistent footer or other readily discoverable site navigation.
- [ ] A short affiliate disclosure appears near relevant commercial links, not only on a separate policy page.
- [ ] On mobile, disclosures remain visible and understandable without needing to open a hidden menu or scroll past the CTA.
- [ ] Tables, cards, logos, buttons and comparison labels do not conceal that a link is commercial.
- [ ] Disclosure text is readable, high-contrast, and not visually subordinate to the promotional claim.
- [ ] Every commercial link has a recorded destination, partner/programme, intended product category, and evidence of the relationship.
- [ ] No link is presented as a recommendation or verification merely because it is monetised.
- [ ] Contact details and privacy-request instructions are tested end-to-end.
- [ ] Any cookie/consent controls are tested for their actual behaviour; the policy matches the implementation.
- [ ] Build output and rendered pages are checked, not just the JSON source.
- [ ] The relevant gambling/advertising counsel has separately approved the site's commercial content scope under TASK-11.

## 6. Suggested evidence record

For each decision, maintain a record with these fields:

| Field | What to capture |
|---|---|
| Item | Specific claim, data flow, link placement or policy clause |
| Observed fact | What the implementation actually does |
| Evidence | File path, deployed URL, settings export, agreement or test result |
| Owner confirmation | Person responsible and confirmation date |
| Legal question | Any unresolved interpretation |
| Counsel response | Written answer or reference to restricted advice |
| Action | Keep, rewrite, implement, remove or defer |
| Reviewer/date | Human reviewer and actual review date |
| Recheck trigger | Change to code, vendor, partner, data use or law |

Do not commit confidential contracts, personal data, credentials, or privileged legal advice to this repository. Record only a non-confidential summary and a secure reference to restricted evidence.

## 7. External legal and regulatory references for review

These sources are starting points, not a substitute for counsel's current-law check:

- South African Department of Forestry, Fisheries and the Environment, PAIA & POPIA overview: https://www.dffe.gov.za/legislation/paia_popia
- National Treasury POPIA overview: https://www.treasury.gov.za/POPIA/default.aspx
- Advertising Regulatory Board, current Codes of Advertising Practice (the ARB notes that its code is dynamic): https://www.arb.org.za/The_Codes/
- Consumer Protection Act, 2008, section 41 (false, misleading or deceptive representations): https://www.gov.za/documents/consumer-protection-act

Counsel should verify current legislation, regulations, regulator guidance and the ARB code/appendices in force at the time of approval. This document does not determine which provisions apply to a specific processing activity or advertising arrangement.

## 8. Exit criteria — TASK-12 remains open until met

- [ ] Owner has confirmed the legal publisher identity and working contact route.
- [ ] Actual production deployment/domain and data-processing inventory are evidenced.
- [ ] Actual cookies, logs, analytics, ad-tech, affiliate tracking, forms, embeds and third-party services have been tested and recorded as present/absent/unknown.
- [ ] Active affiliate relationships and all commercial-link placements are inventoried.
- [ ] Privacy notice, terms and affiliate disclosure have been revised to match observed facts.
- [ ] Qualified South African counsel has reviewed the drafts and supplied written conclusions; the gambling/advertising review dependencies from TASK-11 are addressed where relevant.
- [ ] All required technical controls and visible disclosures have been implemented and tested.
- [ ] Page statuses are updated only after a human reviewer records evidence, source(s), reviewer and actual verification date.
- [ ] A non-confidential approval summary and recheck triggers are recorded.

Until these gates are met, the three pages remain draft frameworks and must not be described as final, verified, or legally compliant.
