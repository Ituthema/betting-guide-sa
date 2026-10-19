# Betting Guide SA — crawlable static architecture

This is a framework-free, static multi-page rebuild using the visual tokens and stylesheet from the supplied `betting-guide-sa-improved-review.html`. Every important route is a physical `index.html` file, so the page content and metadata are present in the initial HTML response rather than being injected after a hash-route change.

## Build

Requirements: Python 3.9+; no third-party packages are required.

```bash
python3 scripts/build.py
```

Output is written to `dist/`. To emit absolute canonical URLs and an XML sitemap, set the actual production origin first:

```bash
SITE_URL="https://your-real-domain.example" python3 scripts/build.py
```

Replace that example with the domain that will actually serve the site. Do not deploy the example domain. Without `SITE_URL`, the build intentionally omits canonical tags and does not create an XML sitemap, avoiding fabricated canonical URLs.

## Route architecture

- `/` — home / discovery
- `/bookmakers/` — bookmaker directory
- `/bookmakers/{operator}/` — individual bookmaker review records
- `/promotions/`, `/promotions/welcome-offers/`, `/promotions/terms-checklist/`
- `/sports/` and `/sports/{soccer,rugby,cricket,tennis,horse-racing,esports}/`
- `/casino/`, `/casino/slots/`, `/casino/live-casino/`
- `/guides/beginners/`, `/guides/odds/`, `/guides/bankroll/`, `/guides/responsible-gambling/`
- `/about/`, `/legal/privacy/`, `/legal/terms/`, `/search/`

The content records live in `content/pages.json`; `scripts/build.py` applies one reusable page shell, shared navigation/footer, metadata, related-reading links, evidence records, search index, 404 page and deployment headers. The full source CSS is retained in `assets/site.css`, with additions for the static navigation and search page.

## Content verification model

Each content record has a `status`, `lastVerified`, and `sources` collection. Allowed operational states used in this starter are `needs-verification`, `editorial-review`, `legal-review-required`, and `verified`. A `verified` record is rejected by the build if it has no verification date or no source URLs. The site does **not** claim that any operator review, live promotion, licence, payment claim, rating, game count or legal policy has already been independently verified.

Before marking an operator-specific record `verified`, record:

1. Claim or field checked, with evidence captured separately if needed.
2. Direct official source URL (regulator source for licence claims; operator terms for offer/payment terms).
3. Date checked, reviewer and relevant jurisdiction.
4. Expiry/recheck date for volatile offers and terms.
5. Any conflict or uncertainty and the resolution.

Do not populate a promotion as current from an affiliate landing page alone if the underlying terms are not available. Legal pages are frameworks and require legal review against the actual business and implementation.

## Search and indexing

`/search/` is a static HTML listing of all pages, with client-side filtering and query-string support. It remains useful without JavaScript because all result links are present in the HTML. Search is over the curated page title, category and description index; it is not a full-text search engine over every paragraph.

Each page has a unique title and meta description, plus Open Graph title/description. Canonical tags and `sitemap.xml` are generated only when `SITE_URL` is set. Deploy at the origin root or adapt the generator for your hosting base path before using a project subdirectory.

## Deploy

Publish the contents of `dist/` to a static host (Cloudflare Pages, Netlify, or a root-domain GitHub Pages site). Configure `SITE_URL` in the build environment to the final HTTPS origin. Confirm that `/bookmakers/betway/` and other nested paths load directly, without first visiting the home page. For GitHub Pages project sites under `username.github.io/repository/`, configure a base path before deployment; this starter targets root-origin hosting.

## Launch gates — not yet certified

- Verify all commercial links, affiliate relationships and operator names.
- Verify licensing through the relevant official regulator and jurisdiction; do not infer legality from an operator’s own marketing.
- Replace the privacy/terms frameworks with legally reviewed policies matching actual cookies, analytics, forms, hosting and data processing.
- Add a working contact backend only after choosing the provider and privacy handling; no fake-success contact form is included in this architecture.
- Run automated HTML/link checks, keyboard and screen-reader tests, mobile viewport checks, Lighthouse/PageSpeed and security-header checks on the deployed domain.
- Review gambling-advertising and affiliate disclosure obligations with qualified counsel.

This is a production-oriented architecture starter, not a certification that the content, legal compliance, operator status or hosting configuration has been verified.

## Quality checks

```bash
python3 scripts/build.py
python3 scripts/validate.py
# or: npm run check
```

The validator checks unique titles and meta descriptions, exactly one H1 per HTML document, generated direct routes, and local assets/internal links. It is a basic build check, not a substitute for a deployed-site crawl, browser testing or a legal/factual audit.
