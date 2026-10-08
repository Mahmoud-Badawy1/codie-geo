# Website and brand audit orchestration (upstream-first)

Use the installed original components under `vendor/geo-seo-core/`. When the audit engine is missing, run `python bootstrap.py` automatically if shell access and Internet are available and user authorization covers accessing public source. Otherwise give the user `/codie-geo install` setup directions. Never claim a full website audit ran if the original modules were not available or pages could not be fetched. Ask permission before probing non-public or authenticated resources.

## Source modules and order

1. `vendor/geo-seo-core/geo/SKILL.md`: original audit architecture and rubric.
2. `vendor/geo-seo-core/skills/geo-audit/SKILL.md`: site-wide synthesis, scoring, scope.
3. Specialist skills: `geo-technical`, `geo-crawlers`, `geo-schema`, `geo-citability`, `geo-content`, `geo-llmstxt`, `geo-brand-mentions`, `geo-platform-optimizer`.
4. Original agents under `vendor/geo-seo-core/agents/`: use one at a time in a single-agent environment; parallel execution is optional, not required.
5. `vendor/geo-seo-core/skills/geo-report/SKILL.md` and `geo-report-pdf/SKILL.md`: report workflow; PDF only if rendering support exists.
6. `geo-compare`, `geo-proposal`, `geo-prospect` optionally when explicitly requested.

## Audit procedure

- Identify project profile, target domain and business model; enumerate representative URLs and capture UTC checked-at timestamp and access limitations.
- Verify public robots.txt, sitemap.xml, rendered/indexable content, canonical, titles/descriptions, headings, internal links, structured data, page accessibility, Core Web Vitals *only when measurements are actually available*, and content answers. Do not equate HTML inspection with a real browser measurement.
- Assess citation-ready passages, original research/data, author/entity credibility, contextual backlinks/brand discussion, AI crawler policies. Never infer actual search-engine/LLM inclusion merely from robots permissions or `llms.txt`.
- Check platform-specific discoverability when a valid public measurement mechanism is accessible; otherwise label visibility **not tested**. Never invent AI mentions, rankings, scores from a provider, or live citations.
- Generate evidence table per finding: finding ID, URL, observed fact, verified date, verification method, severity, impact, confidence, primary source where applicable, recommended fix.
- Audit rubric and suggested composite scores are heuristics, not Google's or a model provider's official ranking metrics. Show weights and observed/missing measurement coverage separately. If inaccessible, mark untested rather than zero.
- Save raw audit JSON, executive summary, evidence-linked markdown/html report, and optional PDF; classify untested controls clearly. Require human review before site changes.

## Outputs

`audits/YYYY-MM-DD/{audit.json,audit.md,report.html,report.pdf (optional),evidence.csv}`. Use the destination and naming conventions from the project profile when they differ. Put severity, confidence, impact and owner in findings. Record source links in the report. A PDF is never mandatory when tools cannot create it.

## Scope boundaries

No invented search-console access, website ownership, competitor traffic, search volume, PageSpeed scores or AI-platform visibility metrics. Do not treat experimental voluntary protocols as universal requirements. Respect site crawl restrictions, rate limits and user access. Never auto-deploy website edits without authorization.
