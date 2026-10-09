#!/usr/bin/env python3
"""Heuristic passage audit; NOT measured frequency of AI citations."""
import argparse,json,re,sys

def score(text):
    words=re.findall(r"[\w'-]+",text)
    n=len(words)
    clarity= int(bool(re.search(r'(?i)\b(is|are|means|defined|because|how|why|what|who)\b',text)))
    detail= int(bool(re.search(r'\d|%|\b(20\d\d|study|report|source|according to)\b',text,re.I)))
    readability=int(60<=n<=220)
    structured=int(bool(re.search(r'[:\n]\s*(?:[0-9]+[.)]|[-*] )',text)))
    raw=min(100,round(20+clarity*20+detail*25+readability*20+structured*15))
    return {'score_heuristic_0_to_100':raw,'word_count':n,'observations':{'answers_directly':bool(clarity),'specific_evidence_signals':bool(detail),'passage_length_reasonable':bool(readability),'structured_information':bool(structured)},'limits':'Readiness heuristic. It does not test whether any AI platform cited this content.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source',help='UTF-8 text file');a=p.parse_args()
 try:print(json.dumps(score(open(a.source,encoding='utf8').read()),indent=2))
 except Exception as e: print(e,file=sys.stderr);sys.exit(1)
