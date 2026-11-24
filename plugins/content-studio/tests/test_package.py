from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "content-studio"
SCRIPT = SKILL / "scripts" / "content.py"
EXPECTED = [
    "Motion Canvas", "HyperFrames", "Remotion", "Three.js", "Manim", "Rough.js",
    "mo.js", "Anime.js", "GSAP", "WhisperX", "Auto-Editor", "FFmpeg", "D3.js",
    "Lottie-web", "Shiki", "sharp", "Playwright",
]


class PackageTests(unittest.TestCase):
    def test_all_tool_references_exist_and_are_linked(self):
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        routing = (SKILL / "references" / "tool-routing.md").read_text(encoding="utf-8")
        for name in EXPECTED:
            with self.subTest(tool=name):
                self.assertIn(name, skill)
                self.assertIn(name, routing)
                self.assertTrue((SKILL / "references" / {
                    "Motion Canvas": "motion-canvas.md", "HyperFrames": "hyperframes.md",
                    "Remotion": "remotion.md", "Three.js": "three-js.md", "Manim": "manim.md",
                    "Rough.js": "rough-js.md", "mo.js": "mo-js.md", "Anime.js": "anime-js.md",
                    "GSAP": "gsap.md", "WhisperX": "whisperx.md", "Auto-Editor": "auto-editor.md",
                    "FFmpeg": "ffmpeg.md", "D3.js": "d3.md", "Lottie-web": "lottie.md",
                    "Shiki": "shiki.md", "sharp": "sharp.md", "Playwright": "playwright.md",
                }[name]).is_file())

    def test_both_plugin_manifests_and_commands_exist(self):
        claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        codex = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(claude["name"], "content-studio")
        self.assertEqual(codex["name"], "content-studio")
        commands = ROOT / "commands"
        for name in ("plan", "build", "animate", "captions", "render", "qa", "publish-pack", "tools", "content-studio"):
            self.assertTrue((commands / f"{name}.md").is_file())

    def test_init_and_caption_commands(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project = root / "demo"
            subprocess.run([sys.executable, str(SCRIPT), "init", str(project)], check=True, capture_output=True, text=True)
            coverage = json.loads((project / "coverage.json").read_text(encoding="utf-8"))
            self.assertEqual(len(coverage["tools"]), 17)
            transcript = root / "transcript.json"
            transcript.write_text(json.dumps([{"start": 0, "end": 1.25, "text": "hello"}]), encoding="utf-8")
            output = root / "captions.srt"
            subprocess.run([sys.executable, str(SCRIPT), "captions", str(transcript), str(output)], check=True, capture_output=True, text=True)
            self.assertIn("00:00:01,250", output.read_text(encoding="utf-8"))

    def test_coverage_gate_rejects_unrun_tools(self):
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp)
            (project / "coverage.json").write_text(json.dumps({"tools": []}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), "coverage", str(project)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing record", result.stdout)


if __name__ == "__main__":
    unittest.main()
