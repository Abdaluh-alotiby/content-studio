# Content Studio

Portable Claude and Codex plugin package for planning, building, animating, captioning, rendering, and verifying video content.

## Included

- Shared Content Studio skill and all 17 tool guides.
- Claude plugin manifest and eight namespaced commands.
- Codex plugin manifest and marketplace metadata.
- Local project scaffold and media QA command line helper.
- Package tests and installation instructions.

The default workflow requires a working contribution from each catalog tool. Read `skills/content-studio/references/constraints.md` before production. Package tests validate this distribution; they do not run renderers or prove a production complete.

## Install in Claude Code

Add this repository as a plugin marketplace or install the plugin folder with Claude Code's plugin command. The plugin lives at `plugins/content-studio`. Invoke `/content-studio:content-studio` or one of the stage commands:

`/content-studio:plan`, `/content-studio:build`, `/content-studio:animate`, `/content-studio:captions`, `/content-studio:render`, `/content-studio:qa`, `/content-studio:publish-pack`, `/content-studio:tools`.

## Install in Codex

Add this repository as a Codex marketplace, then install the plugin:

```sh
codex plugin marketplace add Abdaluh-alotiby/content-studio --ref main
codex plugin add content-studio@content-studio-marketplace
```

The skill is available as `$content-studio`. Use `$content-studio plan <request>`, `build`, `animate`, `captions`, `render`, `qa`, or `publish-pack`. The skill can also be copied directly into a Codex skills directory.

## Local commands

Requires Python 3.10+. FFmpeg and ffprobe are needed for media verification; install individual renderers and model dependencies using their upstream guides.

```sh
python skills/content-studio/scripts/content.py --help
python skills/content-studio/scripts/content.py init ./my-video --engine hyperframes --title "My video"
python skills/content-studio/scripts/content.py doctor --project ./my-video
python skills/content-studio/scripts/content.py coverage ./my-video
python skills/content-studio/scripts/content.py verify ./my-video/final.mp4 --width 1920 --height 1080 --fps 30 --duration 15 --report ./my-video/qa/media.json
python skills/content-studio/scripts/content.py complete ./my-video
```

Caption conversion reads a JSON list or an object with a `segments` list. Each segment needs numeric `start`, `end`, and string `text`. It validates timing and writes SRT; it does not transcribe speech.

## Tests

```sh
python -m unittest discover -s tests -v
```

These package tests check layout, command files, and the 17-tool catalog. They are not end-to-end renderer tests.

## Package scope

The archive contains the reusable skill/plugin distribution. It does not include renderers, model weights, fonts, media assets, generated videos, or authentication credentials. Installing it does not publish content externally.

