# Stage 1 — topic research and structured brief

## Inputs

Project profile, prior topics or content log, public website and product/service facts, available search/competitor sources, request-specific focus, current date + correct target timezone. Validate any external tool-access assumptions.

## Procedure

1. **Deduplicate first.** Inspect saved prior topic index, relevant day folders and research sheets when accessible. Compare central intent, not only headline keywords. If old records are inaccessible, say what was actually checked; do not certify absence of duplicates.
2. **Generate candidates.** For news-facing projects, scan official changelogs, vendor announcements, standards bodies, reputable journalism, relevant GitHub releases/issues, practitioner communities and search-discovery evidence. For evergreen projects, study recurring audience questions, demand patterns, content gaps, documentation changes and commercially relevant jobs-to-be-done. Do not imply fresh news is mandatory.
3. **Score 3–5 candidates** (0–5 each): (a) direct project relevance, (b) clear search/answer-engine intent, (c) evidence quality, (d) freshness or evergreen durability, (e) content differentiation, (f) realistic conversion or audience usefulness. Document short rejection reasons. Prefer the best fit rather than the most sensational news.
4. **Verify carefully.** Seek authoritative originals for features, dates, safety facts, changes, market stats and technical behavior. Keep primary sources separate from analysis/context and community signals. For product or competitor limitations, anchor to vendor documentation. Report source published/updated dates where available and a `checked_on` date. No invented search volume, rank position, trends, vulnerabilities, or citations.
5. **Map competitive SERP intent.** Identify concrete competing pages/URLs where available, target question, their strongest coverage and a genuinely useful missing angle. Don't pretend to have Search Console or paid SEO metrics unless linked.
6. **Pick ONE main topic** and write the research brief using `templates/research-brief.md`. Include SEO/AEO/GEO *when relevant to the user's goal*: query cluster; concise answerable questions; named entities/source relationships; internal links to verified pages; proposed title options; useful visual concepts. Include all fields requested by the project; mark unknowns transparently.
7. **Check project-specific claims.** Tie article angle to the actual offerings, not forced sales copy. Separate what the product does, what a third-party incident establishes, and what is inference. List every important claim and evidence needed.
8. **Deliver research only.** Save to authorized storage; update content log or index with status `RESEARCH_READY` or `REVIEW_REQUIRED`. If approval is configured, stop for approval. NEVER draft full article in this stage.

## Suggested brief minimum fields

- Project, researched date, proposed channel and target market, candidate comparison, selected topic and rationale.
- Trend trigger / evergreen signal; why now; audience problem; search intent; primary + secondary keywords; AEO questions; GEO entities, definitions and citation hooks.
- Competitors with URLs and gaps; differentiation; product/organization angle, boundaries; factual claim map.
- Dated primary sources and secondary/context sources, confidence and unresolved checks.
- Internal links (verified URLs or `needs verification`), visuals with rights notes, article outline, recommended titles, call to action, editorial risks.

## Confirmation

Only state remote file saved if a connector returns a verified file reference or successful retrieval. Otherwise attach local brief and label `REMOTE SAVE PENDING`.
