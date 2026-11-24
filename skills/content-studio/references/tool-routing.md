# All-tools integration map

Use every tool by default. Assign roles before implementation and read `constraints.md`. This map is this skill's architecture, not an upstream requirement.

| Tool | Required working contribution |
|---|---|
| HyperFrames | Render an editable HTML scene |
| Remotion | Render a parameterized React scene |
| Motion Canvas | Render a diagram or code animation |
| Manim | Render a geometric or mathematical explanation |
| Three.js | Render a lit 3D shot with deliberate camera motion |
| Rough.js | Generate a seeded sketch graphic used in a scene |
| mo.js | Produce a seekable burst or emphasis accent |
| Anime.js | Animate an SVG/DOM/object element on explicit time |
| GSAP | Sequence a paused, seekable scene timeline |
| WhisperX | Transcribe/align real speech and inspect captions |
| Auto-Editor | Analyze/cut supplied or authorized demo footage |
| FFmpeg | Assemble/encode the film and inspect with ffprobe |
| D3.js | Render a chart from declared data |
| Lottie-web | Load and frame-seek a vector animation |
| Shiki | Generate highlighted code used in an explainer/companion |
| sharp | Produce a thumbnail/contact sheet or image variant |
| Playwright | Run browser checks and capture evidence |

Use separate render passes for incompatible engines. Do not let React, GSAP and Anime.js own the same DOM property. Use outputs in the main film where editorially useful; otherwise use the declared companion integration reel. Keep that distinction in coverage evidence. A missing integration blocks all-tools completion; exceptions require an explicit user instruction.

