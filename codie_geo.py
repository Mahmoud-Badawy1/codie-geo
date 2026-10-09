#!/usr/bin/env python3
"""Resolve /codie-geo commands to first-class, locally installed Codie GEO skills.

The host assistant must read the returned SKILL.md and perform the work with
its own permitted tools. This helper does not fake an AI agent or browser.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
REG=json.loads((ROOT/'commands.json').read_text(encoding='utf-8'))

def route(tokens):
    args=list(tokens)
    if args and args[0] in ('/codie-geo','codie-geo'):args.pop(0)
    command=args[0].lower() if args else 'all'
    params=args[1:]
    if command.startswith(('https://','http://')):
        params=args
        command='all'
    elif command not in REG['audit_commands'] and command not in REG['workflow_commands']:
        params=args
        command='all'
    if command=='content' and not any(a.startswith(('https://','http://')) for a in params):
        command='create'
    if command in REG['audit_commands']:
        info=REG['audit_commands'][command]
        path=info['local_skill']
        vendor=info.get('upstream_skill')
        vendorp=f'vendor/geo-seo-core/skills/{vendor}/SKILL.md' if vendor else None
        return {'command':command,'path':path,'installed':(ROOT/path).is_file(),
                'source':'local-codie-geo', 'optional_upstream_path':vendorp,
                'upstream_available':bool(vendorp and (ROOT/vendorp).is_file()),
                'arguments':params}
    path=REG['workflow_commands'][command]
    return {'command':command,'path':path,'installed':(ROOT/path).is_file(),
            'source':'local-codie-geo','arguments':params}

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1] in ('--help','-h'):
        print((ROOT/'COMMANDS.md').read_text(encoding='utf-8'))
    else:
        print(json.dumps(route(sys.argv[1:]),indent=2))
