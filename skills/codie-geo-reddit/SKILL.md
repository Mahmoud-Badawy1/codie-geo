---
name: codie-geo-reddit
description: Reddit community-first discussion as part of the Codie GEO unified agent.
---
# Reddit community-first discussion

**Invocation:** `/codie-geo reddit`. This skill is part of the parent `/codie-geo` agent and can also run as a stage in its automatic end-to-end workflow.

## What to deliver
Choose an appropriate community only if verified, provide genuine non-spammy discussion, disclose affiliations, follow subreddit rules, keep hashtags out of post text and never fabricate community engagement.

## Required playbook
Read `platforms/reddit.md` from the package root and execute its detailed procedure. Use the project profile, previously verified evidence and stage outputs rather than starting over. Refer to `SKILL.md` for user permission, uncertainty, source, and writing rules.

## Result and handoff
Write the requested output to the configured destination when available, or return it in chat. Mark `complete`, `limited`, `blocked`, or `approval-required` accurately and pass the relevant findings to the next Codie GEO stage. Never claim remote saves, searches, generated files or performance metrics without performing them.
