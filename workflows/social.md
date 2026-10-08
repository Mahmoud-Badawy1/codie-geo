# Native social media production and article repurposing

## Activation and defaults
Run after an approved article/brief (or a well-specified standalone topic) when called by `/codie-geo create`, `/codie-geo social`, `/codie-geo repurpose`, `/codie-geo all`, or a direct channel command. **If no channel names appear in the command and no previously saved explicit channel override exists, produce Instagram + LinkedIn + X + Reddit + Facebook.** Don't silently replace this with LinkedIn-only. A single-channel command affects one run, unless `/codie-geo set-channels` updates the project profile.

- `research` is research-only: may propose distribution ideas, never writes full posts by default.
- `create` with no format restriction: researched article + all five posts (in all configured languages if viable).
- `social` / `repurpose` with no channel: all five posts, no new article unless requested.
- `/codie-geo x` alone: only X deliverables.
- `channels` prints configured list; `set-channels instagram linkedin` stores selection, then future generic `create` and `social` honor it.
- Explicit requests like 'article only', 'just Instagram', 'no social', and 'only LinkedIn' override defaults for that run without mutating saved profile.

## Repurposing method (not copy-paste)
1. Read the original research and finished article. Select the **one insight that is most useful to each audience**; do not try to summarize the entire article five times.
2. Map verified facts, core story, audience tension, credible examples, applicable CTA and authoritative source links. Do not introduce unverified claims during repurposing.
3. Draft a distinct entry point for each platform. Vary the angle and content, not just the first line or length.
4. Provide a publication-ready **post body/caption**, clear optional CTA, source/link strategy, and **hashtags** (or an explicit no-hashtag recommendation for Reddit with suggested topical tags listed separately).
5. Provide 1-2 alternate hooks per channel, suggested visual or format, concise art-direction notes, accessible alt text, and optionally first comment if the platform needs it.
6. For X, check character length for a standard post (aim <=280 including links/hashtags and account for URL handling); when the full insight won't fit, supply a thread with numbered parts. Avoid hardcoding unsupported platform limits in the briefing.
7. For Reddit, choose a suitable *type* of subreddit or a verified community if researched; respect its rules. Write a genuinely helpful, non-salesy title and body ending in a relevant open discussion prompt, not a disguised ad. Prefer no hashtags *in the post*, but provide a separately labeled optional **hashtag/keyword suggestions (not for Reddit posting)** field so the five-channel package still covers hashtags.
8. Review platform-specific playbooks in `platforms/` and QA the results before saving; use `templates/social-package.md` and `templates/social-manifest.json`.
9. Provide one unified campaign angle plus measurable, project-relevant goals, avoiding unverifiable algorithm/ranking promises. If approval is required, do not publish.

## Prohibitions
- No identical text with swapped hashtags across all platforms.
- No fabricated testimonials, personal episodes, usage stats, case studies, urgency, scarcity or developer experiments.
- No unnatural hashtag stuffing, engagement-bait, viral guarantees, 'AI-proof' promises, automated spam, promotional Reddit astroturfing or deceptive affiliate links.
- No Arabic tatweel U+0640; no decorative long dash separators; avoid habitual em-dash overuse.
- No fake 'published' status. Save to existing storage when connected/authorized, else create local files and flag unsynced outputs.
