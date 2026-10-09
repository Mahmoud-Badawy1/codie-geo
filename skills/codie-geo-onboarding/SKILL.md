---
name: codie-geo-onboarding
description: Project setup and reusable profile as part of the Codie GEO unified agent.
---
# Project setup and reusable profile

**Invocation:** `/codie-geo setup`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Collect project identity, URL, region, audience, voice, languages, content goals, channels, approval gates, and output storage once. Save/reuse a profile; proceed automatically into the complete pipeline when invoked via /codie-geo.

## Required playbook
Read `workflows/onboarding.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
