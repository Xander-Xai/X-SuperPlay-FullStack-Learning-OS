# ai-fullstack-workbench：单项目全栈蓝图

> **DESIGN_ONLY / NO_APP_CODE / NOT_RUN**。这是唯一 ROADMAP 的项目设计附件，不是新的执行路线。本仓尚未生成下面的实际应用代码。所有测试只允许合成或明确获授权的数据。

## 项目目标

企业 AI 工作台纵切闭环：登录→项目管理/分页→文档上传→后端业务与权限→数据库→Celery 异步→SSE 进度→错误重试→部署/追踪与恢复。先普通 Web MVP，再强化可靠性，RAG 用 Mock/已有适配器，不重复造复杂 Agent 平台。

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
- **P2 选修**：真实 RAG、复杂观测仪表盘、Next.js/Spring Boot 深度与特殊架构扩展。

## 最终交付必须有真实证据

完整架构图、ER 图、接口 Schema、部署手册、E2E/安全负例、Worker 失败恢复、数据库并发、备份回滚、性能与 Trace、独立答辩。具体按照 [G01–G12](../learning/ACCEPTANCE.md) 逐项验收。不把本蓝图或学习项目自动当成 Utility-Sites 产品开工授权。
