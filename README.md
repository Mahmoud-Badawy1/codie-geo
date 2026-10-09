# Codie GEO

**One agent to understand how your website is discovered, decide what to improve, and turn that strategy into content ready to publish.**

Codie GEO combines a complete SEO and generative-engine optimization (GEO) audit with reporting, a practical improvement plan, fresh-topic research, natural article writing, and social media content. It works for **any brand or project**, not just a specific company. Your first run creates a reusable profile; later runs build on what the agent already learned, when your platform supports saved files.

## Start with one command

```text
/codie-geo https://yourwebsite.com
```

Or simply run `/codie-geo` after you have saved your website in the project profile.

Codie GEO runs the full process: **Website audit → GEO score → report → improvement plan → topic research → article → five social posts → publishing checklist and QA.** No need to call the seven stages separately. It prepares content for your approval; it does not publish it without permission.

## What you get

- **A clearer picture of your website:** See what makes your pages easy or difficult for search engines and AI search products to discover, understand and reference.
- **Useful scores and explanations:** A six-part GEO readiness score (0–100), with sources and a clear distinction between checked facts and unknowns.
- **A report that tells you what to do:** Quick wins, missing signals, major technical and content issues, and a prioritized 30/60/90-day roadmap.
- **Better editorial ideas:** Real search intent, market and competitor content gaps, current changes and reputable sources, not a list of disconnected trends.
- **Original content:** Helpful articles, answer-ready explanations, SEO metadata, natural storytelling, source links and a visual plan that fits your brand.
- **A complete social campaign:** Distinct copy for Instagram, LinkedIn, X, Reddit and Facebook, with suitable hashtags and visual guidance. All five are the default unless you choose otherwise.
- **A final readiness review:** Factual consistency, citation checks, content structure, appropriate image usage and platform-by-platform QA.

## How a full website audit works

1. **Discover:** Inspect your homepage, find a relevant sitemap, identify your business category and representative pages.
2. **Five specialized reviews:** Codie GEO coordinates AI visibility (citability, crawler access, `llms.txt` and brand mentions), platform-specific readiness (ChatGPT, Perplexity, Google AI search), technical SEO (indexing, mobile, rendering and measurable speed), helpful content and trust signals (E-E-A-T), and structured data (Schema.org/JSON-LD).
3. **Make sense of the results:** Combine verifiable findings into a weighted, 0–100 GEO *readiness* score.
4. **Generate your report:** Summarize the important findings, potential quick wins and priorities; optionally produce a PDF with scoring charts when PDF tools are available.
5. **Build from what you found:** Turn weaknesses into a realistic improvement plan and fresh, relevant content ideas, then prepare the publication materials and run QA.

These five reviews can run together where the AI platform supports independent subagents, or sequentially in a single agent. **The GEO score is a diagnostic heuristic, not a Google/OpenAI score or a guarantee of AI citations.**

### GEO scoring breakdown

| Assessment | Weight |
|---|---:|
| AI Citability & Visibility | 25% |
| Brand Authority Signals | 20% |
| Content Quality & E-E-A-T | 20% |
| Technical Foundations | 15% |
| Structured Data | 10% |
| Platform Optimization | 10% |

The report identifies what could and could not be verified. The weights add to 100%, but a high readiness score does not prove actual AI search visibility.

## Extra capabilities you can run separately

| Use this | To get this |
|---|---|
| `/codie-geo audit <url>` | Complete website GEO/SEO review |
| `/codie-geo quick <url>` | Quick visibility snapshot |
| `/codie-geo citability <url>` | Ways to make important content more answer-ready |
| `/codie-geo crawlers <url>` | Check `robots.txt` instructions for AI crawlers |
| `/codie-geo llmstxt <url>` | Review or draft an optional `llms.txt` file |
| `/codie-geo brands <url>` | Search for public brand/entity mentions and gaps |
| `/codie-geo platforms <url>` | Platform-specific recommendations |
| `/codie-geo schema <url>` | Check or generate relevant structured data |
| `/codie-geo technical <url>` | Review crawlability, rendering and technical health |
| `/codie-geo content-audit <url>` | Assess existing page quality and E-E-A-T |
| `/codie-geo report <url>` | Client-ready written report |
| `/codie-geo report-pdf <url>` | PDF report and score charts, when available |
| `/codie-geo compare` | See changes between comparable past audits |
| `/codie-geo proposal` | Draft an audit-grounded project proposal |
| `/codie-geo prospect` | Organize authorized prospective client records |

### From finding problems to publishing content

| Use this | To get this |
|---|---|
| `/codie-geo` | The full audit-to-publish workflow |
| `/codie-geo setup` | Create or change a project profile |
| `/codie-geo plan` | Prioritized 30/60/90-day action plan |
| `/codie-geo research` | One well-sourced SEO/AEO/GEO topic research brief, without an article |
| `/codie-geo create` | Researched article plus all five social drafts by default |
| `/codie-geo social` | Five native social posts from an existing article |
| `/codie-geo instagram`, `linkedin`, `x`, `reddit`, `facebook` | Copy for only the named platform |
| `/codie-geo repurpose` | Adapt an existing approved article into social content |
| `/codie-geo hooks`, `copy`, `visuals` | Strong openings, human-centered copywriting or art direction |
| `/codie-geo qa` | Content, source and publishing-readiness assessment |
| `/codie-geo channels` | Review your default publishing platforms |

Use `/codie-geo content <url>` to audit existing content. Use `/codie-geo create` to write new content.

## More than SEO scores

**AI citation readiness.** Identify which passages directly answer real questions, contain checkable facts and can stand on their own. A suggested passage word count is a writing heuristic, never a requirement imposed by search platforms.

**AI crawler access.** Review `robots.txt` signals relevant to AI bots and recommend intentional allow/block choices. Public crawler directives alone do not prove a bot actually accessed your site.

**Brand and entity discovery.** Look for real mentions on public sources, communities and professional platforms. Never treat an unsupported claim about brand-mention correlations as a proven ranking formula.

**Platform readiness.** Consider different ways AI-driven search interfaces might discover and use your content without pretending to know their private ranking algorithms.

**Structured data and `llms.txt`.** Help express your site identity with accurate Schema.org markup and, when useful, an optional `llms.txt` reference; neither promises preferential treatment by AI services.

**Client-ready reporting.** Create actionable Markdown reports or PDF reports with charts where PDF generation is supported and measured data exists.

**Editorial storytelling.** Use relevant real experiences, helpful examples, concise answers and natural transitions. Avoid generic AI-style filler, invented quotes, fake customer stories, exaggerated claims and the Arabic tatweel character (ـ).

## Easy setup

1. Download and extract the ZIP.
2. Add the `codie-geo` folder to your AI assistant's accessible instructions/skills, or ask it to read `codie-geo/SKILL.md`.
3. Run `/codie-geo https://yourwebsite.com` (or tell the assistant to follow the skill if it does not support custom slash commands).
4. Answer the initial questions about your business, audience, language, goals and where you want files saved.
5. Review the audit, content plan, article, social posts and QA report before publishing.

For an assistant with a terminal, optional Python utilities and PDF generation require installing dependencies from `requirements.txt`. All `skills/codie-geo-*` folders ship **inside this ZIP** and are usable as instruction skills without an extra bootstrap. Additional upstream source-code components can optionally be installed later using `python codie-geo/bootstrap.py`, but this step is not required to find or route any local Codie GEO skill.

**Works with:** compatible file-reading agents on Claude Code, Codex, VS Code/GitHub Copilot and other assistants that accept instruction files. Each system decides whether `/codie-geo` can be registered as a literal command. Research requires web access; remote storage, scheduling, visuals, and PDF generation require suitable host tools. The skill does not silently grant them.

## Useful for

**Agencies** delivering client audits and reports. **Marketing teams** producing a documented strategy. **Creators** looking for research-driven stories. **Local businesses** improving answerable service information. **SaaS and ecommerce brands** building more credible product education.

## Where the guidance comes from

- [Google Search Central: creating helpful, reliable content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Schema.org](https://schema.org/)

Codie GEO does not promise rankings, citations or sales that have not been measured. you can know more about us [here].(https://codiemarket.com)
