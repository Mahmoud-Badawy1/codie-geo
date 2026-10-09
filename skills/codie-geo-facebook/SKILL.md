---
name: codie-geo-facebook
description: Facebook relatable story posts as part of the Codie GEO unified agent.
---
# Facebook relatable story posts

**Invocation:** `/codie-geo facebook`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Build a conversational caption with audience relevance, practical hook, context, genuine CTA, restrained hashtags and visual idea.

## Required playbook
Read `platforms/facebook.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
