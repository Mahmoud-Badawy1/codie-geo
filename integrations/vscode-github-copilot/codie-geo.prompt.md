---
description: Codie GEO website auditing and audit-to-publishing workflow
---
Read `codie-orchestrator/SKILL.md` and associated `commands.json` and local module folders. `/codie-geo` or no arguments runs the full audit-to-content QA pipeline, onboards if required, and uses source-backed evidence. `/codie-geo <action>` routes to that local skill. Never require `/geo`. The optional original upstream `vendor/geo-seo-core` may be installed via `bootstrap.py` but is not required for the included local modules.
