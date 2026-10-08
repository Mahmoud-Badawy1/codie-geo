# Stage 2 — adaptable content creation

## Preconditions

Load project profile and selected approved research brief. If not approved but profile requires approval, stop at the checkpoint. Re-check sources if time-sensitive. Use any user-provided editorial prompt or examples as a supplemental style guide, subject to verified facts and safety.

## Required editorial references and default deliverables

Before drafting, read `editorial/copywriting.md` and `editorial/source-prompt-adaptation.md`. For visual suggestions read `editorial/visual-search.md`.

**Default content package for `/codie-geo create`, `/codie-geo article`, and stage 2 of `/codie-geo all`: one fully researched article (if an article is relevant to the configured project) PLUS five *distinct* publish-ready platform posts: Instagram, LinkedIn, X, Reddit, Facebook.** Include native copy, channel-specific hashtags (Reddit: a separate off-Reddit topical tag suggestion, not hashtags in body), CTA/link approach, visual idea and alt text. Explicit user constraints or saved selected channels override the five-channel default. If the user explicitly requests social-only, do not create a new article. The research-only stage never produces full content.

Read `workflows/social.md` and all selected `platforms/*.md` after writing the main piece. Use `templates/social-package.md` and record deliverables. The two stages share sourced claims but **not identical prose**.

## Steps

1. **Decide outputs from profile**: blog HTML, Markdown, Google Doc, CMS fields, social copy, newsletter, video script, or another explicitly selected format. For a general create request with no channel indicated, default to **article + Instagram, LinkedIn, X, Reddit and Facebook**, unless an explicit saved project restriction exists. Do not assume bilingual output. Work in the requested languages; adapt culturally and idiomatically rather than mechanically translating. For right-to-left web content, set proper `lang` and `dir` if HTML is requested.
2. **Editorial brief**: distill angle, audience question, working title, hook, structure, proof points, constraints, ideal CTA, internal links, target reading experience. Align length/depth with channel and project rather than universal word-count rules.
3. **Write original useful content**: lead with something specific, provide clear definitions and examples, surface constraints, acknowledge unknowns and alternative viewpoints when relevant, use readable paragraphs and credible voices. Do not impersonate experience or invent case studies, quotes, success metrics, interview data, or testimonials. Avoid generic padded or repetitive prose.
4. **SEO/AEO/GEO where useful**: use descriptive headline and slug, natural topical vocabulary, short direct answers to genuine user questions, relevant internal links and helpful FAQ; sensible metadata/schema only when applicable and supported. Do not misrepresent structured data or promise rankings in AI search engines.
5. **Evidence discipline**: link factual claims to original reputable sources; include source dates or as-of qualifiers for volatile topics, distinguish commentary from evidence. Verify URLs, product claims, terminology and brand restrictions.
6. **Visual workflow**: honor user preferences and rights. Create or source diagrams/images only if requested/configured and the tools exist. Track source, license/permission, attribution, file names, alt text and accessibility. Never present generated mockups as real security evidence or reproduce leaked/private screenshots.
7. **Native distribution**: create each selected social post using `workflows/social.md` and the channel playbook; include copy and hashtag suggestions for each, a native format/visual plan and accurate source/CTA placement. If sources are missing, state the gap and avoid asserting unverified claims.
8. **Deliver package**: save requested variants and metadata; append to manifest; update content index/status; record citations, asset dependencies and links. Store drafts in appropriate authorized location. Publishing requires separate permission unless previously approved in the project workflow.

## Handoff to QA

Provide exact filenames/URLs, the research brief identifier, content version, produced languages, selected social channels, full social copy/hashtags per platform, source list, visual inventory, CMS metadata, internal-link list and any unresolved editorial risks. Mark `DRAFT_READY_FOR_QA`, not `PUBLISHED`.
