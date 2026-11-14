# ADR-0001：全栈学习主栈、作用域与仓库边界

> **历史快照（ADR-0001）**：此文件中的“当前V3/Java必修”是当时的决策记录，不能作为2026-11-14现行学习顺序。以[ADR-0004当前权威规则](ADR-0004-fullstack-foundations-and-authority.md)及[ADR-0003需求驱动](ADR-0003-demand-driven-learning.md)为准。

- 状态：**SUPERSEDED IN PART (Java/Spring/24-week scope) by [ADR-0002](ADR-0002-v3-multistack-expansion.md)**；本文件仍保留 W1–W8 技术取舍的历史记录，不代表 V3.0 当前 Java 学习优先级。
- 日期：2026-11-13
- 背景：已有 Python/FastAPI、RAG/Agent 经验，但需补齐 React/TS、SQL 事务、工程化与端到端调试；避免双份前后端路线造成重复学习。

## 决策

1. 以 `ROADMAP.md` 为**唯一学习主线**，八周作为参考预算，专项知识库按 Gap 使用。
2. 工作台先用 Vite+React+TS + React Router、FastAPI、PostgreSQL、Redis、Celery、Orval、Docker Compose。先单体分层与纵切功能，延后复杂编排。
3. **历史决策（已被 ADR-0002 部分覆盖）**：当时 Next.js 深度和 Spring Boot 深度都按岗位触发。**当时的 V3.0 改为 Java/JVM/Spring W09–W13 必修，Next SSR W17 必做比较，完整 Next 迁移按需选修。**
4. 统一 OpenAPI 契约：FastAPI 生成 Schema，导出固定文件，Orval 生成类型与客户端，CI 校验漂移；若需求简单可用 openapi-typescript 而非 Orval。
5. W5 Request ID 只做日志关联；选择旧W8/G08完整观测验收时，最小OTel/W3C Trace Context跨服务Span须实测，高级观测平台/仪表盘属于 P2 选修。仅有 UUID Header 不等于完成 Trace。
6. 本仓记录学习证据，Dev-Workbench 管工程方法，Utility-Sites 管产品授权与当前业务边界，不跨仓自动发布/改造。

## 代价与复审触发

- Vite SPA 对公开 SEO 页和部分 SSR 场景不合适；需要这些能力时单独评估 Next.js。
- 主栈是学习取舍，不是公司技术标准；岗位要求、部署环境、成本、安全需求发生变化时记录新 ADR。
- 即使 AI 生成代码、CI 通过，仍需真人独立复现与负例测试。
