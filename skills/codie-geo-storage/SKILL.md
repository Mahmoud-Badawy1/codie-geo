---
name: codie-geo-storage
description: Persistent project and daily artifact delivery as part of the Codie GEO unified agent.
---
# Persistent project and daily artifact delivery

**Invocation:** `/codie-geo storage`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Respect existing Drive/Sheets or local hierarchy, date/week/day counting, content and references sheets, images subfolders and project history. Verify actual file writes; never invent remote links.

## Required playbook
Read `workflows/storage.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
