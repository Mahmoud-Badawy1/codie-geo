#!/usr/bin/env python3
"""Prepare repeatable, verifiable brand research queries without inventing mentions."""
import argparse,json,urllib.parse
PLATFORMS=['reddit.com','linkedin.com','youtube.com','wikipedia.org','github.com','medium.com','producthunt.com','stackoverflow.com','g2.com','trustpilot.com']
def queries(brand):
 return [{'platform':domain,'query':f'site:{domain} "{brand}"','search_url':'https://www.google.com/search?q='+urllib.parse.quote(f'site:{domain} "{brand}"'),'finding':'unverified; requires browsing'} for domain in PLATFORMS]
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('brand');a=p.parse_args();print(json.dumps({'brand':a.brand,'queries':queries(a.brand),'warning':'This script plans searches; it does not verify brand mentions.'},indent=2))
