#!/usr/bin/env python3
"""Small, dependency-free project scaffold and media QA helpers for Content Studio."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

TOOLS = [
    "Motion Canvas", "HyperFrames", "Remotion", "Three.js", "Manim",
    "Rough.js", "mo.js", "Anime.js", "GSAP", "WhisperX", "Auto-Editor",
    "FFmpeg", "D3.js", "Lottie-web", "Shiki", "sharp", "Playwright",
]


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def init_project(path: Path, engine: str, title: str) -> None:
    path = path.resolve()
    if path.exists() and any(path.iterdir()):
        raise ValueError(f"Refusing to overwrite non-empty directory: {path}")
    path.mkdir(parents=True, exist_ok=True)
    for name in ("src", "assets", "renders", "qa", "logs"):
        (path / name).mkdir(exist_ok=True)
    (path / "plan.md").write_text(
        f"# {title}\n\n- Selected engine: {engine}\n- Canvas: 1920x1080\n"
        "- Frame rate: 30 fps\n- Duration: 15 seconds\n\n"
        "Replace these defaults with the approved brief. See the skill's production guide.\n",
        encoding="utf-8",
    )
    write_json(path / "project.json", {"title": title, "engine": engine, "width": 1920, "height": 1080, "fps": 30, "duration_seconds": 15})
    write_json(path / "coverage.json", {"tools": [
        {"name": name, "status": "not_run", "version": "", "command": "", "log": "",
         "source": "", "output": "", "sha256": "", "use": ""} for name in TOOLS
    ]})
    write_json(path / "scope-exceptions.json", {"user_instruction": "", "excluded_tools": []})
    write_json(path / "qa" / "review.json", {"reviewer": "", "visual_review": "", "audio_review": ""})


def doctor(project: Path) -> int:
    checks = {
        "python": sys.version.split()[0],
        "project_exists": project.is_dir(),
        "ffmpeg": shutil.which("ffmpeg"),
        "ffprobe": shutil.which("ffprobe"),
    }
    if project.is_dir():
        checks["project_manifest"] = (project / "project.json").is_file()
        checks["coverage_file"] = (project / "coverage.json").is_file()
    blockers = []
    if not checks["project_exists"]:
        blockers.append("project directory does not exist")
    if not checks.get("project_manifest", False):
        blockers.append("project.json is missing")
    if not checks.get("coverage_file", False):
        blockers.append("coverage.json is missing")
    # FFmpeg is required for final media verification; absence is reported, not hidden.
    if not checks["ffmpeg"]:
        blockers.append("ffmpeg is not installed")
    if not checks["ffprobe"]:
        blockers.append("ffprobe is not installed")
    report = {"checks": checks, "blockers": blockers, "ready": not blockers}
    print(json.dumps(report, indent=2))
    return 0 if not blockers else 1


def captions(source: Path, target: Path) -> None:
    raw = read_json(source)
    segments = raw.get("segments") if isinstance(raw, dict) else raw
    if not isinstance(segments, list):
        raise ValueError("transcript JSON must be a list or contain a segments list")
    lines = []
    previous_end = -1.0
    for index, item in enumerate(segments, 1):
        try:
            start, end = float(item["start"]), float(item["end"])
            text = str(item["text"]).strip()
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"invalid segment {index}: expected start, end, and text") from exc
        if start < 0 or end <= start or start < previous_end or not text:
            raise ValueError(f"invalid or overlapping segment {index}")
        previous_end = end
        lines.extend([str(index), f"{timestamp(start)} --> {timestamp(end)}", text, ""])
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines), encoding="utf-8")


def timestamp(seconds: float) -> str:
    ms = round(seconds * 1000)
    hours, ms = divmod(ms, 3_600_000)
    minutes, ms = divmod(ms, 60_000)
    secs, ms = divmod(ms, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{ms:03}"


def fps_value(stream: dict[str, Any]) -> float | None:
    value = stream.get("avg_frame_rate") or stream.get("r_frame_rate")
    if not value or value == "0/0":
        return None
    try:
        numerator, denominator = value.split("/", 1)
        return float(numerator) / float(denominator)
    except (ValueError, ZeroDivisionError):
        return None


def verify(video: Path, width: int, height: int, fps: float, duration: float,
           report_path: Path, require_audio: bool) -> int:
    result: dict[str, Any] = {"file": str(video), "checks": {}, "passed": False}
    errors: list[str] = []
    if not video.is_file():
        errors.append("video file does not exist")
    elif not shutil.which("ffprobe") or not shutil.which("ffmpeg"):
        errors.append("ffprobe and ffmpeg are required")
    else:
        probe = subprocess.run(
            ["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)],
            capture_output=True, text=True,
        )
        if probe.returncode:
            errors.append("ffprobe failed: " + probe.stderr.strip())
        else:
            data = json.loads(probe.stdout)
            streams = data.get("streams", [])
            v = next((s for s in streams if s.get("codec_type") == "video"), None)
            a = next((s for s in streams if s.get("codec_type") == "audio"), None)
            actual_duration = float(data.get("format", {}).get("duration", 0) or 0)
            actual_fps = fps_value(v) if v else None
            result["checks"] = {
                "dimensions": bool(v and v.get("width") == width and v.get("height") == height),
                "fps": bool(actual_fps is not None and abs(actual_fps - fps) <= 0.05),
                "duration": abs(actual_duration - duration) <= max(0.25, duration * 0.02),
                "audio_present": bool(a),
                "full_decode": False,
            }
            result["metadata"] = {"width": v.get("width") if v else None, "height": v.get("height") if v else None,
                                  "fps": actual_fps, "duration_seconds": actual_duration,
                                  "video_codec": v.get("codec_name") if v else None,
                                  "audio_codec": a.get("codec_name") if a else None}
            if require_audio and not a:
                errors.append("audio is required but no audio stream was found")
            for key in ("dimensions", "fps", "duration"):
                if not result["checks"][key]:
                    errors.append(f"{key} did not match the requested value")
            decode = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-f", "null", "-"],
                                    capture_output=True, text=True)
            result["checks"]["full_decode"] = decode.returncode == 0
            if decode.returncode:
                errors.append("full decode failed: " + decode.stderr.strip())
    result["errors"] = errors
    result["passed"] = not errors
    write_json(report_path, result)
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


def coverage(project: Path) -> int:
    path = project / "coverage.json"
    if not path.is_file():
        print("coverage.json is missing", file=sys.stderr)
        return 1
    data = read_json(path)
    records = {r.get("name"): r for r in data.get("tools", []) if isinstance(r, dict)}
    errors = []
    for name in TOOLS:
        r = records.get(name)
        if not r:
            errors.append(f"{name}: missing record")
            continue
        for field in ("version", "command", "log", "source", "output", "sha256", "use"):
            if not r.get(field):
                errors.append(f"{name}: missing {field}")
        if r.get("status") != "passed":
            errors.append(f"{name}: status is not passed")
        for field in ("log", "source", "output"):
            item = project / str(r.get(field, ""))
            if not item.is_file() or item.stat().st_size == 0:
                errors.append(f"{name}: {field} file is missing or empty")
        output = project / str(r.get("output", ""))
        if output.is_file() and r.get("sha256"):
            digest = hashlib.sha256(output.read_bytes()).hexdigest()
            if digest.lower() != str(r["sha256"]).lower():
                errors.append(f"{name}: output SHA-256 mismatch")
    print(json.dumps({"passed": not errors, "tools_expected": len(TOOLS), "errors": errors}, indent=2))
    return 0 if not errors else 1


def complete(project: Path) -> int:
    errors = []
    media = project / "qa" / "media.json"
    review = project / "qa" / "review.json"
    if coverage(project) != 0:
        errors.append("tool coverage gate failed")
    if not media.is_file() or not read_json(media).get("passed"):
        errors.append("media verification is missing or failed")
    if not review.is_file():
        errors.append("qa/review.json is missing")
    else:
        data = read_json(review)
        if not data.get("reviewer") or not data.get("visual_review") or not data.get("audio_review"):
            errors.append("reviewer, visual_review, and audio_review evidence are required")
    result = {"complete": not errors, "errors": errors}
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("init", help="create a new production workspace")
    p.add_argument("directory", type=Path)
    p.add_argument("--engine", default="hyperframes")
    p.add_argument("--title", default="Untitled Content Studio project")
    p = sub.add_parser("doctor", help="check local project and media-tool availability")
    p.add_argument("--project", required=True, type=Path)
    p = sub.add_parser("captions", help="convert aligned transcript JSON to SRT")
    p.add_argument("transcript", type=Path)
    p.add_argument("output", type=Path)
    p = sub.add_parser("verify", help="check media metadata and decode the entire file")
    p.add_argument("video", type=Path)
    p.add_argument("--width", required=True, type=int)
    p.add_argument("--height", required=True, type=int)
    p.add_argument("--fps", required=True, type=float)
    p.add_argument("--duration", required=True, type=float)
    p.add_argument("--report", required=True, type=Path)
    p.add_argument("--require-audio", action="store_true")
    p = sub.add_parser("coverage", help="validate all 17 tool evidence records")
    p.add_argument("project", type=Path)
    p = sub.add_parser("complete", help="apply coverage, media, and review completion gates")
    p.add_argument("project", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "init":
            init_project(args.directory, args.engine, args.title)
            print(f"Created project: {args.directory.resolve()}")
            return 0
        if args.command == "doctor":
            return doctor(args.project)
        if args.command == "captions":
            captions(args.transcript, args.output)
            print(f"Wrote captions: {args.output}")
            return 0
        if args.command == "verify":
            return verify(args.video, args.width, args.height, args.fps, args.duration, args.report, args.require_audio)
        if args.command == "coverage":
            return coverage(args.project)
        if args.command == "complete":
            return complete(args.project)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
