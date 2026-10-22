# TASK-11 — Content-scope decision and legal-review brief

**Status: OWNER-ADOPTED PRECAUTIONARY INTERIM SCOPE — continue low-risk development and evidence gathering; hold only specific high-risk promotions that cannot currently be verified.**  
**Prepared:** 2026-10-22  
**Repository snapshot:** `content/pages.json` blob `72aff34e4cd70401bd2c3970250c96a5afa403e4`  
**Owner decision recorded here:** operational precaution only; **not a legal opinion, counsel approval, or compliance certification**.

## 1.1 Owner-reported bookmaker checks and affiliate onboarding status

**Owner-reported update (2026-10-22):** the project owner states that every bookmaker currently listed on the site has already been checked for legal registration/licensing to operate in South Africa. The owner also states that no bookmaker affiliate programme applications have yet been submitted because the programmes require a working website before approving prospective affiliates.

**Evidence status:** this is a record of the owner's report, not an independent re-audit performed by this documentation change. Before publishing a specific licence claim or marking a bookmaker record `verified`, retain the source URL or official register extract, review date, exact legal entity, relevant provincial authority and the scope the evidence supports. Do not infer that the operator's every product or promotion is covered by the same evidence.

**Implementation consequence:** build and complete the working website before affiliate applications. Until a programme accepts the publisher and its terms are reviewed, do not claim that the site is an approved affiliate partner, invent tracking links, or state that commissions are already earned. Prepare the affiliate disclosure so it can accurately describe the actual relationship when one exists, and recheck each programme's terms before using its links or promotional assets.

## 1. Decision

Adopt **Option A as the current risk-control posture**, not as a finding that a paid legal opinion is a prerequisite for all project progress. Continue building navigation, page templates, source/evidence tooling, neutral educational material, privacy fact-finding, accessibility, testing and other work that does not depend on unresolved promotional claims. Sports and horse-racing information, odds education and responsible-gambling education may continue through human editorial review and evidence checks.

For now, **do not publish casino/slots/live-casino affiliate CTAs, bonus promotions or participation-oriented calls to action unless the exact product, operator, advertising treatment and applicable legal scope can be verified from authoritative sources and the project owner has recorded the decision**. Where public sources do not resolve a material question, keep that specific promotion unpublished and continue unrelated work. This is a precaution, not a conclusion that every neutral mention or educational discussion of casino games is unlawful. Professional advice is an optional escalation route for unresolved or high-impact questions, not a blanket prerequisite for developing the site.

Do not add affiliate URLs, promo codes, current bonus claims or “play now” links to held casino pages. Do not use this document to mark any operator as licensed or verified. A checklist or source citation alone does not guarantee compliance.

## 2. Why the hold is necessary

Official and current source material creates a material distinction between online betting and online casino-style gambling:

- The National Gambling Board says online gambling is prohibited except online betting through bookmakers licensed in South Africa, including sports and horse-racing betting. Its enforcement page states that distinction: https://www.ngb.org.za/industry-regulation/enforcement/
- The NGB's FAQ says operators are licensed by provincial licensing authorities and that a legally licensed online operator should display licensing information on its digital platform: https://www.ngb.org.za/faqs/
- The NGB's Verified Operators portal says its data comes from provincial licensing authorities and was last updated 4 September 2026 when checked for this brief: https://www.ngb.org.za/verified-operators/
- Section 15 of the National Gambling Act addresses false/misleading advertising, advertising unlawful gambling, targeting minors, warning statements and inducements. Official Act page: https://www.gov.za/documents/national-gambling-act-0
- The National Gambling Regulations' advertising provisions include restrictions on implying guaranteed success, presenting gambling as a way out of financial difficulties, and placing ads in media primarily directed at under-18s. Check the current regulations and applicable provincial rules with counsel.
- The Advertising Regulatory Board maintains a Gambling Appendix and says its code is dynamic; verify the version currently in force before release: https://www.arb.org.za/The_Codes/

**Practical rule for uncertainty:** first check the current National Gambling Act and Regulations, National Gambling Board guidance and verified-operator information, the relevant provincial licensing authority, and the current Advertising Regulatory Board code/appendix. Save the exact source URL, access/review date, product and legal-entity match, and the conclusion supported by that evidence. Do not infer that a bookmaker's licence automatically authorises every product on its website or that an operator appearing on the NGB portal is licensed for every advertised product. If authoritative sources do not resolve the specific question, do not publish that claim or promotion yet; continue work on unrelated site features. A qualified adviser can be consulted if affordable or if the unresolved risk justifies escalation, but this document does not make paid advice a universal project gate.

## 3. Page-scope inventory

The list below covers all **77** records in the audited content snapshot. These are provisional editorial actions, not legal findings. Existing `status` fields remain unchanged.

### Home and general directory
- `/` — **KEEP, subject to editorial/legal review — clearly identify site as independent affiliate publisher if applicable; no unsupported claims or live promotional CTAs.**
- `/bookmakers/` — **KEEP AS EDITORIAL DRAFT — do not advertise specific offers, bonuses or commercial claims until independently verified and legally reviewed.**
- `/about/` — **KEEP, subject to editorial/legal review — clearly identify site as independent affiliate publisher if applicable; no unsupported claims or live promotional CTAs.**

### Promotions
- `/promotions/` — **KEEP AS EDITORIAL DRAFT — do not advertise specific offers, bonuses or commercial claims until independently verified and legally reviewed.**
- `/promotions/welcome-offers/` — **KEEP AS EDITORIAL DRAFT — do not advertise specific offers, bonuses or commercial claims until independently verified and legally reviewed.**
- `/promotions/terms-checklist/` — **KEEP AS EDITORIAL DRAFT — do not advertise specific offers, bonuses or commercial claims until independently verified and legally reviewed.**

### Casino and slots — hold pending legal review
- `/casino/` — **HOLD / REWRITE — do not promote online casino/slots participation or link to casino gameplay pending written legal advice; consider a neutral legality explainer.**
- `/casino/slots/` — **HOLD / REWRITE — do not promote online casino/slots participation or link to casino gameplay pending written legal advice; consider a neutral legality explainer.**
- `/casino/live-casino/` — **HOLD / REWRITE — do not promote online casino/slots participation or link to casino gameplay pending written legal advice; consider a neutral legality explainer.**

### Operator reviews — informational templates only until each operator is verified
- `/bookmakers/betway/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/hollywoodbets/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/easybet/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/lulabet/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/jackpot-city/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/supabets/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/betfred/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/sunbet/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/10bet/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/gbets/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/lucky-fish/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/betshezi/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/world-sports-betting/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/sportingbet/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/yesplay/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/bet-co-za/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/playabets/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/interbet/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**
- `/bookmakers/fafabet/` — **KEEP AS UNPUBLISHED/UNPROMOTED REVIEW TEMPLATE — no operator-specific endorsement or affiliate CTA until official identity, product scope, licence evidence and terms are checked.**

### Sports and educational guides
- `/sports/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/sports/soccer/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/sports/rugby/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/sports/cricket/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/sports/tennis/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/sports/horse-racing/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/sports/esports/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/beginners/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/odds/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/bankroll/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/responsible-gambling/` — **KEEP AS INFORMATIONAL DRAFT — refresh against official sources and record review date before marking verified.**
- `/guides/soccer/1x2-market/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/double-chance/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/over-under-goals/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/both-teams-to-score/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/half-time-full-time/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/first-half-markets/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/handicap-markets/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/corners-markets/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/cards-markets/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/outright-markets/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/psl-fixtures-guide/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/premier-league-markets/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/afcon-guide/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/football-odds-formats/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/accumulator-bets-explained/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/soccer/cash-out-explained/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/payments/bank-transfer-deposits/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/payments/instant-eft/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/payments/bank-card-payments/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/payments/ewallet-payments/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/payments/withdrawal-times/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/payments/account-verification/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/payments/failed-deposit/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/payments/withdrawal-checklist/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/bookmakers/compare-bookmakers/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/bookmakers/licensing-checklist/` — **KEEP AS INFORMATIONAL DRAFT — refresh against official sources and record review date before marking verified.**
- `/bookmakers/mobile-apps/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/bookmakers/customer-support/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/bookmakers/bonus-terms-comparison/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/bookmakers/payout-limits/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/risk/expected-value-basics/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/risk/betting-records/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/risk/setting-limits/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/risk/chasing-losses/` — **KEEP AS INFORMATIONAL DRAFT — review factual claims and sources before publication; no operator promotion unless separately approved.**
- `/guides/risk/self-exclusion/` — **KEEP AS INFORMATIONAL DRAFT — refresh against official sources and record review date before marking verified.**

### Legal and affiliate policy pages
- `/legal/privacy/` — **HOLD FOR LEGAL REVIEW — draft only; confirm actual business/data practices before publishing as final policy.**
- `/legal/terms/` — **HOLD FOR LEGAL REVIEW — draft only; confirm actual business/data practices before publishing as final policy.**
- `/affiliate-disclosure/` — **HOLD FOR LEGAL REVIEW — draft only; confirm actual business/data practices before publishing as final policy.**

## 4. Low-cost verification workflow before releasing held content

Use this sequence for each proposed page, operator claim, promotion or commercial link. It is designed to let the startup progress without treating a paid legal consultation as a prerequisite for every task. It is an internal control, not a legal safe harbour.

1. **Define the exact item.** Record the URL/page, exact product category, legal operator entity, province/jurisdiction, intended audience, commercial relationship and whether the item is neutral education, a comparison, an ad, an affiliate link or a call to action.
2. **Check official sources first.** Review the current National Gambling Act and Regulations, National Gambling Board guidance/verified-operator data, the relevant provincial licensing authority, and the current Advertising Regulatory Board code and gambling appendix. Check the actual product and legal entity, not only the brand name.
3. **Check the claim itself.** Save official terms or product information for any offer, price, odds, payment, availability or operator feature. Record exact URL, date checked, evidence excerpt/screenshot where permitted, expiry/recheck date, and reviewer.
4. **Run the advertising-risk check.** Do not use misleading or unsupported claims, target minors, imply guaranteed success, present gambling as income or relief from financial difficulty, encourage chasing losses, or omit applicable responsible-gambling warnings. Check the format-specific and current rules before publication.
5. **Make and record a proportionate decision.** Mark the item as verified for the specific claim/date, editorial review, needs verification, or hold. A verified status must not be used to certify the whole operator or prove every product lawful.
6. **Escalate only the unresolved issue.** If official material is conflicting, incomplete or does not establish the legality of a high-impact product/promotion, keep that item unpublished and document the exact question. Seek regulator clarification or qualified advice when available and proportionate. Do not stop unrelated development.
7. **Recheck when facts change.** Revisit the evidence when the operator, offer, product, affiliate arrangement, law, regulator guidance or ARB code changes, and before volatile offers go live.

### Specific questions for an optional adviser or regulator clarification

- Whether a particular product/category can be discussed, compared, advertised or linked to under the evidence available.
- Whether a specific operator's provincial licence covers the exact entity and product.
- Which warnings, disclosures, age safeguards and placement rules apply to the exact format.
- Whether the affiliate arrangement or paid traffic method changes the assessment.

Keep confidential advice and contracts outside this public repository. Record only a non-confidential summary, date, scope and resulting project decision.

## 5. Editorial controls during the hold

- No new casino affiliate links, casino bonus/promo-code promotions, “claim offer” CTAs or operator-specific casino recommendations.
- Do not describe any operator or product as “legal”, “licensed”, “approved” or “safe” without current evidence for the exact legal entity, product and relevant licensing scope.
- Check operator claims against the NGB Verified Operators portal and the relevant provincial licensing authority; record the source URL and actual review date.
- Do not publish unverified bonus amounts, odds, payout speeds, withdrawal limits, game counts or comparative superlatives.
- Keep educational explanations distinct from encouragement to participate; never imply gambling is income, investment, a solution to financial trouble, or a guaranteed way to win.
- Maintain responsible-gambling information and adult-only audience safeguards as counsel advises.
- Keep every content status unchanged until a human editor has checked sources and recorded a genuine verification date.

## 6. Exit criteria for TASK-11

TASK-11 can move from initial triage into ongoing controlled implementation when the project owner has completed the following evidence-based steps; **a paid legal opinion is not a prerequisite for unrelated site development or for recording verified facts**:

- [ ] Each proposed commercial item has a recorded category, operator legal entity, product scope, intended format and audience.
- [ ] Official national and relevant provincial sources have been checked, with URL and actual review date recorded.
- [ ] The current ARB code/appendix and relevant advertising rules have been checked for the intended format.
- [ ] Each factual claim has direct supporting evidence, reviewer/date and a recheck trigger; unsupported claims remain unpublished.
- [ ] Applicable warning, age-safeguard and affiliate-disclosure requirements have been identified and implemented before the relevant promotion is released.
- [ ] Unresolved high-risk items are specifically held, with the question and missing evidence recorded; other development continues.
- [ ] The owner records keep/rewrite/retire decisions for the affected pages and any redirects.
- [ ] No page or operator is upgraded to verified without evidence for the exact claim; this is not a blanket legal-compliance certification.
- [ ] If regulator guidance or qualified advice is later obtained, update the decision with the date, scope, assumptions and actions without publishing confidential material.

This document records a **precautionary operating decision, not legal clearance**. TASK-12 (privacy, terms and affiliate disclosure) can proceed in parallel through factual inventory, implementation checks and page-specific drafting. Do not represent any legal page as final or any high-risk promotion as approved merely because this checklist is complete.