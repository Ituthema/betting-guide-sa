# Main-branch baseline audit — 22 October 2026

**Repository:** [Ituthema/betting-guide-sa](https://github.com/Ituthema/betting-guide-sa)  
**Audited ref:** `main` at `d87037a3d9791a5499621cf9cb779568a3fc0392`  
**Commit:** [Merge pull request #17](https://github.com/Ituthema/betting-guide-sa/commit/d87037a3d9791a5499621cf9cb779568a3fc0392) — expanded development plan  
**Audit status:** Source/configuration inspection complete; executable checks and deployment verification require recorded CI/live evidence below.

> This is a dated snapshot. It must not be treated as a guarantee that the branch or deployment has not changed since the audit began.

## 1. Executive result

The current main branch contains a Python-generated static site and a GitHub Actions workflow intended to build, validate and deploy `dist/` to GitHub Pages. The workflow configuration is present, but a workflow file alone does not establish that the latest run passed or that the deployment is healthy.

The content source parses as valid JSON and contains 77 content records:
- 55 `editorial-review`
- 19 `needs-verification`
- 3 `legal-review-required`
- 0 `verified`
- 3 records have one or more source entries; 74 have none.
- 0 records have a non-null `lastVerified` date.
- 19 individual bookmaker records plus one bookmaker directory page (20 records in the bookmaker category).

The site is not content-verified merely because it builds. The current content evidence state remains a major release risk.

## 2. Ref and repository evidence

- Main SHA observed: `d87037a3d9791a5499621cf9cb779568a3fc0392`.
- The SHA is a merge commit for PR #17; the documentation update is present on main.
- Current key source paths: `content/pages.json`, `scripts/build.py`, `scripts/validate.py`, `scripts/check-banned-claims.sh`, and `.github/workflows/pages.yml`.
- `sitemap.xml` and `robots.txt` are not source-root files. The build script creates them under `dist/`; the workflow uploads `dist/`.

## 3. Build and validation design

The repository documents these commands, from the root:
```bash
python3 scripts/build.py
python3 scripts/validate.py
bash scripts/check-banned-claims.sh dist
```

The workflow uses Python 3.12 and runs those commands in the same order, with `SITE_URL=https://ituthema.github.io/betting-guide-sa` for the build. The build script:
- reads `content/pages.json`;
- creates `dist/`;
- rejects records marked `verified` if they lack a verification date or source URLs;
- generates route HTML, search assets/index, `404.html`, headers, `robots.txt`, and (when `SITE_URL` is set) `sitemap.xml`.

The validator checks generated HTML for titles, descriptions, exactly one H1, duplicate title/description values, and missing local link/asset targets. The claim checker scans generated files for selected high-risk promotional phrases. These checks are useful but do not replace factual verification, browser testing, accessibility checks, or a production-site crawl.

**Execution evidence:** pending until the GitHub Actions run triggered for this audit PR completes and its job steps are inspected. Do not read this section as a pass before that update is committed.

## 4. GitHub Actions configuration findings

Workflow: `.github/workflows/pages.yml`  
Name: `Build and deploy Betting Guide SA`

Triggers:
- push to `main`;
- pull requests targeting `main`;
- manual `workflow_dispatch`.

Jobs:
- `build`: checkout, Python 3.12, build, validate, risky-claim scan, configure Pages, upload `dist`;
- `deploy`: runs only for non-PR events on `refs/heads/main`, after `build` succeeds.

The connector query for workflow runs associated with the merge commit returned no entries because that available query is limited to pull-request-triggered runs. This is **not evidence that no run exists or that the run failed**. Inspect the audit PR's actual workflow run and job steps before finalising status.

## 5. Deployment configuration risks

1. The workflow sets `SITE_URL=https://ituthema.github.io/betting-guide-sa`, which is a project-site URL under a repository subpath.
2. The README says the starter targets root-origin hosting and warns that a GitHub Pages project site under `username.github.io/repository/` needs base-path support before deployment.
3. The generator contains root-absolute paths in its generated 404 page (for example `/site.css`, `/`, and `/bookmakers/`). These paths may resolve at the domain root rather than under `/betting-guide-sa/` when deployed as a project site.
4. The generator writes the sitemap using the configured `SITE_URL`; this creates canonical/sitemap URLs with the repository prefix, but does not by itself prove all internal links and assets correctly use that prefix.
5. The source root does not contain `sitemap.xml` or `robots.txt`; these should be verified in the build artifact and at the deployed URL, not by looking only for root source files.

**Conclusion:** there is a likely base-path consistency issue between the workflow's project-site URL and the README's stated root-origin deployment assumptions. This is a configuration risk to test, not a claim that every deployed route is broken.

## 6. Deployment verification status

The public URLs checked by the web retrieval tool were not accessible through that tool during this audit. No HTTP status, response body, TLS status, Pages environment status, active deployment URL, or current deployment commit could be confirmed from that attempt.

- Live homepage HTTP status: **not verified**.
- Nested route direct-load behavior: **not verified**.
- Live `/sitemap.xml` and `/robots.txt`: **not verified**.
- GitHub Pages deployment status and URL: **not verified**.
- Production domain/DNS/custom-domain configuration: **not verified**.

Do not treat a retrieval-tool access error as proof that the site is down. Confirm the actual Pages deployment and test the live URLs from a normal browser or GitHub Pages deployment history.

## 7. Content and release risks

| Priority | Finding | Evidence / consequence | Next action |
|---|---|---|---|
| P0 | CI and deployment outcome not yet recorded | Workflow configuration exists; no authoritative run/deployment result recorded in this report yet | Inspect run linked to audit PR and latest main push; capture job conclusions |
| P0 | Potential Pages base-path mismatch | Workflow uses a project URL; README warns project subpath needs base-path support; 404 output uses root-absolute paths | Test deployed routes/assets; either configure root-domain hosting or implement explicit base-path support |
| P1 | Most content has no source entries | 74/77 records have no source entries | Build claim-level evidence register; do not mark unsubstantiated claims verified |
| P1 | No records have a verification date | 0/77 have non-null `lastVerified`; 0 verified | Define and enforce verification lifecycle and review dates |
| P1 | 19 bookmaker detail records need verification | All 19 individual bookmaker records are currently `needs-verification` in the source snapshot | Verify each material claim against official/regulator sources |
| P1 | Automated checks are limited | HTML structure/local links and a fixed set of promotional phrases only | Add schema/content freshness checks; schedule manual/mobile/accessibility testing |
| P2 | Source-root sitemap/robots absent by design | Generated at build time into `dist/` | Confirm build artifact and live endpoints after successful build/deployment |

## 8. Commands and exact outcomes

### Local execution
A local clone was attempted in the audit environment but failed before checkout because the environment could not resolve `github.com`. Therefore, the commands below were **not executed locally in this environment**:
- `python3 scripts/build.py`
- `python3 scripts/validate.py`
- `bash scripts/check-banned-claims.sh dist`

Do not report local results as passed. The CI run triggered for this audit PR will be used as the reproducible execution evidence if it completes.

### GitHub Actions
- Audit PR URL: to be recorded after creation.
- Workflow run URL/ID: pending.
- Build job: pending.
- Validate step: pending.
- Risky-claim scan step: pending.
- Deploy job: should be skipped for pull-request events by workflow condition; this PR cannot prove a production deployment succeeded.

## 9. Recommended next actions

1. Capture the audit PR workflow run, job status, and exact step outcomes; update this report with actual results.
2. Independently inspect the most recent `main` push run and Pages deployment history; do not infer deploy success from PR CI.
3. Fix or explicitly resolve the base-path decision before relying on project-site deployment.
4. Add a smoke-test checklist for homepage, one nested bookmaker page, one guide page, 404, CSS/JS assets, canonical tags, sitemap and robots.
5. Create a claim-level source register and resolve the 19-versus-20 bookmaker-list discrepancy intentionally.
6. Keep monetisation and high-risk promotions gated until evidence and programme approval are documented.

## 10. Audit limitations

This audit inspected the current main source files through GitHub integration and parsed the complete `content/pages.json` payload for counts. The local clone attempt was blocked by DNS/network resolution in the audit environment. Live URL retrieval did not yield an HTTP response, and the available commit-run query did not return push-triggered runs for the merge SHA. These are evidence limitations, not proof of site failure.
