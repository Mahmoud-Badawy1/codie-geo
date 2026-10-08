# Stage 3 — independent editorial, factual and delivery QA

## Audit

1. **Project fit**: correct project and campaign, goal, audience, channel, voice, region, language variants, approved topic and CTA. Verify claims against actual organization/product capabilities.
2. **Research quality**: no duplicated core intent against accessible history, credible dated sources, correctly attributed claims, no invented data, no misleading omission, secure handling of sensitive/security material.
3. **Editorial**: useful distinctive answer, clear introduction and headings, substantive evidence, natural language, strong but accurate CTA, no plagiarism or generic filler. Check localization with separate editorial attention.
4. **SEO/AEO/GEO when configured**: title/description/slug, main topic alignment, helpful Q&A, named-entity accuracy, readable snippet candidates, actual valid internal links, no keyword stuffing or invented performance measures.
5. **Technical**: requested output formats and encoding, HTML structure and directionality if applicable, links, JSON-LD compliance when provided, no broken asset paths, complete CMS fields.
6. **Visual/legal/accessibility**: asset files exist, no unlicensed or undocumented usage, attribution recorded, alt text meaningful, no exposure of private artifacts.
7. **Delivery**: confirm file existence and readable content in the real target system; inspect folder/sheet records, destination links, sharing restrictions and final manifest. Never confuse a planned file name with uploaded content.
8. **Repair and re-check**: correct safe editorial/formatting issues automatically if authorized; do not silently change facts, product claims, permissions, publish destinations or approvals. When blocked, provide precise remedial steps.

## Mandatory copy and social audit

- Verify the article and all requested social channels exist; if no channel is named, check default Instagram, LinkedIn, X, Reddit and Facebook **unless an explicit saved restriction exists**.
- Verify each post has its own publishable text, channel-appropriate hashtag suggestions, truthful hook, relevant CTA/link plan, visual idea and alt text where applicable. Reddit body should be free of hashtags; provide off-Reddit topic suggestions separately.
- Compare the five posts semantically, not just by length: materially different lead/angle/structure; no duplicate cross-post text.
- Verify all real-experience language and claimed customer anecdotes against provided source material; otherwise remove or label hypothetical.
- Scan Arabic prose for U+0640 tatweel and final prose for repeated horizontal dashes, generic filler, excessive em dashes, forced templates, fabricated stats, manipulative open loops, repetitive phrasing and irrelevant hashtag piles. Optional CLI: `python tools/lint_copy.py output-folder/` (text formats supported).
- Do not claim an AI-detector score or guarantee content can't be identified as AI-generated. Human review plus genuine original evidence is the benchmark.
- Confirm article → posts traceability in social manifest and any platform-policy / approval requirements.

## Explicit results

- `READY`: all required items exist and meet configured acceptance criteria (not necessarily published).
- `READY_WITH_NOTES`: minor non-blocking exceptions disclosed.
- `BLOCKED`: consequential missing, unverified or inaccessible requirements.
- `LOCAL_ONLY_REMOTE_SYNC_PENDING`: local artifacts exist but remote upload is not confirmed.
- `REQUIRES_HUMAN_APPROVAL`: mandatory editorial/compliance/publishing sign-off pending.

Return a compact report with checked items, repaired items, blockers, links/artifacts actually verified and suggested next action. Do not make claims of '100% accuracy' or guarantee search performance.
