---
name: codie-geo-social
description: Five-platform social publishing package as part of the Codie GEO unified agent.
---
# Five-platform social publishing package

**Invocation:** `/codie-geo social`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Default to Instagram, LinkedIn, X, Reddit, Facebook unless user chooses channels. Each needs native copy, creative hook, CTA, relevant hashtags where appropriate, and visual direction; Reddit posts should avoid pasted promotional hashtags.

## Required playbook
Read `workflows/social.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
