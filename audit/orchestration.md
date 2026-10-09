# Unified audit orchestration

Start with `orchestrator/SKILL.md`, `skills/codie-geo-audit/SKILL.md`, the five role files in `agents/`, and the individual specialty instructions in `skills/`.

## Five specialists, one report

1. **AI Visibility:** citability, crawler policy, optional llms.txt and brand signals.
2. **Platform Analysis:** ChatGPT, Perplexity and Google AI search readiness; live mentions only where verified.
3. **Technical SEO:** indexability, sitemap/robots, page metadata and markup, canonical, speed only if measured.
4. **Content Quality:** E-E-A-T signals, freshness, reader satisfaction, original facts and content gaps.
5. **Structured Data:** existing JSON-LD, factual correctness, relevant templates and validation plan.

May run in parallel if the host supports truly independent subtasks, otherwise run sequentially.

## Audit sequence

1. Read saved profile and get the site URL. Scope public pages only. Record current timestamps and URL samples.
2. Fetch home and crawl sitemap where permitted. Run local `scripts/fetch_page.py` or live host browser tools and collect HTTP/title/headings/structured-data evidence.
3. Delegate five roles. Each returns finding IDs, observed URLs, source evidence, confidence, issue severity, recommended action, status and testing limits. Use specialist source instructions in `skills/`; if original vendor files are present, read them for detailed added methods.
4. Use `scripts/score_audit.py` with **25%, 20%, 20%, 15%, 10%, 10%** weighting. If any required score is unmeasured, give an incomplete score instead of inventing values.
5. Generate a dated Markdown report and optional PDF with `scripts/generate_pdf_report.py`. Give actionable issues by impact and effort; write quick wins and 30/60/90 roadmap.
6. Feed findings into `planning/optimization.md`, then current topic research, writing, all five social posts and QA. Preserve evidence throughout.

## Safety and factual integrity

Live Core Web Vitals, Search Console traffic, rankings, and actual AI citations cannot be inferred from a single HTML fetch. Record missing observations and use live official tool measurements only when genuinely available. `llms.txt` is optional. No automatic site editing or external posting. Respect crawl restrictions and rate limits.

## Provenance

Local modules and utilities are provided in this package. Original upstream code, if desired, is fetched by `python bootstrap.py` to `vendor/geo-seo-core` and remains MIT-licensed. Do not assert that this optional download already exists.
