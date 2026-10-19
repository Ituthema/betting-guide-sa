#!/usr/bin/env python3
"""Build crawlable static pages from content/pages.json. Python standard library only."""
import json, os, re, html, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
SITE_URL = os.environ.get('SITE_URL', '').strip().rstrip('/')
PAGES = json.loads((ROOT/'content/pages.json').read_text())

def esc(s): return html.escape(str(s or ''), quote=True)
def route_path(slug): return slug if slug.endswith('/') else slug + '/'
def href(slug): return ('../' * 0) + route_path(slug) + 'index.html'
def rel_asset(current, name):
    cur = Path(current.strip('/'))
    base = ROOT/'dist'/cur
    return os.path.relpath(ROOT/'dist'/name, base).replace(os.sep, '/')

def rel_href(current, target):
    cur = Path(current.strip('/'))
    dest = Path(route_path(target).strip('/'))
    # from a page index.html in its directory
    rel = os.path.relpath((ROOT/'dist'/dest/'index.html'), (ROOT/'dist'/cur/'index.html').parent)
    return rel.replace(os.sep, '/')

records = list(PAGES)
records = list(PAGES)
# Content governance: never mark content verified without dated source evidence.
for r in records:
    if r.get('status') == 'verified' and (not r.get('lastVerified') or not r.get('sources')):
        raise SystemExit(f"Invalid verified record without date and sources: {r['slug']}")
    if r.get('status') == 'verified' and any(not x.get('url') for x in r.get('sources', [])):
        raise SystemExit(f"Invalid source URL in verified record: {r['slug']}")

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
shutil.copy2(ROOT/'assets/site.css', OUT/'site.css')
with (OUT/'site.css').open('a') as cssout: cssout.write('\n/* Static multi-page architecture additions */\n.editorial-note{padding:12px 0;background:var(--navy-3);border-bottom:1px solid var(--border);color:var(--muted);font-size:13px}.editorial-note strong{color:var(--gold)}.site-search{max-width:760px;margin-top:22px}.site-search label{display:block;margin-bottom:8px;color:var(--muted)}.search-row{display:flex;gap:10px;flex-wrap:wrap}.search-row input{flex:1;min-width:220px;padding:12px 14px;border:1px solid var(--border-l);border-radius:var(--r);background:var(--navy-2);color:var(--text);font:inherit}.search-result[hidden]{display:none!important}.h-nav{display:flex;align-items:center;gap:clamp(8px,1.6vw,20px);flex-wrap:wrap}.h-nav-link{font-family:var(--fh);font-size:12px;color:var(--text);white-space:nowrap}.h-nav-link:hover{color:var(--gold)}.hero{min-height:320px;background:radial-gradient(ellipse at 80% 20%,rgba(200,149,42,.15),transparent 50%),var(--navy-2)}.hero-content{padding-block:56px}.hero .sec-title{font-size:clamp(28px,4.5vw,44px);line-height:1.15;margin:12px 0}.article-body p{max-width:850px;margin-top:14px}.footer-grid h2{font:600 14px var(--fh);margin-bottom:10px;color:var(--gold)}.footer-grid p{margin:6px 0}.footer-grid a{color:var(--muted)}.footer-grid a:hover{color:var(--gold)}#age-bar{display:flex;justify-content:center;align-items:center;gap:14px;padding:7px 14px;background:var(--gold);color:#080f1e;font:600 11px var(--fh);letter-spacing:.4px}#age-bar button{border:0;background:transparent;color:inherit;font-size:18px;cursor:pointer}@media(max-width:760px){.h-inner{height:auto;min-height:60px;align-items:flex-start;flex-direction:column;padding-block:12px}.h-nav{gap:8px 14px}.h-nav-link{font-size:11px}.grid-3{grid-template-columns:1fr}.hero-content{padding:36px var(--g)}.footer-grid{grid-template-columns:1fr 1fr}}@media(max-width:420px){.footer-grid{grid-template-columns:1fr}.search-row input{min-width:0;width:100%}}\n')
shutil.copy2(ROOT/'assets/search.js', OUT/'search.js') if (ROOT/'assets/search.js').exists() else None
shutil.copy2(ROOT/'assets/site.js', OUT/'site.js') if (ROOT/'assets/site.js').exists() else None

def status_label(r):
    st=r.get('status','needs-verification')
    return {'verified':'Verified with sources','editorial-review':'Editorial review','legal-review-required':'Legal review required','needs-verification':'Needs verification'}.get(st,st.replace('-',' ').title())

def page_html(r):
    slug=r['slug']; title=r['title']; description=r['description']
    canonical = f'<link rel="canonical" href="{esc(SITE_URL+route_path(slug))}">' if SITE_URL else ''
    ogurl = f'<meta property="og:url" content="{esc(SITE_URL+route_path(slug))}">' if SITE_URL else ''
    body = []
    for sec in r.get('sections',[]):
        body.append(f'<section class="sec sec-alt"><div class="wrap article-body"><h2 class="sec-title">{esc(sec["heading"])}</h2><p>{esc(sec["body"])}</p></div></section>')
    related = [x for x in records if x['slug'] != slug and x['category'] in (r['category'], 'guide')][:6]
    cards=[]
    for x in related:
        dest=rel_href(slug,x['slug'])
        cards.append(f'<article class="pc"><div class="pc-body"><span class="tag tag-review">{esc(x["category"])}</span><a class="pc-title" href="{esc(dest)}">{esc(x["shortTitle"])}</a><p class="pc-excerpt">{esc(x["description"])}</p></div></article>')
    sections=''.join(body)
    related_html = f'<section class="sec"><div class="wrap"><h2 class="sec-title">Related <span>reading</span></h2><div class="grid-3">{"".join(cards)}</div></div></section>' if cards else ''
    sources = ''.join(f'<li><a href="{esc(s["url"])}" rel="noopener noreferrer">{esc(s.get("label") or s["url"])}</a> — checked {esc(s.get("checkedAt") or "date not recorded")}</li>' for s in r.get('sources',[]) if s.get('url'))
    source_html = f'<section class="sec"><div class="wrap"><h2 class="sec-title">Evidence <span>record</span></h2><p>Last verified: {esc(r.get("lastVerified") or "Not yet verified")}</p><ul>{sources}</ul></div></section>'
    search_url=rel_href(slug,'/search/')
    return f'''<!doctype html>
<html lang="en-ZA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | Betting Guide SA</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#080f1e"><meta property="og:type" content="website"><meta property="og:site_name" content="Betting Guide SA"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}">{ogurl}{canonical}<link rel="stylesheet" href="{esc(rel_asset(slug,'site.css'))}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet"><script defer src="{esc(rel_asset(slug,'site.js'))}"></script><script defer src="{esc(rel_asset(slug,'search.js'))}"></script></head>
<body><a class="skip-link" href="#main-content">Skip to main content</a><div id="age-bar" role="note"><span>18+ only. Gambling involves risk. Please play responsibly.</span><button type="button" id="age-close" aria-label="Dismiss age reminder">×</button></div>
<nav class="ticker" aria-label="Site categories"><div class="ticker-track"><a class="ti" href="{esc(rel_href(slug,'/bookmakers/'))}">Bookmaker reviews</a><a class="ti" href="{esc(rel_href(slug,'/promotions/'))}">Promotions</a><a class="ti" href="{esc(rel_href(slug,'/sports/'))}">Sports guides</a><a class="ti" href="{esc(rel_href(slug,'/casino/'))}">Casino guides</a></div></nav>
<header class="site-header"><div class="h-inner"><a class="logo" href="{esc(rel_href(slug,'/'))}" aria-label="Betting Guide SA home">BETTING<span>GUIDE</span><sub>SA</sub></a><nav class="h-nav" aria-label="Main navigation"><a class="h-nav-link" href="{esc(rel_href(slug,'/bookmakers/'))}">Bookmakers</a><a class="h-nav-link" href="{esc(rel_href(slug,'/promotions/'))}">Promotions</a><a class="h-nav-link" href="{esc(rel_href(slug,'/sports/'))}">Sports Guides</a><a class="h-nav-link" href="{esc(rel_href(slug,'/casino/'))}">Casino</a><a class="h-nav-link" href="{esc(rel_href(slug,'/guides/beginners/'))}">Beginners</a><a class="h-nav-link" href="{esc(search_url)}">Search</a></nav></div></header>
<div class="editorial-note"><div class="wrap"><strong>Editorial status:</strong> {esc(status_label(r))}. {('Commercial links may earn a commission; this does not determine editorial conclusions. ' if r['category'] in ('bookmaker','promotions') else '')}Current operator terms and legal status must be checked at source.</div></div>
<main id="main-content" tabindex="-1"><section class="hero"><div class="hero-content"><span class="tag tag-review">{esc(r['category'])}</span><h1 class="sec-title">{esc(title)}</h1><p class="hero-excerpt">{esc(r['intro'])}</p><div class="hero-meta"><span>18+ only</span><span>•</span><span>{esc(status_label(r))}</span></div></div></section><section class="sec"><div class="wrap"><p class="sec-desc">{esc(description)}</p></div></section>{sections}{source_html}{related_html}<section class="sec sec-dark"><div class="wrap"><h2 class="sec-title">Search the <span>site</span></h2><form class="site-search" role="search" action="{esc(search_url)}"><label for="site-search-input">Find a guide or review</label><div class="search-row"><input id="site-search-input" name="q" type="search" placeholder="Search bookmakers, sports, casino…"><button class="btn btn-gold" type="submit">Search</button></div></form></div></section></main>
<footer role="contentinfo"><div class="footer-top"><div class="wrap footer-grid"><div><div class="fc-logo">BETTING<span>GUIDE</span> SA</div><p class="fc-desc">Informational guides to bookmaker terms, sports markets and casino mechanics. Content is not a guarantee of outcomes.</p></div><div><h2>Explore</h2><p><a href="{esc(rel_href(slug,'/bookmakers/'))}">Bookmaker reviews</a></p><p><a href="{esc(rel_href(slug,'/promotions/'))}">Promotions</a></p><p><a href="{esc(rel_href(slug,'/sports/'))}">Sports guides</a></p></div><div><h2>Learn</h2><p><a href="{esc(rel_href(slug,'/guides/odds/'))}">Betting odds</a></p><p><a href="{esc(rel_href(slug,'/guides/bankroll/'))}">Risk management</a></p><p><a href="{esc(rel_href(slug,'/guides/responsible-gambling/'))}">Responsible gambling</a></p></div><div><h2>Information</h2><p><a href="{esc(rel_href(slug,'/about/'))}">About</a></p><p><a href="{esc(rel_href(slug,'/affiliate-disclosure/'))}">Affiliate disclosure</a></p><p><a href="{esc(rel_href(slug,'/legal/privacy/'))}">Privacy</a></p><p><a href="{esc(rel_href(slug,'/legal/terms/'))}">Terms</a></p></div></div></div><div class="footer-rg"><div class="wrap"><strong>18+ | Gamble responsibly</strong><span>Never gamble with money you cannot afford to lose.</span></div></div><div class="footer-copy">© Betting Guide SA. Review all operator terms at the source before acting.</div></footer></body></html>'''

# Main routes and content pages.
for r in records:
    outpath=OUT/route_path(r['slug']).strip('/')/'index.html'
    if r['slug']=='/': outpath=OUT/'index.html'
    outpath.parent.mkdir(parents=True,exist_ok=True)
    outpath.write_text(page_html(r))

# Search page has server-rendered, crawlable page list; JS adds live filtering.
search_record={'slug':'/search/','title':'Search Betting Guide SA','shortTitle':'Search','category':'search','description':'Search bookmaker reviews, promotions, sports guides and casino explainers.','intro':'Search indexed pages by title, topic or description. Search results link to independent, crawlable URLs.','sections':[{'heading':'Search all content','body':'Enter a term such as bookmaker, soccer, casino, bonus terms or bankroll management. Results are generated from the site content index.'}],'status':'editorial-review','lastVerified':None,'sources':[]}
records.append(search_record)
search_dir=OUT/'search'; search_dir.mkdir(exist_ok=True)
# overwrite the search route with dedicated UI and static links as a no-JS fallback
cards=[]
for r in records:
    if r['slug']=='/search/': continue
    cards.append(f'<article class="pc search-result" data-search-text="{esc((r["title"]+" "+r["description"]+" "+r["category"]).lower())}"><div class="pc-body"><span class="tag tag-review">{esc(r["category"])}</span><a class="pc-title" href="{esc(os.path.relpath(OUT/route_path(r["slug"]).strip("/")/"index.html", search_dir).replace(os.sep,"/"))}">{esc(r["title"])}</a><p class="pc-excerpt">{esc(r["description"])}</p></div></article>')
search_html=f'''<!doctype html><html lang="en-ZA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Search Betting Guide SA</title><meta name="description" content="Search bookmaker reviews, promotions, sports guides and casino explainers."><meta name="theme-color" content="#080f1e"><link rel="stylesheet" href="../site.css"><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,60;0,60;0,60;1,60&display=swap" rel="stylesheet"><script defer src="../site.js"></script><script defer src="../search.js"></script></head><body><a class="skip-link" href="#main-content">Skip to main content</a><header class="site-header"><div class="h-inner"><a class="logo" href="../">BETTING<span>GUIDE</span><sub>SA</sub></a><nav class="h-nav"><a class="h-nav-link" href="../bookmakers/">Bookmakers</a><a class="h-nav-link" href="../promotions/">Promotions</a><a class="h-nav-link" href="../sports/">Sports</a><a class="h-nav-link" href="../casino/">Casino</a></nav></div></header><main id="main-content"><section class="hero"><div class="hero-content"><h1 class="sec-title">Search <span>the site</span></h1><p class="hero-excerpt">Find a bookmaker review, promotion explainer, sport guide or casino article.</p><form class="site-search" role="search" id="search-form"><label for="site-search-input">Search pages</label><div class="search-row"><input id="site-search-input" name="q" type="search" placeholder="Try “soccer” or “withdrawal terms”"><button class="btn btn-gold" type="submit">Search</button></div></form><p id="search-status" aria-live="polite">All pages are listed below.</p></div></section><section class="sec"><div class="wrap"><div class="grid-3" id="search-results">{"".join(cards)}</div></div></section></main><footer class="footer-copy">18+ only · Gamble responsibly · Content requires source verification where indicated.</footer></body></html>'''
(OUT/'search'/'index.html').write_text(search_html)

# Index and sitemap generation.
(OUT/'search-index.json').write_text(json.dumps([{'title':r['title'],'description':r['description'],'category':r['category'],'url':route_path(r['slug'])} for r in records if r['slug']!='/search/'],ensure_ascii=False,indent=2))
if SITE_URL:
    urls=''.join(f'<url><loc>{esc(SITE_URL+route_path(r["slug"]))}</loc></url>' for r in records)
    (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>')
    (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+SITE_URL+'/sitemap.xml\n')
else:
    (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\n# Set SITE_URL and rebuild to generate an absolute sitemap URL.\n')
(OUT/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n')
(OUT/'404.html').write_text('<!doctype html><html lang="en-ZA"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found | Betting Guide SA</title><meta name="description" content="The requested page could not be found. Browse bookmaker reviews, promotions, sports guides and casino explainers."><link rel="stylesheet" href="/site.css"><main class="sec"><div class="wrap"><h1 class="sec-title">Page <span>not found</span></h1><p>The page may have moved. Browse the main categories instead.</p><p><a href="/">Home</a> · <a href="/bookmakers/">Bookmakers</a> · <a href="/promotions/">Promotions</a> · <a href="/sports/">Sports guides</a> · <a href="/casino/">Casino</a></p></div></main></html>')
print(f'Built {len(records)} content pages into {OUT}; SITE_URL={SITE_URL or "not configured"}')
