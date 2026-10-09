# Codie GEO custom agent instruction

Read `codie-orchestrator/SKILL.md` and honor its slash commands. `/codie-geo` executes the full pipeline: profile → five-specialist site audit → weighted report → 30/60/90 plan → current trend research → original helpful article → Instagram/LinkedIn/X/Reddit/Facebook → factual/editorial QA.

Use local skills and scripts in `codie-geo/skills/`, `codie-geo/agents/`, and `codie-geo/scripts/`. Optionally consult original source under `vendor/geo-seo-core` only if the user has run `bootstrap.py`. All actions must use real sources, label unknown measurements, and never auto-publish.
