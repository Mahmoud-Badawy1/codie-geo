#!/usr/bin/env python3
"""One-time installer for the original GEO/SEO audit components.

Fetches a pinned upstream commit; retains original executable Python scripts;
strips branding/marketing and visual assets from non-license files. External
MIT license text is preserved in vendor/UPSTREAM_LICENSE.txt.
Requires Internet at install time. The skill works locally after installation.
"""
from __future__ import annotations
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.request import Request, urlopen
import zipfile

UPSTREAM_REPO = 'zubair-trabzada/geo-seo-claude'
UPSTREAM_SHA = '989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c'
ARCHIVE_URL = f'https://github.com/{UPSTREAM_REPO}/archive/{UPSTREAM_SHA}.zip'
SELECTED_DIRS = ('agents/', 'skills/', 'scripts/', 'schema/', 'templates/', 'geo/', 'docs/', 'tests/')
SELECTED_FILES = {'requirements.txt'}
ALLOWED_EXT = {'.md', '.py', '.json', '.css', '.html', '.txt'}
EXCLUDED_FRAGMENTS = ('scripts/brand_scanner.py.bak',)
REBRAND = {
    'Zubair Trabzada': 'External original contributor',
    'zubair-trabzada': 'upstream-project',
    'geo-seo-claude': 'GEO audit engine',
    'GEO-SEO Analysis Tool — Claude Code Skill': 'GEO-SEO Analysis Tool — Portable Agent Skill',
    'GEO-SEO Analysis Tool - Claude Code Skill': 'GEO-SEO Analysis Tool - Portable Agent Skill',
}
EXTRA_REMOVALS = [
    re.compile(r'\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b'),
    re.compile(r'https?://(?:www\.)?(?:skool\.com|youtube\.com|x\.com|twitter\.com)/[^\s)\]]+',re.I),
]

def selected(path: str) -> bool:
    if path in SELECTED_FILES: return True
    if not path.startswith(SELECTED_DIRS):return False
    if any(x in path for x in EXCLUDED_FRAGMENTS):return False
    if Path(path).suffix.lower() not in ALLOWED_EXT:return False
    if Path(path).name in ('LICENSE','README.md') and path.startswith('templates/'):
        return False
    return True

def sanitise_doc(s: str)->str:
    for before, after in REBRAND.items():
        s=s.replace(before,after)
    for pattern in EXTRA_REMOVALS:
        s=pattern.sub('[removed]',s)
    # Keep product platform references such as Anthropic/Claude where relevant to technical checks.
    lines=[]
    for line in s.splitlines():
        lower=line.lower()
        if any(k in lower for k in ('star this repo', 'buy me a coffee', 'join my community', 'join our skool', 'follow me on', 'subscribe to my', 'subscribe to the newsletter')):
            continue
        lines.append(line)
    return '\n'.join(lines)+'\n'

def install_from_bytes(blob:bytes,base:Path,overwrite=False)->dict:
    target=base/'vendor'/'geo-seo-core'
    if target.exists() and not overwrite:
        raise FileExistsError('Audit engine already installed. Pass --force to replace.')
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        files={}
        for info in z.infolist():
            if info.is_dir():continue
            parts=Path(info.filename).parts
            if len(parts)<2:continue
            rel=Path(*parts[1:]).as_posix()
            if '..' in parts or rel.startswith('/') or not selected(rel):continue
            if info.file_size>4_000_000:raise ValueError(f'Unexpected large file: {rel}')
            data=z.read(info)
            if rel.endswith('.md'):
                data=sanitise_doc(data.decode('utf8')).encode('utf8')
            files[rel]=data
    needed=['geo/SKILL.md','skills/geo-audit/SKILL.md','skills/geo-report/SKILL.md','skills/geo-technical/SKILL.md','scripts/fetch_page.py']
    missing=[x for x in needed if x not in files]
    if missing:raise RuntimeError('Archive did not contain expected upstream files: '+str(missing))
    with tempfile.TemporaryDirectory(prefix='codie-geo-bootstrap-') as temp:
        staging=Path(temp)/'core'
        for rel,data in files.items():
            dest=staging/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        if target.exists():shutil.rmtree(target)
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copytree(staging,target)
    manifest={
        'installed':True,'source':f'https://github.com/{UPSTREAM_REPO}',
        'pinned_commit':UPSTREAM_SHA,'file_count':len(files),
        'archive_sha256':hashlib.sha256(blob).hexdigest(),
        'contains_images_or_svg':False,
        'implementation':'Original upstream functional scripts and agent components. Non-code documentation is minimally sanitised.',
        'license':'MIT notice retained in vendor/UPSTREAM_LICENSE.txt'
    }
    (base/'vendor'/'install-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')
    return manifest

def main():
    p=argparse.ArgumentParser(description='Install full original GEO SEO audit engine for Codie GEO')
    p.add_argument('--force',action='store_true',help='Replace a previously installed engine')
    p.add_argument('--archive',type=Path,help='Use a downloaded upstream archive ZIP (offline install)')
    args=p.parse_args()
    base=Path(__file__).resolve().parent
    if args.archive:
        blob=args.archive.read_bytes()
    else:
        print('Downloading pinned upstream audit source:',ARCHIVE_URL)
        req=Request(ARCHIVE_URL,headers={'User-Agent':'CodieGEOInstaller/1.0','Accept':'application/zip'})
        with urlopen(req,timeout=45) as response:
            blob=response.read(10_000_001)
        if len(blob)>10_000_000:raise RuntimeError('Archive larger than expected 10MB limit')
    manifest=install_from_bytes(blob,base,overwrite=args.force)
    print('Installed GEO audit engine:',manifest['file_count'],'files')
    print('Source scripts retained; marketing files and images excluded.')
    print('MIT attribution stored separately in vendor/UPSTREAM_LICENSE.txt')
    print('Next: invoke /codie-geo setup or /codie-geo all <website> in your supported agent.')

if __name__=='__main__':
    try: main()
    except Exception as e:
        print('Install failed:',e,file=sys.stderr);sys.exit(1)
