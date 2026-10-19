# Betting Guide SA: Research-Backed Improvement Workflow

Prepared 2026-10-19. Companion to `ROADMAP.md` (task list) and `REVIEW.md` (code review of `Index.html`).
This document explains **why** each change matters (with sources), **how** to do it step by step, and **how to prove it is done**.

Not legal advice. Anything marked **[LEGAL]** should be confirmed with a South African gambling or advertising attorney before you publish.

---

## 0. How to use this document

1. Work the phases in order: **Gate G0, Phase 0, 1, 2, 3, 4, then Phase 5 (ongoing)**.
2. One task = one branch = one pull request. Branch name: `task/T0.2-cookie-decline`. Commit message starts with the task ID.
3. A task is done only when its **Done when** check passes. Paste the command output into the PR description.
4. Tick the box in `ROADMAP.md` in the same PR.

Pull request checklist (copy into `.github/pull_request_template.md`):

```markdown
- [ ] Task ID(s): 
- [ ] "Done when" evidence pasted below
- [ ] `scripts/check-banned-claims.sh` passes
- [ ] No new third-party hosts (fonts, images, scripts)
- [ ] Responsible-gambling message and helpline still present on every page with an offer
- [ ] Any bookmaker fact I touched has a `verified_on` date from today
```

---

## 1. Research summary: what the evidence changes

### 1.1 The biggest finding: casino content is the main legal exposure

| Finding | Source |
|---|---|
| The National Gambling Board (NGB) states that online or interactive gambling is illegal in South Africa, with the single exception of online sports betting through licensed bookmakers. Traditional online casino games are outside that exception. | MyBroadband, "New laws coming for online gambling in South Africa" (30 Jun 2026); Bandwidth Blog (1 Jul 2026) |
| Practitioner guidance says advertising an unlawful gambling activity is itself prohibited, and gives advertising an offshore online casino through South African media as an example. | Chambers, Gaming Law 2025: South Africa |
| No law has passed to legalise online casino. The Remote Gambling Bill (B11-2024) and the 2018 amendment bill have both stalled. In mid-2026 the trade minister said a new Bill is being fast-tracked, together with new gambling-advertising rules. | Polity (15 May 2026); Mail & Guardian (22 Jul 2026); Yogonet (3 Jul 2026) |
| Some licensed bookmakers offer casino-style products by presenting them as bets on game outcomes. The NGB has pushed provincial regulators to act, and the provinces have not followed. The legal position is **contested**, not settled in your favour. | MyBroadband (30 Jun 2026) |

How this lands on `Index.html` (counted from the file): **176** mentions of "casino", **198** of "slot(s)", **53** of "Spina Zonke", **26** of "live casino", and nav pages `casino`, `slots`, `lucky` and `luckyfish`. Lucky Fish is promoted mainly for its "2,000+ casino games". This is a larger risk than any item in the original review.

**[LEGAL]** Decision required before any content work: see Gate G0.

### 1.2 Gambling advertising rules (apply as your content floor)

The NGB's 1 December 2025 directive to the provincial licensing authorities restates the rules:

- Section 15 of the National Gambling Act: no advertising that is misleading, unlawful, or directed at minors. Every gambling ad needs responsible-gambling messaging in the prescribed format. No advertising that presents gambling as "free" or "discounted" in a way that works as an improper inducement.
- Regulation 3 of the National Gambling Regulations: no advertising that implies guaranteed success, portrays excessive play, presents gambling as a solution to financial hardship, or suggests outcomes depend mainly on skill or certainty.
- PLAs were told to remove advertising for operators **not licensed in their province**.

Source: NGB statement, 1 Dec 2025 (`ngb.org.za/wp-content/uploads/2025/12/NGB-Statement-Gambling-Advertising.pdf`).

Caveat: the directive is addressed to the licensing authorities and licensees. Whether it binds an independent affiliate publisher directly is a **[LEGAL]** question. Treat it as the minimum standard anyway: the regulator is actively monitoring digital advertising, and operators will drop affiliates that create exposure for them.

The Advertising Regulatory Board (ARB) is also tightening its Gambling Code. A revised draft went out for comment (deadline 28 Feb 2026). Check whether the final version is in force (Phase 5 watchlist).

What this changes in the roadmap:

- "Zero risk" (3 places) and the 199 mentions of "free" need rewriting, not just the three "zero risk" lines (T0.7).
- Responsible-gambling messaging must travel with every offer, not just sit in the footer. Today the SARGF slogan "Winners know when to stop" appears **once** in the file (new T0.9).

### 1.3 Privacy and cookies (POPIA)

- Electronic direct marketing (email, SMS) needs opt-in consent under section 69 of POPIA. The Information Regulator's Guidance Note on Direct Marketing (3 Dec 2024) is non-binding but sets expectations. Source: Baker McKenzie, DLA Piper Africa, BusinessTech.
- Section 72 restricts transferring personal information outside South Africa without adequate protection or consent.
- POPIA has no cookie-specific section. Several vendor guides say opt-in consent before non-essential cookies is the safe reading, and commentary on the 2024 guidance note says cookies fall within electronic marketing. These are vendor and law-firm opinions, so treat opt-in as best practice and confirm with your attorney.
- Practical conclusion: your only third-party load today is Google Fonts (and `bit.ly` redirects on click). Self-hosting the fonts removes the consent problem for page loads and also helps speed (T0.8). Then "Decline" has something real to decline (analytics, if you add it).
- If you collect emails (newsletter), you are processing personal information: you need opt-in, an unsubscribe, a privacy policy, and an Information Officer registered with the Information Regulator (vendor guides say this is mandatory; verify on the Regulator's site).

### 1.4 Operator verification is now much easier

- The NGB launched a public **Verified Operators** portal in April 2026: a searchable register of licensed land-based and online operators, built with the provincial authorities. A platform missing from the list is not authorised to offer gambling in South Africa. Sources: iGamingBusiness; Hypertext (Apr 2026).
- Licences are issued by the nine provincial authorities, not by the NGB, so a complete record holds the **issuing province and licence number** (T0.10, T1.5).

### 1.5 Responsible-gambling details to use exactly

- SARGF / NRGP toll-free helpline: **0800 006 008** (24/7). WhatsApp or SMS: **076 675 0710**. Slogan: "Winners know when to stop". Official site: `responsiblegambling.org.za`. Sources: SARGF FAQ; NGB festive-season release; EWN (6 Nov 2025).
- Your 11 links go to `http://www.responsiblegambling.co.za` (insecure, and not the domain the SARGF currently publishes under). Replace with the `https` SARGF site (new T0.11).
- SARGF reported a 55% rise in addiction-related helpline calls in the year to Feb 2025 (EWN). Use it, with a source link, if you want a data point in the RG page.

### 1.6 SEO structured data: one roadmap item is out of date

- Google removed **FAQ rich results for all sites on 7 May 2026**, and dropped FAQ support from the Rich Results Test and Search Console reports (June 2026). FAQPage markup is harmless and can still help other systems read the page, but it will not show anything in Google. Review and BreadcrumbList rich results are still supported. Sources: Search Engine Journal-style coverage (exchange4media, TechWyse, SEOcrawl).
- So T2.3's old done-when ("Rich Results Test passes on the FAQ pages") **cannot be met**. Replaced below.

### 1.7 Tooling facts confirmed

- Astro deploys to GitHub Pages with the official `withastro/action@v2` plus `actions/deploy-pages@v4`. For a project page (`username.github.io/repo`) set both `site` and `base`; with a custom domain set only `site`. Source: Astro docs.
- `lycheeverse/lychee-action@v2` is the current link-checker action, and its README recommends pinning to a commit SHA. Source: lychee-action README.

### 1.8 Not verified (do not rely on these without checking)

- Google's Review snippet guidelines (what counts as an eligible third-party review): check Google Search Central before shipping `Review` markup.
- Core Web Vitals thresholds used here (LCP 2.5 s, INP 200 ms, CLS 0.1) are from memory of Google's published "good" bands.
- I did not check any individual bookmaker's licence, bonus terms, or whether each is on the NGB portal. That is the work in T0.10 and T1.5.
- The `.co.za` vs `.org.za` SARGF domain question: confirm which is canonical before replacing links.

---

## 2. Gate G0: Decide the content scope (0.5 day, blocks everything else)

Why first: if casino and slots pages are going away or being rewritten, any polish on them (ratings, JSON, images, SEO) is wasted.

Options:

| Option | What it means | Trade-off |
|---|---|---|
| **A. Sports betting and information only** (recommended) | Remove or neutralise `casino`, `slots`, `lucky`, `luckyfish` pages and casino promotions. Keep sports betting, horse racing, odds education, responsible gambling. Add one neutral explainer: "Is online casino legal in South Africa?" | Less content (and likely less affiliate revenue from casino), but consistent with the NGB's stated position |
| **B. Keep casino content** | Keep pages, add legal review and strong disclaimers | Highest regulatory and partner risk. Only proceed with written advice from a gambling attorney |

Steps:

1. Inventory pages: list every key of the `PAGES` object (browser console or `grep "PAGES"` in the script) and mark each page: sports / casino / education / RG / other.
2. Record the decision in `docs/decisions/0001-content-scope.md` (date, option, reasoning, who advised).
3. If A: create a redirect/retirement list (old `#slots` → new explainer page). It feeds T2.5.
4. If B: book the legal review first, and add its conclusions to `docs/decisions/`.

**Done when:** the decision file exists and the page inventory marks every page keep / rewrite / retire.

---

## 3. Phase 0: Stop the risks (about 3 days)

### T0.1 Remove or source unverified figures (30 min)

- Delete "Join 100,000+ SA Bettors" (line 1441), or replace it with a figure you can document (for example, your own analytics, with the date).
- Decide on "2,000+ games" and "all 20 licensed SA bookmakers": either source them (operator page, NGB portal count, dated) or remove them.
- The old grep also matched money amounts like "R5,000+500 Spins". Use:

```bash
grep -niE "[0-9,]+\+ (SA )?(bettors|players|users|members)" Index.html
```

**Done when:** that grep returns nothing and every remaining numeric claim has a source in `data/` or a footnote.

### T0.2 Make cookie "Decline" real (1 h)

Today both buttons call the same function and store `cookie_consent=1`.

```js
const CK = 'cookie_consent';
function setConsent(granted) {
  try {
    localStorage.setItem(CK, granted ? '1' : '0');
    localStorage.setItem(CK + '_at', new Date().toISOString());
  } catch {}
  document.getElementById('cookie')?.remove();
  if (granted) loadOptionalScripts();   // empty today; analytics would go here
}
document.getElementById('ck-yes')?.addEventListener('click', () => setConsent(true));
document.getElementById('ck-no')?.addEventListener('click',  () => setConsent(false));
```

- Relabel the buttons "Accept" and "Decline" (they say "Understood" and "Dismiss" now).
- Show the banner again when the stored choice is older than 12 months (common practice, not a legal rule).
- Until you add analytics, `loadOptionalScripts()` stays empty and the banner is a notice. If you never add optional scripts, you can replace the banner with a privacy notice and drop consent state entirely.

**Done when:** in DevTools, clicking Decline stores `0`, clicking Accept stores `1`, and the Network tab shows no third-party requests after Decline.

### T0.3 Replace the 4 `.apk` links (2 h)

Lines 3715, 3719, 3721, 3769. The Gbets APK sits on `gblog.co.za` (a blog upload folder), and Sportingbet's on a media CDN.

- Replace each with the operator's official app page (their site's "download the app" page, or the Google Play / App Store listing).
- Link text: "Official app page", with `rel="noopener noreferrer"`.
- Tell readers to download only from the operator's own site or an official store.

**Done when:** `grep -c "\.apk" Index.html` returns 0.

### T0.4 Remove hotlinked images (2 h)

13 distinct images load from `bettingguide.co.za` (77 references to that domain).

1. Request logo packs from each operator's affiliate programme (they supply brand assets), or use the operator's own press page.
2. Save to `public/img/logos/<slug>.svg` (or `.webp`), 110x36 or the displayed size.
3. Replace the 13 `src` URLs. Keep the `alt`, `width`, `height` already present.
4. Replace the non-logo images (slot screenshots, cricket menu background) with your own artwork or remove them.

**Done when:** `grep -c "bettingguide.co.za" Index.html` returns 0 and the Network tab shows no requests to that domain.

### T0.5 Rename to `index.html`, write the README (1 h)

```bash
git mv Index.html tmp.html && git mv tmp.html index.html   # two steps: safe on case-insensitive systems
```

README sections: purpose, structure, how to run locally, how to deploy, how to update bookmaker data, contact, disclosure link. (If you move to Astro in Phase 2 the README gets rewritten; keep this one short.)

**Done when:** GitHub Pages serves `/` and the README covers all six sections.

### T0.6 Fix the visible backslashes (30 min)

13 strings contain `\\'` inside double-quoted JS strings, rendering `Betway\'s`.

```bash
grep -nF "\\\\'" Index.html          # locate
sed -i "s/\\\\\\\\'/\\\\'/g" Index.html   # \\' -> \'   (check the diff before committing)
```

Review the diff by eye: the file also contains correct `\'` escapes that must stay.

**Done when:** `grep -cF "\\\\'" Index.html` returns 0 and the Hollywoodbets, Betway and Gates of Olympus text renders without backslashes.

### T0.7 Rewrite risky claims (1.5 h)

Basis: NGB directive (section 15, Regulation 3). Targets:

| Claim today | Replace with |
|---|---|
| "Zero risk" (3 places) | "No deposit needed. Wagering requirements and withdrawal limits apply." |
| "R50 Free" / "free" offers (199 mentions of "free") | "R50 bonus on sign-up (terms apply)": state what it is and its conditions in the same sentence |
| "Best no-deposit offer in SA", "most casino games of any SA licensed bookmaker", "SA's newest licensed bookmaker" | Delete, or state a dated, sourced fact ("As of 2026-10-19, X lists N games") |
| "Best", "#1" ranking labels (15 hits for "#1") | Tie to the published rating method (T1.3) or remove |

Create `docs/claims-policy.md` listing the rules above (one page). It becomes the reference for the banned-claims CI check.

**Done when:** `scripts/check-banned-claims.sh` (Appendix A) passes and a manual read of every offer card finds no unconditional "free" or risk-free wording.

### T0.8 Self-host fonts (1 h)

1. Download Oswald (400/500/600/700) and Source Serif 4 (400, 600, italic 400) as `.woff2` (for example via google-webfonts-helper or the fonts' open-source repositories; both are OFL licensed).
2. Put them in `public/fonts/`, add `@font-face` rules with `font-display: swap`.
3. Remove the two `preconnect` tags and the Google Fonts `<link>`.
4. Preload only the one or two files used above the fold.

**Done when:** the Network tab shows zero requests to `fonts.googleapis.com` or `fonts.gstatic.com`.

### T0.9 Responsible-gambling messaging on every offer (new, 3 h)

Basis: NGB directive (messaging must be in all advertising) and ARB code.

- Add a standard strip to every offer card, bonus table and "Visit site" button group:
  `18+ | Winners know when to stop | Helpline 0800 006 008 | WhatsApp/SMS 076 675 0710 | Terms apply`
- Add one site-wide sticky or footer block with the same text.
- Build it once as a component/template so it cannot be forgotten on new pages.
- Keep it legible: not small grey text.

**Done when:** every page that contains an operator link or bonus also contains the RG strip (script: count pages with `href="/go/` and without the RG component; expect 0 mismatches).

### T0.10 Verify every operator against the NGB portal (new, 3 h)

1. For each bookmaker on the site, search the NGB Verified Operators portal and record: operator legal name, issuing province, licence number, status, date checked.
2. Cross-check on the issuing provincial board's own register where one is public.
3. Remove or park any operator you cannot verify. Also check each operator is licensed in the province you cite (the NGB directive targets operators not licensed in the relevant province).
4. Save the results in `data/licences-2026-10.csv` for now; T1.1 moves them into JSON.

**Done when:** every operator shown on the site has a portal-verified row with a licence number and date.

### T0.11 Fix the responsible-gambling links (new, 20 min)

- Replace the 11 `http://www.responsiblegambling.co.za` links with the current `https` SARGF URL (confirm the canonical domain first; the SARGF publishes under `responsiblegambling.org.za`).
- Also upgrade `http://www.ngb.org.za`, `gamblerssa.com` and the other `http://` links to `https` where the site supports it.

**Done when:** `grep -c 'href="http://' Index.html` returns 0 and each RG link opens a live page.

**Phase 0 gate:** run `scripts/phase0-check.sh` (Appendix B). All checks green before starting Phase 1.

---

## 4. Phase 1: Content integrity (about 4 days)

### T1.1 Move bookmaker facts into `data/bookmakers.json` (1.5 days)

Schema (one object per operator; example):

```json
{
  "slug": "example-bookmaker",
  "name": "Example Bookmaker",
  "operator_legal_name": "Example Online (Pty) Ltd",
  "products": ["sports", "horse-racing"],
  "licences": [
    { "authority": "Western Cape Gambling and Racing Board", "number": "XXXX", "status": "active",
      "ngb_portal_checked_on": "2026-10-19", "verified_on": "2026-10-19", "source_url": "https://..." }
  ],
  "bonus": {
    "headline": "R1,000 first-deposit bonus",
    "wagering": "x times bonus", "min_odds": "1.50", "expires": "2026-12-31",
    "terms_url": "https://...", "verified_on": "2026-10-19"
  },
  "rating": { "overall": 4.2, "criteria": { "licence_compliance": 4.5, "odds": 4.0 }, "rated_on": "2026-10-19" },
  "affiliate": { "path": "/go/example-bookmaker/", "target": "https://...", "rel": "sponsored nofollow noopener" },
  "app_page": "https://..."
}
```

Steps:

1. Extract every operator fact from the templates into the JSON (use T0.10's CSV for licences).
2. Replace the hard-coded strings in templates with reads from the JSON.
3. Add `scripts/data_freshness.py` (Appendix D) and a schema check (`ajv` or a small Python check) so a missing `verified_on` fails CI.

**Done when:** `grep -nE "R[0-9,]+\+?[0-9 ]*(Spins|Free)" Index.html` finds no bonus text outside the data-driven render, and the schema check passes.

### T1.2 Dates (0.5 day)

- Replace the 142 "2025" references: keep only genuinely historical ones ("launched in 2025"), and make everything else data-driven.
- Replace "Updated weekly" (3 places) with "Last verified: <date from data>". Do not claim a cadence you do not keep (the monthly job in T4.2 supports "monthly").
- Update `<title>`s and meta descriptions that carry a year.

**Done when:** `grep -c "2025" Index.html` returns only reviewed historical cases (list them in the PR), and "Updated weekly" returns 0.

### T1.3 "How we rate" page (0.5 day)

Suggested weights (a starting proposal, adjust to your real method, then keep it fixed):

| Criterion | Weight |
|---|---|
| Licence and compliance (verified on NGB portal) | 25% |
| Odds and margins | 20% |
| Markets and product breadth (sports) | 15% |
| Deposits and withdrawals (speed, fees, methods) | 15% |
| App and site usability | 10% |
| Customer support | 10% |
| Responsible-gambling tools (limits, self-exclusion) | 5% |

- Compute `overall` from the criteria in a script so ratings cannot drift (fixes the Betfred 4.2 vs 4.3 and Lucky Fish 4.2 vs 4.1 conflicts, see T1.6).
- Link every star or "x/5" to this page.
- State how you test (dates, accounts, what you measured) and your commercial relationship (T1.4).

**Done when:** every rating element links to `/how-we-rate/` (script check) and the page lists all criteria, weights and the testing date.

### T1.4 Affiliate disclosure (0.5 day)

- Above the fold on every comparison and bonus page, plain language: you earn commission if readers sign up through your links; it does not change the rating method; link to "How we rate".
- Repeat a short form next to each "Visit site" button group.
- Test at 360 px wide (phone) and 1280 px: visible without scrolling.

**Done when:** a Playwright or manual screenshot test at both widths shows the banner in the first viewport on each page type.

### T1.5 Full terms verification (1 day, builds on T0.10)

For each operator: open the live terms page, record headline bonus, wagering, minimum odds, expiry, eligible markets, withdrawal limits, and the licence line shown in their footer. Store the URL and `verified_on`. Keep screenshots in `evidence/<slug>/<date>.png` (private repo or a private drive if you prefer).

**Done when:** every JSON entry has `licences[].verified_on`, `bonus.verified_on`, and a `terms_url`.

### T1.6 One rating per operator (0.5 day, new)

Known conflicts (lines): Betfred 4.2 (2041) vs 4.3 (2070); Lucky Fish 4.2 (2013) vs 4.1 (3504); equal 4.2 scores shown as five stars for two operators and four for Sportingbet (2040-2043).

- Stars are derived from the score by one function (for example, `Math.round(score)` or a half-star scale), never typed by hand.

**Done when:** a script that collects every rating string per operator finds exactly one distinct value each.

### T1.7 Replace `bit.ly` links (0.5 day, new)

6 distinct `bit.ly` links used 77 times.

- Create `/go/<slug>/` pages (Astro: Phase 2; interim: static HTML files) that redirect to the affiliate target with a meta refresh and `<meta name="robots" content="noindex">`. Add `Disallow: /go/` to `robots.txt`.
- Mark every outbound affiliate link `rel="sponsored nofollow noopener"` (Google's recommended attribute for paid or affiliate links).
- Keep the real affiliate URLs only in `data/bookmakers.json`.
- Rotating a link now means editing one data field instead of 77 occurrences.

**Done when:** `grep -c "bit.ly" Index.html` returns 0 and every affiliate link has `rel` containing `sponsored`.

### T1.8 Promotion wording pass (0.5 day, new)

Apply `docs/claims-policy.md` to every promo card: state the main conditions beside the headline figure (wagering, minimum odds, expiry, "terms apply"), remove urgency pressure ("claim now before it ends") and anything implying gambling fixes money problems.

**Done when:** a reviewer (you plus one other person) signs the checklist in the PR for each promo card.

---

## 5. Phase 2: Architecture and SEO (about 7 days)

Current state: one 403 KB file, 304 KB of inline JS, 63 KB of CSS, hash routing, one `<title>`, no canonical or JSON-LD, all pages rendered by `innerHTML`.

### T2.1 + T2.2 Move to a static build with Astro (4 days)

Approach: migrate page by page (keep the old site live until parity).

1. Scaffold: `npm create astro@latest`, empty template, TypeScript optional.
2. `astro.config.mjs`:

```js
import { defineConfig } from 'astro/config';
export default defineConfig({
  site: 'https://itumelengthema90-collab.github.io',
  base: '/betting-guide-rsa',   // remove `base` and set `site` to your domain if you add a custom domain
});
```

3. Layout `src/layouts/Base.astro`: `<title>`, meta description, canonical (`Astro.url`), Open Graph, the RG strip, the disclosure banner, nav, footer.
4. Convert each `PAGES.<key>` template into `src/pages/<slug>.astro` (or content collections for guides), reading from `data/bookmakers.json`.
5. Split CSS into `src/styles/{tokens,layout,components}.css`, import in the layout.
6. Move JS widgets (lucky numbers, calculators, accordions) into small modules loaded only on the pages that use them.
7. Deploy workflow `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages
on:
  push: { branches: [main] }
  workflow_dispatch:
permissions: { contents: read, pages: write, id-token: write }
concurrency: { group: pages, cancel-in-progress: true }
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: withastro/action@v2
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: { name: github-pages, url: "${{ steps.deployment.outputs.page_url }}" }
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

8. In the repo: Settings, Pages, Source = GitHub Actions.

Why Astro here: output is plain HTML per page (what search engines and users without JS get), islands for the few interactive bits, and an official Pages action. Eleventy would also work; pick one and do not mix.

Parity check before switching: for each old page key, confirm the new URL exists, content matches (diff the visible text), and the page has its own `<title>`, description and canonical.

**Done when:** every page has its own URL, `<title>`, meta description and canonical tag (a build-time script lists any page missing one), and no source file exceeds 50 KB (`find src -type f -size +50k` returns nothing).

### T2.5 Preserve old links (new, 2 h)

Hash URLs (`/#slots`) cannot be redirected on a static host. Add a tiny script to the new home page that maps `location.hash` to the new path (`#betway-review` becomes `/betway-review/`) and sends retired pages (Gate G0) to the explainer. Keep it for 6 to 12 months.

**Done when:** each old hash from the Gate G0 inventory lands on the right new page (test list in `tests/redirects.txt`).

### T2.3 Structured data and crawl files (1 day) (replaces the old done-when)

- `BreadcrumbList` on every page below home.
- `Review` on review pages, only for operators you actually reviewed; follow Google's current review snippet guidelines (see 1.8, not verified here).
- `FAQPage` is optional: Google no longer shows FAQ rich results (since 7 May 2026), so only add it where it matches visible FAQ content and you want other systems to read it.
- `sitemap.xml` (Astro's sitemap integration) and `robots.txt` (`Disallow: /go/`, sitemap URL).
- Validate with the Schema Markup Validator and the Rich Results Test (Review and Breadcrumb only).

**Done when:** the validators report no errors on one page of each type, and the sitemap lists every page.

### T2.4 Images and performance (1 day)

- Logos as SVG, photos as WebP, explicit `width` and `height`, `loading="lazy"` below the fold, `fetchpriority="high"` on the single largest above-fold image.
- Lighthouse CI (Phase 4) measures a lab LCP. Also check real-user data once you have traffic (Search Console Core Web Vitals report).

**Done when:** Lighthouse CI reports LCP at or under 2.5 s on the mobile preset for the home page and one review page, three runs, median.

---

## 6. Phase 3: Features (about 6 days)

### T3.1 Newsletter with double opt-in (1.5 days)

- Choose a provider that supports double opt-in, stores a consent timestamp and source, offers one-click unsubscribe, and lets you pick or see the data location (POPIA section 72). Do not pick on price alone.
- Form: email only, an unticked consent checkbox with plain wording ("Send me betting guides and bookmaker updates by email"), link to the privacy policy.
- Write `/privacy/` covering what you collect, why, who processes it, retention, how to access, correct or delete, and how to complain to the Information Regulator. Have it reviewed **[LEGAL]**.
- Check with the Information Regulator whether you need to register an Information Officer, and do it if so.

**Done when:** a test signup receives the confirmation email, the address stays unconfirmed until the link is clicked, and unsubscribe works.

### T3.2 Calculators (2 days)

- Odds converter (decimal, fractional, American), implied probability, bookmaker margin (overround), stake and return, bankroll/Kelly (clearly labelled as education).
- Pure functions in `src/lib/calc.ts` with unit tests.
- Test cases come from the worked examples in your odds and bankroll guides (these become the "done when").
- Add the RG strip and a line that calculators do not predict outcomes.

**Done when:** `npm test` passes with at least one test per worked example, and results match the guides to the stated rounding.

### T3.3 Responsible-gambling self-check and session reminder (1.5 days)

- Self-check: 9 to 10 plain questions with a simple score band and sensible next steps. If you use a published screening tool (for example, the Problem Gambling Severity Index), confirm its licence terms and cite it; otherwise write your own and say it is not a diagnosis.
- Session reminder: after a set time on the site (for example, 30 minutes), a dismissible "take a break" notice.
- Every result state shows: helpline 0800 006 008, WhatsApp or SMS 076 675 0710, SARGF link, and self-exclusion information (the NGB maintains a national register of excluded persons).

**Done when:** every result path shows the helpline and SARGF link, and the page passes keyboard-only use.

### T3.4 Filter and sort for the comparison matrix (1 day)

- Filters: licence province, bonus type, payment method, app available. Sort: rating, bonus, name.
- Use real form controls (`<select>`, `<input type="checkbox">`), `aria-live` for the result count, and no default sort that favours the highest-commission partner (disclose any "featured" slot as sponsored).

**Done when:** it works with keyboard only, at 360 px width, and a screen-reader pass announces result counts.

---

## 7. Phase 4: Quality gates (about 2 days)

### T4.1 CI pipeline

`.github/workflows/ci.yml` (pin every `uses:` to a commit SHA once you have chosen versions; check current releases first):

```yaml
name: CI
on:
  pull_request:
  push: { branches: [main] }
permissions: { contents: read }
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-node@v5
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run build
      - name: Banned claims
        run: bash scripts/check-banned-claims.sh dist
      - name: Data freshness (fail if older than 45 days)
        run: python3 scripts/data_freshness.py 45 --fail
      - name: HTML validation
        run: npx html-validate "dist/**/*.html"
      - name: Link check
        uses: lycheeverse/lychee-action@v2
        with:
          args: --no-progress --exclude-mail './dist/**/*.html'
          fail: true
      - name: Lighthouse CI
        run: npx @lhci/cli@latest autorun
```

`lighthouserc.json`:

```json
{
  "ci": {
    "collect": { "staticDistDir": "./dist", "numberOfRuns": 3 },
    "assert": {
      "assertions": {
        "categories:accessibility": ["error", { "minScore": 0.95 }],
        "categories:seo": ["error", { "minScore": 0.95 }],
        "categories:performance": ["warn", { "minScore": 0.9 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }]
      }
    }
  }
}
```

Notes:

- Operator sites often block bots. Add accepted status codes or an exclude list to the lychee config for those hosts (see lychee's documentation for the `--accept` and `--exclude` options) rather than turning link checking off.
- The `/go/` redirect pages should be excluded from Lighthouse's URL list.
- Lighthouse's SEO and accessibility scores are automated checks; they do not replace a manual keyboard and screen-reader pass.
- Add `.github/dependabot.yml` with the `github-actions` ecosystem so pinned SHAs stay current.
- In Settings, Branches, protect `main`: require the `checks` job and a PR.

**Done when:** a PR that adds a broken link, a "zero risk" phrase, a stale `verified_on`, or drops accessibility below 0.95 fails CI (test each with a throwaway branch).

### T4.2 Monthly re-verification issue

`.github/workflows/monthly-review.yml`:

```yaml
name: Monthly bonus re-verification
on:
  schedule: [{ cron: "0 6 1 * *" }]
  workflow_dispatch:
permissions: { contents: read, issues: write }
jobs:
  open-issue:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - name: Build checklist
        run: python3 scripts/data_freshness.py 0 > body.md
      - name: Open issue
        env: { GH_TOKEN: "${{ github.token }}" }
        run: |
          gh issue create --title "Verify bookmaker data: $(date -u +%Y-%m)" \
            --label verification --body-file body.md
```

(`max_age 0` lists every operator, so the issue is the full monthly checklist.)

**Done when:** a manual `workflow_dispatch` run creates the issue with one checkbox per operator and field.

### T4.3 Regulatory watch issue (new)

Same pattern as T4.2, quarterly, with the Phase 5 watchlist as the issue body.

---

## 8. Phase 5: Ongoing operations

### 8.1 Monthly verification routine (about 2 hours per 10 operators)

1. Open the issue created by T4.2.
2. For each operator: NGB portal check, provincial register check, open live terms, compare headline bonus, wagering, minimum odds, expiry.
3. Update `data/bookmakers.json` (`verified_on` = today).
4. Open a PR; CI checks freshness and claims; merge.
5. Remove or flag any operator that is missing from the portal, suspended, or whose terms no longer match what you publish.

### 8.2 Regulatory watchlist (check at least quarterly)

| Item | Why it matters | Where to look |
|---|---|---|
| New national gambling Bill (said to be heading to Cabinet in 2026) and the Remote Gambling Bill (B11-2024) | Could legalise or tighten online casino; changes Gate G0 | Parliament (pmg.org.za), dtic, NGB |
| NGB / provincial advertising norms and standards | Expected as licence conditions; may restrict affiliate and bonus advertising | NGB website, trade press |
| ARB Gambling Advertising Code (revised draft consulted early 2026) | Self-regulatory standard for wording and RG messages | arb.org.za |
| National Treasury proposal of a 20% national tax on online gambling gross revenue | May change operator bonuses and affiliate economics | National Treasury, Polity |
| Information Regulator guidance on direct marketing and online tracking | Newsletter and cookie practice | inforegulator.org.za |
| Google structured-data and spam-policy changes | Review markup, affiliate quality | Google Search Central blog |

### 8.3 Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Casino promotion treated as promoting unlawful gambling | Medium to high | High | Gate G0 decision, legal review |
| Operator drops you for non-compliant wording | Medium | Medium | Claims policy, RG strip, CI banned-claims check |
| Stale bonus data misleads readers | High without process | High | `verified_on`, freshness gate, monthly issue |
| Migration breaks existing URLs | Medium | Medium | Hash redirect map, parity check |
| Affiliate link rot after `bit.ly` removal | Low | Medium | Links held in one data field, link checker |

---

## Appendix A: `scripts/check-banned-claims.sh`

```bash
#!/usr/bin/env bash
# Usage: bash scripts/check-banned-claims.sh [dir]   (defaults to .)
set -euo pipefail
DIR="${1:-.}"
PATTERNS='zero risk|risk-free|risk free|guaranteed|sure ?bet|never lose|easy money|free money|100,000\+|most .* of any SA|best .* in SA'
if grep -rniE --include='*.html' --include='*.md' --include='*.json' --include='*.astro' \
     --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=.github --exclude-dir=scripts \
     -e "$PATTERNS" "$DIR" | grep -v 'claim-ok'; then
  echo "Banned claim found. Rewrite it, or mark a vetted sentence with 'claim-ok'." >&2
  exit 1
fi
echo "No banned claims."
```

## Appendix B: `scripts/phase0-check.sh`

```bash
#!/usr/bin/env bash
set -u
f="${1:-index.html}"
fail=0
check() { if [ "$2" != "0" ]; then echo "FAIL  $1 ($2)"; fail=1; else echo "ok    $1"; fi; }
check "unverified audience claims"     "$(grep -ciE '[0-9,]+\+ (SA )?(bettors|players|users|members)' "$f")"
check "direct .apk links"              "$(grep -c '\.apk' "$f")"
check "hotlinked bettingguide.co.za"   "$(grep -c 'bettingguide.co.za' "$f")"
check "visible backslash escapes"      "$(grep -cF "\\\\'" "$f")"
check "Google Fonts requests"          "$(grep -cE 'fonts\.(googleapis|gstatic)\.com' "$f")"
check "bit.ly links"                   "$(grep -c 'bit\.ly' "$f")"
check "http:// links"                  "$(grep -c 'href="http://' "$f")"
check "banned claims"                  "$(bash scripts/check-banned-claims.sh . >/dev/null 2>&1; echo $?)"
exit $fail
```

(Adjust the file path when the build moves to Astro, and run the same checks against `dist/`.)

## Appendix C: Reusable responsible-gambling block

```html
<aside class="rg-strip" aria-label="Responsible gambling">
  <strong>18+</strong> Winners know when to stop.
  Free, confidential help 24/7: <a href="tel:0800006008">0800 006 008</a>
  or WhatsApp/SMS <a href="https://wa.me/27766750710">076 675 0710</a>.
  <a href="https://www.responsiblegambling.org.za/" rel="noopener">SARGF</a>.
  Terms apply. Gambling can be addictive.
</aside>
```

(Confirm the exact prescribed wording and format with the NGB directive and your attorney; the strip above uses the published SARGF slogan and numbers.)

## Appendix D: `scripts/data_freshness.py`

```python
#!/usr/bin/env python3
"""List bookmaker data older than N days. Usage: data_freshness.py [max_age_days] [--fail]"""
import json, sys, pathlib, datetime as dt

max_age = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 35
data = json.loads(pathlib.Path("data/bookmakers.json").read_text())
today = dt.date.today()
stale = []

def check(name, field, value):
    if not value:
        stale.append((name, field, "missing", 9999)); return
    age = (today - dt.date.fromisoformat(value)).days
    if age >= max_age:
        stale.append((name, field, value, age))

for b in data:
    check(b["name"], "bonus", b.get("bonus", {}).get("verified_on"))
    lic = b.get("licences", [])
    check(b["name"], "licence", min((l.get("verified_on", "") for l in lic), default="") or None)
    check(b["name"], "rating", b.get("rating", {}).get("rated_on"))

print(f"# Bookmaker data verification ({today})\n")
for name, field, value, age in stale:
    print(f"- [ ] {name}: {field} last verified {value} ({age} days)")
sys.exit(1 if stale and "--fail" in sys.argv else 0)
```

---

## Appendix E: Task order and effort

| Step | Tasks | Effort (solo) |
|---|---|---|
| Gate | G0 | 0.5 day (plus legal turnaround) |
| Phase 0 | T0.1 to T0.11 | about 3 days |
| Phase 1 | T1.1 to T1.8 | about 4 days |
| Phase 2 | T2.1 to T2.5 | about 7 days |
| Phase 3 | T3.1 to T3.4 | about 6 days |
| Phase 4 | T4.1 to T4.3 | about 2 days |
| Phase 5 | monthly and quarterly routines | about 2 hours per 10 operators per month |

Total: about 3.5 to 4 weeks of focused solo work, not counting legal review.

## Appendix F: Sources

- NGB statement on gambling advertising, 1 Dec 2025: ngb.org.za/wp-content/uploads/2025/12/NGB-Statement-Gambling-Advertising.pdf
- NGB festive-season warning release (helpline, WhatsApp/SMS, illegal online gambling): ngb.org.za/wp-content/uploads/2025/12/NGB-Media-Release_Festive-Season-Warning-against-Illegal-and-Compulsive-Gambling.pdf
- MyBroadband, "New laws coming for online gambling in South Africa" (30 Jun 2026): mybroadband.co.za/news/government/656213-new-laws-coming-for-online-gambling-in-south-africa.html
- Bandwidth Blog (1 Jul 2026): bandwidthblog.co.za/2026/07/01/south-africa-online-gambling-bill/
- Yogonet (3 Jul 2026): yogonet.com/international/news/2026/07/03/125228-south-africa-moves-to-tighten-gambling-laws-and-advertising-rules-amid-addiction-concerns
- Chambers, Gaming Law 2025, South Africa: practiceguides.chambers.com/practice-guides/gaming-law-2025/south-africa
- Polity, "A national tax on online betting in South Africa" (15 May 2026): polity.org.za/article/a-national-tax-on-online-betting-in-south-africa-2026-05-15
- Mail & Guardian, legal status of online gambling (22 Jul 2026): mg.co.za/partner-content/2026-07-22-is-online-gambling-legal-in-south-africa-what-the-data-actually-shows/
- iGamingBusiness, NGB verification portal: igamingbusiness.com/legal-compliance/regulation/south-africa-regulator-verification-portal-combat-unlicensed-operators/
- Hypertext, NGB Verified Operators (Apr 2026): htxt.co.za/2026/04/is-your-betting-site-legal-the-ngb-now-has-a-tool-to-check/
- ARB Gambling Code consultation (Werksmans via Polity, 23 Feb 2026): polity.org.za/article/advertising-regulatory-board-ups-the-ante-on-responsible-gambling-advertising-2026-02-23
- SARGF FAQ: responsiblegambling.org.za/frequently-asked-questions-faqs/
- EWN, helpline calls up 55% (6 Nov 2025): ewn.co.za/2025/11/06/calls-for-responsible-gambling-grow-as-addiction-surges
- Baker McKenzie, direct marketing under POPIA: insightplus.bakermckenzie.com/bm/data-technology/south-africa-direct-marketing-under-scrutiny-key-regulatory-developments-in-2024
- DLA Piper Africa, Guidance Note on Direct Marketing: dlapiperafrica.com/en/south-africa/insights/2025/Data-Protection-Guidance-Note-on-Direct-Marketing
- BusinessTech, spam and direct marketing (30 Jan 2025): businesstech.co.za/news/?p=809391
- Google FAQ rich results ended 7 May 2026: techwyse.com/news/ai-search/google-faq-rich-results-deprecated-2026; exchange4media.com/digital-news/google-deprecates-faq-content-feature-154581.html
- Astro, deploy to GitHub Pages: docs.astro.build/en/guides/deploy/github/
- lychee-action: github.com/lycheeverse/lychee-action