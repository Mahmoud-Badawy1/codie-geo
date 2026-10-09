#!/usr/bin/env python3
"""Generate optional llms.txt proposal from verified site entries."""
import argparse,json,urllib.parse,sys

def generate(site_name,home,desc,pages):
 if urllib.parse.urlsplit(home).scheme not in ('http','https'):raise ValueError('Homepage must be https URL')
 lines=[f'# {site_name}', '',f'> {desc}', '', '## Important pages', '']
 for p in pages:
  url=p['url'];title=p['title'];note=p.get('description','')
  if urllib.parse.urlsplit(url).scheme not in ('http','https'):continue
  lines.append(f'- [{title}]({url})'+(f': {note}' if note else ''))
 lines += ['','<!-- Optional proposed convention, not an official search ranking signal. -->','']
 return '\n'.join(lines)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input',help='JSON: name,url,description,pages');p.add_argument('-o','--output',default='llms.txt');a=p.parse_args()
 try:
  d=json.load(open(a.input,encoding='utf8'));open(a.output,'w',encoding='utf8').write(generate(d['name'],d['url'],d['description'],d['pages']));print(a.output)
 except Exception as e:print(e,file=sys.stderr);sys.exit(1)
