# ai-fullstack-workbench：单项目全栈蓝图

> **DESIGN_ONLY / NO_APP_CODE / NOT_RUN**。这是唯一 ROADMAP 的项目设计附件，不是新的执行路线。本仓尚未生成下面的实际应用代码。所有测试只允许合成或明确获授权的数据。

## 项目目标

企业 AI 工作台纵切闭环：登录→项目管理/分页→文档上传→后端业务与权限→数据库→Celery 异步→SSE 进度→错误重试→部署/追踪与恢复。先普通 Web MVP，再强化可靠性；W9–W24 在**同一个产品**中添加 Java Spring 的独立审计/通知业务边界，并做前端深入与体系化排障；RAG 用 Mock/已有适配器。不要为学两门后端语言而重复构建同一套业务。

## 目标目录（未来实现路径，不代表当前已经存在）

```text
X-SuperPlay-FullStack-Learning-OS/
├── README.md
├── ROADMAP.md                         # 唯一主线
├── docs/
│   ├── learning/
│   │   ├── PROGRESS.md                # 唯一状态
│   │   ├── ACCEPTANCE.md
│   │   └── references/
│   ├── architecture.md                # 待生成
│   ├── database.md                    # 待生成
│   ├── api.md                         # 待生成
│   ├── deployment.md                  # 待生成
│   ├── incidents.md                   # 待故障实验
│   └── decisions/
├── ai-fullstack-workbench/
│   ├── apps/
│   │   ├── web/                        # Vite/React/TypeScript
│   │   │   └── src/
│   │   │       ├── api/
│   │   │       │   └── generated/      # Orval 自动生成
│   │   │       ├── components/
│   │   │       ├── features/
│   │   │       ├── hooks/
│   │   │       ├── pages/
│   │   │       └── routes/
│   │   ├── java-service/               # W12+ Spring Boot 独立边界，非现存代码
│   │   │   ├── src/main/java/          # Controller/Service/Repo
│   │   │   └── src/test/java/          # JUnit + Testcontainers
│   │   └── api/                        # FastAPI
│   │       ├── app/
│   │       │   ├── routers/
│   │       │   ├── services/
│   │       │   ├── repositories/
│   │       │   ├── schemas/
│   │       │   ├── models/
│   │       │   ├── workers/
│   │       │   └── core/
│   │       ├── migrations/
│   │       └── tests/
│   ├── labs/                            # W9+ Java / Next SSR / Node 运行时的受控实验
│   ├── contracts/
│   │   └── openapi.json                # FastAPI 导出
│   ├── infra/
│   │   ├── nginx/
│   │   └── compose.yaml
│   ├── e2e/                             # Playwright
│   └── .env.example
└── .github/workflows/                 # W7 CI，尚未实现
```

实际完整路径示例（方便检索）：`ai-fullstack-workbench/apps/web`、`ai-fullstack-workbench/apps/api`、`ai-fullstack-workbench/contracts/openapi.json`、`ai-fullstack-workbench/infra/`、`ai-fullstack-workbench/e2e/`。

**注意**：用户示意图中 `docs/learning/roadmap.md` / `progress.md` 与本仓已存在的根目录 `ROADMAP.md` / `docs/learning/PROGRESS.md` 只取一份。这里以现存根目录 Roadmap、学习目录进度为权威，不复制第二套文件。

## 端到端数据流

```text
React UI / TanStack Query
   ↓ 生成的 TypeScript API client（OpenAPI/Orval）
Nginx HTTPS → FastAPI Router / 认证/资源授权
   ↓
Service → Repository → PostgreSQL（任务状态唯一权威）
   ├── 文件对象存储（验证大小/类型/权限）
   └── Celery 入队 → Redis Broker → Worker → DB 更新
                    ↓
       API 查询/事件流 → React 状态展示
```

文件上传通常先完成权限和文件大小/类型/路径安全校验；原始对象文件与数据库元数据区分管理。任务创建返回 `202 Accepted` + 任务 ID（如异步接受），前端断线后从 DB 查询真实状态，不依赖 SSE 保留在内存中的状态。

## 数据模型草案

| 实体 | 主要字段 | 核心约束 |
|---|---|---|
| users | id、登录名、password_hash、状态 | 禁止明文密码/敏感日志 |
| projects | id、owner_id、name、updated_at | 服务端按归属/成员鉴权 |
| documents | id、project_id、object_key、status | 文件元数据/对象存储分离 |
| tasks | id、project_id、document_id、status、idempotency_key、run_id、retry_count | 唯一键+事务+任务状态机 |
| task_events（可选） | task_id、sequence、event_type、timestamp | SSE 恢复/事件顺序 |
| audit_logs（可选） | actor、resource、action、request_id、timestamp | 不存密钥或不必要个人数据 |

## API 契约草案（非已实现 API）

| 方法路径示例 | 业务 | 失败/权限测试 |
|---|---|---|
| POST /api/auth/login、/logout | 登录/登出 | 无效凭证、过期、CSRF |
| GET/POST /api/projects | 列表/新增项目 | 过滤、分页、越权 |
| PATCH/DELETE /api/projects/{id} | 修改/删除项目 | 用户 A/B 隔离、并发 |
| POST /api/projects/{id}/documents | 上传文件 | 大小/类型/无权上传 |
| POST /api/projects/{id}/tasks | 创建异步任务 | 幂等重放、202+task_id |
| GET /api/tasks/{id} | 查询业务权威状态 | 资源权限、任务丢失 |
| GET /api/tasks/{id}/events | SSE 进度 | 断连/重连/资源回收 |

真实类型以 FastAPI 生成且由 CI 固定的 `contracts/openapi.json` 为唯一来源，不能手写前端重复维护字段。

## MVP/P1/P2 验收定位

- **MVP**：登录/项目 CRUD/分页/表单/服务端权限、错误态；主链路浏览器→API→DB。
- **P1 必修**：上传、Celery/Redis、SSE、幂等、OpenAPI/Orval、迁移、Compose/CI/测试、Request ID 和 W8 最小 OpenTelemetry Trace。
- **W9–W24 必修拓展**：Java Core/JVM/Spring Boot 独立业务服务；前端 HTML/CSS/可访问性、JS/TS、React 架构性能、Next SSR 对比、Node Runtime 及可靠消息/一致性。**Spring Boot 不再归入 P2。**
- **P2 选修**：真实 RAG、复杂观测仪表盘、完整 Next.js 框架替代、Kubernetes 集群与特殊架构扩展。

## 最终交付必须有真实证据

完整架构图、ER 图、接口 Schema、部署手册、E2E/安全负例、Worker 失败恢复、数据库并发、备份回滚、性能与 Trace、独立答辩。具体按照 [G01–G12](../learning/ACCEPTANCE.md) 逐项验收。不把本蓝图或学习项目自动当成 Utility-Sites 产品开工授权。

## V3.0 扩展：Java/前端/跨运行时集成边界

- Phase A：`apps/web` React SPA + `apps/api` FastAPI 是唯一基础产品主链路。
- Phase B：`labs/java-core` 训练语法/集合/JVM 并发；`apps/java-service` 使用 Spring MVC + Security + PostgreSQL **独立 schema/表**，拥有审计/通知等清晰单一业务职责。Java 服务不得直接绕过 Python 域的 Repo 改写其表。
- Phase C：`labs/rendering-comparison` 只比较 SSR/SPA/Next 服务边界；`labs/node-runtime` 比较 Node event loop、Streams 与 BFF。两者不建设独立生产业务。
- 一次完整集成：React → Python API → 消息/Java 独立职责 → DB 状态更新 → 前端查询；必须包含双方鉴权、超时、幂等与 Trace/日志关联。Kafka/RabbitMQ **选择一种**作为高级消息实验，不要求重复引入两种。
- 配置：Java 服务通过可选 Compose profile 启停。W8 基线不需要 Java 运行才能启动；W24 多栈答辩则需要有实测 Java 服务。
- 数据：同一数据库服务器可以用**独立 schema / ownership** 学习；不要让两个服务在没有所有权规则下同时更新同一业务表。
- 目标项目目录是**规划**，不是已经实现。所有新实验仍状态 `NOT_RUN`。
