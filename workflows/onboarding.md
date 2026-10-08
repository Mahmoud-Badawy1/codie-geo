# First-run onboarding: ask, adapt, save

## When to interview

Interview on first run ONLY when a usable project profile is absent; on subsequent calls load it and ask only when the request changes major requirements. If the user supplies relevant information in conversation, use it; do not repeat answered questions. Avoid giant questionnaires. Ask in a few conversational batches, not a lengthy form.

### Batch 1 — the four pivotal questions

Ask naturally, e.g.:

1. **What project is this for?** Name, public website(s), what you offer/do, and industry/topic. Links optional.
2. **Who are you trying to reach, where, and what should they do?** Audience, geography, funnel goal, and conversion or desired response.
3. **What type of content and where will it go?** E.g. news-based blog posts, evergreen tutorials, product pages, newsletters, LinkedIn, YouTube scripts; frequency if recurring.
4. **Where should the work live?** Google Drive/Sheets, local folders, Notion, CMS, or just chat output; ask for a folder/link only if storage is required.

If the user responds partially, populate the known settings and ask for missing *essential* information only, or proceed in a temporary workspace when possible.

### Social default disclosed at first use

Tell new users: "When I write an article, I can also prepare Instagram, LinkedIn, X, Reddit and Facebook versions by default. Would you prefer all five or a saved subset?" **If they do not answer this optional question, keep all five**; do not block onboarding. Ask which brand accounts exist only if publication/cross-linking is requested. Gather authentic brand stories or language examples where possible, never demand real customer data to get started.

### Batch 2 — only the questions needed for this project

- Brand voice and examples (website/style guide/links); taboos, competitor brands, citation preferences; verified customer stories if available (optional).
- Social content defaults: all five platforms unless user specifies a smaller set; content pillars, social handles if relevant, hashtags/CTA preferences, organic vs paid, group/community rules, brand approval.
- Publishing languages and localization (do not assume English/Arabic), desired lengths and formats (Markdown, HTML, Docs, CMS JSON, social).
- SEO/AEO/GEO priorities; search-market locale; internal pages or sitemap to link.
- Topic boundaries and existing content index; permission to scan previous archives and history.
- Research constraints: primary sources, regions, recency, competitors, regulated topics and fact-review needs.
- Visuals: original generated graphics vs licensed images vs no images; credits/alt text and rights requirements.
- Structure: existing folder structure or choose from flat, date-based, week/day; naming rule and storage targets.
- Workflow: approval after research, after drafting, before publishing? Autonomous vs human review; connection permissions and calendar cadence.
- Success criteria: relevant visits, leads, conversions, subscriptions, readability, topical authority, or publishing consistency.

Do NOT ask irrelevant items. Separate required setup questions from optional enhancements. For sensitive/regulatory domains, ask about legal/compliance review and clearly mark content as requiring appropriate human sign-off.

## Profile creation / updates

1. Generate unique stable `project_id` and `project_slug` based on explicit project name; avoid private information in file names. Never overwrite an unrelated profile.
2. Copy `templates/project.example.yaml` and replace example placeholders with confirmed or explicitly labeled `null` values. Use `null` rather than fake dates, links or statistics.
3. Default `approval.research_to_content: true` if the user has not authorized automatic content creation. Default `publishing.auto_publish: false`.
4. Output a compact configuration summary and identify unresolved optional settings without blocking a useful next step.
5. Write settings in the project workspace where possible; offer a downloadable config file for portability when cross-chat persistence is otherwise unavailable. Secrets or API keys should be kept out of the profile and ZIP.
6. User may change project with `switch project`, update with `update profile`, or start afresh with `new project`.

## Sample first-run response

"I can tailor the research → writing → QA workflow to your project. What is the project/site and what does it offer? Who is the target audience and primary goal? Which content formats/languages do you want? Finally, should I save output to Google Drive, another workspace, or local downloadable files?"

## Resolution rules

Explicit user choices > previously stored project profile > attached brand docs > safe suggested defaults. Existing naming/filing conventions always win over this package's examples. If multiple plausible project profiles exist, ask which one to use. Explain access limitations immediately rather than claiming remote changes.
