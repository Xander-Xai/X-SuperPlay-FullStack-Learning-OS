# 全栈开发系统学习路线 V2.0 — 唯一执行主线

> 状态：**PLAN / NOT_RUN / UNASSESSED**（初始建库，未代表已学完、代码已跑通或生产已部署）。
> 版本：2026-11-13；目标：**8 周 × 6 天 × 3 小时 = 144 小时参考预算**。学习可因工作和面试调整，能力以证据验收而非时间打卡为准。

## 0. 一句话决策

**只执行这一条全栈路线**。前端、后端既有路线降为专项知识字典，遇到真实 Gap 再查阅和补实验，不分别推进第二套 8 周进度。上游 [AI-Learning-OS](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS) 保留岗位驱动六周专题作为*参考与紧急 Gap 训练*，与本仓八周统一执行主线不是相互竞争的进度表。

## 1. 学习目标与非目标

- 目标：掌握 **需求→设计→数据模型→API 契约→前端→后端→异步→测试→部署→观测→排障→复盘** 全链路；独立维护并解释一个 AI Web 工作台。
- 已有 Python/FastAPI/RAG/Agent 经验可快速诊断、跳过重复入门，但必须完成实际考核；不存在“做过项目=掌握”的自动豁免。
- 项目：`ai-fullstack-workbench`（本学习仓内工作目录，按项目规模逐步扩展；无需立刻创建独立远程仓）。
- 本期核心栈：React + TypeScript + Vite + React Router + TanStack Query + Tailwind/shadcn/ui；FastAPI + Pydantic + SQLAlchemy/Alembic；PostgreSQL + Redis + Celery；OpenAPI + Orval；Docker Compose + Nginx + pytest + Playwright + GitHub Actions。
- 明确后置：Next.js 深度、Java/Spring Boot 深度、Kubernetes、复杂微服务与重复构建完整 RAG 平台。若有效 JD 触发 MUST，可按需插入针对性实验并记录变更理由。
- 资源优先官方文档；不追求工具数量。无客户授权时只用合成/许可数据；不产生真实业务/生产部署宣称。

## 2. 学习与交付边界

- 不做两份重复课程进度；前端/后端知识按 [专项字典](docs/learning/references/) 检索。
- W1 仍掌握 HTML 语义化、盒模型、布局和浏览器机理，但不长期手写原生 DOM 大项目。
- W3 默认使用 Orval 生成类型、请求函数与 Query Hooks；`openapi-typescript` 是类型生成的替代路径，**不等价**于 Orval 客户端生成能力。
- 后端 Schema 改动只有在导出 OpenAPI → 重新生成 → TS Typecheck / CI / 契约测试后才可能暴露不兼容；不能保证所有运行时语义变更都自动报错。
- W5 Request ID 用于日志关联；W8 OpenTelemetry/W3C `traceparent` 做服务间 trace。两者不可互称；数据库和 Celery 的追踪都需要显式埋点/上下文传播。
- Celery `acks_late` 不是 Worker 遭杀后必定重投递的保证；重投递策略、`task_reject_on_worker_lost`、去重和幂等须在隔离环境验证。
- SSE 必须处理网络块≠事件、代理缓冲、重连以及连接取消；原生 EventSource 与 fetch-stream 的 Header/方法限制不同。
- AI 可生成重复 UI/CRUD/CI 初稿，但**跨端状态、认证刷新、并发锁、幂等与流解析**必须先本人独立实现最小正确版本；所有代码均需本人审查和测试。

## 3. 八周学习计划

| 周 | 主题 | 预算 | 验收产物 |
|---|---|---:|---|
| W1 | Web / JavaScript / TypeScript | 18h | 实现泛型 request<T>：超时、取消、错误归一化、request_id |
| W2 | React / 前端工程 | 18h | 后台壳、项目列表/筛选/分页/编辑 |
| W3 | FastAPI / 认证 / 契约自动化 | 18h | 登录/登出/项目 API |
| W4 | PostgreSQL / Redis / 并发 | 18h | 双连接并发更新实验 |
| W5 | 全栈联调 / 权限 / 日志关联 | 18h | 登录/CRUD/上传纵向切片 |
| W6 | Celery / SSE / 任务可靠性 | 18h | 任务提交、进度查询、SSE 展示 |
| W7 | Docker / CI / 安全 / 部署 | 18h | 从干净环境部署 web/api/worker/db/redis |
| W8 | 性能 / 可观测性 / 系统设计 | 18h | 从浏览器到 API/Worker 的观测演示 |

### W1｜Web / JavaScript / TypeScript（18h）

- **学习范围**：HTTP/DNS/TLS/CORS/Cookie；JS 作用域/闭包/Event Loop/Promise/async；TS 泛型/联合/收窄；Fetch/AbortController。
- **实战产物**：实现泛型 request<T>：超时、取消、错误归一化、request_id；模拟请求逆序响应。
- **独立验收**：用浏览器 Network 解释一次预检；区分 HTTP 非 2xx、网络失败、主动取消；独立解释微任务。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

### W2｜React / 前端工程（18h）

- **学习范围**：Vite+React+TS、路由、状态快照/组件身份、useEffect 清理、TanStack Query、Tailwind/shadcn/ui、基础 CSS/语义化。
- **实战产物**：后台壳、项目列表/筛选/分页/编辑；Mock API；组件与状态测试。
- **独立验收**：快速切换查询无旧数据覆盖；loading/empty/error/重试齐全；可独立解释 Effect 与缓存失效。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

### W3｜FastAPI / 认证 / 契约自动化（18h）

- **学习范围**：Router-Service-Repository、Pydantic、Session/JWT/RBAC、错误映射、OpenAPI、Orval、CI 契约漂移检查。
- **实战产物**：登录/登出/项目 API；从 /openapi.json 固定 Schema，生成 TS 客户端与 Query Hooks。
- **独立验收**：更改后端字段，重新生成并执行 tsc 检查；403 资源权限负例、过期会话、错误响应均有测试。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

### W4｜PostgreSQL / Redis / 并发（18h）

- **学习范围**：SQL/索引/EXPLAIN、事务 ACID/MVCC/隔离、悲观与乐观锁、死锁、SQLAlchemy/Alembic、Redis TTL。
- **实战产物**：双连接并发更新实验；查询计划对照；热点缓存集中失效和回源缓解实验。
- **独立验收**：证明无超扣/丢失更新，展示事务与索引证据，记录缓存回源指标及限制。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

### W5｜全栈联调 / 权限 / 日志关联（18h）

- **学习范围**：真实前后端联调、表单/上传/分页、会话刷新和 CSRF、资源级 AuthZ、X-Request-ID 结构化日志。
- **实战产物**：登录/CRUD/上传纵向切片；浏览器 Network→API→DB→日志 request_id 对应。
- **独立验收**：A 用户不可读取 B 用户资源；中断/超时/无效凭证状态正确；能以 request_id 找到对应后端日志。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

### W6｜Celery / SSE / 任务可靠性（18h）

- **学习范围**：业务状态机、幂等键、ack/retry、Worker 中断恢复、任务队列、SSE 分块/事件边界/断连资源释放。
- **实战产物**：任务提交、进度查询、SSE 展示；在隔离环境 kill Worker，模拟重投递与重复提交。
- **独立验收**：不重复副作用；重启后权威状态可查询；流断连/重连和缓冲均可复现并有测试。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

### W7｜Docker / CI / 安全 / 部署（18h）

- **学习范围**：多阶段构建、Compose volumes/healthcheck、Nginx HTTPS、GitHub Actions、pytest/Playwright、越权/XSS/CSRF/上传安全、备份恢复。
- **实战产物**：从干净环境部署 web/api/worker/db/redis；CI；测试与恢复演练。
- **独立验收**：独立复现环境、通过核心测试；Secret 不入库；恢复和回滚有实际日志与版本。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

### W8｜性能 / 可观测性 / 系统设计（18h）

- **学习范围**：P50/P95/P99、负载模型与可复现基线、结构化日志、OpenTelemetry traceparent/Span、技术 ADR、独立答辩。
- **实战产物**：从浏览器到 API/Worker 的观测演示；负载分析；架构图/ERD/部署手册/演示。
- **独立验收**：报告包含环境并发/数据规模及前后对比；能独立定位慢请求、解释权衡并完成陌生变更。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

## 4. 项目 MVP / P1 / P2

| 级别 | 功能 | 验收重点 |
|---|---|---|
| MVP（必须先完成） | 登录/登出、项目 CRUD、列表筛选分页、基础 RBAC、统一错误态 | 浏览器→API→DB 可见；403 越权负例 |
| P1（核心工程） | 上传、业务任务状态、Worker/Redis、SSE 进度、OpenAPI 自动化、数据库迁移、CI/部署 | 断连重连、重复提交、数据一致性、干净环境复现 |
| P2（可选扩展） | RAG 问答、OpenTelemetry、性能专项、Next.js 或 Spring Boot | 只有需求/岗位触发才投入；不挤占 P0 验收 |

**不可提前将 Mock/API Stub/单次 CI 通过写作生产交付或个人独立能力达标。**

## 5. 每周节奏和验证协议

- 参考每周 18 小时：原理 3h、编码 9h、故障实验 4h、复盘 2h。按实际主题调整。
- 每个知识点：**原理→本人先写→故障注入→测试/排障→闭卷讲解→迁移复测**。
- 人的能力级别：L1 能解释；L2 能独立编写和测试；L3 能复现故障、归因、修复并说明取舍。**不等于** Dev-Workbench 的工程成熟度 L0–L6、也不替代 AI-Learning-OS 的 0–4 人工评分量表。
- 每周记录 [学习进度](docs/learning/PROGRESS.md)；使用 [实验模板](docs/learning/EXPERIMENT-TEMPLATE.md) 记测试命令、结果、环境、截图/日志定位、未验证项。
- 允许停止/延期：面试、工作交付、安全/成本、缺少环境与授权。优先真实业务和求职任务，不凭日历填“完成”。

## 6. 能力验收清单（总 Gate）

- [ ] React 登录、列表、表单、分页、错误态；竞态/取消行为有测试
- [ ] API Schema、后端 AuthN/AuthZ 与错误响应测试通过
- [ ] 导出 OpenAPI → Orval 生成 → TS 检查及 CI 漂移检查
- [ ] SQL 行锁/乐观锁/事务回滚和索引性能实验
- [ ] Redis 缓存失效/并发回源故障与保护实验
- [ ] Worker 中断、重试、去重、幂等与持久任务状态实验
- [ ] SSE 分块/断连/重连/取消与资源清理实验
- [ ] Request ID 日志关联；有必要时 Trace/Span 实测
- [ ] Compose 从新环境复现启动、健康检查、数据持久化
- [ ] CI、单元/集成、Playwright E2E 和服务端越权负例
- [ ] HTTPS、密钥隔离、备份/恢复及版本回退演练
- [ ] 架构/ERD/接口/部署文档；本人独立说明取舍与根因

## 7. 权威学习资源（随用随查）

- Web：[MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development)
- TS：[TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)
- React：[React Learn](https://react.dev/learn)；[React Router](https://reactrouter.com/)；[TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview)
- UI：[Tailwind CSS](https://tailwindcss.com/docs)；[shadcn/ui Vite](https://ui.shadcn.com/docs/installation/vite)
- 后端：[FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)；[SQLAlchemy](https://docs.sqlalchemy.org/)；[Alembic](https://alembic.sqlalchemy.org/)
- 契约：[Orval](https://orval.dev/docs/)；[openapi-typescript](https://openapi-ts.dev/introduction)
- 数据：[PostgreSQL](https://www.postgresql.org/docs/current/)；[Redis](https://redis.io/docs/latest/)
- 异步/通信：[Celery Tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html)；[MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- 交付：[Docker](https://docs.docker.com/get-started/)；[Playwright](https://playwright.dev/docs/intro)；[GitHub Actions](https://docs.github.com/en/actions)；[OpenTelemetry](https://opentelemetry.io/docs/)
- 更深入的工程过程：[Dev-Workbench 学习入口](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench/blob/main/docs/learning/START-HERE.md)。
- 上游能力评分：[AI-Learning-OS 全栈评分](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/assessments/ai-native-fullstack-rubric.md)（可能为私有仓，需访问权限）。

## 8. 仓库协作关系

统一看 [仓库索引](docs/REPOSITORY-INDEX.md)。主线知识和个人学习证据在此；工程方法在 Dev-Workbench，业务验证在 Utility-Sites；**知识引用不构成发布/改造/商业授权**。
