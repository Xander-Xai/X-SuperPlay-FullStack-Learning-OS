# 从一个需求到真正上线｜全栈工程交付链路与可选 AI 知识库案例

> **作用**：补足[42节点知识图](KNOWLEDGE-GRAPH.md)里“懂每层，却不会把系统交付出去”的跨层能力。不新增第二套课程或学习进度；按[需求路由](DEMAND-ROUTER.md)跳进所需阶段。真实应用发布由目标仓库与业务授权控制，本页只是**教学方案/验收设计**，不代表已经上线。
>
> 快捷入口：[专业+大白话全景图](FULLSTACK-MENTAL-MODEL.md) · [学习会话卡](GAP-SESSION-TEMPLATE.md) · [发布限制](../project/DOWNSTREAM-RELEASE-GATES.md) · [可选节奏](OPTIONAL-EXECUTION-MODES.md)。

## 一、全栈不是框架叠罗汉，而是连续的业务责任链

~~~mermaid
flowchart TD
  Need["用户问题 / 需求和验收AC"] --> Scope["明确权限、数据和失败边界"]
  Scope --> Design["系统设计 / ADR / 结构与数据流"]
  Design --> Contract["模型+约束+Migration+OpenAPI契约"]
  Contract --> Implement["浏览器/UI ↔ API/业务 ↔ SQL/缓存/异步"]
  Implement --> Verify["单测→集成→E2E→安全→故障/性能"]
  Verify -->|未通过| Design
  Verify -->|通过| Staging["隔离环境部署 / 迁移 / 备份恢复"]
  Staging --> Release{"获业务授权并通过上线Gate？"}
  Release -->|否| Verify
  Release -->|是| Production["正式发布 / HTTPS / 可观测性"]
  Production --> Feedback["SLO/错误/用户反馈→改进需求"]
  Feedback --> Need
~~~

**大白话**：业务需求是“要盖什么房子”，设计与数据模型是“承重图纸”，接口契约是“各施工队的统一尺寸表”，测试是“承重/消防试验”，部署与回滚是“正式交付和维修预案”。不能把“房子渲染图很好看”当作“可以让人居住”。

**专业边界**：这是反复迭代的过程，设计与编码通常交错进行；并非每个小工具都需要数据库、队列、AI或企业级基础设施。

## 二、阶段到知识点、产物、失败验证的一一映射

| 阶段 | 先问什么 | 最小产物 | 按需知识节点 | 必须核对的反例 |
|---|---|---|---|---|
| 1 需求 | 谁受益、何为成功、何为非目标？ | 用户故事、AC、风险与数据使用边界 | P01/P02 | 无权限、离线、重复提交是否有预期 |
| 2 架构 | 现有系统是什么、该不该加服务？ | 组件/数据流图、ADR、依赖边界 | P02/F01/B01 | 模块边界导致跨库事务怎么办 |
| 3 数据与契约 | 谁拥有数据、字段如何变更？ | ER图、Migration、约束、OpenAPI | D01/B01/B02 或 B04/B07 | 字段删除、N+1、越权ID |
| 4 UI与API | 加载、空、错、取消、冲突怎么展示？ | 可操作界面、表单、错误规范、服务端权限 | F02/F03/F04或F08/E03 | 逆序请求、会话过期、恶意文件 |
| 5 长任务（可选） | 是否必须离开请求线程继续运行？ | 任务状态机、重试/幂等记录、状态查询 | B06/D02/D03 | Worker死亡、重复投递、浏览器断开 |
| 6 测试 | 功能对了，失败时是否也正确？ | Pytest/Vitest/Playwright、权限及故障报告 | E01/E03/D01 | 权限伪造、事务冲突、依赖超时 |
| 7 部署 | 别人的干净机器能复现吗？ | Dockerfile/Compose、版本/密钥、迁移、手册 | E02/E05/P03 | 数据卷丢失、迁移失败、TLS错误 |
| 8 运行 | 变慢/报错时如何定位、回滚？ | 日志/指标/Trace、告警、备份恢复与成本记录 | E04/P03 | P95劣化、备份无法恢复、回滚不兼容 |

术语说明：**Router → Service → Repository → ORM/SQL** 是常见的职责划分，不是要求每个小接口都拆四层或十几类；事务边界需与业务原子性对齐，绝不能只看分层文件夹命名。

## 三、贯通案例：企业 AI 知识库“上传 PDF → 异步解析 → 问答”

> 这是**可选的业务场景**，用于展示跨层关系；学习仓并不为它或任何单一下游项目服务。简单网站、已有 Vue 后台、Spring 服务维护仍可选自己的真实场景。

~~~mermaid
sequenceDiagram
  autonumber
  participant Browser as Web/移动前端
  participant API as API服务
  participant DB as PostgreSQL
  participant Object as 对象存储
  participant Broker as 队列
  participant Worker as Worker/索引
  Browser->>API: POST 上传(登录凭证)
  API->>API: 认证、知识库资源授权、大小/类型/文件安全策略
  API->>Object: 安全存储原始文件/受限对象键
  API->>DB: 保存文件元数据和任务记录
  API->>Broker: 可靠调度（按需使用Outbox/重试协调）
  API-->>Browser: 202 Accepted + task_id + status_url（仅在已接受并可跟踪时）
  Worker->>Broker: 消费已接受任务
  Worker->>Object: 读PDF、解析与切块
  Worker->>DB: 更新可追踪的业务任务状态
  Worker->>Worker: Embedding / 安全索引
  Browser->>API: GET任务状态（或订阅SSE）
  API-->>Browser: 最新权威状态/允许的进度
  Browser->>API: 授权RAG问答请求
  API->>API: 知识库/文档粒度权限过滤、证据选择
  API-->>Browser: 答案或有依据的拒答
~~~

**先识别职责，不着急堆模型：** F04/F08 管界面状态；F01/B01 管 HTTP/契约；B02/B04 管服务端权限与业务规则；D01 管持久任务状态；D05 管PDF对象与搜索索引；B06 管Worker可靠性；F11 管展示进度所需的实时流；A01 管RAG证据质量；E01/E02/E04 管测试、发布和排障。

**专业注意事项：**
- HTTP 202 只表示请求已被接受处理，**不保证最终成功**。只有任务记录/调度状态已经被可靠接纳并可查询时，才按设计返回 202；如果对象写入、DB提交、队列投递之间存在跨资源一致性问题，要设计补偿/Outbox/重试，不可把三次调用当作单个事务。
- 上传的前端类型/大小验证仅改善体验；后端需验证身份、对象归属、扩展名与内容策略、尺寸/配额、恶意文档风险，不能信任客户端路径和MIME。
- PDF解析、切块、Embedding、向量写入要有**幂等键与索引版本策略**；Worker重新执行不应重复计费或把旧结果覆盖新版本。
- Redis可以用作缓存/队列底座，不能默认代替持久业务任务账本；SSE断连≠Worker应该被取消。
- 多用户RAG检索必须按授权范围过滤；“模型说可以读取”不是授权依据。查询日志/原文需脱敏。
- RAG属于可选业务功能，不等于做一个普通SaaS必须学习Agent或向量库。

相关官方起点：[FastAPI安全](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) · [FastAPI上传](https://fastapi.tiangolo.com/tutorial/request-files/) · [HTTP 202语义](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/202) · [Celery任务](https://docs.celeryq.dev/en/stable/userguide/tasks.html) · [PostgreSQL事务](https://www.postgresql.org/docs/current/transaction-iso.html) · [Playwright](https://playwright.dev/docs/writing-tests)。上游已有[企业AI Capstone](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md)与[LAB02 API](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md)、[LAB08数据库](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB08.md)、[LAB09权限](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB09.md)、[LAB11交付](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB11.md)，均作为参考而非本人已通过实验。

## 四、跨业务场景的 12 条交付核查（未执行、默认全部 UNASSESSED）

> **这是产品交付核查清单，不是新增的G25–G36考试，也不是自动记录的学习进度。** 具体任务按风险选相关项；若宣称完整SaaS上线则不可省略影响安全/数据/运营的关键项。

- [ ] DOD-01 新环境根据文档能够启动，依赖版本/密钥管理可复现。
- [ ] DOD-02 登录、退出、过期会话与服务器端拒绝可观察。
- [ ] DOD-03 A、B 两用户无法越权读取/修改对方资源（资源级授权）。
- [ ] DOD-04 CRUD/搜索/分页/校验在正常和异常条件下可证实。
- [ ] DOD-05 重复提交、并发事务不破坏数据/不会重复副作用。
- [ ] DOD-06 如有后台任务，状态可查询、失败可诊断、重试幂等；无后台任务标 N/A 并说明。
- [ ] DOD-07 单测+集成测试验证核心业务与权限边界。
- [ ] DOD-08 浏览器E2E验证一条关键真实用户路径。
- [ ] DOD-09 Compose/目标部署环境的持久化、健康检查、密钥隔离通过。
- [ ] DOD-10 CI自动执行格式/类型/构建/测试，失败能阻止发布。
- [ ] DOD-11 获批生产上线时才核验HTTPS、最小暴露面、日志/指标/告警。
- [ ] DOD-12 备份**恢复实测**、失败回滚/前后兼容、排障手册已验证。

证据写在当次[会话卡](GAP-SESSION-TEMPLATE.md)和真实工程 PR、CI / 演练记录；仅能确认“通过”的项附真实运行环境、commit、日志/结果。**本仓目前没有真实知识库 SaaS 生产上线证据，也未执行这12项。**

## 五、任务与技术的最短连接方式

- **只做静态格式转换站**：从 U01/F02/F03/E01 开始，缺账号/持久数据就不建数据库与Worker。
- **Vue管理后台**：从 F08、B01、E03 开始；已有API直接复用，不强行学React或Java。
- **接手Spring业务接口**：从 B03/B04 开始，用B05/D01只解决这次的事务/授权问题。
- **AI知识库**：从已会的Python接口出发，当前最缺哪一段（登录、上传、Worker或部署）就先做该段的失败实验。

**结束条件**：目标业务AC已运行通过、关键负例可复现与修复、本人能解释故障链路；其余未触发知识保持待查阅状态。