# Codie GEO command dispatcher

**Only user-facing command prefix: `/codie-geo`.** The complete command table lives in `commands.json`.

1. No arguments, a bare website URL, or `all` -> `workflows/unified-all.md`. Do onboarding if no project profile exists.
2. Audit actions (`audit`, `quick`, `page`, `citability`, `crawlers`, `llmstxt`, `brands`, `platforms`, `schema`, `technical`, `content-audit`, `report`, `report-pdf`, `compare`, `proposal`, `prospect`) -> read `skills/codie-geo-<action>/SKILL.md` using `commands.json` mappings. `quick` and `page` use `codie-geo-audit`. If vendor original files are present, consult those as additional specialist source material.
3. Editorial actions (`plan`, `research`, `create`, `social`, social-network-specific, `qa`) -> use local workflows and handoff artifacts from preceding stages.
4. `/codie-geo content <url>` -> audit existing page quality; `/codie-geo content` without URL -> write from latest approved brief. `/codie-geo create` always writes.
5. `report` runs on an actual prior audit, or audits a supplied URL first. PDF requires actual local PDF capability.
6. Be explicit about unavailable tools: inaccessible sites, Google Search Console, AI-platform search, timing metrics or local file output. Do not pretend scripts or parallel agents executed.

For a standalone local first-pass test, run `python scripts/audit_cli.py quick https://example.com`, `technical`, `schema`, `content`, `crawlers`, `llmstxt` or `citability`. More complex brand/platform research requires a connected AI agent with search access.

### Evidence shape

`finding_id`, `page_url`, `dimension`, `observed_fact`, `tool_or_source`, `captured_at`, `confidence`, `severity`, `recommended_action`, `verification_step`, `status`. Keep unknowns and blocked checks distinct from failures.
