#!/usr/bin/env python3
"""Safely create a public GitHub repository from a clean, committed checkout."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path


def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("owner", help="GitHub owner; must match the active gh account")
    parser.add_argument("repository", help="new repository name")
    parser.add_argument("--directory", type=Path, default=Path.cwd())
    parser.add_argument("--execute", action="store_true", help="create the public repository and push")
    args = parser.parse_args()
    root = args.directory.resolve()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", args.owner) or not re.fullmatch(r"[A-Za-z0-9_.-]+", args.repository):
        parser.error("owner and repository must contain only letters, digits, dot, underscore, or hyphen")
    if not shutil.which("gh") or not shutil.which("git"):
        parser.error("git and GitHub CLI (gh) are required")
    account = run("gh", "api", "user", "--jq", ".login")
    if account.returncode or account.stdout.strip().casefold() != args.owner.casefold():
        parser.error("the active gh account does not match the requested owner")
    git = lambda *a: run("git", *a, cwd=root)
    if not (root / ".git").is_dir() or git("status", "--porcelain").stdout.strip():
        parser.error("run from a Git checkout with a clean working tree")
    if git("remote").stdout.strip():
        parser.error("refusing to replace or reuse an existing Git remote")
    if run("gh", "repo", "view", f"{args.owner}/{args.repository}").returncode == 0:
        parser.error("the target GitHub repository already exists")
    if any(p.name.lower() in {".env", ".env.local", "id_rsa", "id_ed25519"} for p in root.rglob("*") if p.is_file()):
        parser.error("sensitive-looking filenames must be reviewed and removed before publishing")
    print(f"Ready to create PUBLIC repository {args.owner}/{args.repository} from {root}")
    if not args.execute:
        print("Dry run only. Re-run with --execute to create the repository and push.")
        return 0
    created = run("gh", "repo", "create", f"{args.owner}/{args.repository}", "--public", "--source", str(root), "--remote", "origin", "--push")
    print(created.stdout, end="")
    if created.stderr:
        print(created.stderr, end="")
    return created.returncode


if __name__ == "__main__":
    raise SystemExit(main())
