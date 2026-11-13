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
    week_state_rows = re.findall(r"^\| W(?:[1-8]|0[9]|1[0-9]|2[0-4]) \|[^\n]*$", progress, re.M)
    equals(len(week_state_rows), 24, "module status rows")
    allowed = {"NOT_RUN", "IN_PROGRESS", "PARTIAL", "FAIL", "BLOCKED", "PASS_WITH_EVIDENCE"}
    for line in week_state_rows:
        cells = [value.strip() for value in line.strip("|").split("|")]
        state = cells[2] if re.fullmatch(r"W[1-8]", cells[0]) else cells[3]
        if state not in allowed:
            raise AssertionError(f"{cells[0]} invalid state: {state}")
        if state == "PASS_WITH_EVIDENCE":
            evidence = cells[4] if re.fullmatch(r"W[1-8]", cells[0]) else cells[5]
            if evidence in {"", "—", "-", "NOT_RUN"}:
                raise AssertionError(f"{cells[0]} passed without real evidence link")
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

    assert "432" in roadmap and "参考" in roadmap, "historical 432h optional coverage budget missing"
    assert "SUPERSEDED IN PART" in adr1, "ADR-0001 outdated without supersession"
    adr3 = load("docs/decisions/ADR-0003-demand-driven-learning.md")
    assert "Java" in adr2 and "历史" in adr3, "historical Java coverage must be documented"
    assert "需求驱动" in adr3 and "requires" in adr3, "ADR-0003 demand-driven rule missing"
    assert "不要求" in roadmap and "按需" in roadmap, "current roadmap must not force a weekly sequence"
    assert "W09-W24-EXECUTION-PLAYBOOK.md" in readme, "README playbook entry missing"
    assert "STACK-VERSION-POLICY.md" in readme, "README versions entry missing"

    total = check_markdown_links()
    print(f"ROADMAP DOCS PASS: 24 coordinates; 24 gates; 16x6 optional day templates; "
          f"{total} relative links checked; learner results are not inferred.")

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, ValueError) as error:
        print(f"ROADMAP DOCS FAIL: {error}", file=sys.stderr)
        sys.exit(1)
