#!/usr/bin/env python3
"""Static Roadmap/document integrity gate. This is NOT a training or application test."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load(path: str) -> str:
    p = ROOT / path
    if not p.is_file():
        raise AssertionError(f"Required file missing: {path}")
    return p.read_text(encoding="utf-8")

def equals(actual, expected, name: str) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, observed {actual!r}")

def check_markdown_links() -> int:
    count = 0
    missing = []
    for source in sorted(ROOT.rglob("*.md")):
        if ".git" in source.parts:
            continue
        content = source.read_text(encoding="utf-8")
        # Only check relative file existence, not GitHub-specific anchor slug generation.
        for link in re.findall(r"\]\(([^)]+)\)", content):
            link = link.strip().strip("<>")
            if not link or re.match(r"^(?:https?://|mailto:|#)", link):
                continue
            path_part = link.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            # Do not permit resolved relative links to escape the repository.
            dest = (source.parent / path_part).resolve()
            try:
                dest.relative_to(ROOT)
            except ValueError:
                missing.append((str(source.relative_to(ROOT)), link, "outside repository"))
                continue
            count += 1
            if not dest.exists():
                missing.append((str(source.relative_to(ROOT)), link, str(dest.relative_to(ROOT))))
    if missing:
        for source, link, target in missing:
            print(f"BROKEN LINK {source}: {link} -> {target}", file=sys.stderr)
        raise AssertionError(f"{len(missing)} broken relative Markdown links")
    return count

def main() -> None:
    roadmap = load("ROADMAP.md")
    progress = load("docs/learning/PROGRESS.md")
    acceptance = load("docs/learning/ACCEPTANCE.md")
    playbook = load("docs/learning/W09-W24-EXECUTION-PLAYBOOK.md")
    readme = load("README.md")
    adr1 = load("docs/decisions/ADR-0001-stack-and-boundaries.md")
    adr2 = load("docs/decisions/ADR-0002-v3-multistack-expansion.md")

    base_weeks = re.findall(r"^### W([1-8])｜", roadmap, re.M)
    ext_weeks = re.findall(r"^#### W(0[9]|1[0-9]|2[0-4])｜", roadmap, re.M)
    equals(base_weeks, [str(i) for i in range(1, 9)], "W1-W8")
    equals(ext_weeks, [f"{i:02d}" for i in range(9, 25)], "W09-W24")

    gates = re.findall(r"^\| (G\d{2}) \|", acceptance, re.M)
    equals(gates, [f"G{i:02d}" for i in range(1, 25)], "G01-G24")

    progress_rows = re.findall(r"^\| (W(?:[1-8]|0[9]|1[0-9]|2[0-4])) \|", progress, re.M)
    equals(progress_rows, [f"W{i}" for i in range(1, 9)] +
           [f"W{i:02d}" for i in range(9, 25)], "progress W1-W24")
    equals(len(re.findall(r"\| NOT_RUN \|", progress)), 24, "initial week states")
    # Every week added by V3 must retain its own actionable six-day checklist.
    sections = re.split(r"(?=^### W(?:0[9]|1[0-9]|2[0-4])｜)", playbook, flags=re.M)[1:]
    equals(len(sections), 16, "V3 weekly playbook sections")
    for index, section in enumerate(sections, start=9):
        expected = f"W{index:02d}"
        assert section.startswith(f"### {expected}｜"), f"{expected}: wrong section title"
        days = re.findall(r"^- \*\*D([1-6]) / 3h\*\*", section, re.M)
        equals(days, list("123456"), f"{expected} day plan")
        assert "本周 DoD" in section, f"{expected} missing DoD"
        assert "先修验收" in section, f"{expected} missing prerequisites"

    assert "432h" in roadmap or "432 小时" in roadmap, "24-week budget missing"
    assert "SUPERSEDED IN PART" in adr1, "ADR-0001 outdated without supersession"
    assert "Java/JVM/Spring" in adr2, "ADR-0002 no longer describes Java mandatory"
    assert "W09–W13 必修" in roadmap, "Java/Spring mandatory status missing"
    assert "W09-W24-EXECUTION-PLAYBOOK.md" in readme, "README playbook entry missing"
    assert "STACK-VERSION-POLICY.md" in readme, "README versions entry missing"

    total = check_markdown_links()
    print(f"ROADMAP DOCS PASS: 24 weeks; 24 gates; 16x6 daily tasks; "
          f"{total} relative links checked; actual training remains NOT_RUN.")

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, ValueError) as error:
        print(f"ROADMAP DOCS FAIL: {error}", file=sys.stderr)
        sys.exit(1)
