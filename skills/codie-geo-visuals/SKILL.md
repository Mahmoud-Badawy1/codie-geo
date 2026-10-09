---
name: codie-geo-visuals
description: Professional image concepts and reference search as part of the Codie GEO unified agent.
---
# Professional image concepts and reference search

**Invocation:** `/codie-geo visuals`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Produce visual concepts, practical art direction, stock/portfolio search keywords in 12 layers, platform search queries, exclusion terms and asset licensing reminders. Do not include unlicensed third-party imagery.

## Required playbook
Read `editorial/visual-search.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
