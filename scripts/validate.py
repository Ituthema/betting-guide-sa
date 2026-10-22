#!/usr/bin/env python3
"""Basic build QA for metadata, direct-route output, and internal links."""
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import re, sys, os
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]/'dist'
SITE_URL=os.environ.get('SITE_URL','').strip().rstrip('/')
SITE_BASE_PATH=urlparse(SITE_URL).path.rstrip('/')
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.title=''; self.description=''; self.h1=0; self.links=[]; self._title=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='title': self._title=True
        if tag=='meta' and a.get('name','').lower()=='description': self.description=a.get('content','')
        if tag=='h1': self.h1+=1
        if tag in ('a','link','script'):
            u=a.get('href') or a.get('src')
            if u: self.links.append(u)
    def handle_endtag(self,tag):
        if tag=='title': self._title=False
    def handle_data(self,data):
        if self._title: self.title += data

def main():
    if not ROOT.exists(): print('Run scripts/build.py first.'); return 2
    files=sorted(ROOT.rglob('*.html')); errors=[]; titles=[]; descriptions=[]; routes=0
    for f in files:
        p=Parser(); p.feed(f.read_text())
        rel=f.relative_to(ROOT).as_posix()
        if not p.title.strip(): errors.append(f'{rel}: missing title')
        if not p.description.strip(): errors.append(f'{rel}: missing meta description')
        if p.h1 != 1: errors.append(f'{rel}: expected exactly one h1, found {p.h1}')
        titles.append(p.title.strip()); descriptions.append(p.description.strip())
        if f.name=='index.html': routes+=1
        for u in p.links:
            if u.startswith(('http://','https://','mailto:','tel:','#','data:')): continue
            # Root-absolute paths are valid for the documented root-origin deployment.
            if u.startswith('/'):
                if SITE_BASE_PATH:
                    errors.append(f'{rel}: root-absolute local target {u} bypasses configured site base path {SITE_BASE_PATH}/')
                target=ROOT/u.lstrip('/')
            else:
                target=(f.parent/u).resolve()
            if target.is_dir(): target=target/'index.html'
            if not target.exists(): errors.append(f'{rel}: missing local target {u}')
    for val,n in Counter(titles).items():
        if n>1: errors.append(f'duplicate title ({n}): {val}')
    for val,n in Counter(descriptions).items():
        if n>1: errors.append(f'duplicate meta description ({n}): {val}')
    if errors:
        print('\n'.join(errors)); print(f'FAILED: {len(errors)} issue(s) across {len(files)} HTML files'); return 1
    print(f'PASS: {len(files)} HTML documents; {routes} direct index routes; unique titles/descriptions; local links/assets resolve.')
    return 0
if __name__=='__main__': sys.exit(main())
