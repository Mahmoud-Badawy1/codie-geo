---
name: codie-geo-plan
description: Prioritized improvement strategy as part of the Codie GEO unified agent.
---
# Prioritized improvement strategy

**Invocation:** `/codie-geo plan`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Convert actual audit findings into evidence-linked quick wins and a 30/60/90-day roadmap. Include impact, effort, source, confidence, owner, dependencies and how to verify results.

## Required playbook
Read `planning/optimization.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
