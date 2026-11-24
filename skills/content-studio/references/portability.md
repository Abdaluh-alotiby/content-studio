# Portable plugin packaging

The source skill is `content-studio`. Export the dual-host repository using `python scripts/export_plugin.py <new-or-empty-repository>`. The exporter preserves a preinitialized `.git` directory and refuses to overwrite other files. It copies this skill into `plugins/content-studio/skills/content-studio`, with packaging assets excluded to prevent recursion.

Claude reads `.claude-plugin/plugin.json` and namespaced command files. Codex reads `.codex-plugin/plugin.json`, its marketplace and the same skill. A minimal root `plugin.json` also exposes standard Agent Plugins metadata. Manifests do not execute renderers automatically. Install instructions and command mappings are in the exported README.

Run the exported repository's test suite and host validators before publishing. `scripts/publish.py` defaults to a dry run and requires `--execute` to create a PUBLIC repository using the active device's `gh` account. It validates that account matches the owner argument, requires a clean committed tree, checks secrets by filename, and refuses an existing origin. It does not collect or persist authentication credentials.

Official packaging references, checked 2026-11-23:
- https://developers.openai.com/plugins/build/plugins
- https://learn.chatgpt.com/docs/developer-commands?surface=cli
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/plugin-marketplaces

