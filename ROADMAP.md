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

#### W1 补充：学时、底层机制与实验协议

**学时**：Web/浏览器 **5h** + JS 异步/Event Loop **6h** + TS 类型 **5h** + 复盘 **2h** = 18h。

- HTTP 方法、状态码、DNS/TCP/TLS、Cookie/Session、CORS 预检和浏览器 DevTools；HTML 语义化、表单、CSS 盒模型、Flex/Grid、响应式只学必要原理，不花整周做原生 DOM 后台。
- JS 作用域/闭包、宏任务/微任务、Promise、async/await、异常传播；TS 泛型、接口、联合/辨别联合、类型收窄、推断。
- **实验 W1-A**：在浏览器 Network 面板还原“URL→连接→HTTP→页面”，比较跨域预检与实际业务请求。保存请求/响应字段与口述链路。
- **实验 W1-B**：本人写 `request<T>()` 支持 AbortSignal、超时、错误归一化、X-Request-ID；分别验证 HTTP 非 2xx、网络失败、手动取消、超时。不能把断网伪装成 HTTP 状态码。
- **实验 W1-C**：A 先请求、B 后请求却先返回，模拟竞态；确保旧 A 不能覆盖新 B。必须独立解释异步顺序和闭包原因。
- **验收**：真实命令、测试、Network 证据以及关 AI 口述；实验代码尚不存在时状态必须 NOT_RUN。

### W2｜React / 前端工程（18h）

- **学习范围**：Vite+React+TS、路由、状态快照/组件身份、useEffect 清理、TanStack Query、Tailwind/shadcn/ui、基础 CSS/语义化。
- **实战产物**：后台壳、项目列表/筛选/分页/编辑；Mock API；组件与状态测试。
- **独立验收**：快速切换查询无旧数据覆盖；loading/empty/error/重试齐全；可独立解释 Effect 与缓存失效。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

#### W2 补充：学时、React 心智模型与验证

**学时**：组件与状态 **7h** + Router/取数 **4h** + CSS/表单 **4h** + 调试/测试 **3h** = 18h。

- React Render/Commit、state snapshot、组件 identity、`key`、Props/State/Context、`useState`/`useRef`/`useEffect` 依赖、清理和 Strict Mode。
- TanStack Query Query Key、stale 状态、缓存失效、Mutation、乐观更新。组件局部状态不等于服务器状态；不是所有异步请求都需要手写在 Effect 中。
- Vite + React Router + Tailwind + shadcn/ui 构造布局、筛选、分页、表单、编辑弹窗、详情、Mock API；为加载、空、错、重试、成功分别实现可观察状态。
- **实验 W2-A**：快速切换搜索条件，验证旧请求不会覆盖最新结果；说明 Effect cleanup/Query Key 与数据竞态的关系。
- **实验 W2-B**：新增/删除项目后缓存失效和渲染正确；使用组件测试与交互断言而不只检查截图。
- **验收**：Mock 数据必须标 MOCK；页面可交互、有失败态和可访问性基础，不凭 UI 美观判 PASS。

### W3｜FastAPI / 认证 / 契约自动化（18h）

- **学习范围**：Router-Service-Repository、Pydantic、Session/JWT/RBAC、错误映射、OpenAPI、Orval、CI 契约漂移检查。
- **实战产物**：登录/登出/项目 API；从 /openapi.json 固定 Schema，生成 TS 客户端与 Query Hooks。
- **独立验收**：更改后端字段，重新生成并执行 tsc 检查；403 资源权限负例、过期会话、错误响应均有测试。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

#### W3 补充：接口契约的唯一来源和 CI 破坏性实验

**学时**：利用已有 FastAPI 经验，先约 **6h** 建立 Router→Service→Repository、Pydantic、异常/基础 API；其余 **12h** 用于认证、契约生成、集成测试和 CI。

```text
FastAPI Router + Pydantic（接口权威）
  → /openapi.json 导出并固定为 contracts/openapi.json
  → pnpm gen:api 使用 Orval
  → apps/web/src/api/generated/ 类型、客户端、TanStack Query Hooks
  → Typecheck + Schema/生成产物差异检查 + API 集成/契约测试
```

- `openapi-typescript` 主要是 OpenAPI→TS 类型生成；`Orval` 在恰当配置下还能产出请求函数和 Query Hooks。不要把两者能力等同。
- **实验 W3-A**：修改后端返回字段名/类型/枚举，重新导出 Schema、生成前端 API，再运行 TS 类型检查；旧代码受生成类型约束时应出现相应错误，然后修复并复测。
- **实验 W3-B**：构造运行时 Schema 不一定能捕获的权限/业务语义变化，使用契约/集成测试补足。不能声称“后端一改，前端必自动报错”。
- 登录/登出/受保护端点/会话过期；理解 Session、JWT、HttpOnly/Secure/SameSite Cookie、CSRF、RBAC 和资源级授权的区别。
- **验收**：API 规范、401/403/非法参数/超时/异常和生成流程均有可执行证据；不靠隐藏前端按钮做 AuthZ。

### W4｜PostgreSQL / Redis / 并发（18h）

- **学习范围**：SQL/索引/EXPLAIN、事务 ACID/MVCC/隔离、悲观与乐观锁、死锁、SQLAlchemy/Alembic、Redis TTL。
- **实战产物**：双连接并发更新实验；查询计划对照；热点缓存集中失效和回源缓解实验。
- **独立验收**：证明无超扣/丢失更新，展示事务与索引证据，记录缓存回源指标及限制。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

#### W4 补充：高优先级数据库与缓存实验

**学时**：SQL/索引 **5h** + 事务/并发 **8h** + Redis **3h** + 复盘/测试 **2h**。

- SQL：JOIN、GROUP BY、CTE、索引选择性/复合索引、`EXPLAIN (ANALYZE, BUFFERS)`、索引写入成本；ORM Session/N+1/Alembic 迁移。
- 并发：ACID、MVCC、隔离级别、锁等待、死锁、悲观/乐观锁、唯一约束及条件 UPDATE，明确事务边界。
- **实验 W4-A**：测试库初始化余额 100，两独立连接并发读/写。先复现丢失更新，再用 `SELECT ... FOR UPDATE`、乐观版本或条件 UPDATE 修复，证明不会超扣；记录锁等待/回滚与死锁负例。
- **实验 W4-B**：固定数据量与分布，索引前后比较查询计划、耗时和写入代价；不要把一次实验当通用优化规律。
- **实验 W4-C**：热点 Key 同时过期、并发回源，测 DB QPS/延迟/错误率；对照 TTL 抖动、互斥重建或请求合并。区分缓存雪崩与单热点击穿、说明缓存一致性。
- **验收**：提交 Schema、Migration、并发测试、EXPLAIN 报告和缓存回源对照；仅允许使用隔离测试库。

### W5｜全栈联调 / 权限 / 日志关联（18h）

- **学习范围**：真实前后端联调、表单/上传/分页、会话刷新和 CSRF、资源级 AuthZ、X-Request-ID 结构化日志。
- **实战产物**：登录/CRUD/上传纵向切片；浏览器 Network→API→DB→日志 request_id 对应。
- **独立验收**：A 用户不可读取 B 用户资源；中断/超时/无效凭证状态正确；能以 request_id 找到对应后端日志。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

#### W5 补充：登录态、跨端关联和真正的 Trace 边界

**建议学时**：登录态/权限 **5h** + CRUD/文件上传联调 **5h** + Request ID/结构化日志 **4h** + 故障/验收 **4h**。

```text
浏览器 Network（请求/响应 request_id）
 → 可信入口 Nginx/FastAPI（生成或校验 X-Request-ID）
 → Router/Service/DB 客户端（带关联日志或 Span）
 → 任务入队（传播 request_id + task_id/run_id）
 → Celery Worker（处理日志/状态）
```

- `X-Request-ID` 只是便于检索的日志关联符；客户端值应在可信入口校验长度/格式或重新生成，并回传响应头。不能把未知 Header 原样写入日志。
- `traceparent` 属 W3C Trace Context：只有实际 OpenTelemetry instrumentation、上下文传播、Span 收集与导出查看，才叫可验证的分布式 Trace。
- PostgreSQL 查询不能仅凭 HTTP Header 就自动串起，需要显式日志关联或 DB 客户端 tracing。**W5 要求 Request ID/结构化日志可检索，W8 最小 OTel Trace 为必修**。
- 强化 HttpOnly/Secure/SameSite、CSRF、401 vs 403、刷新并发、资源级授权；同源反代可降低 CORS 复杂度但不能代替理解跨域。
- **验收**：从浏览器复制 ID 找到 API 日志和异步触发的入队记录；用户 B 无法访问/修改 A 的资源；断网、上传失败、Token 失效、请求超时状态正确。

### W6｜Celery / SSE / 任务可靠性（18h）

- **学习范围**：业务状态机、幂等键、ack/retry、Worker 中断恢复、任务队列、SSE 分块/事件边界/断连资源释放。
- **实战产物**：任务提交、进度查询、SSE 展示；在隔离环境 kill Worker，模拟重投递与重复提交。
- **独立验收**：不重复副作用；重启后权威状态可查询；流断连/重连和缓冲均可复现并有测试。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

#### W6 补充：Worker 故障、业务幂等与 SSE 分块

**学时**：任务状态机 **6h** + 幂等/恢复 **6h** + SSE/状态同步 **4h** + 测试 **2h**。

权威状态在 PostgreSQL：`PENDING → QUEUED → RUNNING → SUCCEEDED/FAILED/CANCELLED`，需要重试时增加 `RETRY_WAIT`；Celery 内部状态不是业务状态机唯一来源。

- **实验 W6-A：隔离环境杀 Worker**：记录 ACK 配置、broker、任务 ID，在执行中终止 Worker/子进程，观察状态/消息重投递；比较 `acks_late`、`task_reject_on_worker_lost` 的行为及重复执行风险。**不能声称 `acks_late=True` 必然重投递**。
- **实验 W6-B：幂等重放**：连续点击、重复入队、并发 Worker 与失败重试；使用业务幂等键、唯一约束或可验证的去重策略，证明不存在重复扣费、重复记录或不可逆副作用。
- **实验 W6-C：SSE 分块/断连**：一个 `text/event-stream` 事件切成任意网络块，必须按空行拼出事件；模拟浏览器刷新、网络重连、代理缓冲、服务器取消、资源回收及节流渲染。
- `EventSource` 适合简单 GET 订阅、有浏览器原生重连，但不能任意增加 Header；`fetch + ReadableStream` 可定义方法/Header/请求体，却要自己处理事件缓冲、解析、重连。
- **验收**：浏览器关闭只终止该连接而非应继续运行的后台任务；重开后查询数据库任务状态；故障、幂等、SSE 负例均可复现。RAG 只接 Mock/已有服务。

### W7｜Docker / CI / 安全 / 部署（18h）

- **学习范围**：多阶段构建、Compose volumes/healthcheck、Nginx HTTPS、GitHub Actions、pytest/Playwright、越权/XSS/CSRF/上传安全、备份恢复。
- **实战产物**：从干净环境部署 web/api/worker/db/redis；CI；测试与恢复演练。
- **独立验收**：独立复现环境、通过核心测试；Secret 不入库；恢复和回滚有实际日志与版本。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

#### W7 补充：交付与恢复不能只看 compose up

**建议学时**：Docker/Compose **5h** + CI/测试 **5h** + Nginx/安全 **4h** + 备份/恢复/回滚 **4h**。

- Dockerfile 多阶段、镜像与 Volume/Network、Compose 健康检查与持久化；Nginx 反代、HTTPS/TLS、请求大小限制、合理超时。
- GitHub Actions Lint、Typecheck、Unit/Integration Test、Build；Pytest、Playwright E2E 与测试数据库隔离。
- Web 安全：XSS、CSRF、SQL 注入、文件上传限制、RBAC 与资源级越权；密钥不能提交公开仓。
- **实验 W7-A**：干净、授权的测试环境部署 web/api/worker/db/redis，初始化迁移、跑健康检查和 E2E。
- **实验 W7-B**：模拟数据库故障和配置错误；真实执行备份恢复、服务回退并保留回执。若无域名/证书等外部条件则标 BLOCKED，不冒充 HTTPS 已通过。
- **验收**：复现启动、测试、安全负例、恢复命令有证据。不能将“Compose 可启动”视为生产交付成功。

### W8｜性能 / 可观测性 / 系统设计（18h）

- **学习范围**：P50/P95/P99、负载模型与可复现基线、结构化日志、OpenTelemetry traceparent/Span、技术 ADR、独立答辩。
- **实战产物**：从浏览器到 API/Worker 的观测演示；负载分析；架构图/ERD/部署手册/演示。
- **独立验收**：报告包含环境并发/数据规模及前后对比；能独立定位慢请求、解释权衡并完成陌生变更。
- **证据**：实际 commit SHA、命令、环境、日志/测试输出、失败→修复对照；未运行写 `NOT_RUN`，不可预填 PASS。

#### W8 补充：性能基线、OpenTelemetry、技术答辩

**建议学时**：性能基线 **5h** + Metrics/Logs/Traces **4h** + 故障注入/性能优化 **5h** + 架构/答辩 **4h**。

- 固定测试机器、并发、业务请求分布、数据规模；报告吞吐、错误率、P50/P95/P99、CPU/内存与优化前后差异，不设无上下文的绝对 P95 目标。
- **最小 OpenTelemetry 实测是 W8/P1 必修**：至少跨一个后端服务或异步边界完成 Span/traceparent 传播、导出和查看，并用具体 Trace 定位慢请求。复杂仪表盘和广泛细粒度埋点可 P2 选修。
- 复现 SQL 慢查询、任务延迟、数据库不可用和 SSE 断流，在日志/Trace/指标里归因并复测。
- 输出架构图、ERD、API 契约/部署操作手册、性能/测试报告、ADR 和一场本人独立技术答辩。
- **验收**：严格按 [G01–G12](docs/learning/ACCEPTANCE.md) 逐项给真实证据；关键门槛未过必须记录 FAIL/PARTIAL 后返工，不能因到 W8 自动毕业。

## 4. 项目 MVP / P1 / P2

**设计目标目录、业务数据流、API 草案和按阶段演进见 [PROJECT-BLUEPRINT](docs/project/PROJECT-BLUEPRINT.md)**。业务代码目录尚不存在，不将蓝图视为已实现。

| 级别 | 功能 | 验收重点 |
|---|---|---|
| MVP（必须先完成） | 登录/登出、项目 CRUD、列表筛选分页、基础 RBAC、统一错误态 | 浏览器→API→DB 可见；403 越权负例 |
| P1（核心工程） | 上传、业务任务状态、Worker/Redis、SSE 进度、OpenAPI 自动化、数据库迁移、CI/部署 | 断连重连、重复提交、数据一致性、干净环境复现 |
| P2（可选扩展） | 真实 RAG 问答、高级 OpenTelemetry 仪表盘/深度追踪、额外性能专项、Next.js 或 Spring Boot | 真实业务/JD 触发，且不挤占必修验收 |
| P1（W8 必修补充） | 最小 OpenTelemetry Trace/Span 跨边界实测 | 不可由 Request ID 的日志关联替代 |

**不可提前将 Mock/API Stub/单次 CI 通过写作生产交付或个人独立能力达标。**

## 5. 每周节奏和验证协议

**详细 AI Coding 责任边界与 L1–L3 评分见 [AI-CODING-POLICY](docs/learning/AI-CODING-POLICY.md)**。生成文件≠测试通过≠本人独立掌握。

- 参考每周 18 小时：原理 3h、编码 9h、故障实验 4h、复盘 2h。按实际主题调整。
- 每个知识点：**原理→本人先写→故障注入→测试/排障→闭卷讲解→迁移复测**。
- 人的能力级别：L1 能解释；L2 能独立编写和测试；L3 能复现故障、归因、修复并说明取舍。**不等于** Dev-Workbench 的工程成熟度 L0–L6、也不替代 AI-Learning-OS 的 0–4 人工评分量表。
- 每周记录 [学习进度](docs/learning/PROGRESS.md)；使用 [实验模板](docs/learning/EXPERIMENT-TEMPLATE.md) 记测试命令、结果、环境、截图/日志定位、未验证项。
- 允许停止/延期：面试、工作交付、安全/成本、缺少环境与授权。优先真实业务和求职任务，不凭日历填“完成”。

## 6. 能力验收清单（总 Gate）

[最终 12 项可执行验收与证据模板](docs/learning/ACCEPTANCE.md) 使用 G01–G12 编号，与以下 12 项一一对应：

- [ ] **G01** React 登录、列表、表单、分页、错误态；竞态/取消行为有测试
- [ ] **G02** API Schema、后端 AuthN/AuthZ 与错误响应测试通过
- [ ] **G03** 导出 OpenAPI → Orval 生成 → TS 检查及 CI 漂移检查
- [ ] **G04** SQL 行锁/乐观锁/事务回滚和索引性能实验
- [ ] **G05** Redis 缓存失效/并发回源故障与保护实验
- [ ] **G06** Worker 中断、重试、去重、幂等与持久任务状态实验
- [ ] **G07** SSE 分块/断连/重连/取消与资源清理实验
- [ ] **G08** Request ID 日志关联；W8 最小 OTel Trace/Span 实测（必修）
- [ ] **G09** Compose 从新环境复现启动、健康检查、数据持久化
- [ ] **G10** CI、单元/集成、Playwright E2E 和服务端越权负例
- [ ] **G11** HTTPS、密钥隔离、备份/恢复及版本回退演练
- [ ] **G12** 架构/ERD/接口/部署文档；本人独立说明取舍与根因

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
## 9. 执行补充：唯一项目结构、评分与资料检索约定

- **唯一 Roadmap**：根目录 `ROADMAP.md`；不要另创建 `docs/learning/roadmap.md` 造成冲突。
- **唯一进度**：`docs/learning/PROGRESS.md`；当前所有周均 `NOT_RUN / UNASSESSED`。
- **唯一项目**：`ai-fullstack-workbench` 是计划中的应用工作目录，目标结构见 [完整项目蓝图](docs/project/PROJECT-BLUEPRINT.md)；今天没有创建应用功能代码。
- **参考字典**：[frontend](docs/learning/references/frontend.md) / [backend](docs/learning/references/backend.md) 按 Gap 查资料、做最小实验、回主线记录证据，不是第二/第三份进度计划。
- **AI 边界**：重点跨端状态、刷新并发、数据库锁/幂等、SSE 解析、Worker 恢复本人先写；CRUD/UI/测试/CI 框架可 AI 辅助，所有生成代码仍需运行与审查。参见 [AI-CODING-POLICY](docs/learning/AI-CODING-POLICY.md)。
- **L1/L2/L3**：L1 不看资料解释，L2 自己实现与测试，L3 故障注入/归因/修复/取舍；与上游 0–4 和 Dev-Workbench L0–L6 各自分离。
- **内容验收映射**：[V2.0 落盘覆盖矩阵](docs/quality/ROADMAP-COVERAGE.md)；这是文档核对，不是个人技能通过。
