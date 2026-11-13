# 全栈能力验收目录 G01–G24（按需求选择）

> 学员状态：**全部 NOT_RUN / UNASSESSED**。G01–G24是知识图谱覆盖的能力验证目录，**不是单个项目必须全部通过的列表，也没有G01→G24的强制解锁顺序**。当前需求选相关Gate，先满足目标模块最低先修，再本人实现/失败注入。参考[知识图](KNOWLEDGE-GRAPH.md)与[需求路由](DEMAND-ROUTER.md)；完成证据仍只记[PROGRESS](PROGRESS.md)。

| Gate | 要求 | 应保留的独立实验证据 | 必测反例 |
|---|---|---|---|
| G01 | React 登录/列表/表单/分页/路由、异步状态 | 浏览器/E2E、Query 状态、本人实现 | 断网、空值、快速切换、重复点击 |
| G02 | API 校验、异常、认证及资源级权限 | Pytest/响应/数据库状态 | 400/401/403、用户 B 越权 A |
| G03 | OpenAPI→Orval→Typecheck/CI 漂移 | 导出文件与生成命令、失败再修复日志 | 改响应字段后 TS 校验或契约测试暴露 |
| G04 | PostgreSQL 事务/并发/索引 | 双连接命令、无超扣断言、EXPLAIN 报告 | 丢失更新、锁等待/死锁、回滚 |
| G05 | Redis 热点失效保护 | 回源并发、QPS/延迟数据对照 | Key 集中到期后请求放大 |
| G06 | Celery 状态/幂等/Worker 恢复 | Worker 终止/重试和 DB 状态 | 重投递、重复副作用、悬挂状态 |
| G07 | SSE 分块/重连/取消/资源清理 | 任意 chunk 拆分、网络断连测试 | chunk≠event、代理缓冲、资源泄漏 |
| G08 | X-Request-ID 与最小 OTel Trace | Network→API/Worker 日志、traceparent/Span 导出 | UUID 存在但 Trace 没有跨度 |
| G09 | Compose 干净环境启动和持久化 | 环境/命令、Healthcheck、重启数据 | 缺失环境、容器重启丢数据 |
| G10 | CI/单测/集成/E2E/权限负例 | GitHub Actions 运行及 Playwright/Pytest | 仅 Mock 通过、服务端越权未测 |
| G11 | HTTPS/密钥/备份恢复/回滚 | TLS 与配置证据、恢复后的完整性 | Secret 泄漏、备份不可恢复 |
| G12 | 架构/ERD/API/部署/答辩 | 图文资料、问题回答、独立陌生约束复测 | 讲不清根因或 AI 代写含糊 |

## 状态与硬门槛

- `NOT_RUN` 未执行；`IN_PROGRESS` 正在做；`PARTIAL` 有缺失；`FAIL` 测试失败；`BLOCKED` 外部前提不足；`PASS_WITH_EVIDENCE` 真实命令、负例、解释和复测完整。
- 证据字段：测试日期、环境版本、`project_repo@full_commit`、命令/断言/原始日志路径、失败与修复、AI_ASSISTED/INDEPENDENT 范围、后续迁移复测日期。
- 任意未授权跨用户泄露、泄密、未批准外部写操作，或把 Mock/教程/CI 讲成真实生产交付，均不可判 PASS。
- W7/W8 的 HTTPS/生产就绪演练如缺域名或授权环境应标 BLOCKED，不可伪造已经上线的事实。

## 独立能力标准

L1=关文档能解释；L2=独立编码测试；L3=故障注入/定位/修复与取舍说明。与上游 AI-Learning-OS 的 0–4 独立量表，以及 Dev-Workbench 的工程成熟度等级各自独立。

每次记录可复制 [实验模板](EXPERIMENT-TEMPLATE.md)；学习状态只更新 [PROGRESS.md](PROGRESS.md)。

## V3.0 扩展 Gate：Java/Spring、前端深度、多栈工程

> G01–G12与G13–G24只区分历史写入阶段；不是当前的先后顺序。“必修”仅针对选择做全领域完整覆盖挑战，不能把Java/Spring等当所有业务应用的部署前提。

| Gate | 能力域 | 对应周次 | 必须留下的独立证据 | 反例/故障 |
|---|---|---|---|---|
| G13 | Java 语法/泛型/集合/构建 | W09–W10 | JUnit 对领域规则、泛型/Collection 进行实际测试 | equals/hashCode、Map 重复、Stream 副作用 |
| G14 | JVM/JMM/并发/JFR | W11 | 共享变量竞态修复、JFR 与虚拟线程 I/O 对照 | 可见性失效、连接池瓶颈 |
| G15 | Spring IoC/MVC/Boot | W12 | Java 独立业务域 Controller→Service→Repository 测试 | 错误 Bean、无效参数、统一异常 |
| G16 | Spring Data/Security/事务 | W13 | PostgreSQL Testcontainers、权限、事务、JPA/JDBC 测试 | @Transactional 代理失效、N+1、跨租户越权 |
| G17 | HTML/CSS/a11y/响应式 | W14 | 390px/1280px 布局、语义表单与键盘操作实测 | 溢出、无法聚焦、无 label |
| G18 | JavaScript/TypeScript/构建 | W15 | TS strict、ESM、Bundle 分析和懒加载对照 | unsafe any、错误打包或 Source Map |
| G19 | React 深层/表单/性能 | W16 | Profiler/Query 回滚/RTL+E2E 测试 | 旧状态覆盖、乐观更新回滚失败 |
| G20 | SSR/Next.js 与 Node Runtime | W17–W18 | SPA/SSR/SSG 比较 + Node Stream/BFF 最小实验 | Hydration、缓存泄密、Backpressure |
| G21 | 消息/数据库/Outbox | W19–W20 | RabbitMQ/Kafka 二选一、消费去重/延迟回放与 SQL 对照 | 消息重复/乱序、跨服务表所有权冲突 |
| G22 | OIDC/OAuth/租户安全 | W21 | PKCE/OIDC 认知、服务端授权与多租户 API 负例 | 凭证过期、B 用户越权访问 A |
| G23 | Linux/部署/性能/监控 | W22–W23 | Compose/恢复、JFR/Web Vitals/OTel Span 性能对照 | 慢前端、慢 SQL、服务中断/回滚失败 |
| G24 | 跨语言集成与系统答辩 | W24 | React→FastAPI→Java 业务域→DB→UI 可观测业务纵切 | 重复事件、Java 服务失败、无鉴权调用、无法独立排障 |

## 只有自愿全面覆盖挑战，才使用旧阶段毕业标准

- **阶段 A（W1–W8）**：G01–G12 均 PASS_WITH_EVIDENCE，只能说明 React+FastAPI 基础纵切达到本项目标准。
- **阶段 B（W9–W16）**：G13–G19 均有独立测试通过（Java Core/JVM/Spring 必修，HTML/CSS/TS/React 深化必修）。
- **阶段 C（W17–W24）**：G20–G24 全部真实执行；G01–G19 未回归失败，独立对陌生业务变更完成修复/复测，才能称路线毕业。
- **单个项目任务**：Next.js、Java/Spring、Celery等均按场景决定是否需要；若选择完整全栈知识覆盖挑战，相关专题应各自提供独立实验，但**当前下游应用上线验收由其真实需求/平台规范决定**。
- **证据**：`gate_id / repo@commit / tool_versions / commands / observed / negative_case / fix / AI_ASSISTED / INDEPENDENT / retest_date / state`。
- **硬失败**：越权、泄密、未经授权发布/跨仓修改、把模拟数据和 AI 生成代码当作真实客户或个人独立通过的证据。
