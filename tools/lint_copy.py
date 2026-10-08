#!/usr/bin/env python3
"""Static copy review for text/Markdown/HTML files; no third-party deps.
Checks high-signal style issues only; does not assess whether content is human-written.
"""
from pathlib import Path
import argparse
import re
import sys

EXTS = {'.md', '.txt', '.html', '.htm', '.csv'}
BAD_CLICHES = [
    'in today\'s fast-paced world', 'in today’s fast-paced world',
    'unlock the power of', 'in an ever-evolving landscape',
    'dive into the world of', 'game-changing solution',
]


def review_text(text):
    warnings = []
    for idx, line in enumerate(text.splitlines(), 1):
        if chr(0x640) in line:
            warnings.append((idx, 'Arabic tatweel U+0640 found; remove ornamental stretching'))
        if re.search(r'[—–]{3,}|[-=]{7,}', line) and not re.fullmatch(r'\s*[-=]{3,}\s*', line):
            warnings.append((idx, 'Decorative repeated dash/line in copy'))
        if line.count('—') >= 2:
            warnings.append((idx, 'Multiple em dashes; simplify punctuation where practical'))
        for cliché in BAD_CLICHES:
            if cliché in line.lower():
                warnings.append((idx, f'Generic opening/phrase: {cliché}'))
    return warnings


def main():
    p = argparse.ArgumentParser(description='Check final copy for tatweel and generic punctuation/filler')
    p.add_argument('path', type=Path, help='Text file or folder containing final content')
    args = p.parse_args()
    paths = ([args.path] if args.path.is_file() else
             sorted(f for f in args.path.rglob('*') if f.suffix.lower() in EXTS and f.is_file())) if args.path.exists() else []
    if not paths:
        print('No supported text files found', file=sys.stderr)
        return 2
    total = 0
    for file in paths:
        try:
            content = file.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as e:
            print(f'{file}: Could not read: {e}', file=sys.stderr)
            return 2
        warns = review_text(content)
        total += len(warns)
        for line, msg in warns:
            print(f'{file}:{line}: {msg}')
    print(f'Reviewed {len(paths)} files, {total} style warning(s).')
    return 1 if total else 0

if __name__ == '__main__':
    raise SystemExit(main())
