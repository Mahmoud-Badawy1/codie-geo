# Codie GEO slash-command adapters

The authoritative workflow is `../SKILL.md` plus `../workflows/`. These adapters supply platform-specific entry points; do not copy the project profile into them.

## Claude Code

Copy `claude-code/commands/codie-geo.md` to your project `.claude/commands/codie-geo.md` **if your Claude Code setup uses custom commands**. Alternatively install the entire `codie-geo/` folder as a Claude Code skill under `.claude/skills/` and use the platform-provided skill invocation. Prefer the single working approach in your environment.

## VS Code / GitHub Copilot Chat

Copy `vscode-github-copilot/codie-geo.prompt.md` to `.github/prompts/codie-geo.prompt.md`. Keep `codie-geo/SKILL.md` and workflow files in the workspace for that prompt to reference. Use the prompt in the prompt picker (or `/codie-geo` if supported by your version/configuration).

## Generic agents and ChatGPT

Provide `SKILL.md` as instructions (along with the remaining folders), name the agent **Codie GEO**, and invoke it with a natural-language instruction. Literal `/codie-geo` requires the host platform to provide a slash-command mechanism; the package can't alter any app UI by itself.
