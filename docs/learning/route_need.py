#!/usr/bin/env python3
"""Route a concrete development gap to its minimum concepts and official references."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

GRAPH_PATH = Path(__file__).with_name("knowledge-map.json")
TOPICS_PATH = Path(__file__).with_name("cross-cutting-topics.json")
ALIASES = {
    "F01": ["http", "cors", "网络请求", "浏览器", "cookie", "tls"],
    "F02": ["html", "css", "布局", "响应式", "无障碍", "表单"],
    "F03": ["typescript", "javascript", "ts", "js", "事件循环", "异步"],
    "F04": ["react", "hook", "组件", "状态管理", "tanstack"],
    "F05": ["next", "ssr", "rsc", "seo", "服务端渲染"],
    "F06": ["node", "bff", "stream", "流式"],
    "F07": ["vite", "bundle", "前端性能", "构建"],

    "F08": ["vue", "vue3", "vue 3", "composition api", "vue后台", "vue组件", "响应式watch"],
    "F09": ["nuxt", "nuxtjs", "nuxt.js", "vue ssr", "vue服务端渲染"],
    "F10": ["pwa", "service worker", "serviceworker", "离线缓存", "离线网页"],
    "F11": ["websocket", "web socket", "sse", "eventsource", "server-sent events", "实时双向", "实时通信", "长连接", "断流"],
    "B07": ["nestjs", "nest.js", "express", "node后端", "node api", "node服务端"],
    "B08": ["golang", "go语言", "go后端", "go服务", "goroutine"],
    "B09": ["rust", "c++", "cuda", "cpp", "原生性能"],
    "D05": ["对象存储", "向量数据库", "全文搜索", "milvus", "minio", "elasticsearch"],
    "E05": ["编译打包", "构建产物", "jar", "maven", "gradle", "cargo"],
    "M03": ["electron", "tauri", "桌面应用", "桌面开发", "电脑客户端"],
    "M04": ["uni-app", "uniapp", "跨端小程序", "跨端框架"],
    "M05": ["kotlin", "swift", "原生安卓", "原生ios", "原生开发"],
    "A02": ["mcp", "model context protocol", "mcp server", "工具协议", "工具调用协议"],
    "B01": ["openapi", "rest", "接口契约", "orval"],
    "B02": ["fastapi", "pydantic", "python接口", "python api"],
    "B03": ["java", "jvm", "jfr", "并发", "集合", "泛型"],
    "B04": ["spring", "spring boot", "spring mvc", "java接口", "java api"],
    "B05": ["jpa", "mybatis", "spring security", "事务代理", "hibernate"],
    "B06": ["celery", "worker", "任务队列", "后台任务", "任务可靠性", "重试幂等"],
    "D01": ["postgres", "postgresql", "sql", "数据库", "死锁", "索引", "事务"],
    "D02": ["redis", "缓存", "cache"],
    "D03": ["rabbitmq", "kafka", "outbox", "消息队列"],
    "D04": ["mysql", "innodb"],
    "E01": ["github actions", "ci", "测试", "playwright", "git"],
    "E02": ["docker", "nginx", "部署", "linux", "https"],
    "E03": ["oauth", "oidc", "登录", "鉴权", "授权", "多租户"],
    "E04": ["opentelemetry", "trace", "监控", "排障", "性能"],
    "U01": ["静态工具", "静态网站", "工具站", "seo工具"],
    "M01": ["微信小程序", "小程序"],
    "M02": ["移动app", "移动应用", "expo", "flutter", "react native"],
    "A01": ["agent", "rag", "大模型", "智能体", "llm"],
    "P04": ["支付", "计费", "订阅", "webhook"],
    "P01": ["需求", "用户故事", "验收条件", "产品prd"],
    "P02": ["架构", "模块边界", "技术选型"],
    "P03": ["上线", "生产发布", "恢复", "运营"],
}


def load() -> dict:
    data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    return {n["id"]: n for n in data["nodes"]}


def load_topics() -> dict:
    """Return supplementary cross-cutting topics without changing 42 core node IDs."""
    data = json.loads(TOPICS_PATH.read_text(encoding="utf-8"))
    return {n["id"]: n for n in data["topics"]}


def find_topics(query: str, catalog: dict | None = None) -> list[dict]:
    """Match specific foundational gaps; preserve core find() behavior and its ID contract."""
    catalog = catalog if catalog is not None else load_topics()
    q = query.casefold().strip()
    if not q:
        return []
    hits: list[tuple[int, dict]] = []
    for topic in catalog.values():
        score = 100 if q == topic["id"].casefold() else 0
        title = topic["title"].casefold()
        if q in title or title in q:
            score += 25
        for alias in topic["aliases"]:
            if alias_matches(alias, q):
                score += 10 + min(len(alias), 12)
        if score:
            hits.append((score, topic))
    hits.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
    return [node for _, node in hits[:3]]


def topic_to_dict(topic: dict, core: dict) -> dict:
    return {
        "id": topic["id"], "kind": "cross_cutting_topic", "title": topic["title"],
        "priority": topic["priority"], "parent_nodes": [
            {"id": id_, "title": core[id_]["title"]} for id_ in topic["parent_nodes"]],
        "definition": topic["definition"], "analogy": topic["analogy"],
        "boundary": topic["boundary"], "official": topic["official"],
        "lab": topic["lab"], "failure": topic["failure"],
        "state": "UNASSESSED",
    }


def describe_topic(topic: dict, core: dict) -> str:
    t = topic_to_dict(topic, core)
    return "\n".join([
        f"{t['id']} · {t['title']} (横向补漏，不新增学习Gate)",
        "适用范围：" + t["priority"],
        "原42节点归属：" + "、".join(n["id"] for n in t["parent_nodes"]),
        "专业定义：" + t["definition"], "大白话：" + t["analogy"],
        "适用边界：" + t["boundary"],
        "权威阅读：" + t["official"],
        "最小实验：" + t["lab"], "失败注入：" + t["failure"],
        "状态：UNASSESSED，需本人真实实验/复测，静态索引不算学会",
    ])


def alias_matches(alias: str, query: str) -> bool:
    """Avoid Java matching JavaScript and js/ts matching NestJS as substrings."""
    a = alias.casefold()
    if a in {"java", "js", "ts", "go", "ci"}:
        return bool(re.search(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", query))
    return a in query


def find(query: str, catalog: dict) -> list[dict]:
    q = query.casefold().strip()
    if not q:
        return []
    result = []
    for id_, node in catalog.items():
        score = 0
        title = node["title"].casefold()
        if q == id_.casefold():
            score += 100
        if q in title or title in q:
            score += 15
        for alias in ALIASES.get(id_, []):
            if alias_matches(alias, q):
                score += 10 + min(len(alias), 10)
        if score:
            result.append((score, node))
    result.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [x[1] for x in result[:5]]


def minimum_prerequisites(node: dict, catalog: dict) -> list[dict]:
    """Topological prerequisite concepts; not an obligation to pass all previous weeks."""
    visited: set[str] = set()
    ordered: list[dict] = []

    def walk(item: dict) -> None:
        for dep_id in item["requires"]:
            if dep_id not in visited:
                visited.add(dep_id)
                walk(catalog[dep_id])
                ordered.append(catalog[dep_id])

    walk(node)
    return ordered


def to_dict(node: dict, catalog: dict) -> dict:
    """Versioned, machine-readable learning plan; no claim of learner mastery."""
    return {
        "id": node["id"],
        "title": node["title"],
        "definition": node["definition"],
        "mechanism": node["mechanism"],
        "analogy": node["analogy"],
        "boundary": node["boundary"],
        "requires": node["requires"],
        "minimum_concepts": [{"id": n["id"], "title": n["title"]}
                             for n in minimum_prerequisites(node, catalog)],
        "read_first": node["read_first"],
        "study_url": node["study_url"],
        "upstream": node.get("upstream", []),
        "upstream_role": node["upstream_role"],
        "lab": node["lab"],
        "failure": node["failure"],
        "coordinates": node["coordinates"],
        "gates": node["gates"],
        "state": "UNASSESSED",
    }


def describe(node: dict, catalog: dict) -> str:
    p = to_dict(node, catalog)
    return "\n".join([
        f"{p['id']} · {p['title']}",
        "专业定义：" + p["definition"],
        "核心机制：" + p["mechanism"],
        "大白话：" + p["analogy"],
        "理解边界：" + p["boundary"],
        "最低先修：" + ("；".join(x["id"] + " " + x["title"] for x in p["minimum_concepts"]) or "无"),
        "旧知识坐标：" + ", ".join(p["coordinates"]) + "（不是执行顺序）",
        "相关验收：" + ", ".join(p["gates"]),
        "官方阅读章节：" + p["study_url"],
        "应读内容：" + p["read_first"],
        "上游资料（" + p["upstream_role"] + "）：" + ("；".join(p["upstream"]) or "暂无"),
        "最小实验：" + p["lab"],
        "错误注入：" + p["failure"],
        "学习完成状态：UNASSESSED；需要本人运行及独立复测证据",
    ])

def main() -> None:
    parser = argparse.ArgumentParser(description="Demand-first full-stack skill lookup")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--query", help='natural task text, e.g. "Spring API"')
    group.add_argument("--node", help="knowledge node ID, e.g. B04")
    group.add_argument("--list", action="store_true", help="list 42 core capability IDs")
    group.add_argument("--topic", help="cross-cutting topic ID, e.g. X06")
    group.add_argument("--list-topics", action="store_true", help="list supporting X01-X17 topics")
    parser.add_argument("--json", action="store_true", help="emit structured skill cards for coding agents")
    args = parser.parse_args()
    catalog = load()
    supporting = load_topics()
    if args.list_topics:
        if args.json:
            print(json.dumps([{"id": t["id"], "title": t["title"]} for t in supporting.values()], ensure_ascii=False, indent=2))
        else:
            for t in supporting.values():
                print(f"{t['id']} · {t['title']}")
        return
    if args.topic:
        selected = supporting.get(args.topic.upper())
        if selected is None:
            parser.error(f"Unknown cross-cutting topic {args.topic}; use --list-topics")
        if args.json:
            print(json.dumps(topic_to_dict(selected, catalog), ensure_ascii=False, indent=2))
        else:
            print(describe_topic(selected, catalog))
        return
    if args.list:
        if args.json:
            print(json.dumps([{"id": x["id"], "title": x["title"]} for x in catalog.values()], ensure_ascii=False, indent=2))
            return
        for n in catalog.values():
            print(f"{n['id']} · {n['title']}")
        return
    if args.node:
        target = catalog.get(args.node.upper())
        if target is None:
            parser.error(f"Unknown node {args.node}; use --list")
        if args.json:
            print(json.dumps(to_dict(target, catalog), ensure_ascii=False, indent=2))
        else:
            print(describe(target, catalog))
        return
    matches = find(args.query, catalog)
    extra = find_topics(args.query, supporting)
    if not matches and not extra:
        parser.error("No confident match; use --list or --list-topics to select an ID")
    if args.json:
        # Keep the historical JSON array shape for query consumers.
        print(json.dumps(
            [to_dict(n, catalog) for n in matches] +
            [topic_to_dict(t, catalog) for t in extra],
            ensure_ascii=False, indent=2))
    else:
        for n in matches:
            print(describe(n, catalog))
            print()
        for t in extra:
            print(describe_topic(t, catalog))
            print()


if __name__ == "__main__":
    main()
