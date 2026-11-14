# 学习状态台账｜需求会话优先，W/G为覆盖坐标

> **LEARNER_NOT_RUN / UNASSESSED**。当前执行顺序不是W1→W24；以下历史周表仅便于查漏，不是必须打卡的进度日历。

> 补充17个基础专题X01–X17的学习资料见[横向基础卡](CROSS-CUTTING-FOUNDATIONS.md)，其证据仍由本文件对应需求会话记录；**不另建一份X专题进度表，也不自动赋予任何PASS**。

## 当前需求驱动学习队列（真正的优先级来源）

> 从[按需入口](DEMAND-ROUTER.md)定位知识节点，使用[学习会话卡](GAP-SESSION-TEMPLATE.md)留独立实验。**未收到本人的真实任务选择前，此表不自动设W1或S0为下一步。**

| 当前需求/项目 | 节点及最小先修 | 任务/Issue与实验 | 本人状态 | 真实证据 | 下一Gap |
|---|---|---|---|---|---|
| 尚未选定 | — | — | NOT_RUN | — | 待实际需求 |

## 历史W1–W24知识覆盖状态（不是日历）

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

> W09–W24 的每周 D1–D6、先修与 DoD 见 [执行手册](W09-W24-EXECUTION-PLAYBOOK.md)。G13/G20/G21/G23 等覆盖多周，因此**每周交付证据必须分别记录**，不能只凭一个合并 Gate 宣称两周都通过。

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

> **任意跳学**：例如先B04(Spring API)、再D01(SQL)、最后F04(React)；只有本次用到的目标节点需要对应Gate证据。其余模块继续NOT_RUN，不影响当前项目合理交付。

## 产品驱动代码基线（不是本人课程得分）

| 里程碑 | 代码与测试状态 | 学习者独立考核 | 生产/下游状态 |
|---|---|---|---|
| S0 ReconLab 合成核对预览 | API/Web 代码、npm lockfile 已提交；GitHub Python/React CI 通过（仅工程基线） | **NOT_RUN** | TRAINING_ONLY / NO_AUTHORIZATION |
| S1 CSV/PG/AuthZ | NOT_RUN | NOT_RUN | NOT_READY |
| S2 Celery/SSE | NOT_RUN | NOT_RUN | NOT_READY |
| S3 Java Audit/Outbox | NOT_RUN | NOT_RUN | NOT_READY |
| S4 真实上线审核 | BLOCKED | NOT_RUN | Utility-Sites DEVELOPMENT_ON_HOLD |

课程能力与真实产品分别记状态，不能把AI基线和CI通过变为本人L3或产品上线。**只有选择ReconLab案例时**再参考[其S0–S4练习](PRODUCT-DRIVEN-EXECUTION.md)；其他项目按[通用需求路由](DEMAND-ROUTER.md)开始。

## 当前执行焦点

- **下一项由当前真实需求决定**：未选定；不得擅自固定W1或ReconLab S0。入口：[DEMAND-ROUTER](DEMAND-ROUTER.md)。
- **阻塞/风险**：尚未启动实测；待记录开发环境与独立实验结果。
- **历史课程参考预算**：原W1–W24总432h只在选择完整补课模式时使用；需求驱动按本次任务估时，不以累计小时数替代通过标准。

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
