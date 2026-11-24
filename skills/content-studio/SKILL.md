---
name: content-studio
description: Plan, write, animate, edit, render, and verify videos, reels, explainers, product demos, technical tutorials, mathematical animations, 3D scenes, captions, and social publishing copy. Use for content-generation requests involving Motion Canvas, HyperFrames, Remotion, Three.js, Manim, Rough.js, mo.js, Anime.js, GSAP, WhisperX, Auto-Editor, or FFmpeg, including Arabic and English productions.
---

# Content Studio

Deliver usable content and editable source. Treat the production steps and all-tools coverage as mandatory whenever this skill is invoked. Reduce scope only when the user explicitly requests that exception, and record their instruction. Follow host instructions and user preferences first. A skill cannot force its own invocation or override the host's permissions.

## Required workflow

1. **Brief.** Extract subject, audience, message, platform, language, aspect ratio, duration, assets, narration and deliverables. Ask only for blocking information; otherwise record assumptions and proceed. For a new unspecified video use 1920×1080, 30 fps, 15 seconds; use 1080×1920 for an explicitly vertical reel. Never silently crop footage.
2. **Research.** Check changing facts and technical APIs against primary sources. Keep claim/source pairs in `sources.md`. Inspect existing locks and installed CLI help before selecting versions. Never invent APIs, statistics, endorsements or real product screens.
3. **Write.** Create the script, hook, storyboard with start/end frames, on-screen copy, narration, sound cues and closing action. Specify layout, typography, palette, spacing, camera and motion timing. For a small edit, update only the affected plan.
4. **Select tools.** Read [tool-routing.md](references/tool-routing.md). Use ALL 17 tools in the default all-tools mode. Read [constraints.md](references/constraints.md) before implementation. Assign each tool a working contribution to the requested production or a clearly labeled companion integration reel. Use separate scenes/passes where engines conflict; never run competing clocks on the same object. Do not quietly omit tools or replace execution with imports.
5. **Preflight.** Run `python <skill-dir>/scripts/content.py doctor --project <project-dir>`. Read the selected CLI's help. Use project-local packages and isolated Python environments; pin dependencies and keep locks. Do not assume GPU, Chromium, fonts, LaTeX, model weights or paid services exist. Report blockers and complete independent work.
6. **Build.** Create editable scenes/components and external configuration for copy, colors, timing and media. Use local licensed assets and deterministic time; preserve originals. Read [production.md](references/production.md) for timing, Arabic, audio and design rules.
7. **Preview.** Render a representative section. Inspect beginning, middle, ending, each transition, smallest text, captions and 3D effects. Seek identical frames repeatedly and out of order. Fix missing fonts, clipping, jitter, dead frames and unexpected silence. Listen when sound is required; metadata cannot prove audio quality.
8. **Render and verify.** Produce the requested final file. Run `python <skill-dir>/scripts/content.py verify <video> --width <w> --height <h> --fps <fps> --duration <seconds> --report <project-dir>/qa/media.json`. Add `--require-audio` when sound is expected. This checks metadata and full decoding, not creative quality. Complete [quality-gates.md](references/quality-gates.md) with honest evidence. Run `content.py coverage <project>` and `content.py complete <project>`; a failed gate forbids declaring the production complete.
9. **Deliver.** Supply rendered output, editable source, script/storyboard, required captions, sources/credits, locks, reproduction commands and QA findings. Add title, description, thumbnail direction and platform copy when relevant. Distinguish rendered, inspected, untested and blocked work. Never call an HTML preview or unrun source a finished video. External publishing requires authorization for that destination.

## Tool references

Load only the selected references, plus production and quality gates.

| Tool | Read | Role |
|---|---|---|
| Motion Canvas | [motion-canvas.md](references/motion-canvas.md) | Code and diagram animation |
| HyperFrames | [hyperframes.md](references/hyperframes.md) | Editable HTML-to-video |
| Remotion | [remotion.md](references/remotion.md) | React video compositions |
| Three.js | [three-js.md](references/three-js.md) | 3D scenes, lighting and cameras |
| Manim Community | [manim.md](references/manim.md) | Mathematical animation |
| Rough.js | [rough-js.md](references/rough-js.md) | Sketch graphics on Canvas/SVG |
| mo.js | [mo-js.md](references/mo-js.md) | Bursts and motion accents |
| Anime.js | [anime-js.md](references/anime-js.md) | DOM/SVG/object timelines |
| GSAP | [gsap.md](references/gsap.md) | Sequencing and motion control |
| WhisperX | [whisperx.md](references/whisperx.md) | Transcription and aligned captions |
| Auto-Editor | [auto-editor.md](references/auto-editor.md) | Footage trimming and timelines |
| FFmpeg | [ffmpeg.md](references/ffmpeg.md) | Encode, mix, mux and inspect |
| D3.js | [d3.md](references/d3.md) | Data-driven charts |
| Lottie-web | [lottie.md](references/lottie.md) | Frame-seekable vector assets |
| Shiki | [shiki.md](references/shiki.md) | Syntax-highlighted code |
| sharp | [sharp.md](references/sharp.md) | Thumbnails and image variants |
| Playwright | [playwright.md](references/playwright.md) | Browser checks and screenshots |

Scaffold with `python <skill-dir>/scripts/content.py init <new-directory> --engine hyperframes --title "Project title"`. This creates a production workspace and plan; it does not install a renderer or generate a finished film. Follow the chosen reference for engine setup. Starter examples are in `assets/`. Run `--help` for command options.

Convert transcript segments with `python <skill-dir>/scripts/content.py captions transcript.json captions.srt`. It preserves segment timing and rejects invalid/overlapping cues; it does not transcribe speech or invent word timing. Transcribe final edited footage or explicitly remap timestamps after cuts.

For an explicit text-only request, record that user-approved scope exception and mark media gates not applicable. An engine preference alone does not waive the remaining tool integrations. Preserve existing project conventions and user changes. Never store productions inside the installed skill.

## Command modes

Use `content-studio` with `plan`, `build`, `animate`, `captions`, `render`, `qa`, or `publish-pack`. Claude plugin shortcuts are `/content-studio:plan`, `/content-studio:build`, `/content-studio:animate`, `/content-studio:captions`, `/content-studio:render`, `/content-studio:qa`, `/content-studio:publish-pack`, and `/content-studio:tools`. The main plugin skill is `/content-studio:content-studio`; a standalone Claude installation exposes `/content-studio`. In Codex use `$content-studio <mode> <request>`; do not invent slash-command registration. Stage-specific commands inherit constraints and must not claim whole-project completion.

For portable distribution or installation instructions, read [portability.md](references/portability.md). Use `scripts/export_plugin.py <new-or-empty-repository>` to reproduce this skill's Claude/Codex plugin package. Packaging assets are not production examples.

