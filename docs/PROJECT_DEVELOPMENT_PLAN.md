# Betting Guide SA — Project Development Plan
**Version:** 1.0  
**Last updated:** 22 October 2026  
**Repository:** https://github.com/Ituthema/betting-guide-sa  
**Primary workflow:** Android + Termux; GitHub web/connector workflow is acceptable  
**Deployment target:** GitHub Pages (confirm current configuration before release)  
**Product category:** South African bookmaker information, comparison and affiliate publishing website  
**Reference competitor:** https://bettingguide.co.za/  
**Status:** Planning baseline; current main branch and deployment must be rechecked before execution

---

## 1. Purpose and governing principles

This plan turns the project specification into a staged, testable implementation programme. The objective is to build a useful, mobile-first South African betting information and comparison site that can later support approved affiliate partnerships. The site is an information/marketing publisher, not a bookmaker or betting operator.

### Non-negotiable rules
- Evidence before publication: do not invent licence status, operator features, offers, odds, payouts, ratings, user reviews, affiliate relationships, partner approvals, or legal conclusions.
- Treat user-provided claims as leads to verify, not as independent evidence.
- No unapproved affiliate links, bonus CTAs, casino/slots/live-casino promotions, or claims that a programme has accepted the site.
- Clearly distinguish editorial information from advertising or commercial relationships when those relationships actually exist.
- Do not promise POPIA compliance, advertising approval, or legal compliance merely because a template or banner exists.
- Do not assume cookie banners are universally required or sufficient for a particular advertising integration. Decide based on actual technology, data flows, vendor terms, and applicable requirements.
- Keep the existing Python-generated static-site architecture unless an explicit architecture decision approves a change.
- Do not merge pull requests without explicit user approval.
- Every task must be scoped, validated, and reported with actual results. Never report a check as passed if it was not run.

## 2. Current baseline — snapshot, not a live guarantee

The most recent documented review reported:
- 77 content records in content/pages.json.
- Statuses: 55 editorial-review, 19 needs-verification, 3 legal-review-required, and 0 verified.
- 19 individual bookmaker records.
- 3 records with source entries, 74 without source entries.
- 0 records with a lastVerified date.
- Existing scripts: scripts/build.py, scripts/validate.py, and scripts/check-banned-claims.sh.
- Existing client-side search: assets/search.js.
- Existing site behavior in assets/site.js includes an 18+ reminder and sticky-header behavior.
- No contact backend was selected; avoid forms that imply successful delivery when no backend exists.
- Actual production domain, DNS, live page behavior, monetisation approval, affiliate acceptance, analytics deployment, and latest CI result were not established by that review.

**Recheck these figures and files against main before using them as current facts.** Store a dated baseline report when the next audit is completed.

## 3. Product scope and exclusions

### V1 — in scope
1. Homepage explaining the site's purpose and how information is reviewed.
2. Bookmaker directory and consistent individual bookmaker information pages.
3. Evidence-backed comparison criteria and clearly labelled editorial methodology.
4. Soccer/betting education that explains markets and risks without promising outcomes.
5. Responsible-gambling information with official, verified support references.
6. About, contact (only when a functioning contact route exists), editorial policy, corrections policy, privacy information, and commercial-disclosure pages.
7. Search, category navigation, readable mobile layout, accessible interaction, page-specific metadata, canonical URLs, sitemap and robots rules.
8. Source register, verification timestamps, expiry/review dates and content status workflow.
9. Build and validation checks that prevent publication of known unsupported or prohibited claims.

### Deferred until evidence and approval exist
- Affiliate tracking links and commercial offer CTAs.
- Bonus amounts, wagering terms, free bets, odds boosts, deposit matches, and time-limited offers.
- Casino, slots, live casino, and Spina Zonke promotional pages or CTAs.
- Google Analytics, ad pixels, ad network scripts, newsletter collection, or other third-party tracking.
- AdSense or other advertising integration.
- Any statement implying the site is legally approved, an operator partner, or accepted by an affiliate programme.

These are not permanently ruled out. Each requires a specific, documented readiness check before implementation.

### Out of scope
- Accepting bets, holding customer funds, operating gambling accounts, processing deposits/withdrawals, or presenting the site as a bookmaker.
- Fake reviews, fabricated first-hand testing, fabricated ratings, scraped private data, or misleading endorsements.
- Automated publication of unreviewed high-risk claims.

## 4. Repository architecture and source of truth

Expected current implementation:
- content/pages.json — page content and metadata.
- scripts/build.py — generated static HTML output.
- scripts/validate.py — content/output/link/metadata validation.
- scripts/check-banned-claims.sh — selected claim-pattern checks.
- assets/ — shared styles and browser-side scripts.
- .github/workflows/pages.yml — deployment workflow.

Verify the current tree before relying on this list. Do not introduce a Node/npm/Astro workflow or hash-only routing merely because the original specification mentioned it.

### Content ownership
- JSON source records are the editable source of truth for generated pages.
- Generated HTML is a build artifact unless the repository explicitly documents otherwise.
- Shared layout changes belong in templates/build logic or shared assets, not in repetitive manual edits to generated output.
- Keep content data separate from presentation and validation logic.
- Never overwrite a user change or a newer main-branch commit based on a stale audit.

## 5. Phased roadmap

### Phase 0 — Baseline and release integrity
**Goal:** establish what is actually in main and whether a deployable build can be reproduced.

Tasks:
- P0.1 Capture main commit SHA, complete file inventory, open PRs and latest workflow status.
- P0.2 Run the documented build, validator, and banned-claim checker from the repository root.
- P0.3 Record warnings separately from hard failures; do not silently waive them.
- P0.4 Confirm GitHub Pages source/workflow, custom domain setting, DNS state, HTTPS, and whether deployment preserves required files.
- P0.5 Inspect generated homepage, bookmaker detail pages, legal/editorial pages, sitemap.xml and robots.txt.
- P0.6 Test key routes on mobile viewport and check broken links, 404 behavior, canonical tags, and sitemap URLs.
- P0.7 Save a dated baseline report with commands, exact outputs, URLs tested, screenshots if available, and unresolved defects.

**Acceptance:** build and validation outcomes are reproducible; production domain and deployment state are either verified or explicitly marked unknown; no deployment claims are inferred from repository code alone.

### Phase 1 — Catalogue reconciliation and evidence register
**Goal:** settle which operators and claims belong in V1 and provide traceable evidence for each published factual claim.

Tasks:
- P1.1 Reconcile the project-spec list against the current 19 individual bookmaker records. Earlier materials mention PalaceBet and ScoreBet while the repository includes Interbet; decide each entry explicitly.
- P1.2 Create a bookmaker master register with canonical operator name, official website, product scope, South African relevance, verification status, source URLs, date checked, reviewer, next review date, and publication decision.
- P1.3 Create a source register that distinguishes primary sources (operator terms, regulator/government sources, official support pages) from secondary sources.
- P1.4 Define field-level evidence rules for licence claims, ownership, products, payment methods, promotions, terms, customer support and responsible-gambling tools.
- P1.5 Add a content review lifecycle: draft → needs-verification → editorial-review → legal-review-required (where appropriate) → verified/publishable; rejected or expired records must not silently remain current.
- P1.6 Add lastVerified, reviewDue or equivalent fields only where the schema and validation can support them; define how missing and stale dates behave.
- P1.7 Ensure every material operator claim has a source and a checked date. A source URL alone does not prove the claim was verified.
- P1.8 Record disagreements and unavailable evidence instead of filling gaps with guesses.

**Acceptance:** catalogue differences are resolved by an explicit decision; every operator page has a documented evidence status; unsupported high-risk claims cannot be published as verified.

### Phase 2 — Editorial quality and responsible-gambling content
**Goal:** make the site transparent, accurate, useful and non-deceptive.

Tasks:
- P2.1 Review About, methodology, editorial policy, corrections policy and commercial disclosure pages.
- P2.2 Ensure rankings/comparisons state criteria, limitations, evidence dates and whether the site has a commercial relationship.
- P2.3 Review every responsible-gambling support link, contact detail, service name and availability against an official source.
- P2.4 Explain that betting involves financial risk; avoid “guaranteed win”, “risk-free profit”, “sure bet”, or equivalent claims.
- P2.5 Clearly label educational examples as examples, not predictions or recommendations.
- P2.6 Ensure 18+ messaging is visible and understandable, but do not treat a visual reminder alone as proof of compliance.
- P2.7 Add a corrections route that actually works; do not claim contact submissions are sent unless a real backend or working email destination is configured.
- P2.8 Review language for South African relevance, plain-language clarity and accessibility.

**Acceptance:** pages have a named editorial purpose, evidence where factual claims require it, working contact/correction paths, and no unsupported safety, legal or performance promises.

### Phase 3 — Mobile UX, accessibility and technical SEO
**Goal:** ensure users and search engines can navigate the static site reliably.

Tasks:
- P3.1 Test common Android screen widths, portrait orientation, keyboard navigation and touch targets.
- P3.2 Check contrast, visible focus, heading order, form labels, link purpose, image alternatives and reduced-motion behavior where relevant.
- P3.3 Check unique page titles and descriptions, one meaningful H1, canonical URL correctness and internal links.
- P3.4 Generate sitemap URLs from canonical path routes, not historical hash URLs.
- P3.5 Confirm robots.txt does not accidentally block pages intended for indexing.
- P3.6 Check 404 handling and ensure internal links do not point to stale slugs.
- P3.7 Confirm SITE_URL or equivalent is set only to the verified production origin; remove stale domains and placeholder brands.
- P3.8 Inspect page weight, image dimensions, font loading, JavaScript errors and search behavior.
- P3.9 Avoid adding schema markup that claims ratings, offers, reviews or organisation details not supported by visible page content.

**Acceptance:** generated pages pass automated validation; key pages work on mobile; canonical/sitemap/robots references agree with the verified domain and actual routes.

### Phase 4 — Affiliate programme readiness
**Goal:** prepare honest applications without pretending approval already exists.

Tasks:
- P4.1 Publish sufficient original, evidence-backed content and transparent editorial/contact information.
- P4.2 Prepare a factual publisher profile: audience, geography, content types, traffic only if measured, and current launch status.
- P4.3 Maintain a programme application tracker: operator/programme, official application URL, requirements, date applied, response, approved properties, permitted channels, prohibited claims, link rules and contract review status.
- P4.4 Apply only through official programme channels and answer application questions truthfully.
- P4.5 Record accepted terms and written approval before enabling that programme's links or offers.
- P4.6 Confirm whether each programme permits the site's planned traffic sources, brand bidding, coupon/bonus content, social promotion, email and particular product categories.
- P4.7 Add disclosure language only when accurate for the site's real relationships; never claim commissions or partnerships before they exist.
- P4.8 Add link IDs and click measurement only after approval and a privacy/data-flow review.

**Acceptance:** no affiliate link is live without a documented basis for using it; application and approval status are accurately represented.

### Phase 5 — Privacy, advertising and monetisation gates
**Goal:** add commercial technology only when the actual integration and requirements are known.

For each proposed vendor (analytics, advertising, affiliate tracking, newsletter, embedded media):
1. Identify the vendor and official terms/policies.
2. List data collected, purposes, cookies/local storage, third-party requests, retention and recipients.
3. Decide what notices, choices, consent or opt-out controls are appropriate for that actual setup.
4. Update the privacy information and implement only the controls the integration needs.
5. Confirm vendor eligibility, publisher/site requirements and prohibited-content rules.
6. Test behavior with and without choices where relevant, including that declined optional tracking does not fire if the design promises that.
7. Record the decision and recheck when vendor scripts or terms change.

**Order:** affiliate approvals and terms first for affiliate features; ad-network eligibility and current policy checks before ads; analytics only after the purpose and data handling are documented. Do not treat any specific consent banner as universal legal advice or a guaranteed approval mechanism.

**Acceptance:** no vendor script or monetisation feature is described as active until verified in code and production; notices match actual data flows; programme and network requirements have been checked against current official documents.

### Phase 6 — Automation, monitoring and content operations
**Goal:** make quality checks repeatable without automatically publishing uncertain claims.

Tasks:
- P6.1 Run build and validation in GitHub Actions on pull requests and main updates.
- P6.2 Fail CI on structural errors, duplicate metadata, broken internal links, malformed content, invalid dates and disallowed claims where reliably detectable.
- P6.3 Treat external-link failures carefully: transient network blocks and anti-bot pages should be warnings requiring review, not proof a page is false.
- P6.4 Add a content freshness report for records nearing review due dates or missing required evidence.
- P6.5 Add an expired-offer/page process only if time-sensitive offers are later approved for publication.
- P6.6 Keep human review required for licensing, legal, financial, bonus, payout and other material commercial claims.
- P6.7 Track errors, build failures and content corrections; define a rollback procedure.
- P6.8 Do not add paid services until a cost/benefit case is approved.

**Acceptance:** CI reports deterministic results, content warnings are actionable, and automation cannot silently upgrade unverified records to verified.

### Phase 7 — Controlled launch and ongoing improvement
**Goal:** launch only after the release gate is satisfied.

Pre-launch checklist:
- [ ] Current main SHA and PR status recorded.
- [ ] Build and validator pass, or every remaining warning has a documented owner and decision.
- [ ] Key mobile routes manually checked.
- [ ] Domain, HTTPS, canonical URLs, sitemap and robots rules verified against the actual deployment.
- [ ] Operator facts and support references have evidence and review dates.
- [ ] Legal/editorial/privacy pages accurately describe the actual site.
- [ ] No unapproved affiliate or ad scripts are present.
- [ ] Forms, email links and contact routes work as described.
- [ ] 404, navigation, search and internal links tested.
- [ ] Backup/rollback method understood.
- [ ] Release note records what changed and what remains incomplete.

After launch, measure only with approved, disclosed tools: indexed pages, search queries, organic clicks, content freshness, broken links, corrections, and—once legitimately active—affiliate clicks/conversions or ad performance. Do not invent baseline metrics or forecasts.

## 6. Backlog and task sequencing

Priority labels: **P0** blocks reliable releases; **P1** required before broad publication/affiliate applications; **P2** useful improvement; **P3** optional/conditional.

| ID | Priority | Work item | Dependencies | Definition of done |
|---|---|---|---|---|
| DOC-01 | P0 | Re-run baseline audit of main | None | Dated report with commit, inventory, actual test outputs, CI and deployment status |
| CAT-01 | P1 | Reconcile operator catalogue | DOC-01 | Explicit decisions for PalaceBet, ScoreBet, Interbet and any other discrepancies |
| EVD-01 | P1 | Create evidence register | CAT-01 | Every current operator page mapped to claims, sources, dates and review status |
| DAT-01 | P1 | Define content verification schema and rules | EVD-01 | Missing/stale evidence is detectable; no false verified status |
| EDT-01 | P1 | Review editorial/legal/responsible-gambling pages | EVD-01 | Source-backed pages and working correction/contact route |
| SEO-01 | P1 | Verify domain, canonical, sitemap, robots and 404 | DOC-01 | All agree with confirmed deployment and route structure |
| QA-01 | P1 | Mobile/accessibility/manual QA | DOC-01 | Checklist results and reproducible defect list |
| CI-01 | P1 | Strengthen CI for content and build checks | DOC-01 | Required checks run on PR; failures block merge where appropriate |
| AFF-01 | P1 | Prepare affiliate application pack and tracker | EDT-01, QA-01 | Honest publisher profile and documented application workflow |
| AFF-02 | P0 before activation | Gate affiliate links by programme approval | AFF-01 | No links/offers enabled without programme-specific evidence/terms |
| PRIV-01 | P1 before third-party tracking | Data-flow and privacy review | Specific vendor selected | Inventory, user notice/choices and implementation checks match actual vendor |
| ADS-01 | P2, gated | Evaluate advertising eligibility | Stable site, policy review | Current requirements recorded; no integration before approval/eligibility |
| ANA-01 | P2, gated | Evaluate analytics | Purpose and privacy review | Minimal justified measurement and documented data handling |
| OPS-01 | P2 | Content freshness and correction operations | DAT-01, CI-01 | Review-due report and documented correction/rollback process |
| GROW-01 | P3 | Expand pages and categories | Evidence pipeline stable | New pages pass the same evidence and QA gates |

Do not start all work items in parallel. DOC-01 should be first; CAT-01 and SEO-01 can be separate scoped tasks after the baseline is known. Keep code changes independent from documentation-only changes when possible.

## 7. Content and evidence data model

Adapt names to the actual schema rather than implementing blindly. Minimum logical fields to support:
- stable ID and canonical slug;
- page type/category;
- title, description and body/content;
- editorial status;
- source list with publisher, URL, source type, relevant claim/field, date accessed and optional note;
- last verified date and next review date;
- reviewer or review record;
- publication eligibility and reason for hold;
- commercial relationship status, where relevant;
- optional expiry date for genuinely time-limited material.

Rules:
- Do not mark a record verified because it has a URL; the source must support the specific claim.
- A source that is an affiliate landing page or operator marketing page may prove what the operator advertises, but not independent quality or regulatory status by itself.
- Keep a dated history of material corrections where practical.
- Avoid storing sensitive user information unless a clear need and safe handling process are established.

## 8. Verification and release commands

From the repository root, run the commands that exist in the current branch:
- \`python3 scripts/build.py\`
- \`python3 scripts/validate.py\`
- \`bash scripts/check-banned-claims.sh\`

Do not assume these are sufficient. Inspect the actual output and workflow; add commands only when the relevant tool is installed and the repository supports it. Record exit codes and meaningful output. Run the build before validating generated output if that is the documented workflow.

For each PR report:
1. Base and head branch/commit.
2. Files changed and why.
3. Exact validation commands run and their outputs.
4. CI result from GitHub, if available.
5. Manual checks performed and those not performed.
6. Known risks, warnings and follow-up tasks.
7. Confirmation that no unrelated files or live promotional claims were changed.

## 9. Scoped task template

Use this template for each coding agent or repository task:

**Task ID and title:**  
**Base:** latest main; record the exact SHA first.  
**Goal:** one measurable outcome.  
**Allowed files:** list exact paths.  
**Forbidden scope:** unrelated architecture changes, whole-repository rewrites, unapproved commercial integrations, unsupported claims.  
**Evidence:** files/lines, source URLs, issue/PR or command output supporting the task.  
**Implementation rules:** preserve current Python static-site architecture; inspect only necessary files; do not fabricate data; keep changes minimal.  
**Validation:** run the relevant repository commands and report exact outputs.  
**Acceptance criteria:** testable checklist.  
**Deliverables:** branch, commit/PR link, changed-file list, tests and unresolved issues.  
**Stop condition:** if evidence is missing, schema differs, or the task would require a legal/commercial assumption, stop and report rather than guess.  
**Merge policy:** do not merge without explicit user approval.

## 10. Risk register

| Risk | Impact | Mitigation / trigger |
|---|---|---|
| Unverified operator or licence claims | High | Evidence register; block verification/publishing until supported |
| Unapproved affiliate offer or link | High | Programme-specific approval and terms gate |
| Unsupported legal/compliance statement | High | Use precise factual wording; verify against official sources; obtain qualified advice if/when feasible |
| Expired or misleading promotion | High | Keep promotional claims deferred until approval; if later added, store expiry and run automated freshness checks |
| Incorrect production domain/canonical | High | Verify repository, Pages settings, DNS and live response independently |
| Broken or stale pages | Medium | Internal-link validation, sitemap checks, scheduled review |
| False-positive external-link checker | Medium | Separate hard failures from transient warnings; manual review |
| Third-party tracking without matching notice/choice | High | Data-flow review before integration; verify actual production behavior |
| Overly broad AI-generated changes | Medium | Narrow tasks, allowed-file lists, small PRs and human review |
| Unsupported traffic/revenue forecasts | Medium | Label as hypotheses; replace only with measured data and explicit assumptions |

## 11. Decisions that must be recorded, not guessed

- Final brand name and production domain.
- Final operator list and disposition of catalogue discrepancies.
- Which affiliate programmes, if any, approve the site and what terms apply.
- Whether and when advertising or analytics is introduced.
- Whether any casino/slots/live-casino content is appropriate and permitted for the site's actual publisher/programme setup.
- Actual contact/corrections channel.
- Content review cadence and person responsible.
- Any material architecture change from Python-generated static pages.

Until a decision is recorded with evidence, use the safer default: keep the item deferred and do not publish a claim of completion.

## 12. Change history

- 22 October 2026 — Created as the operational companion to WEBSITE DEVELOPMENT PROJECT DOCUMENTATION.txt Version 1.2. Consolidates current architecture, baseline caveats, evidence standards, phased roadmap, backlog, validation, release gates and scope controls.
