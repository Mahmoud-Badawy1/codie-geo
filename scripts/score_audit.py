#!/usr/bin/env python3
"""Compute documented Codie GEO heuristic weighted score."""
import sys,json,argparse
WEIGHTS={'citability_visibility':0.25,'brand_authority':0.20,'content_eeat':0.20,'technical':0.15,'structured_data':0.10,'platform_optimization':0.10}
def compute(scores):
 missing=[name for name in WEIGHTS if scores.get(name) is None]
 if missing:return {'score':None,'status':'incomplete','missing':missing,'weights':WEIGHTS,'warning':'Do not treat missing measures as zero or assume a complete score.'}
 for k in WEIGHTS:
  if not isinstance(scores[k],(int,float)) or not 0<=scores[k]<=100:raise ValueError(f'Invalid 0-100 score: {k}')
 return {'score':round(sum(scores[k]*w for k,w in WEIGHTS.items()),1),'status':'complete_heuristic','weights':WEIGHTS,'warning':'Score is a proprietary readiness heuristic, not an AI platform visibility or citation measurement.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('json_file');a=p.parse_args()
 try:print(json.dumps(compute(json.load(open(a.json_file,encoding='utf8'))),indent=2))
 except Exception as e:print(e,file=sys.stderr);sys.exit(1)
