---
name: codie-geo-content-audit
description: Existing content quality and E-E-A-T signals for Codie GEO
---
# Existing content quality and E-E-A-T signals

**Invocation under the unified agent:** `/codie-geo content` (see root `commands.json` for aliases).

## Why it matters
This module is an independently addressable component of the unified audit. It feeds evidence and actionable findings into the one Codie GEO delivery pipeline.

## Inputs
Representative article, service, product and about pages.

## Process
Review accuracy, first-hand expertise signals, audience fit, information gain, factual support, revision dates, author evidence, semantic structure and answer completeness. Use E-E-A-T as qualitative assessment, not an officially measured ranking metric. Advise clear copy and original examples.

## Original upstream instructions
For exact upstream logic from the MIT-licensed reference implementation, check `vendor/geo-seo-core/skills/geo-content/SKILL.md`. If present, use its original specialist steps with the safety and delivery requirements in Codie GEO's root `SKILL.md`. If absent, carry out the workflow documented above with available host tools and state the difference. Do not imply original scripts executed if they are not installed.

## Outputs
content-audit.md, editorial-backlog.csv

## Evidence rules
- Attach source URL and retrieval/publication date wherever available.
- Record coverage, confidence and any inaccessible pages.
- Never invent tests, tool results, traffic, rankings or citations.
- Transfer this module's findings to the audit report and then to research and publishing.

## Integration
This is a first-class local Codie GEO skill, available immediately without running an installer. Follow the steps above using tools actually available to the host; if optional original source exists, read `vendor/geo-seo-core/skills/geo-content/SKILL.md` to expand the specialist assessment. Record executed versus unavailable checks. Hand structured results to the shared audit report and content pipeline.
