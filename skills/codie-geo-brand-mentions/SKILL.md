---
name: codie-geo-brand-mentions
description: Third-party brand and entity signals for Codie GEO
---
# Third-party brand and entity signals

**Invocation under the unified agent:** `/codie-geo brand-mentions` (see root `commands.json` for aliases).

## Why it matters
This module is an independently addressable component of the unified audit. It feeds evidence and actionable findings into the one Codie GEO delivery pipeline.

## Inputs
Verified company name, aliases, products and relevant competitors.

## Process
Look for independently verifiable mentions in relevant publications, communities, repositories, product directories, reviews, LinkedIn, Reddit, video and knowledge pages. Record exact citations. Do not use invented counts or claim mention-to-visibility correlation as causation.

## Original upstream instructions
For exact upstream logic from the MIT-licensed reference implementation, check `vendor/geo-seo-core/skills/geo-brand-mentions/SKILL.md`. If present, use its original specialist steps with the safety and delivery requirements in Codie GEO's root `SKILL.md`. If absent, carry out the workflow documented above with available host tools and state the difference. Do not imply original scripts executed if they are not installed.

## Outputs
brand-presence.md, source-register.json

## Evidence rules
- Attach source URL and retrieval/publication date wherever available.
- Record coverage, confidence and any inaccessible pages.
- Never invent tests, tool results, traffic, rankings or citations.
- Transfer this module's findings to the audit report and then to research and publishing.

## Integration
This is a first-class local Codie GEO skill, available immediately without running an installer. Follow the steps above using tools actually available to the host; if optional original source exists, read `vendor/geo-seo-core/skills/geo-brand-mentions/SKILL.md` to expand the specialist assessment. Record executed versus unavailable checks. Hand structured results to the shared audit report and content pipeline.
