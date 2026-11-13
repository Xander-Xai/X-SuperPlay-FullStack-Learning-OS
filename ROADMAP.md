# 全栈知识 Roadmap V4.2（整合上游资料）｜知识逻辑完整，按需求自由跳学

> **统一能力地图，不是按周通关日历。** 旧W1–W24保留知识覆盖坐标和可选引导式任务；原24周/432小时只是完整补基础的历史参考预算，**你实际学习什么、先学哪个模块，都由项目/JD/故障需求决定**。
>
> **先用[需求驱动入口](docs/learning/DEMAND-ROUTER.md)选择目标** → [知识依赖关系图](docs/learning/KNOWLEDGE-GRAPH.md)看技术作用与最小先修 → [权威资料](docs/learning/OFFICIAL-RESOURCES.md)查具体章节 → [模板](docs/learning/GAP-SESSION-TEMPLATE.md)真正编码/测试/复盘。下游覆盖见[能力覆盖矩阵](docs/learning/REQUIREMENTS-COVERAGE.md)。
>
> **实战载体不限定单个项目**：有权限的当前下游项目、隔离Labs、以及[ReconLab可选合成演示](ai-fullstack-workbench/README.md)均可。该演示CI通过不等于学习者独立掌握或ReconCheck获授权上线。

## 先在脑中建立技术的整体关系（不要求同时实作所有方向）

- **[一张全栈链路图 + 一张语言/框架树 + 一张请求时序图](docs/learning/FULLSTACK-MENTAL-MODEL.md)**：解释客户端、网络与API、后端、数据、异步、安全、CI与运维各自负责什么。
- **[42节点知识图](docs/learning/KNOWLEDGE-GRAPH.md)**、[42张专业+大白话学习卡](docs/learning/NODE-STUDY-CARDS.md)：含最低先修、官方原始资料、平行技术路线和具体上游讲解；不仅有React、FastAPI、Java，现已加入**Vue3/Nuxt、Node/NestJS、WebSocket、PWA、桌面Electron/Tauri、uni-app、Go/Rust/C++、MCP**等可选分支。
- **[20份上游 AI-Learning-OS 前后端原资料](docs/learning/UPSTREAM-ASSET-INDEX.md)**：复用已有[编程语言全景图](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)、Vue3+FastAPI案例、企业AI 18 Labs、Java专项、多端平台实训与评分规范。
- **[官方资料逐节点索引](docs/learning/OFFICIAL-RESOURCES.md)**：MDN、Vue、Nuxt、React、Next、Node、Nest、FastAPI、Spring、PostgreSQL、Go/Rust、平台文档等；根据本次问题选择具体章节。
- **[需求→知识→实验](docs/learning/DEMAND-ROUTER.md)**：项目需要Vue就查F08，需要Spring就查B04，需要MCP就查A02；不会的补最低先修，**不是必须花2–3个月从头按顺序学**。

### 前后端分层与技术选型的速记

| 层 | 它解决什么问题 | 常见技术分支 | 什么时候才需要研究 |
|---|---|---|---|
| 浏览器/UI | 用户看到、输入、交互和响应式 | HTML/CSS、JS/TS、Vue或React | 有Web页面时 |
| 应用渲染 | 页面在哪里生成、数据如何缓存 | Vue+Vite、React+Vite、Nuxt、Next | 需要SEO/SSR/混合渲染时按需 |
| 传输协议 | 组件与服务间怎么请求/推送数据 | HTTP/REST/OpenAPI、SSE、WebSocket、MCP(用于AI工具) | 依据同步、实时、双向/工具能力 |
| 业务后端 | 校验身份/业务、执行权限/规则 | Python/FastAPI、Java/Spring、Node/Nest、Go | 有服务端逻辑时按项目栈选 |
| 数据与异步 | 持久、缓存、检索、可靠事件 | PostgreSQL/MySQL、Redis、对象存储、向量检索、MQ、Worker | 真正需要数据/长任务/跨服务时 |
| 生产交付 | 质量/安全/部署/回滚与观测 | Git/CI、Docker/Linux、测试、OTel | 需要稳定维护/正式上线时 |
| 其他终端 | 桌面/小程序/移动/原生设备能力 | Electron/Tauri、uni-app、RN/Flutter、Kotlin/Swift | 终端或商店/本地系统能力要求触发 |

**技术定义**不能只靠比喻；**学习顺序**也不能由框架清单机械安排。每次先确定当前需求→专业原理和关系→官方资料→最小代码+负例→独立修复→回到业务。

**[AI-Native学习协议与可复制导师指令](docs/learning/AI-NATIVE-LEARNING-PROTOCOL.md)**：利用AI定位代码、写脚手架和测试骨架；本人决定业务/权限/正确性，亲手做负例和陌生约束复考。遇到问题先修当前Gap，不机械重复所有基础课程。

**严格验收**：只有每个节点同时具备专业定义、底层机制、大白话与适用边界、最小先修、具体官方小节、上游资料性质、动手实现与故障负例，才叫“资料能用”；详情见[42张知识卡](docs/learning/NODE-STUDY-CARDS.md)。阅读完仍不等于本人掌握。

## 0. 执行原则

- **学习地图是系统化的**：了解客户端/网络/API/业务/数据/异步/安全/部署每层的责任、关系、替代方案；W坐标只帮助查漏。
- **学习路径是动态的**：例如直接开始Spring MVC的B04，只先补B03最低Java语法；需要事务时再学D01/B05。不能要求必须学完W1–W11才能接Java岗位。
- **目标是能做下游多种产品**：静态站/SaaS/企业Web/小程序/移动App/AI应用/CLI等按实际技术与平台选择，不为一个产品强制装齐所有技术。
- **技术能力有证据**：每项通过原理L1→独立实现L2→故障诊断L3；证据与当前项目的交付验收分开，只有在本人实验后更新[PROGRESS](docs/learning/PROGRESS.md)。
- **参考体系**：W1–W24原有专题、专项字典和96个D1–D6任务仍保留，作为**可选查漏材料**而非必经顺序。
- **Java/Spring Boot 是知识地图的重要分支**：旧V3曾将W9–W13标为全量课程必修；当前V4.2不强制所有产品学习Java。只因岗位、既有系统或目标功能触发，直接跳进对应节点与最低先修。

## 1. 学习目标与非目标

- 目标：理解 **需求→设计→数据模型→API 契约→前端→后端→异步→测试→部署→观测→排障→复盘** 的责任关系；按当前产品需要独立实现、部署与维护相应部分，而不把单一工作台当唯一终点。
- 已有 Python/FastAPI/RAG/Agent 经验可快速诊断、跳过重复入门，但必须完成实际考核；不存在“做过项目=掌握”的自动豁免。
- 实战选项：当前有权限的产品或代码仓优先；也可以选择独立小实验，`ai-fullstack-workbench` 仅为本仓已有的合成核对**可选教材**，后续CSV/DB/Java等是该案例扩展思路，不绑定所有学习。
- 核心栈：React + TypeScript + Vite/React Router + TanStack Query/Tailwind/shadcn/ui；Python FastAPI/Pydantic/SQLAlchemy；**Java 核心/JVM/Spring Boot/Spring MVC/Spring Security/Spring Data**；PostgreSQL/Redis/Celery；OpenAPI/Orval；Docker/Nginx/CI/E2E。W9–W24 增加 Java/JVM、前端进阶、Node/SSR 原理和分布式可靠性。
- **Java/Spring、Next/Nuxt、Node/Nest 等均纳入地图**，不因技术范围广就强制一一安装/实作；有目标岗位/现有系统才进入对应专题。Kubernetes、复杂微服务与重复搭建RAG均由实质需求触发。
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

## 3. 历史知识组 A：W1–W8（覆盖坐标，按需跳学）

> 以下W1–W8为历史课程顺序，仅代表基础知识领域及其相关实验。可以直接按需求选其中W3、W6等；G01–G12是能力类别，而不是当前任务的前置锁。

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
- PostgreSQL 查询不能仅凭 HTTP Header 就自动串起，需要显式日志关联或 DB 客户端 tracing。**选择W5/W8整套旧课程时要求Request ID/结构化日志与OTel Trace；按当前任务只选择相关验证**。
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
- **如果选取原W8全面运维挑战，最小OpenTelemetry实测为其验收项**：至少跨一个后端服务或异步边界完成 Span/traceparent 传播、导出和查看，并用具体 Trace 定位慢请求。复杂仪表盘和广泛细粒度埋点可 P2 选修。
- 复现 SQL 慢查询、任务延迟、数据库不可用和 SSE 断流，在日志/Trace/指标里归因并复测。
- 输出架构图、ERD、API 契约/部署操作手册、性能/测试报告、ADR 和一场本人独立技术答辩。
- **验收**：严格按 [G01–G12](docs/learning/ACCEPTANCE.md) 逐项给真实证据；关键门槛未过必须记录 FAIL/PARTIAL 后返工，不能因到 W8 自动毕业。

## 4. ReconLab 可选教学案例：MVP / P1 / P2

**设计目标目录、业务数据流、API 草案和按阶段演进见 [PROJECT-BLUEPRINT](docs/project/PROJECT-BLUEPRINT.md)**。业务代码目录尚不存在，不将蓝图视为已实现。

| 级别 | 功能 | 验收重点 |
|---|---|---|
| MVP（必须先完成） | 登录/登出、项目 CRUD、列表筛选分页、基础 RBAC、统一错误态 | 浏览器→API→DB 可见；403 越权负例 |
| P1（核心工程） | 上传、业务任务状态、Worker/Redis、SSE 进度、OpenAPI 自动化、数据库迁移、CI/部署 | 断连重连、重复提交、数据一致性、干净环境复现 |
| P2（可选扩展） | 真实 RAG 问答、高级 OTel 仪表盘、完整 Next.js 迁移、NestJS/Vue/K8s 集群和其他专项 | 有真实业务/JD 触发才投入，Java/Spring旧W09–W13为覆盖坐标，现按需选择 |
| P1（W8 必修补充） | 最小 OpenTelemetry Trace/Span 跨边界实测 | 不可由 Request ID 的日志关联替代 |

**不可提前将 Mock/API Stub/单次 CI 通过写作生产交付或个人独立能力达标。**

## 5. 可选周节奏及按需实验验证协议

**详细 AI Coding 责任边界与 L1–L3 评分见 [AI-CODING-POLICY](docs/learning/AI-CODING-POLICY.md)**。生成文件≠测试通过≠本人独立掌握。

- 如选择连续课程，可参考每周18小时：原理3h、编码9h、故障实验4h、复盘2h。**真实需求驱动时按一次Gap任务安排学习时长，不强制凑满18小时。**
- 每个知识点：**原理→本人先写→故障注入→测试/排障→闭卷讲解→迁移复测**。
- 人的能力级别：L1 能解释；L2 能独立编写和测试；L3 能复现故障、归因、修复并说明取舍。**不等于** Dev-Workbench 的工程成熟度 L0–L6、也不替代 AI-Learning-OS 的 0–4 人工评分量表。
- 每周记录 [学习进度](docs/learning/PROGRESS.md)；使用 [实验模板](docs/learning/EXPERIMENT-TEMPLATE.md) 记测试命令、结果、环境、截图/日志定位、未验证项。
- 允许停止/延期：面试、工作交付、安全/成本、缺少环境与授权。优先真实业务和求职任务，不凭日历填“完成”。

## 6. 阶段 A 能力验收清单（G01–G12）

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
## 9. 历史单项目案例与评分约定（本仓不绑定唯一项目）

- **唯一 Roadmap**：根目录 `ROADMAP.md`，现覆盖 W1–W24；不要另创建 `docs/learning/roadmap.md` 造成冲突。
- **唯一进度**：`docs/learning/PROGRESS.md`；当前 W1–W24 均 `NOT_RUN / UNASSESSED`。
- **项目不是唯一**：`ai-fullstack-workbench` 已有可运行合成案例，只作为可选实验载体；真实需求优先选择有权限的下游项目或最小独立Lab。目标结构见 [案例蓝图](docs/project/PROJECT-BLUEPRINT.md)。
- **参考字典**：[frontend](docs/learning/references/frontend.md) / [backend](docs/learning/references/backend.md) 按 Gap 查资料、做最小实验、回主线记录证据，不是第二/第三份进度计划。
- **AI 边界**：重点跨端状态、刷新并发、数据库锁/幂等、SSE 解析、Worker 恢复本人先写；CRUD/UI/测试/CI 框架可 AI 辅助，所有生成代码仍需运行与审查。参见 [AI-CODING-POLICY](docs/learning/AI-CODING-POLICY.md)。
- **L1/L2/L3**：L1 不看资料解释，L2 自己实现与测试，L3 故障注入/归因/修复/取舍；与上游 0–4 和 Dev-Workbench L0–L6 各自分离。
- **内容验收映射**：[V3.0 落盘覆盖矩阵](docs/quality/ROADMAP-COVERAGE.md)；这是文档核对，不是个人技能通过。

## 十、V3.0 历史强化组（保留W09–W24作覆盖索引）

**原 V2.0 的 W1–W8 保留为第一阶段“端到端基线”，其学时、实验和 G01–G12 验收不重置。** 但它只覆盖 React/FastAPI 主链路，无法代表具备 Java/Spring 生态、成熟前端架构、复杂数据一致性与生产级交付的完整能力。V3.0 在**同一个 ROADMAP** 中继续 W9–W24，不另创建“Java 8 周”或“前端 8 周”竞争路线。

| 阶段 | 周次 | 目标 | 时间预算 | 过关含义 |
|---|---|---|---:|---|
| **A 基础纵切** | W1–W8 | 原 React+FastAPI+DB/Redis/Celery+部署 MVP | 8×18=**144h** | 能做基础前后端闭环，G01–G12 |
| **B 语言/框架深入** | W9–W16 | Java/JVM/Spring 完整基础，深入 HTML/CSS/TS/React 工程 | 8×18=**144h** | 能维护 Java API + 前端进阶，不靠教程照抄 |
| **C 多栈交付与架构** | W17–W24 | SSR/Node 原理、消息与一致性、安全/云/性能和最终答辩 | 8×18=**144h** | 两种后端协作 + 前端性能/跨端故障，G01–G24 |

**全覆盖历史参考预算**：24周/432小时（每周6天×3h）是自愿系统补课时的估算；**不是用户的执行顺序与强制学时**。新增 W09–W24 的 [6天×3h 详细执行手册](docs/learning/W09-W24-EXECUTION-PLAYBOOK.md)；开发环境需按 [工具版本约束](docs/learning/STACK-VERSION-POLICY.md) 选择和固定。它是学习与验收预算，不是“保证 24 周成为资深架构师”。岗位面试可按真实 JD 使用同一任务台账进行 **Gap Jump**：重排例如 W9 Java 基础 / W12 Spring API 的具体实验，仍需补回对应 Gate，不产生第二套计划。

### 十一、扩展后的技术能力地图

> 可通过 [能力矩阵](docs/learning/CAPABILITY-MATRIX.md) 按知识点快速反查周次、Gate 与专题字典。（每个方向都有最小实测）

| 能力域 | 必备知识（非仅会调用 SDK） | 学习周次 | 级别 |
|---|---|---|---|
| CS/Web | 网络/TLS/HTTP2-3基础、Cookie/缓存/浏览器渲染、Linux 进程/线程/内存/网络 | W1、W14、W22 | P0 |
| HTML/CSS/a11y | HTML 表单语义、布局/Flex/Grid/定位、CSS 层叠/响应式、键盘和可访问性 | W2、W14 | P0 |
| JS/TypeScript | 原型/闭包/Event Loop、ESM、泛型/映射类型、异常/异步取消、构建工具 | W1、W15 | P0 |
| React 工程 | Hooks/状态、Query/Mutation、表单、设计系统、性能分析、组件/E2E 测试 | W2、W16 | P0 |
| 渲染选型 | CSR/SSR/SSG/ISR、Next.js/RSC 边界、SEO、缓存失效 | W17 | P1（对比实验） |
| Node 后端基础 | Node Event Loop/Stream/背压/ESM、BFF/API、NestJS 认识 | W18 | P1（独立最小实验） |
| Java 核心 | OOP、集合/泛型/Stream、异常、Maven/Gradle、并发/JMM/虚拟线程/JVM/GC/JFR | W9–W11 | **按目标需求补齐** |
| Spring 生态 | IoC/AOP/MVC、Boot 自动配置、JPA/JDBC/MyBatis 对比、事务、Security、JUnit/Testcontainers | W12–W13 | **P0 必修** |
| Python 后端 | FastAPI、Pydantic、SQLAlchemy、依赖注入、Pytest、异步与 Worker | W3–W6 | P0（已有基础诊断可加速） |
| 数据与中间件 | PostgreSQL/MySQL SQL 差异、Redis、RabbitMQ/Kafka 二选一、Outbox/幂等/重试/一致性 | W4、W6、W19–W20 | P0+P1 |
| 接口与系统设计 | REST/OpenAPI/版本、OAuth2/OIDC、权限、事件契约、分层/边界、幂等、容量估算 | W3、W12–W13、W19–W24 | P0+P1 |
| 生产交付 | Git/测试/CI/CD、Docker/Nginx、Linux、监控/Traces/性能、安全、备份/恢复 | W7–W8、W21–W24 | P0+P1 |
| 选修生态 | Vue3 对比、GraphQL/gRPC 深挖、WebFlux、微服务拆分、K8s 集群、NoSQL/搜索 | 按真实 JD 触发 | P2 |

**P0/P1/P2 是全面能力地图的覆盖深度，不是所有项目共同的技术栈**。当前需求只有静态工具时，Java/Spring和消息队列不应变成上线阻塞。需求选择请以[需求路由](docs/learning/DEMAND-ROUTER.md)为准。这个优先级不代表全行业所有岗位的统一 JD。

### 十二、W9–W24 强化知识坐标（可任意选择专题）

> 周主题仅是索引；六天教学任务、先修、反例和DoD位于[旧版可选执行手册](docs/learning/W09-W24-EXECUTION-PLAYBOOK.md)。按需只做与当前功能有关的模块和最低先修，不要求6天打卡。

| 周次 | 核心模块 | 小时 | 交付与独立验收 |
|---|---|---:|---|
| W09 | Java 语言核心与工程环境 | 18h | 在同一 Workbench 新建 apps/java-service 草案；手写纯 Java 领域规则、CLI 和 JUnit 5；无需复制整个 FastAPI |
| W10 | Java 集合、Streams、常见设计模式 | 18h | 实现工作台任务去重/聚合与分页规则的纯 Java 模块；对照 HashMap 误用、空值、重键与等价比较 |
| W11 | Java 并发、JVM、数据库访问 | 18h | 制造共享计数器竞态，分别用锁/原子变量解决；对照虚拟线程与线程池 I/O 负载；用 JDBC 操作 PostgreSQL |
| W12 | Spring / Spring Boot Web API | 18h | 实现独立 Java 业务边界：通知/审计规则服务（或一个无需迁移的单独业务功能）；新建 Controller→Service→Repository；OpenAPI 暴露 API |
| W13 | Spring 数据、安全与集成测试 | 18h | Java 服务使用独立 schema/表和 Testcontainers PostgreSQL；资源权限 403、失败事务回滚、依赖测试；只深入实现 JPA 或 MyBatis 一条主路径 |
| W14 | HTML/CSS、浏览器布局与可访问性 | 18h | 将工作台后台页在桌面/移动端实现真实布局，独立修复 3 个溢出/焦点/表单问题；设计 Token 与暗黑模式可选 |
| W15 | JavaScript/TypeScript 深层与前端构建 | 18h | 实现类型安全组件表格与 API 错误模型；切换包大小/懒加载策略；分析 Network/Bundle 输出 |
| W16 | React 高级架构与前端测试 | 18h | 重构任务工作台为 feature slices；大列表虚拟化，Mutation 回滚与并发缓存；错误边界和表单/无障碍自动测试 |
| W17 | 渲染架构：SPA、SSR、SSG、Next.js | 18h | 在 Workbench 的 labs/rendering-comparison 创建最小公开页对比 Vite SPA 与 Next.js SSR/SSG；不替换主 Web 应用 |
| W18 | Node.js 运行时与 BFF/API 思维 | 18h | 用同一工作台合成数据做 Node 小 BFF/流式文件处理对比实验（单独 lab）；不再建第二套生产后端 |
| W19 | 消息系统与最终一致性 | 18h | 为 Java 服务与 Python 任务链设计一个可靠事件/审计链路，在独立 broker 测试环境跑 Outbox→消费→重复投递 |
| W20 | 数据库、缓存、搜索与分布式边界 | 18h | 跨 Python/Java 用同一 SQL 业务语义验证事务/约束；实现高并发分页与缓存失效；追加 MySQL SQL 方言对比卡 |
| W21 | 身份、授权与 API 安全进阶 | 18h | 通过合成租户/模拟 OIDC Provider 验证 Python+Java API 的服务端授权及服务间身份；模拟跨租户越权和 Token 过期 |
| W22 | Linux、云部署、基础设施与容灾 | 18h | 将主应用和 Java 可选服务使用 Compose profile 编排，构建可复现部署/恢复脚本；绘制单机→云环境演进图 |
| W23 | 性能、安全与可观测性深挖 | 18h | 制造三类性能问题（前端渲染/Java I/O/数据库），取浏览器、JFR 和 Span 对照；提出优化并复测 |
| W24 | 完整系统设计、跨语言集成与独立毕业验收 | 18h | 完成主 Workbench（React+FastAPI）与 Java 独立业务服务集成；一条前端→Python→消息/Java→DB→UI 的可观测纵切；答辩与故障恢复 |

#### W09｜Java 语言核心与工程环境（18h）

**必须掌握**：Java 21+ LTS/项目 JDK 冻结；Maven/Gradle 基础、包/模块、泛型、面向对象、异常、Record/枚举/注解、NIO/日期。

**同一个 Workbench 内的实验**：在同一 Workbench 新建 apps/java-service 草案；手写纯 Java 领域规则、CLI 和 JUnit 5；无需复制整个 FastAPI。

**独立验收**：本人解释 Java 与 Python 类型/异常差异；泛型/异常/边界测试可运行，提交准确 JDK 与构建版本。

**验收编号**：G13。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W10｜Java 集合、Streams、常见设计模式（18h）

**必须掌握**：List/Set/Map/HashMap、equals/hashCode、Comparable/Comparator、Streams/Optional、Lambda、接口分层、不可变对象；基础算法与复杂度。

**同一个 Workbench 内的实验**：实现工作台任务去重/聚合与分页规则的纯 Java 模块；对照 HashMap 误用、空值、重键与等价比较。

**独立验收**：集合正确性、复杂度与 Stream 副作用负例；可手写并测试 2 种数据结构方案。

**验收编号**：G13。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W11｜Java 并发、JVM、数据库访问（18h）

**必须掌握**：Thread/Executor/CompletableFuture、synchronized/volatile/Lock、线程安全、虚拟线程与阻塞 I/O、内存模型、堆栈/GC、JFR/jcmd、JDBC/HikariCP。

**同一个 Workbench 内的实验**：制造共享计数器竞态，分别用锁/原子变量解决；对照虚拟线程与线程池 I/O 负载；用 JDBC 操作 PostgreSQL。

**独立验收**：实际线程/GC/连接池日志；能解释吞吐≠延迟与虚拟线程适用边界；并发断言通过。

**验收编号**：G14。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W12｜Spring / Spring Boot Web API（18h）

**必须掌握**：Spring IoC/DI、Bean 作用域/生命周期、配置/自动装配、AOP/代理、Spring MVC DispatcherServlet、Filter/Interceptor、Validation、异常响应、Profiles/Actuator。

**同一个 Workbench 内的实验**：实现独立 Java 业务边界：通知/审计规则服务（或一个无需迁移的单独业务功能）；新建 Controller→Service→Repository；OpenAPI 暴露 API。

**独立验收**：异常/参数/依赖注入测试；对比 FastAPI Depends；能解释 Spring 代理、HTTP 请求路径。

**验收编号**：G15。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W13｜Spring 数据、安全与集成测试（18h）

**必须掌握**：Spring Data JPA/Hibernate、JdbcTemplate/JDBC、MyBatis 机制对比、N+1、事务传播/隔离、@Transactional 自调用、Spring Security FilterChain、认证与授权、JUnit/Mockito/Testcontainers。

**同一个 Workbench 内的实验**：Java 服务使用独立 schema/表和 Testcontainers PostgreSQL；资源权限 403、失败事务回滚、依赖测试；只深入实现 JPA 或 MyBatis 一条主路径。

**独立验收**：复现 @Transactional 不生效边界与 N+1；数据库集成测试必须使用真实 PostgreSQL 容器，不靠纯 H2。

**验收编号**：G16。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W14｜HTML/CSS、浏览器布局与可访问性（18h）

**必须掌握**：语义化 HTML、表单/Constraint Validation、CSS 层叠/特异性/布局流/定位/Flex/Grid、响应式/Container Queries、BEM/CSS Modules、a11y/ARIA/键盘导航、浏览器渲染流水线。

**同一个 Workbench 内的实验**：将工作台后台页在桌面/移动端实现真实布局，独立修复 3 个溢出/焦点/表单问题；设计 Token 与暗黑模式可选。

**独立验收**：390px/1280px 截图与键盘操作；表单标签/焦点/对比度检查；不得只依赖 Tailwind 现成类名。

**验收编号**：G17。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W15｜JavaScript/TypeScript 深层与前端构建（18h）

**必须掌握**：原型链/this/模块、闭包、事件循环与内存泄漏、TS 条件/映射/工具类型、unknown vs any、类型边界、pnpm workspace、Vite 打包/Tree-shaking/代码分割、Source Map。

**同一个 Workbench 内的实验**：实现类型安全组件表格与 API 错误模型；切换包大小/懒加载策略；分析 Network/Bundle 输出。

**独立验收**：TS strict 通过、无无理由 any；对比 JS 分包前后产物与实际加载；能解释 ESM 与打包机制。

**验收编号**：G18。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W16｜React 高级架构与前端测试（18h）

**必须掌握**：渲染与引用稳定性、useReducer/Context、状态分层、React Hook Form + Zod、TanStack Query/Table、Zustand/Redux 选择、Portal/Error Boundary、虚拟列表、Vitest/RTL/Playwright。

**同一个 Workbench 内的实验**：重构任务工作台为 feature slices；大列表虚拟化，Mutation 回滚与并发缓存；错误边界和表单/无障碍自动测试。

**独立验收**：React Profiler/组件测试证明优化前后；不为状态管理而状态管理；请求竞态和回滚负例通过。

**验收编号**：G19。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W17｜渲染架构：SPA、SSR、SSG、Next.js（18h）

**必须掌握**：CSR/SSR/SSG/ISR、SEO、Hydration、RSC 与 Client Components、App Router、Server Actions/Route Handlers、缓存和失效、跨层鉴权边界；Vue3 比较按岗位补充。

**同一个 Workbench 内的实验**：在 Workbench 的 labs/rendering-comparison 创建最小公开页对比 Vite SPA 与 Next.js SSR/SSG；不替换主 Web 应用。

**独立验收**：对比首屏、索引可达性、缓存、构建和部署复杂度；能画服务端/客户端数据和 Secret 边界。

**验收编号**：G20。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W18｜Node.js 运行时与 BFF/API 思维（18h）

**必须掌握**：Node Event Loop、libuv、Stream/背压、Buffer、ESM/CJS、npm/pnpm 安全与配置、Express/Fastify 最小 API、NestJS 概念；GraphQL/gRPC 与 REST 的选择。

**同一个 Workbench 内的实验**：用同一工作台合成数据做 Node 小 BFF/流式文件处理对比实验（单独 lab）；不再建第二套生产后端。

**独立验收**：验证 Streams 背压与异常传播，能解释与 FastAPI/Spring 的运行模型及部署差异；NestJS 非强制完整项目。

**验收编号**：G20。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W19｜消息系统与最终一致性（18h）

**必须掌握**：RabbitMQ 或 Kafka 二选一深入；消息 ACK、重投递、Consumer Group/Offset 概念、幂等消费、重试/DLQ、Outbox、事件 Schema/版本、失败恢复。

**同一个 Workbench 内的实验**：为 Java 服务与 Python 任务链设计一个可靠事件/审计链路，在独立 broker 测试环境跑 Outbox→消费→重复投递。

**独立验收**：服务断开/重复/乱序时不丢业务或无不可控副作用；有实际数据库与队列证据；不要求双学 Kafka/RabbitMQ。

**验收编号**：G21。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W20｜数据库、缓存、搜索与分布式边界（18h）

**必须掌握**：PostgreSQL/常见 MySQL 差异、索引/执行计划/事务对照、连接池/分页/键集分页、Redis 缓存一致性、容量与扩容、分布式锁风险；搜索 ElasticSearch 可按需。

**同一个 Workbench 内的实验**：跨 Python/Java 用同一 SQL 业务语义验证事务/约束；实现高并发分页与缓存失效；追加 MySQL SQL 方言对比卡。

**独立验收**：慢查询定位与容量估算，说明串行化边界/隔离策略；避免假设微服务可共写同一数据表。

**验收编号**：G21。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W21｜身份、授权与 API 安全进阶（18h）

**必须掌握**：OAuth2/OIDC、授权码+PKCE、Session/Refresh Token、CSRF/XSS/SSRF、RBAC/ABAC/多租户隔离、OWASP API Top10、审计、CSP、依赖/镜像漏洞、密钥轮换。

**同一个 Workbench 内的实验**：通过合成租户/模拟 OIDC Provider 验证 Python+Java API 的服务端授权及服务间身份；模拟跨租户越权和 Token 过期。

**独立验收**：越权/伪造/重放负例；证明角色权限不是前端控制；不自建安全协议或在公开库放 Secret。

**验收编号**：G22。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W22｜Linux、云部署、基础设施与容灾（18h）

**必须掌握**：Linux 进程/网络/文件权限/systemd、Nginx/反代/TLS、容器安全、CI/CD 工件/SBOM、环境/Secrets、备份/恢复、蓝绿/灰度；K8s 核心对象与调度概念（选修真机）。

**同一个 Workbench 内的实验**：将主应用和 Java 可选服务使用 Compose profile 编排，构建可复现部署/恢复脚本；绘制单机→云环境演进图。

**独立验收**：健康检查、回滚和数据恢复；资源/部署成本说明；K8s 不要求为学习故意建立复杂集群。

**验收编号**：G23。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W23｜性能、安全与可观测性深挖（18h）

**必须掌握**：Web Vitals LCP/INP/CLS、React Profiler、Bundle/瀑布图、JVM JFR/GC/线程、SQL/Redis/HTTP P95/P99、OpenTelemetry 跨 Python/Java trace、Prometheus/Grafana 概念、负载与容量测试。

**同一个 Workbench 内的实验**：制造三类性能问题（前端渲染/Java I/O/数据库），取浏览器、JFR 和 Span 对照；提出优化并复测。

**独立验收**：固定机器/并发/数据规模/环境；前后对照与失败日志真实存在，不能无条件宣称达某 QPS。

**验收编号**：G23。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

#### W24｜完整系统设计、跨语言集成与独立毕业验收（18h）

**必须掌握**：架构拆分边界、API/事件版本、Saga/Outbox、可维护性/成本、威胁建模、ADR、SLO/SLI、灾备/RTO/RPO、测试金字塔、产品演示与技术面试。

**同一个 Workbench 内的实验**：完成主 Workbench（React+FastAPI）与 Java 独立业务服务集成；一条前端→Python→消息/Java→DB→UI 的可观测纵切；答辩与故障恢复。

**独立验收**：按 G01–G24 清单复核，闭卷独立改一个陌生业务约束；不可用 Mock/文档替代运行验收。

**验收编号**：G24。必须提供 JDK/Node/前端版本、`repo@commit`、真实命令与原始日志、失败注入和本人独立说明；未执行写 `NOT_RUN`。

### 十三、可选跨语言案例架构（仅在选取该实验时适用）

- **W1–W8**：保持 React + FastAPI 单体分层纵向链路。
- **W9–W11**：在同仓 Java `labs/java-core` / `apps/java-service` 学语言和 JVM，不拆 Python 主业务。
- **W12–W13**：新增一个 **Java 专属业务边界**（例如审计/通知规则，不迁移现有项目 CRUD），有独立表、权限、集成测试，不双端同时写同一张表。
- **W17–W18**：Next.js/Node 仅为同仓 `labs/` 对比实验，不替换生产主前端、也不构造第二套重复的用户系统。
- **W19–W24**：只有在消息/跨服务实验需要时，通过 REST/受控事件连接 Python 与 Java；在 Compose Profile 中可单独启停。无服务间认证/超时/幂等/归属边界就不算通过。

单一应用蓝图见 [PROJECT-BLUEPRINT](docs/project/PROJECT-BLUEPRINT.md)；详细专题在 [前端字典](docs/learning/references/frontend.md) 和 [后端字典](docs/learning/references/backend.md)。

### 十四、全面知识覆盖挑战的可选毕业标准与证据规则

原 **G01–G12** 与 **G13–G24** 都保留为独立能力索引，不降级；全面覆盖时可以逐项验证，详见 [ACCEPTANCE](docs/learning/ACCEPTANCE.md)：
- **G13** Java 语言/集合/泛型/构建/设计规则；**G14** JVM、JMM/并发、JFR 与 I/O 负载；
- **G15** Spring Boot IoC/MVC/API；**G16** Spring Data/事务/Security/Testcontainers；
- **G17** HTML/CSS/响应式/a11y；**G18** JS/TS/ESM/Vite 构建与类型安全；
- **G19** React 架构/表单/状态/渲染性能；**G20** SSR/Next.js 与 Node runtime 比较；
- **G21** 中间件/事件投递/事务一致性/数据库差异；**G22** OAuth2/OIDC/多租户/OWASP；
- **G23** Linux/部署恢复/可观测性/前后端性能；**G24** 真正跨 Python+Java 的完整纵切、设计说明与独立变更。

**等级**：L1 关文档讲明原理；L2 独立编码/测试；L3 独立复现故障、定位根因、解释取舍并换场景复考。AI 生成初稿可加速，但不能代替个人独立验收。所有新增 Gate 初始 `NOT_RUN / UNASSESSED`，不能因为本次写入文档就判通过。

### 十五、官方资源补全

- [Dev.java General Tutorials](https://dev.java/learn/)：Java 语言、集合、泛型、Streams、并发、虚拟线程、JFR/JVM。
- [Oracle Java 25 Virtual Threads](https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html)：虚拟线程与性能、Pinned Threads；实际 JDK 以项目固定的受支持 LTS 为准。
- [Spring Boot Reference](https://docs.spring.io/spring-boot/reference/) + [Spring Security](https://docs.spring.io/spring-security/reference/) + [Spring Data JPA](https://docs.spring.io/spring-data/jpa/reference/)：IoC/MVC/数据/事务/认证鉴权。
- [Testcontainers Java + Spring Boot](https://testcontainers.com/guides/testing-spring-boot-rest-api-using-testcontainers/)：真实 PostgreSQL 集成测试。
- [MDN Core Web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core) + [Accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) + [Web Performance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance)：HTML/CSS/交互/性能基础。
- [React Learn](https://react.dev/learn) / [Next.js App Router](https://nextjs.org/docs/app) / [Node.js Learn](https://nodejs.org/en/learn)：状态、SSR/Server Components、Node 运行时。
- [Vitest](https://vitest.dev/guide/) / [Testing Library](https://testing-library.com/docs/react-testing-library/intro/) / [Playwright](https://playwright.dev/docs/intro)：前端单元、组件、E2E。
- [OWASP API Security](https://owasp.org/API-Security/) / [OpenTelemetry](https://opentelemetry.io/docs/) / [Docker](https://docs.docker.com/)：安全、观测与交付。

学习资源以**官方链接+手动实验**为主，不宣称所有文档已被完整阅读或最新版已在本地验证。课程实例、CLI 命令与依赖具体版本必须在开始实验时重新核对并锁定。
