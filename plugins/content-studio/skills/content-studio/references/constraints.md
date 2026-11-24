# Mandatory build contract

Default to all-tools mode. Build functional contributions using every one of the 17 catalog tools. Installation, package imports, dependency declarations, boilerplate, comments, documentation, and a tool name in an output are NOT evidence of a working contribution.

1. Create a plan assigning each tool a concrete job. Connect outputs through shared timing, dimensions and asset paths. Use one clock per scene; compose multiple renderers through exported clips.
2. Implement each tool. For a short requested film, place demonstrations that do not belong editorially into a labeled companion integration reel rather than distorting the main film. Both outputs belong to the complete production package. Do not call a sample integration a customer-facing deliverable.
3. Run each integration and record its actual package/runtime version, reproduction command, successful tool log, nonempty source file, nonempty output artifact, output SHA-256, and how that output is used. Require direct tool execution; a fake file or hand-written success log is forbidden.
4. Record evidence in `coverage.json`, matching the scaffolded schema. Run `content.py coverage <project>` after editing. The gate rejects absent tools, missing/empty artifacts, hash mismatches, failed statuses and missing versions/commands/logs. It does not execute commands or independently prove provenance; the agent must honestly record observed executions, and a reviewer must inspect the logs and outputs.
5. Run `content.py complete <project>` only after coverage, real media verification and human/agent visual/audio review. It must fail when required gates are unfinished. Technical validation alone cannot establish creative quality.
6. Treat GPU, model-download, network, license, missing-data and font problems as blockers. Continue independent work but do not claim completion. WhisperX needs real speech; request or use authorized supplied/generated speech, never label invented timing as transcription. Use user-approved demo data only in a clearly labeled companion.
7. Only an explicit user scope instruction may waive tools. Record the instruction and tool names in `scope-exceptions.json`. Never generate an exception simply because a tool is inconvenient. Repository maintainers can inspect or change this policy; it cannot override host instructions or permissions.
8. Keep dependency manifests and locks. Resolve current packages against official documentation, use exact versions for production, and record environment constraints. Do not install all engines globally. Do not upload private assets, incur cloud charges, clone voices or publish externally without applicable authorization.
9. Preserve source files, asset rights and reproduction commands. Do not embed secrets in code, logs or coverage reports. No credential collection, telemetry beacon or remote upload is required by this plugin.

All-tools completeness applies to productions generated with this skill. The plugin's own package validation is a separate claim: do not describe packaging tests as end-to-end tests of every engine.

