# ADR-0001：全栈学习主栈、作用域与仓库边界

- 状态：**Accepted for study plan**（仅学习选型，不代表实现或生产采纳）
- 日期：2026-11-13
- 背景：已有 Python/FastAPI、RAG/Agent 经验，但需补齐 React/TS、SQL 事务、工程化与端到端调试；避免双份前后端路线造成重复学习。

## 决策

1. 以 `ROADMAP.md` 为**唯一学习主线**，八周作为参考预算，专项知识库按 Gap 使用。
2. 工作台先用 Vite+React+TS + React Router、FastAPI、PostgreSQL、Redis、Celery、Orval、Docker Compose。先单体分层与纵切功能，延后复杂编排。
3. Next.js 深度仅在明确 SSR/SEO/Server Components 需求、或目标 JD 要求时引入；Spring Boot 深度在有效 Java 岗位需求触发时安排；不能把未验证的技术偏好当通用定律。
4. 统一 OpenAPI 契约：FastAPI 生成 Schema，导出固定文件，Orval 生成类型与客户端，CI 校验漂移；若需求简单可用 openapi-typescript 而非 Orval。
5. W5 Request ID 只做日志关联；W8 最小 OTel/W3C Trace Context 跨服务 Span 实测为 P1 必修，高级观测平台/仪表盘属于 P2 选修。仅有 UUID Header 不等于完成 Trace。
6. 本仓记录学习证据，Dev-Workbench 管工程方法，Utility-Sites 管产品授权与当前业务边界，不跨仓自动发布/改造。

## 代价与复审触发

- Vite SPA 对公开 SEO 页和部分 SSR 场景不合适；需要这些能力时单独评估 Next.js。
- 主栈是学习取舍，不是公司技术标准；岗位要求、部署环境、成本、安全需求发生变化时记录新 ADR。
- 即使 AI 生成代码、CI 通过，仍需真人独立复现与负例测试。
