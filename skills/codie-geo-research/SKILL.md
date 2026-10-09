---
name: codie-geo-research
description: Fresh topic research and SEO/AEO/GEO briefs as part of the Codie GEO unified agent.
---
# Fresh topic research and SEO/AEO/GEO briefs

**Invocation:** `/codie-geo research`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Review earlier topic logs/day folders to prevent repeats; validate current trend signals, search intent, competing pages, sources with dates, article angles, visuals, keywords and brand relevance. Do not write the full article for research-only requests.

## Required playbook
Read `workflows/research.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
