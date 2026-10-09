---
name: codie-geo-platforms
description: Platform-specific visibility readiness for Codie GEO
---
# Platform-specific visibility readiness

**Invocation under the unified agent:** `/codie-geo platform-optimizer` (see root `commands.json` for aliases).

## Why it matters
This module is an independently addressable component of the unified audit. It feeds evidence and actionable findings into the one Codie GEO delivery pipeline.

## Inputs
Pages, brand/entity facts, target user prompts.

## Process
Assess factors relevant to ChatGPT, Perplexity, Gemini and Google AI surfaces without pretending to query hidden rankings. If real citation tests are available, preserve prompts, timestamps and results; otherwise provide readiness recommendations marked as inferred.

## Original upstream instructions
For exact upstream logic from the MIT-licensed reference implementation, check `vendor/geo-seo-core/skills/geo-platform-optimizer/SKILL.md`. If present, use its original specialist steps with the safety and delivery requirements in Codie GEO's root `SKILL.md`. If absent, carry out the workflow documented above with available host tools and state the difference. Do not imply original scripts executed if they are not installed.

## Outputs
platform-analysis.md, query-test-plan.json

## Evidence rules
- Attach source URL and retrieval/publication date wherever available.
- Record coverage, confidence and any inaccessible pages.
- Never invent tests, tool results, traffic, rankings or citations.
- Transfer this module's findings to the audit report and then to research and publishing.

## Integration
This is a first-class local Codie GEO skill, available immediately without running an installer. Follow the steps above using tools actually available to the host; if optional original source exists, read `vendor/geo-seo-core/skills/geo-platform-optimizer/SKILL.md` to expand the specialist assessment. Record executed versus unavailable checks. Hand structured results to the shared audit report and content pipeline.
