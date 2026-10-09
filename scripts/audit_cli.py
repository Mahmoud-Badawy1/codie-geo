#!/usr/bin/env python3
"""Lightweight local command runner. Complex research is agent-executed."""
import argparse,json,sys,urllib.parse
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from fetch_page import scan
from score_audit import compute
from citability_scorer import score as passage_score

def run(cmd,url):
 import requests
 if cmd in ('quick','technical','schema','content','page'):
  data=scan(url)
  if cmd=='schema':return {'page':url,'json_ld':data['json_ld'],'note':'Site data extracted, verify against visible details and Schema.org rules.'}
  if cmd=='technical':return {k:data[k] for k in ('input_url','http_status','title','meta_description','meta_robots','canonical','headings','images_missing_alt','internal_links','response_ms','note')}
  return data
 if cmd=='crawlers':
  u=urllib.parse.urlsplit(url);robots=f'{u.scheme}://{u.netloc}/robots.txt';r=requests.get(robots,timeout=15,headers={'User-Agent':'CodieGEO/4.0 (robots audit)'})
  return {'robots_url':robots,'status':r.status_code,'robots_txt':r.text[:20000],'warning':'Review user-agent-specific precedence; this file alone does not prove effective crawler reachability.'}
 if cmd=='llmstxt':
  u=urllib.parse.urlsplit(url);target=f'{u.scheme}://{u.netloc}/llms.txt';r=requests.get(target,timeout=15)
  return {'url':target,'status':r.status_code,'content':r.text[:12000] if r.status_code==200 else None,'note':'llms.txt is optional, not a guaranteed search optimization.'}
 if cmd=='citability':
  import bs4
  r=requests.get(url,timeout=15);s=bs4.BeautifulSoup(r.text,'html.parser')
  for node in s(['script','style','nav','footer']):node.decompose()
  return {'url':url,**passage_score(s.get_text(' ',strip=True)[:15000]),'limitation':'Score is applied to text excerpt; inspect passage-level content manually.'}
 raise ValueError('This command requires an AI agent with live search and/or prior audit context. See SKILL.md: '+cmd)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('command',choices=['quick','technical','schema','content','page','crawlers','llmstxt','citability']);p.add_argument('url');p.add_argument('-o','--output');a=p.parse_args()
 try:
  result=run(a.command,a.url);body=json.dumps(result,indent=2,ensure_ascii=False)
  if a.output:Path(a.output).write_text(body+'\n',encoding='utf8');print(a.output)
  else:print(body)
 except Exception as e:print('ERROR:',e,file=sys.stderr);sys.exit(1)
