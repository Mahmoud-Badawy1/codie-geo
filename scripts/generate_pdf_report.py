#!/usr/bin/env python3
"""Create an evidence-based Codie GEO PDF report with score bars and priorities."""
import json,argparse,sys
from pathlib import Path

def build(data,out):
 try:
  from reportlab.pdfgen import canvas
  from reportlab.lib.pagesizes import A4
  from reportlab.lib.colors import HexColor,white
 except ImportError as e:raise SystemExit('Install reportlab: pip install -r requirements.txt') from e
 W,H=A4;left=46;right=W-46;y=H-48
 c=canvas.Canvas(str(out),pagesize=A4);c.setTitle('Codie GEO SEO and AI search audit')
 navy=HexColor('#183739');muted=HexColor('#526573');teal=HexColor('#2a7372');pale=HexColor('#dceceb');light=HexColor('#eef4f5')
 def page():
  nonlocal y
  c.setFillColor(navy);c.rect(0,H-14,W,14,fill=1,stroke=0)
  c.setFillColor(muted);c.setFont('Helvetica',8);c.drawString(left,24,'CODIE GEO  |  Evidence-based website visibility assessment')
  c.drawRightString(right,24,str(c.getPageNumber()))
  c.setFillColor(navy);y=H-48
 def ensure(height=50):
  nonlocal y
  if y-height < 55:c.showPage();page()
 def text(msg,size=10,bold=False,gap=7):
  nonlocal y
  text_=str(msg).replace('\n',' ')
  max_chars=85 if size>=10 else 100
  for st in range(0,len(text_) or 1,max_chars):
   ensure(size+gap);c.setFillColor(navy if bold else muted);c.setFont('Helvetica-Bold' if bold else 'Helvetica',size)
   c.drawString(left,y,text_[st:st+max_chars]);y-=size+gap
 def heading(label):
  nonlocal y
  ensure(56);y-=6;text(label,14,True,10)
 def bar(label,val,weight):
  nonlocal y
  ensure(43)
  c.setFont('Helvetica',9);c.setFillColor(navy);c.drawString(left,y,label)
  c.drawRightString(right,y,('unknown' if val is None else f'{val:.0f}/100')+f'  [{weight:.0%}]')
  y-=16
  width=right-left;c.setFillColor(light);c.roundRect(left,y-5,width,10,4,fill=1,stroke=0)
  if val is not None:c.setFillColor(teal);c.roundRect(left,y-5,max(2,width*val/100),10,4,fill=1,stroke=0)
  y-=21
 page()
 text('CODIE GEO',20,True,4);text('SEO + AI Search Readiness Report',14,True,16)
 text('Website: '+str(data.get('url','not supplied')))
 text('Checked: '+str(data.get('date','not supplied')))
 text('Coverage: '+str(data.get('scope','not supplied')))
 text('Status: '+str(data.get('evidence_status','partial')))
 heading('Executive overview')
 text(data.get('summary','This report summarizes observed SEO and AI search readiness. Unverified checks must be completed before making definitive claims.'))
 sc=data.get('score',{});val=sc.get('score') if isinstance(sc,dict) else None
 heading('Weighted readiness score')
 text(str(val)+'/100' if val is not None else 'Incomplete - evidence missing',17,True)
 categories=[('AI citability and visibility','citability_visibility',.25),('Brand authority signals','brand_authority',.20),('Content quality and E-E-A-T','content_eeat',.20),('Technical foundations','technical',.15),('Structured data','structured_data',.10),('Platform optimization','platform_optimization',.10)]
 for label,key,weight in categories:
  v=data.get('subscores',{}).get(key)
  if isinstance(v,(int,float)) and 0<=v<=100:bar(label,float(v),weight)
  else:bar(label,None,weight)
 heading('Prioritized findings')
 findings=data.get('findings',[])
 if not findings:text('No documented findings were provided. This does not mean all checks passed.')
 for f in findings[:40]:
  ensure(75);text(str(f.get('priority','CHECK'))+'  '+str(f.get('title','Unnamed issue')),10,True)
  text('Observed: '+str(f.get('observed','Not supplied')),9)
  text('Action: '+str(f.get('recommendation','Verify and plan')),9)
  text('Evidence: '+str(f.get('evidence_url','Not supplied')),8)
 heading('Sources and verification notes')
 for s in data.get('sources',[]):text(str(s),8)
 text('Scores are internal planning heuristics, not direct AI citation measurements.',8)
 c.save();return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('report_json');p.add_argument('output_pdf');a=p.parse_args()
 try:d=json.loads(Path(a.report_json).read_text(encoding='utf8'));build(d,Path(a.output_pdf));print('PDF saved:',a.output_pdf)
 except Exception as e:print(e,file=sys.stderr);sys.exit(1)
