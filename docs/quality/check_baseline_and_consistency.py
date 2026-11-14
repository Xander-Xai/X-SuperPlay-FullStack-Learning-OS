#!/usr/bin/env python3
"""Cross-cutting baseline and current-policy consistency checks. STATIC, not learner or production validation."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
LEARN = ROOT / "docs" / "learning"

def read(path: str) -> str:
    f = ROOT / path
    if not f.is_file():
        raise AssertionError(f"missing {path}")
    return f.read_text(encoding="utf-8")

def validate() -> dict:
    core = json.loads(read("docs/learning/knowledge-map.json"))
    cross = json.loads(read("docs/learning/cross-cutting-topics.json"))
    cards = read("docs/learning/CROSS-CUTTING-FOUNDATIONS.md")
    readme = read("README.md")
    roadmap = read("ROADMAP.md")
    router = read("docs/learning/DEMAND-ROUTER.md")
    policy = read("docs/decisions/ADR-0004-fullstack-foundations-and-authority.md")
    audit = read("docs/quality/BASELINE-AND-CONSISTENCY-AUDIT-20261114.md")

    core_ids = {node["id"] for node in core["nodes"]}
    if core.get("version") != "4.2" or len(core_ids) != 42:
        raise AssertionError("42 current core knowledge nodes changed without governance")
    topics = cross.get("topics", [])
    expected = {f"X{i:02d}" for i in range(1, 18)}
    actual = [t["id"] for t in topics]
    if len(topics) != len(expected) or set(actual) != expected or len(set(actual)) != 17:
        raise AssertionError("X01-X17 topical baseline catalog missing, extra or duplicated")
    parent_links = 0
    for t in topics:
        for field, minimum in {
            "title": 4, "area": 8, "definition": 20, "analogy": 10,
            "boundary": 15, "lab": 15, "failure": 10
        }.items():
            if len(str(t.get(field, "")).strip()) < minimum:
                raise AssertionError(f"{t['id']}: shallow/empty {field}")
        if not t.get("parent_nodes") or not set(t["parent_nodes"]).issubset(core_ids):
            raise AssertionError(f"{t['id']}: missing or unknown core parent")
        parent_links += len(t["parent_nodes"])
        if not t.get("aliases") or any(not a.strip() for a in t["aliases"]):
            raise AssertionError(f"{t['id']}: unsearchable keyword list")
        url = urlparse(t.get("official", ""))
        if url.scheme != "https" or not url.hostname:
            raise AssertionError(f"{t['id']}: invalid canonical reference")
        for extra in t.get("extra_references", []):
            u = urlparse(extra.get("url", ""))
            if u.scheme != "https" or not u.hostname or len(extra.get("label", "")) < 4:
                raise AssertionError(f"{t['id']}: invalid extra chapter")
            if extra["url"] not in cards or extra["label"] not in cards:
                raise AssertionError(f"{t['id']}: precise subject reference not indexed")
        if not re.search(r"^### " + re.escape(t["id"]) + r" ", cards, re.M):
            raise AssertionError(f"{t['id']}: missing professional/plain-language topic card")
        for content in (t["title"], t["definition"], t["analogy"], t["boundary"],
                        t["lab"], t["failure"], t["official"]):
            if content not in cards:
                raise AssertionError(f"{t['id']}: machine/document source mismatch")
    if cards.count("~~~mermaid") < 1:
        raise AssertionError("missing visual technical relationship diagram")
    for p in ("docs/learning/CROSS-CUTTING-FOUNDATIONS.md",
              "docs/decisions/ADR-0004-fullstack-foundations-and-authority.md"):
        if p not in readme or p not in roadmap:
            raise AssertionError(f"current authoritative root navigation missing: {p}")
    if "CROSS-CUTTING-FOUNDATIONS.md" not in router or "--list-topics" not in router or "--topic X06" not in router:
        raise AssertionError("baseline topics exist but are not discoverable by demand router")
    route_code = read("docs/learning/route_need.py")
    for token in ("def load_topics()", "def find_topics(", "def topic_to_dict(", "--list-topics", "--topic"):
        if token not in route_code:
            raise AssertionError(f"router API missing: {token}")

    # Actively misleading statements: historical ADRs may preserve old decisions only
    # with a prominent current-governance link; current root pages may not contain them.
    prohibited = {
        "ROADMAP.md": ("**P0 必修**", "业务代码目录尚不存在", "| P1（W8 必修补充） |"),
        "README.md": ("V4.0 全面知识覆盖坐标",),
        "docs/project/RECON-LAB-CASE.md": ("必须在 W3 换成",),
        "docs/decisions/ADR-0001-stack-and-boundaries.md": ("**当前 V3.0 改为",),
    }
    for p, wrong in prohibited.items():
        s = read(p)
        for phrase in wrong:
            if phrase in s:
                raise AssertionError(f"{p}: current statement contradicts ADR-0004: {phrase}")
    for legacy in ("docs/decisions/ADR-0001-stack-and-boundaries.md",
                   "docs/decisions/ADR-0002-v3-multistack-expansion.md",
                   "docs/learning/W09-W24-EXECUTION-PLAYBOOK.md",
                   "docs/project/PROJECT-BLUEPRINT.md"):
        if "ADR-0004-fullstack-foundations-and-authority.md" not in read(legacy):
            raise AssertionError(f"historical document lacks supersession notice: {legacy}")
    if "PARTIALLY_IMPLEMENTED" not in read("docs/project/PROJECT-BLUEPRINT.md"):
        raise AssertionError("existing synthetic code incorrectly declared absent")
    if not all((ROOT / p).is_file() for p in (
        "ai-fullstack-workbench/apps/api/app/main.py",
        "ai-fullstack-workbench/apps/web/src/App.tsx",
        ".github/workflows/reconlab-slice.yml"
    )):
        raise AssertionError("optional synthetic code evidence not found")
    if "PROGRESS" not in policy or "CI_VERIFIED" not in policy or "INDEPENDENT_PASS" not in policy:
        raise AssertionError("learning source-of-truth and evidence levels not governed")
    if "尚未" not in audit or "已覆盖" not in audit or "遗漏" not in audit:
        raise AssertionError("cross-topic audit must distinguish prior coverage, gaps and limits")
    return {"core_nodes":len(core_ids), "cross_cutting_topics":len(topics),
            "valid_parent_mappings":parent_links, "sources":sum(1+len(t.get("extra_references",[])) for t in topics),
            "contradiction_rules":sum(map(len,prohibited.values())),
            "historical_notices":4}

if __name__ == "__main__":
    try:
        print("BASELINE CONSISTENCY PASS:", validate(),
              "Static docs/routes only; no learner or deployment outcomes implied.")
    except (AssertionError, ValueError, KeyError, OSError, TypeError) as e:
        print(f"BASELINE CONSISTENCY FAIL: {e}", file=sys.stderr)
        sys.exit(1)
