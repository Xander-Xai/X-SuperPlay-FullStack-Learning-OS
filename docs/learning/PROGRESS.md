# 学习进度台账（唯一状态入口，W1–W24）

> **INITIAL / NOT_RUN / UNASSESSED**。创建文档不代表学习启动、实验成功或个人掌握。

| 周 | 计划重点 | 状态 | 独立考核 | 实际证据/Commit | 下一步 |
|---|---|---|---|---|---|
| W1 | Web / JavaScript / TypeScript | NOT_RUN | UNASSESSED | — | 完成 JS/TS 请求实验 |
| W2 | React / 前端工程 | NOT_RUN | UNASSESSED | — | 待前置验收 |
| W3 | FastAPI / 认证 / 契约自动化 | NOT_RUN | UNASSESSED | — | 待前置验收 |
| W4 | PostgreSQL / Redis / 并发 | NOT_RUN | UNASSESSED | — | 待前置验收 |
| W5 | 全栈联调 / 权限 / 日志关联 | NOT_RUN | UNASSESSED | — | 待前置验收 |
| W6 | Celery / SSE / 任务可靠性 | NOT_RUN | UNASSESSED | — | 待前置验收 |
| W7 | Docker / CI / 安全 / 部署 | NOT_RUN | UNASSESSED | — | 待前置验收 |
| W8 | 性能 / 可观测性 / 系统设计 | NOT_RUN | UNASSESSED | — | 待前置验收 |

## 阶段 B/C 扩展周次（初始全部 NOT_RUN）

| 周 | 主题 | 预算 | 状态 | 能力考核 | 测试/Commit |
|---|---|---:|---|---|---|
| W09 | Java 语言核心与工程环境 | 18h | NOT_RUN | UNASSESSED (G13) | — |
| W10 | Java 集合、Streams、常见设计模式 | 18h | NOT_RUN | UNASSESSED (G13) | — |
| W11 | Java 并发、JVM、数据库访问 | 18h | NOT_RUN | UNASSESSED (G14) | — |
| W12 | Spring / Spring Boot Web API | 18h | NOT_RUN | UNASSESSED (G15) | — |
| W13 | Spring 数据、安全与集成测试 | 18h | NOT_RUN | UNASSESSED (G16) | — |
| W14 | HTML/CSS、浏览器布局与可访问性 | 18h | NOT_RUN | UNASSESSED (G17) | — |
| W15 | JavaScript/TypeScript 深层与前端构建 | 18h | NOT_RUN | UNASSESSED (G18) | — |
| W16 | React 高级架构与前端测试 | 18h | NOT_RUN | UNASSESSED (G19) | — |
| W17 | 渲染架构：SPA、SSR、SSG、Next.js | 18h | NOT_RUN | UNASSESSED (G20) | — |
| W18 | Node.js 运行时与 BFF/API 思维 | 18h | NOT_RUN | UNASSESSED (G20) | — |
| W19 | 消息系统与最终一致性 | 18h | NOT_RUN | UNASSESSED (G21) | — |
| W20 | 数据库、缓存、搜索与分布式边界 | 18h | NOT_RUN | UNASSESSED (G21) | — |
| W21 | 身份、授权与 API 安全进阶 | 18h | NOT_RUN | UNASSESSED (G22) | — |
| W22 | Linux、云部署、基础设施与容灾 | 18h | NOT_RUN | UNASSESSED (G23) | — |
| W23 | 性能、安全与可观测性深挖 | 18h | NOT_RUN | UNASSESSED (G23) | — |
| W24 | 完整系统设计、跨语言集成与独立毕业验收 | 18h | NOT_RUN | UNASSESSED (G24) | — |

> 学习可因具体 JD 提前做 W9 Java 或 W12 Spring 最小实验，但原周 Gate 不得跳过、进度不倒填。

## 当前执行焦点

- **唯一下一项**：W1 — 画出浏览器请求链路，手写 `request<T>()`（超时、取消、错误归一化、请求关联 ID）。
- **阻塞/风险**：尚未启动实测；待记录开发环境与独立实验结果。
- **时间预算**：W1–W8=144h；W9–W24=288h；合计 432h 为参考，不以累计小时数替代通过标准。

## 每次复盘格式

```text
日期/模块/本次投入：
学习前水平：L1 | L2 | L3 | UNASSESSED
完成的代码与 commit SHA：
实际执行环境：
真实测试命令及输出链接：
失败注入与根因：
有 AI 辅助的部分：
本人关闭 AI 后独立完成的部分：
下次陌生场景迁移验证日期：
结论：NOT_RUN | FAIL | PARTIAL | PASS_WITH_EVIDENCE
下一步：
```

> L1/L2/L3 仅为本仓学习能力层级；上游的 0–4 独立评分与 Dev-Workbench 工程成熟度状态仍各自独立。
