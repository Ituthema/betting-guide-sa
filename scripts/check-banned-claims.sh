#!/usr/bin/env bash
# Scan built HTML for promotional claims that need editorial review.
# Usage: bash scripts/check-banned-claims.sh [directory] (defaults to .)
set -euo pipefail
DIR="${1:-.}"
python3 - "$DIR" <<'PY'
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
if not root.exists():
    print(f"ERROR: scan path does not exist: {root}", file=sys.stderr)
    sys.exit(2)

# Keep this list deliberately focused on absolute claims identified in WORKFLOW.md.
patterns = [
    ("zero risk", re.compile(r"\bzero[- ]risk\b", re.I)),
    ("risk-free", re.compile(r"\brisk[- ]free\b", re.I)),
    ("guaranteed outcome", re.compile(r"\bguaranteed(?:\s+(?:win|wins|profit|profits|return|returns|success|value))?\b", re.I)),
    ("sure bet", re.compile(r"\bsure\s?bet\b", re.I)),
    ("never lose", re.compile(r"\bnever\s+lose\b", re.I)),
    ("easy money", re.compile(r"\beasy\s+money\b", re.I)),
    ("free money", re.compile(r"\bfree\s+money\b", re.I)),
    ("unverified audience figure", re.compile(r"\b100,000\+\b", re.I)),
    ("unsupported superlative", re.compile(r"\bmost.{0,70}\bof any SA\b", re.I)),
    ("unsupported superlative", re.compile(r"\bbest.{0,70}\bin SA\b", re.I)),
]

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)

# These contexts describe a risk or prohibit the claim rather than promote it.
safe_context = re.compile(
    r"\b(?:avoid(?: calling)?|do not|don't|does not|doesn't|cannot|can't|"
    r"should not|shouldn't|not|without|be cautious(?: about| with)?|"
    r"caution(?:ed)? about|warning against|claims? of|never describe|"
    r"never call|do not describe|should be avoided)\b.{0,100}"
    r"(?:zero[- ]risk|risk[- ]free|guaranteed|sure\s?bet|never\s+lose|"
    r"easy\s+money|free\s+money|100,000\+|most.{0,70}of any SA|best.{0,70}in SA)",
    re.I,
)

files = sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".html", ".md", ".json", ".astro"})
if not files:
    print(f"ERROR: no supported files found under {root}", file=sys.stderr)
    sys.exit(2)

findings = []
for path in files:
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: cannot read {path}: {exc}", file=sys.stderr)
        sys.exit(2)
    if path.suffix.lower() == ".html":
        parser = TextExtractor()
        parser.feed(raw)
        text = " ".join(parser.parts)
    else:
        text = raw
    # Sentence-level matching avoids scanning an entire generated one-line HTML file as one claim.
    sentences = re.split(r"(?<=[.!?])\s+|[\r\n]+", text)
    for sentence in sentences:
        if "claim-ok" in sentence.lower():
            continue
        for label, pattern in patterns:
            match = pattern.search(sentence)
            if match and not safe_context.search(sentence):
                excerpt = re.sub(r"\s+", " ", sentence).strip()
                if len(excerpt) > 220:
                    excerpt = excerpt[:217] + "..."
                findings.append((path, label, excerpt))
                break

if findings:
    for path, label, excerpt in findings:
        print(f"REVIEW REQUIRED [{label}] {path}: {excerpt}")
    print(f"FAILED: {len(findings)} potentially risky claim sentence(s). Rewrite promotional wording or append 'claim-ok' only after documented editorial review.", file=sys.stderr)
    sys.exit(1)

print(f"PASS: no unapproved high-risk promotional claims found across {len(files)} files.")
PY
