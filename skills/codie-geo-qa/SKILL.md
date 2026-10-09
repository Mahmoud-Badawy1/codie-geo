---
name: codie-geo-qa
description: Content and publication readiness as part of the Codie GEO unified agent.
---
# Content and publication readiness

**Invocation:** `/codie-geo qa`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Check facts, source links, coverage, structure, on-brand voice, SEO metadata, AEO questions, dates, visuals/license, Arabic tatweel, each requested social channel, and delivery manifest. Fix editorial issues and record pending approvals.

## Required playbook
Read `workflows/qa.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
