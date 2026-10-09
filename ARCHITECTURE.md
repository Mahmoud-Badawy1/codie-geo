# Codie GEO package map

**One agent:** `/codie-geo` and a shared pipeline. The full workflow is in `skills/codie-geo-all/SKILL.md`.

- `SKILL.md`, `orchestrator/SKILL.md`, `commands.json`, `codie_geo.py` — main entry and routing.
- `skills/codie-geo-audit/`, `...citability/`, `...crawlers/`, `...llmstxt/`, `...brand-mentions/`, `...platforms/`, `...schema/`, `...technical/`, `...content-audit/`, `...report/`, `...report-pdf/`, `...compare/`, `...proposal/`, `...prospect/`, `...update/` — 15 locally available specialist modules.
- `skills/codie-geo-onboarding/`, `...all/`, `...plan/`, `...research/`, `...create/`, `...social/`, `...qa/`, `...copy/`, `...hooks/`, `...visuals/`, `...repurpose/`, `...storage/`, `...instagram/`, `...linkedin/`, `...x/`, `...reddit/`, `...facebook/` — 17 saved editorial and operational workflow skills.
- `agents/codie-geo-*.md` — five specialist analyst instructions; run in parallel where supported.
- `scripts/`, `schema/`, `templates/` — local utilities, structured-data examples and report templates.
- `editorial/`, `platforms/`, `workflows/`, `planning/` — detailed full playbooks, reused rather than duplicated.
- `integrations/` — optional host-specific command wrappers.
- `vendor/UPSTREAM_LICENSE.txt` — retained MIT notice. `vendor/geo-seo-core/` is optional and not bundled; bootstrap can obtain original upstream supplemental source.

The official public command is always `/codie-geo`. The original third-party `geo-*` filenames are retained only **inside** the optional `vendor/geo-seo-core/` subtree for compatibility; never present them as Codie GEO commands or packaged local skills.
