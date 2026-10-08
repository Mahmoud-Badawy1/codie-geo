# Codie GEO — Generic AI Content Agent (`/codie-geo`)

**Codie GEO is the agent name, not the company being researched.** It is a **brand-neutral, reusable** three-stage content agent with senior-level storytelling and five-channel social repurposing: **(1) Research → (2) Content → (3) QA**, plus one-time onboarding. Works for software products, nonprofits, shops, creators, professional services, education and other subject matter. Unlike the earlier Codie-specific package, it makes **no assumptions about industry, Google Drive, languages, weekly folders or publishing frequency**.

## Installation

For AI assistants supporting `SKILL.md`-style skills, extract this ZIP and add the entire `codie-geo/` directory to that assistant's supported skills location. Skill discovery/install paths differ by platform; follow that platform's documentation. For assistants without native skill support, upload `SKILL.md` and the `workflows/` and `templates/` directories as project instructions/context, or paste relevant instructions into a custom agent. It is portable instructions, not a hosted bot or standalone executable.

## First use

Say **`/codie-geo`** (where your AI platform supports slash commands), or **"Use the codie-geo skill to set up my business"**. The agent asks an initial four-question interview, selectively follows up, then saves your answers to `content-workspace/project.yaml` if persistent file access is available. For future chats, provide or keep access to that profile; the ZIP alone cannot carry answers between unconnected environments.

## Invocation examples

- `/codie-geo` — first-run onboarding, or menu of actions for an existing project
- `/codie-geo setup` — set up another project
- `/codie-geo research` — one researched topic, sourced brief only
- `/codie-geo create` — researched article plus Instagram, LinkedIn, X, Reddit and Facebook posts by default
- `/codie-geo social` — all five social posts from a topic/approved article, without writing another article
- `/codie-geo instagram` / `linkedin` / `x` / `reddit` / `facebook` — one platform only
- `/codie-geo repurpose [article/url]` — turn an article into five distinct native posts
- `/codie-geo channels` — show defaults; `/codie-geo set-channels instagram linkedin` — save a preferred subset
- `/codie-geo hooks` — ten hooks; `/codie-geo visuals` — ten visual headlines + creative-reference keywords
- `/codie-geo copy` — optional long/short empathetic campaign copy and hooks, inspired by the supplied DOCX
- `/codie-geo qa` — check quality and verify assets/sources/delivery
- `/codie-geo all` — run all stages with configured approvals
- `/codie-geo switch My Other Project` — switch profile
- `/codie-geo research find a fresh policy topic for my nonprofit` — freeform instructions

Natural-language instructions also work: "Use Codie GEO to research a new topic for my website."

## Other examples

- **"Research one high-potential topic for this project. Save just the brief."**
- **"Create this week's article from the approved research."**
- **"QA the content package and verify all links and files."**
- **"Run the full content workflow, but ask me to approve research first."**
- **"Switch to the second project profile and write a newsletter."**
- **"Update my project profile: write French only and use Notion instead of Drive."**

## Workspace behavior

A profile controls target audience, product/site, voice, goals, locale, language(s), publishing medium, SEO/AEO/GEO tactics, style, research scope, sources, required images, approval checkpoints and storage location. Separate projects use separate profiles and duplicate-topic indexes.

Supports Google Drive/Sheets if the user has connected and authorized them. Otherwise use local output or available connected tools. For an existing Drive project, the agent must inspect and preserve the established naming and documents; for new projects, it proposes suitable organization rather than enforcing `week/day`. Scheduling, remote upload and publication are **not** included merely by installing this ZIP.

## Three core workflows

1. **Research** — original/reputable source-led topic selection, history-based duplicate checking, search-intent and competitor analysis, AEO/GEO where helpful, claim/source maps, ideas for links and visuals, structured brief. No article in this stage.
2. **Content** — story-led, original articles plus platform-native Instagram, LinkedIn, X, Reddit and Facebook posts by default, with ready-to-use copy, hashtags, visual guidance and localized variants as configured. The optional copywriting mode supplies long/short copy and hooks.
3. **QA** — editorial/factual/SEO/asset/accessibility/delivery checks plus social completeness, channel voice, hashtags, originality, Arabic tatweel cleanup, safe repairs and transparent status report.

## Files

- `SKILL.md` = routing & cross-stage policies
- `workflows/*.md` = full task instructions and onboarding
- `templates/project.example.yaml` = settings schema
- `templates/research-brief.md` = comprehensive reusable research form
- `templates/delivery-manifest.json` = machine-readable content handoff
- `examples/example-project.yaml` = fictional plant-care example
- `tools/validate_project.py` = optional local validator (requires Python and PyYAML)

## Validator

```bash
python tools/validate_project.py examples/example-project.yaml
```

Checks for fields needed for running content workflows. For tool-free environments, the AI agent can inspect YAML manually. The checker never modifies your profile.

## Source guidelines

Use relevant official documentation, original reports, primary scientific/technical sources and reputable independent coverage. Keep publication dates and original URLs. Developer discussions/community posts can establish user needs or signal a trend, not independently verify major security claims. Official SEO guidance: [Google Search Central](https://developers.google.com/search/docs/fundamentals/seo-starter-guide). Platform guidance: [Google Drive API](https://developers.google.com/workspace/drive/api/guides/about-sdk).

## Migration from an existing Codie workflow

You **can** create a Codie profile by answering onboarding with Codie/ QC Guard details and selecting its existing Drive folder, bilingual HTML output and week/day scheme. The skill is **named** Codie GEO, but its project scope remains generic. Existing day sheets stay untouched unless user authorizes edits.

## How to activate `/codie-geo` on different platforms

- **Claude Code**: place the `codie-geo/` directory in `.claude/skills/` for project scope (or the equivalent user-wide skills location). Current Claude Code skill discovery determines how the `/codie-geo` invocation appears. An optional command wrapper is provided at `integrations/claude-code/commands/codie-geo.md` for installations using custom command files; do not install both if they conflict.
- **VS Code / GitHub Copilot**: copy `integrations/vscode-github-copilot/codie-geo.prompt.md` into `.github/prompts/` in your repository. Invoke the prompt file through your Copilot Chat prompt selector or its supported slash syntax (`/codie-geo` where enabled). Ensure the attached `codie-geo/` skill files are available for context.
- **Other AI assistants (including ChatGPT)**: add `SKILL.md` as project/agent instructions and use `codie-geo` in the agent's name or natural-language invocation. **A ZIP alone cannot register a literal `/codie-geo` command in every interface.**

See `integrations/README.md` for what the wrappers do. Every platform still needs its own tool permissions and persistent storage for profiles.

## Added editorial depth (DOCX-inspired)

`editorial/copywriting.md` implements a practical storytelling and copywriting process grounded in actual customer pains, evidenced detail, non-manipulative empathy, distinct hooks and factual claims. `editorial/source-prompt-adaptation.md` explains exactly how the two families of instructions from your provided `contentPrompts(1).docx` were adapted: visual keyword research with twelve layers and optional long/short copy, ten visual headlines and ten hooks. The book-specific example does not force every project to sell a book, write Egyptian dialect, or invent personal anecdotes.

Content quality matters more than evading AI detectors. Avoid templated prose, obvious filler, hallucinated lived experiences and Arabic tatweel (U+0640). A lightweight copy lint tool is provided, but it cannot replace an editor.

## Platform publishing notes

All five channels are the default when no channel is selected **and the project has not saved an explicit override**. `social` is social-only; `research` never writes the article. Instagram, LinkedIn, X and Facebook include curated hashtag suggestions. Reddit posts **do not insert hashtags**, because this generally reads as unnatural for subreddit discussions; the output still supplies off-Reddit topical tag ideas in a separate field. Posting is never automatic unless the user has independently authorized and connected a capable tool.

Official editorial references: [Google people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [Google AI search optimization](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [Google guidance on AI-generated content](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content), [LinkedIn professional audience guidance](https://business.linkedin.com/content/dam/me/business/en-us/marketing-solutions/resources/pdfs/5-key-principles-for-marketing-on-linkedIn-95273.pdf).

Run optional local text diagnostics:

```bash
python tools/lint_copy.py ./content-workspace/projects/your-project/
```
