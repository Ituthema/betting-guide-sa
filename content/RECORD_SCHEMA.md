# Content record contract

`pages.json` records use the following fields:

- `slug`: canonical route path, ending in `/` (required)
- `title`: unique, human-readable page title (required)
- `shortTitle`: concise navigation/search label (required)
- `category`: content taxonomy key (required)
- `description`: unique search description (required)
- `intro`: lead paragraph (required)
- `sections`: ordered array of `{ "heading": string, "body": string }`
- `status`: `needs-verification`, `editorial-review`, `legal-review-required`, or `verified`
- `lastVerified`: ISO date or `null`
- `sources`: array of `{ "label": string, "url": string, "checkedAt": string, "reviewer": string }`

No content record in this starter is marked `verified`. Do not promote a record to `verified` until source URLs, a review date and the claim-level evidence log are present. The build script enforces the date/source minimum for records marked verified; editorial review still needs human review for accuracy, legal compliance, tone and completeness.
