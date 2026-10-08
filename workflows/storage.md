# Storage adapters, project isolation and recurrence

## General

Never assume a connected Google Drive, CMS, paid SEO API, search tool, task scheduler or filesystem. Inspect capabilities first. Store project files only in authorized places. A ZIP cannot carry external permissions or persist answers unless a persistent writable workspace is available.

## Supported modes

- `local`: write research as Markdown/YAML, articles in user-selected format, `content-index.csv`, and assets into an explicitly chosen directory. Supply downloadable file links if environment supports them.
- `google_drive`: identify shared folder from the user's authorized link/ID, inspect existing scheme, create only missing authorized directories, and write to existing Google Sheets or create a sheet if instructed. Verify links after writes. Respect user permissions.
- `notion_or_other`: only if a connected integration supports reading/writing pages and the user has authorized it; use its native structure, avoid pretending unsupported actions exist.
- `chat_only`: produce a research brief or draft in chat; provide portable profile so user can reuse in later sessions.

## Default new scheme (only if user chooses week/day)

```
content-workspace/
  project.yaml
  content-index.csv
  projects/<project-slug>/
    week-01/
      day-01/
        day-01-content-and-references.md   # or a spreadsheet with matching name
        images/
        drafts/
        delivery-manifest.json
```

If the user prefers date folders, adapt to `YYYY-MM-DD`; if a flat structure, omit week/day. Existing folders and sheets take precedence, including lowercase naming (e.g. `day5 content and references`) for compatibility. Infer next day from real history and start date; don't equate current calendar day with day sequence without evidence. Never overwrite older research or approved articles without explicit approval.

## Content index

Track date, project_id, content_id, intent/topic fingerprint, audience, keyword, selected angle, research file, draft locations, published URL if verified, sources, stage/status. This is needed to avoid repetitious future research.

## Recurring execution

Skills do not run themselves. If user wants a daily/hourly schedule, use an available scheduler with explicit user authorization. Stage sequencing and remote actions run only through connected tools available in the active agent. Keep time zone configurable. Never claim a schedule exists because the SKILL.md mentions cadence.

## Secrets, privacy and portability

Don't put API keys, access tokens or sensitive unpublished information inside public skill ZIPs. `project.yaml` holds normal project preferences and public links only. Use environment variables or a managed secrets system for credentials. For multiple projects, store separate profiles; selected profile always controls branding and storage.
