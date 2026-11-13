#!/usr/bin/env python3
"""Validate non-linear skills graph and authoritative resource catalog (static only)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
LEARN = ROOT / "docs" / "learning"


def validate() -> dict:
    data = json.loads((LEARN / "knowledge-map.json").read_text(encoding="utf-8"))
    nodes = data["nodes"]
    if data.get("version") != "4.2" or len(nodes) != 42:
        raise AssertionError("knowledge graph missing/too small or obsolete")
    by_id = {n["id"]: n for n in nodes}
    if len(by_id) != len(nodes):
        raise AssertionError("duplicate capability ids")

    upstream_sources = set()
    for node in nodes:
        for link in node.get("upstream", []):
            parsed = urlparse(link)
            if parsed.scheme != "https" or parsed.hostname != "github.com":
                raise AssertionError(f"{node['id']}: upstream source is not a GitHub link")
            if "/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/" not in link:
                raise AssertionError(f"{node['id']}: wrong upstream asset origin")
            upstream_sources.add(link)
    if len(upstream_sources) < 15:
        raise AssertionError(f"upstream content underindexed: {len(upstream_sources)} unique links")

    upstream_index = (LEARN / "UPSTREAM-ASSET-INDEX.md").read_text(encoding="utf-8")
    mental = (LEARN / "FULLSTACK-MENTAL-MODEL.md").read_text(encoding="utf-8")
    lab_docs = (LEARN / "labs" / "README.md").read_text(encoding="utf-8")
    if not (LEARN / "labs" / "request-race.test.mjs").is_file() or "node --test" not in lab_docs:
        raise AssertionError("runnable JS negative-case lab not indexed")
    if upstream_index.count("X-SuperPlay-AI-Learning-OS/blob/main/") < 20:
        raise AssertionError("missing direct upstream links")
    if mental.count("~~~mermaid") < 3:
        raise AssertionError("mental model needs architecture, taxonomy and request sequence")


    official_md = (LEARN / "OFFICIAL-RESOURCES.md").read_text(encoding="utf-8")
    graph_md = (LEARN / "KNOWLEDGE-GRAPH.md").read_text(encoding="utf-8")
    cards_md = (LEARN / "NODE-STUDY-CARDS.md").read_text(encoding="utf-8")
    for n in nodes:
        for required in ("id", "title", "purpose", "requires", "coordinates", "gates", "official", "definition", "mechanism", "analogy", "boundary", "lab", "failure", "read_first", "study_url", "upstream_role"):
            if required not in n:
                raise AssertionError(f"{n.get('id')}: missing {required}")
        min_lengths = {"title": 2, "purpose": 5, "definition": 15, "mechanism": 10,
                       "analogy": 8, "boundary": 12, "lab": 10, "failure": 10, "read_first": 5}
        for field, minimum in min_lengths.items():
            if not isinstance(n[field], str) or len(n[field].strip()) < minimum:
                raise AssertionError(f"{n['id']}: too shallow learning field: {field}")
        if n["upstream_role"] not in ("direct_lab", "track_or_course", "overview_or_reference", "learning_method"):
            raise AssertionError(f"{n['id']}: unsupported upstream content classification")
        if not n["official"]:
            raise AssertionError(f"{n['id']}: no primary source")
        if not re.search(r"^\|\s*" + re.escape(n["id"]) + r"\s*\|", graph_md, re.M):
            raise AssertionError(f"{n['id']}: missing from human graph")
        if not re.search(r"^\|\s*" + re.escape(n["id"]) + r"\s+[^|]*\|", official_md, re.M):
            raise AssertionError(f"{n['id']}: missing official learning section")
        if not re.search(r"^### " + re.escape(n["id"]) + r" · ", cards_md, re.M):
            raise AssertionError(f"{n['id']}: lacks detailed learning card")
        precise = urlparse(n["study_url"])
        if precise.scheme != "https" or not precise.hostname or n["study_url"] not in cards_md or n["study_url"] not in official_md:
            raise AssertionError(f"{n['id']}: missing precise official chapter")
        if n["lab"] not in cards_md or n["failure"] not in cards_md:
            raise AssertionError(f"{n['id']}: no runnable task or negative case in learning card")
        for source in n["official"]:
            url = source["url"] if isinstance(source, dict) else source
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.hostname:
                raise AssertionError(f"{n['id']}: invalid official URL {url}")
            if url not in cards_md and url not in official_md:
                raise AssertionError(f"{n['id']}: base official URL not indexed in learning cards")
        for dep in n["requires"]:
            if dep not in by_id or dep == n["id"]:
                raise AssertionError(f"{n['id']}: bad minimal prerequisite {dep}")

    stack, done = set(), set()

    def visit(node_id: str) -> None:
        if node_id in stack:
            raise AssertionError(f"hard prerequisite cycle: {node_id}")
        if node_id in done:
            return
        stack.add(node_id)
        for dep in by_id[node_id]["requires"]:
            visit(dep)
        stack.remove(node_id)
        done.add(node_id)

    for key in by_id:
        visit(key)

    if by_id["M05"]["requires"] or "D01" in by_id["B05"]["requires"] or "F01" in by_id["E02"]["requires"]:
        raise AssertionError("common association mistakenly required as strict prerequisite")
    if "F04" not in by_id["F05"]["requires"] or by_id["F11"]["title"].find("SSE") < 0:
        raise AssertionError("React/Next or SSE/Worker concept relationship regressed")

    weeks = {w for n in nodes for w in n["coordinates"]}
    gates = {g for n in nodes for g in n["gates"]}
    expect_weeks = {f"W{i:02d}" for i in range(1, 25)}
    expect_gates = {f"G{i:02d}" for i in range(1, 25)}
    if not expect_weeks.issubset(weeks) or not expect_gates.issubset(gates):
        raise AssertionError(f"coverage gap weeks={expect_weeks-weeks} gates={expect_gates-gates}")
    if not all((LEARN / name).is_file() for name in
               ["DEMAND-ROUTER.md", "GAP-SESSION-TEMPLATE.md", "REQUIREMENTS-COVERAGE.md", "NODE-STUDY-CARDS.md"]):
        raise AssertionError("need-first workflow or downstream coverage missing")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if not all(x in readme for x in ("DEMAND-ROUTER.md", "KNOWLEDGE-GRAPH.md", "UPSTREAM-ASSET-INDEX.md", "FULLSTACK-MENTAL-MODEL.md", "NODE-STUDY-CARDS.md")):
        raise AssertionError("need-first entry is not primary")
    return {"nodes": len(nodes), "hard_edges": sum(len(n["requires"]) for n in nodes),
            "distinct_upstream_references": len(upstream_sources),
            "weeks_covered": len(expect_weeks), "gates_covered": len(expect_gates)}


if __name__ == "__main__":
    try:
        stats = validate()
        print("KNOWLEDGE MAP PASS:", stats,
              "Only static source/link and graph structure verified, no learning or deployment implied.")
    except (ValueError, KeyError, AssertionError, OSError) as exc:
        print("KNOWLEDGE MAP FAIL:", exc, file=sys.stderr)
        sys.exit(1)
