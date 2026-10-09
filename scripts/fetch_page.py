#!/usr/bin/env python3
"""Live, read-only public page scan. Run `python scripts/fetch_page.py URL`."""
import argparse, json, re, sys
from urllib.parse import urljoin, urlsplit

def scan(url, timeout=15):
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError as e:
        raise SystemExit('Install dependencies: pip install -r requirements.txt') from e
    if urlsplit(url).scheme not in ('http','https') or not urlsplit(url).hostname:
        raise ValueError('Use a full http(s) URL')
    r=requests.get(url,timeout=timeout,headers={'User-Agent':'CodieGEO/4.0 (public-site-audit)'},allow_redirects=True)
    s=BeautifulSoup(r.text[:2_000_000],'html.parser')
    def meta(key,attr='name'):
        x=s.find('meta',attrs={attr:key});return x.get('content') if x else None
    canonical=s.find('link',rel=lambda v: v and 'canonical' in v)
    title=s.find('title')
    ld=[]
    for elem in s.find_all('script',type='application/ld+json'):
        try:ld.append(json.loads(elem.string or elem.get_text()))
        except json.JSONDecodeError:ld.append({'invalid_json_ld':True})
    heading={f'h{i}':[e.get_text(' ',strip=True) for e in s.find_all(f'h{i}')] for i in range(1,7)}
    imgs=s.find_all('img')
    hrefs=[urljoin(r.url,a['href']) for a in s.find_all('a',href=True) if a['href'].startswith(('/','http'))]
    internal=sum(urlsplit(h).hostname==urlsplit(r.url).hostname for h in hrefs)
    external=len(hrefs)-internal
    robots=meta('robots')
    return {'input_url':url,'final_url':r.url,'http_status':r.status_code,'title':title.get_text(' ',strip=True) if title else None,
      'meta_description':meta('description'),'meta_robots':robots,'canonical':canonical.get('href') if canonical else None,
      'headings':heading,'images':len(imgs),'images_missing_alt':sum(not (e.get('alt') or '').strip() for e in imgs),
      'internal_links':internal,'external_links':external,'json_ld':ld,'og_title':meta('og:title','property'),
      'html_lang':s.html.get('lang') if s.html else None,'text_word_count':len(s.get_text(' ',strip=True).split()),
      'response_ms':int(r.elapsed.total_seconds()*1000),'note':'Response time is not a Core Web Vitals measurement.'}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('--output');a=p.parse_args()
 try:
  result=scan(a.url);data=json.dumps(result,indent=2,ensure_ascii=False)
  if a.output:open(a.output,'w',encoding='utf8').write(data+'\n')
  else:print(data)
 except Exception as e:print(f'ERROR: {e}',file=sys.stderr);sys.exit(1)
