# Auto-Editor

Research checked: 2026-11-23. Verify installed versions before production.

Preview the cut decisions before rendering. Use audio thresholds and margins suitable for the speaker rather than deleting every pause. Render to a new file with `auto-editor input.mp4 -o trimmed.mp4`; preserve the original. Export an editable timeline when the chosen downstream editor supports it. Inspect the installed CLI help because syntax changes. After timing changes, rerun WhisperX on edited media or maintain a valid edit mapping.

Starting command (run in the appropriate project/environment):

```sh
auto-editor input.mp4 --preview
```

Official sources: [Auto-Editor](https://auto-editor.com/) · [Details](https://auto-editor.com/docs/cookbook)

