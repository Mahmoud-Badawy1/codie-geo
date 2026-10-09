# Use in any compatible AI agent

Codie GEO is a **file-based agent skill**, not a guaranteed global command on every platform. Give the host assistant access to the `codie-geo` directory and point it at `SKILL.md`. It should interpret `/codie-geo` as the full workflow, and `/codie-geo <subcommand>` according to `commands.json`.

- **Claude Code:** Install `integrations/claude-code/commands/codie-geo.md` as the one `/codie-geo` command wrapper and keep the whole skill folder accessible. This wrapper is optional.
- **Codex:** Place `integrations/codex/AGENTS.md.example` instructions in the relevant project `AGENTS.md`; supply the skill folder and request `/codie-geo` in a prompt. Literal slash registration depends on version/host support.
- **VS Code / GitHub Copilot:** Use the `integrations/vscode-github-copilot/codie-geo.prompt.md` prompt file with access to the skill folder.
- **Other agents:** Give `integrations/generic/SYSTEM_PROMPT.md` and `SKILL.md` to your tool or register the command with its extension/skill mechanism.

Audit web access, remote Drive storage, PDF generation, and scheduled runs require host-approved capabilities. One ZIP cannot supply every tool's plugin/API credentials. Do not claim a stage ran if no suitable tool executed it.
