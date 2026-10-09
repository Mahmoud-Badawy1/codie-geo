---
name: codie-geo-report-pdf
description: Visual PDF report creation for Codie GEO
---
# Visual PDF report creation

**Invocation under the unified agent:** `/codie-geo report-pdf` (see root `commands.json` for aliases).

## Why it matters
This module is an independently addressable component of the unified audit. It feeds evidence and actionable findings into the one Codie GEO delivery pipeline.

## Inputs
Valid report JSON or Markdown with dated evidence.

## Process
Render clean report with source list, score bars, issue severity, priorities, and assumptions; use scripts/generate_pdf_report.py. Ensure PDF opens, pages are not clipped, and all scores correspond to the audit JSON. PDF generation needs reportlab.

## Original upstream instructions
For exact upstream logic from the MIT-licensed reference implementation, check `vendor/geo-seo-core/skills/geo-report-pdf/SKILL.md`. If present, use its original specialist steps with the safety and delivery requirements in Codie GEO's root `SKILL.md`. If absent, carry out the workflow documented above with available host tools and state the difference. Do not imply original scripts executed if they are not installed.

## Outputs
GEO-AUDIT-REPORT.pdf

## Evidence rules
- Attach source URL and retrieval/publication date wherever available.
- Record coverage, confidence and any inaccessible pages.
- Never invent tests, tool results, traffic, rankings or citations.
- Transfer this module's findings to the audit report and then to research and publishing.

## Integration
This is a first-class local Codie GEO skill, available immediately without running an installer. Follow the steps above using tools actually available to the host; if optional original source exists, read `vendor/geo-seo-core/skills/geo-report-pdf/SKILL.md` to expand the specialist assessment. Record executed versus unavailable checks. Hand structured results to the shared audit report and content pipeline.
