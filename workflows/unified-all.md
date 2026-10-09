# One-command workflow: `/codie-geo` or `/codie-geo all`

**Objective: take a user from a real website/project to an evidence-linked audit and a ready-to-publish article/social package in ONE invocation.** Do not stop between stages simply to ask what to do next when default instructions already establish the next stage. Continue immediately unless approval gates explicitly require input.

## 0. Profile and prerequisites

Load a matching saved project profile. If none, interview using `workflows/onboarding.md`: site / project, audience and geography, goals, brand voice/content languages, authorized output destination, cadence, approvals and five-channel social defaults. Capture only the critical unknowns needed to begin and continue.

Check local specialist folders, optional original-vendor installation and supported tools: public-web access, HTML/robots/sitemap fetch, optional scripts and renderers, Google Drive/Sheets or local folder, chart/PDF generation, public trend research. Report limitations without pretending features are installed.

## 1. Audit using specialist modules

Run `/codie-geo audit [project.website]` internally (actual registry -> `codie-geo-audit`, five integrated specialist agents and supplemental checks): crawl/index/robots, canonical, sitemap, schema, technical health, passage citability, E-E-A-T, brand/entity signals, AI crawler/llms.txt policy and platform-specific readiness. Site scope and sample transparent; do not fabricate search performance or AI visibility.

**Handoff A** save `audits/<date>/audit.json`, page/source evidence, observations with timestamps, and uncertainty fields. If site URL or browsing missing, record an explicit `blocked` audit stage and continue only tasks that can be grounded safely. Do not claim an audit occurred.

## 2. Report

Run `/codie-geo report` from the SAME audit JSON; optionally `/codie-geo report-pdf` if PDF tools exist. Produce executive summary, scope, score/rubric disclosure, evidence, prioritized findings, opportunities and next steps. Visualizations only from actually measured data.

**Handoff B** `audits/<date>/report.md` and optional `report.pdf`, plus findings in reusable structured form.

## 3. Research enhancements and prioritized plan

Use `planning/optimization.md`: validate present best practices and changed search platform guidance, research competitor content/UX and gaps, rank fixes by importance, confidence, implementation effort, likely payoff, dependency and ownership. Group actions into immediate/30-day/60-day/90-day; define verification method and success metric. Audit defects should feed near-term plan; editorial gaps should feed topic candidates. No fictional search-volume estimates.

**Handoff C** `plans/<date>/roadmap.md`, `opportunities.csv` and tracking checklist with links back to findings.

## 4. Fresh trends and topic research

Use `workflows/research.md`, investigate recent reputable sources/search/product news/community interest where relevant; avoid previous themes by reading the project topic history and prior day folders/sheets. Pick topic(s) with valid business connection, organic intent, answer-engine value, differentiated angle and evidence. Cross-reference audit content gaps and roadmap. Save structured brief(s) with current source URLs/dates, queries and competitor pages. Do not recycle stale news because it sounds trendy.

**Handoff D** `research/<date>/topic-brief.md`, `sources.csv`, topic-index updated.

## 5. Create researched article(s)

Use `workflows/content.md` with `editorial/copywriting.md` and `editorial/source-prompt-adaptation.md`: compelling non-generic opening, audience-specific example or verified real story, clear factual structure, practical takeaways, AEO questions/answers, entity accuracy, original thought, natural SEO, metadata, FAQ/schema where valid, internal and external link opportunities. Never fabricate testimony, case studies, product capabilities or first-person lived experience. No Arabic tatweel (ـ). Distinguish verified factual statements and marketing copy.

**Handoff E** `content/<date>/article.md` plus requested `article.html`/CMS fields and visual briefs under `images/` (assets only when licensing/creation permitted). Store local drafts or authorized Drive deliverables.

## 6. Social channels by default

Run `workflows/social.md` using SAME article, sources and positioning. Include exactly these default channels unless user saved an explicit selection: Instagram, LinkedIn, X, Reddit, Facebook. Provide copy/paste-ready platform-native text, hook, length/format, CTA, topic-appropriate hashtags (Reddit keep separate), image/carousel reference concepts. No generic identical cross-posts.

**Handoff F** `social/<date>/<platform>.md` for five platforms and `social-manifest.json`.

## 7. Quality assurance, repairs, readiness report

Apply upstream audit evidence tests plus `workflows/qa.md`: source/date/claim mapping, relevance, technical page issues, metadata/schema lint, broken links where verified, plagiarism/copywriting originality, style/Arabic tatweel, five complete platforms, visual rights, consent to post, and consistency with business capabilities. Fix safe editorial mistakes. Record unresolved warnings, approvals and missing access.

**Handoff G** `qa/<date>/readiness.md`, `delivery-manifest.json` listing actual files, working links and each stage `complete|limited|blocked|approval-required`, next steps. Label `READY TO PUBLISH` ONLY if every required check passes; label `READY FOR REVIEW` if signoff/asset/publishing details remain. Never assert content was published unless an authorized tool confirms it.

## On subsequent runs

Preserve previous audits and research, track dated comparison, avoid duplicate topics and prioritize the highest-impact unresolved actions. Scheduled background runs require a host scheduler; skill files alone cannot schedule themselves.
