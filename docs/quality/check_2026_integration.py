#!/usr/bin/env python3
"""Validate 2026 documentation additions; never infer personal learning progress."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEARN = ROOT / "docs" / "learning"

def load(p):
    return p.read_text(encoding="utf-8")

def validate():
    readme = load(ROOT / "README.md")
    roadmap = load(ROOT / "ROADMAP.md")
    router = load(LEARN / "DEMAND-ROUTER.md")
    modes = load(LEARN / "OPTIONAL-EXECUTION-MODES.md")
    drills = load(LEARN / "INTERVIEW-ENGINEERING-DRILLS.md")
    delivery = load(LEARN / "DELIVERY-LIFECYCLE.md")
    detail = load(LEARN / "DETAIL-GAP-INDEX-2026.md")
    audit = load(ROOT / "docs" / "quality" / "INTEGRATION-2026-REVIEW.md")
    graph = json.loads(load(LEARN / "knowledge-map.json"))
    ids = {n["id"] for n in graph["nodes"]}
    if len(ids) != 42:
        raise AssertionError("original 42 knowledge IDs missing or duplicated")

    windows = re.findall(r"^\| D(\d{2})(?:–D(\d{2}))? \|", modes, re.M)
    days = []
    for first, last in windows:
        a, z = int(first), int(last or first)
        days.extend(range(a, z + 1))
    if days != list(range(1, 15)):
        raise AssertionError("optional 14-day sprint has gaps/overlap")
    weeks = [int(x) for x in re.findall(r"^\| W([1-8]) \|", modes, re.M)]
    if weeks != list(range(1, 9)):
        raise AssertionError("optional 8-week curriculum incomplete")
    qs = [int(x) for x in re.findall(r"^\| Q(\d{2}) ", drills, re.M)]
    if qs != list(range(1, 21)):
        raise AssertionError("interview questions must be Q01-Q20")
    dod = [int(x) for x in re.findall(r"^- \[ \] DOD-(\d{2}) ", delivery, re.M)]
    if dod != list(range(1, 13)):
        raise AssertionError("product delivery checklist must be 12 unchecked items")
    rows = [
        line for line in detail.splitlines()
        if re.match(r"^\| (?:Web与浏览器|前端基础|前端工程|API工程|数据|工程安全|Java专项) \|", line)
    ]
    if len(rows) != 30:
        raise AssertionError(f"expected 30 concrete gap topics; got {len(rows)}")
    for line in rows:
        cells = [s.strip() for s in line.strip("|").split("|")]
        if any(part not in ids for part in cells[1].split("/")):
            raise AssertionError("detail topic references an unknown canonical ID")
        if "https://" not in cells[-1]:
            raise AssertionError("detail topic lacks authoritative link")
    if delivery.count("~~~mermaid") < 2:
        raise AssertionError("cross-layer diagrams missing")
    if "202 Accepted" not in delivery or "不保证最终成功" not in delivery:
        raise AssertionError("HTTP 202 caveat missing")
    if "UNASSESSED" not in delivery or "UNASSESSED" not in drills:
        raise AssertionError("study and product evidence boundaries missing")

    new_files = ("DELIVERY-LIFECYCLE.md","OPTIONAL-EXECUTION-MODES.md",
                 "INTERVIEW-ENGINEERING-DRILLS.md","DETAIL-GAP-INDEX-2026.md")
    for name in new_files:
        if name not in readme or name not in roadmap or name not in router:
            raise AssertionError(f"{name} not referenced from all three entrypoints")
    if "W1–W24" not in roadmap or "不要求" not in roadmap:
        raise AssertionError("old knowledge coordinates or demand-driven governance lost")
    if "已覆盖" not in audit or "新增" not in audit or "未" not in audit:
        raise AssertionError("audit lacks delta or limitations")
    return {"nodes_unchanged":42,"optional_days":14,"optional_weeks":8,
            "interview_questions":20,"delivery_gates":12,"detailed_gaps":30}

if __name__ == "__main__":
    try:
        print("2026 INTEGRATION PASS:",validate(),"Documentation only; learner NOT_RUN.")
    except (AssertionError, KeyError, ValueError, OSError, IndexError) as exc:
        print("2026 INTEGRATION FAIL:",exc,file=sys.stderr)
        sys.exit(1)
