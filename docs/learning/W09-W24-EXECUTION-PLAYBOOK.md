# 历史W09–W24六日任务模板（按需选择，不强制顺序）

> **历史V3手册；现行治理见[ADR-0004](../decisions/ADR-0004-fullstack-foundations-and-authority.md)**。此手册中的“必修/先修验收”只针对**自主选择做完整W09–W24全覆盖挑战**，并非当前所有项目/岗位的强制先修；按需先修请查[知识图](KNOWLEDGE-GRAPH.md)。

> **OPTIONAL_GUIDED_SPRINT / LEARNER_NOT_RUN**。本文件保留旧24周课程中W09–W24的96个D1–D6实验，可在需要系统补课时择取。**当前主入口为[需求驱动学习](DEMAND-ROUTER.md)**：选目标模块→补最小先修→官方资料→真实实验，不必整周/整月按顺序执行。

## 使用说明（选择本模板时才执行）

- 每周参考 D1–D6，共 **18 小时**；每天 3 小时，默认理论/本人编码/负例复盘穿插执行。允许因面试调序，但必须记录 `reorder_reason`，不能跳过证据。
- 旧手册中的先修表属于**完整课程建议**。需求驱动执行时以[知识图的requires](KNOWLEDGE-GRAPH.md)为最低先修；不要求把W09/W10全部通过才能开始W12的最小Spring API。
- **最低必须交付**：一份可运行代码/配置、至少一个失败场景、修复前后证据、本人独立讲解、原始工具和版本命令；P2 选修不得挤占本周最低门槛。
- 各天默认是 3h 时间盒，未完成则标 `PARTIAL` 并推迟，不能将被迫剪掉的测试当 PASS。
- 具体需求会话与独立证据汇总到唯一[PROGRESS](PROGRESS.md)，Gate索引见[ACCEPTANCE](ACCEPTANCE.md)。选择全课程学习时可用周级DoD；按需求学习时只验证本次目标范围，不强制无关周。

## 基线与就业优先策略

- **W1/W2 前置保护**：尽管 CSS 深挖安排 W14，HTML 表单/语义、CSS 盒模型/Flex/Grid/响应式必须先在 W1/W2 学到能使用，不能完全等到 W14。
- **Java 岗位 Gap Jump**：若真实 JD 迫切需要 Java/Spring，可以先执行 W09 基线，再做 W12 最小 API 与 W13 安全/事务；W10/W11 的并发/JVM 和 W14–W24 原计划任务仍在 PROGRESS 中标 NOT_RUN，不宣称掌握。
- **项目集成**：W09–W11 独立 Java 核心实验；W12–W13 建受控 Java 业务边界；W19–W23 逐步集成，W24 只做收口和独立答辩，不允许 W24 从零搭建整个跨语言系统。
- **轻量基础加练**：数据结构/算法、Linux、TCP/HTTP、Git PR/Code Review 每周可额外安排 20–30 分钟用于面试补弱，不挤占必修 18h 的核心故障实验；这种加练不另建路线。

### W09｜Java 核心与工具链（18h；G13）

**先修验收**：能完成 W3/FastAPI 路由与基础 OOP；安装经核实的 JDK + Maven/Gradle

- **D1 / 3h**：选 LTS JDK/构建工具、运行 hello + JUnit，锁定版本
- **D2 / 3h**：类/接口/抽象、多态、包与可访问性
- **D3 / 3h**：泛型边界、record/enum/注解，编译不合法泛型案例
- **D4 / 3h**：checked/unchecked exception、try-with-resources、IO/NIO
- **D5 / 3h**：实现与 Workbench 任务相关的纯 Java 领域规则
- **D6 / 3h**：新增异常/空输入失败测试，关 AI 解释 Python 与 Java 差别

**本周 DoD（完成条件）**：Java 项目构建成功且含独立 JUnit 反例；记录 java -version、mvn -v、commit。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W10｜Java Collections / Stream / 基本算法（18h；G13）

**先修验收**：W09 的 JUnit 项目可运行

- **D1 / 3h**：List/Set/Map/HashMap/equals/hashCode 与冲突分析
- **D2 / 3h**：Comparator/Comparable、泛型 PECS、不可变对象
- **D3 / 3h**：Lambda/Stream/Optional、空值与重复 Key
- **D4 / 3h**：简单算法/数据结构复杂度，时间与空间 O 表示
- **D5 / 3h**：实现业务任务去重、分组、排序、分页规则
- **D6 / 3h**：复现错误 hashCode、并行 Stream 副作用、边界测试

**本周 DoD（完成条件）**：去重规则的多输入断言 + HashMap 失败/修复；能说明算法复杂度和 Stream 适用边界。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W11｜并发 / JMM / JVM / JFR（18h；G14）

**先修验收**：W09–W10 Java 领域模块和运行环境

- **D1 / 3h**：Thread/Executor/CompletableFuture 与线程池队列
- **D2 / 3h**：synchronized/volatile/Atomic/Lock，构造竞态
- **D3 / 3h**：JMM 可见性/有序性、ThreadLocal/上下文泄漏
- **D4 / 3h**：堆/栈、类加载、GC 日志、jcmd/thread dump
- **D5 / 3h**：Virtual Threads vs Platform Threads I/O 实验、JDBC/HikariCP
- **D6 / 3h**：JFR 定位阻塞与连接池瓶颈，对比修复前后

**本周 DoD（完成条件）**：保存 race 的失败/修复测试、JFR 或 jcmd 证据和固定负载数据，不把虚拟线程写成 CPU 加速器。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W12｜Spring Boot / IoC / MVC（18h；G15）

**先修验收**：W11 基础完成；明确 Java 只拥有审计/通知等独立业务域

- **D1 / 3h**：用版本锁定的 Spring Initializr 建 API 工程
- **D2 / 3h**：Bean IoC/自动配置/生命周期，构造 Bean/配置错误
- **D3 / 3h**：Spring MVC DispatcherServlet、Filter/Interceptor、校验
- **D4 / 3h**：Controller→Service→Repository 领域边界与异常统一响应
- **D5 / 3h**：生成 Java OpenAPI 规范，编写 MockMvc/JUnit 测试
- **D6 / 3h**：关 AI 复现无效请求与 Bean 代理差异，出结构图

**本周 DoD（完成条件）**：独立可启动 Spring API、400/403/500 负例和 IOC/代理讲解；不重复 FastAPI 项目 CRUD。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W13｜Spring Data / 事务 / Security（18h；G16）

**先修验收**：W12 Java 独立业务域和 PostgreSQL 测试容器可用

- **D1 / 3h**：PostgreSQL Testcontainers、JDBC/HikariCP 建连
- **D2 / 3h**：JPA/Hibernate 映射与 N+1，MyBatis/JDBC 对照但只选一条主实现
- **D3 / 3h**：@Transactional 代理、自调用、隔离/传播及 rollback
- **D4 / 3h**：Spring Security FilterChain、AuthN/AuthZ/用户隔离
- **D5 / 3h**：JWT/Cookie/CSRF 具体攻击面，权限负例
- **D6 / 3h**：用真实 DB 容器完成事务/锁/越权测试与复盘

**本周 DoD（完成条件）**：JUnit+Testcontainers 通过且有 N+1、自调用事务及 A/B 越权的负例原始日志。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W14｜HTML / CSS / 可访问性（18h；G17）

**先修验收**：W2 SPA 已有可用表单；若未学 HTML/CSS，则在 W1/W2 补最低限基础

- **D1 / 3h**：语义化 HTML5、form/label/keyboard、ARIA 最小使用
- **D2 / 3h**：CSS 盒模型、层叠/Specificity/继承/定位
- **D3 / 3h**：Flex/Grid/Responsive/Container Queries，390px 布局
- **D4 / 3h**：表单校验、焦点管理、错误提示和模态框
- **D5 / 3h**：DevTools DOM/CSSOM/Layout/Paint 观察和主题变量
- **D6 / 3h**：移动/桌面宽度+键盘完整操作录制、修复溢出

**本周 DoD（完成条件）**：工作台在两种宽度可用、表单键盘可访问；至少 1 个失效焦点和布局错误有修复证据。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W15｜JS / TS 深层与构建（18h；G18）

**先修验收**：W1 request<T> 和 W2 React 工作台

- **D1 / 3h**：JS 原型、this、闭包、事件循环和内存问题复现
- **D2 / 3h**：TS 泛型/条件/映射/unknown/never/strict 类型
- **D3 / 3h**：ESM/CJS 与 pnpm workspace/package resolution
- **D4 / 3h**：Vite Bundle/Source Map/Tree-shaking、静态和动态 import
- **D5 / 3h**：优化一个慢加载路由、进行 JS chunk 分析
- **D6 / 3h**：运行 typecheck/build，对比包大小/瀑布图/错误边界

**本周 DoD（完成条件）**：TS strict 可复现、无盲目 any，记录优化前后加载数据及构建命令。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W16｜React 进阶架构与性能（18h；G19）

**先修验收**：W2 基础 UI 和 W5 API 联调已运行或有等价纵切实验

- **D1 / 3h**：状态快照/组件身份/Effect Cleanup 竞态复现
- **D2 / 3h**：Local state、Context、Query server state 的边界重构
- **D3 / 3h**：React Hook Form/Zod 和 TanStack Table 真实表单/分页
- **D4 / 3h**：Mutation/乐观更新/回滚及 Error Boundary
- **D5 / 3h**：React Profiler 大表渲染/虚拟列表/必要 memo
- **D6 / 3h**：Vitest + React Testing Library + Playwright 负例与复盘

**本周 DoD（完成条件）**：保留 Profiler 对比、Query 回滚和无障碍/异常测试，不以 UI 截图代替功能验收。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W17｜Next.js SSR/CSR/SSG 比较（18h；G20）

**先修验收**：W16 React API/组件模型和 W15 ESM/打包理解

- **D1 / 3h**：讲解 CSR/SSR/SSG/ISR 与 SEO/初始加载
- **D2 / 3h**：Next App Router，Server/Client Components/RSC
- **D3 / 3h**：Hydration/Server Actions/Route Handlers 边界
- **D4 / 3h**：制作与 Vite 共用合成内容的最小公开页
- **D5 / 3h**：比较缓存失效、身份/Secret 边界与部署成本
- **D6 / 3h**：真实对比首屏/网络请求和故障，形成 ADR

**本周 DoD（完成条件）**：最小 Next demo 只作 lab；不能无实验宣布 SSR 必更快；主 SPA 不迁移。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W18｜Node.js 与 BFF/流（18h；G20）

**先修验收**：W15 JS Event Loop/ESM，W17 渲染边界

- **D1 / 3h**：Node libuv/Event Loop、Buffer/事件/错误传播
- **D2 / 3h**：Node Stream/backpressure、Readable/Writable
- **D3 / 3h**：ESM/CJS、Process/env/依赖安全和 pnpm
- **D4 / 3h**：Express 或 Fastify 建最小 BFF/API，了解 NestJS
- **D5 / 3h**：大文件流与客户端中断/背压实验
- **D6 / 3h**：与 FastAPI/Spring 性能模型和部署边界进行对照

**本周 DoD（完成条件）**：Node 负载实验可复现；描述 BFF 适用边界，不构造第二套完整生产后端。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W19｜消息队列与可靠事件（18h；G21）

**先修验收**：W6 Celery ACK/幂等、W13 Java 独立域、W4 DB 事务

- **D1 / 3h**：选 RabbitMQ 或 Kafka 一个进行深入并固定版本
- **D2 / 3h**：消息确认、重投递、重试、DLQ/Consumer 模型
- **D3 / 3h**：业务 DB Transactional Outbox 设计与表结构
- **D4 / 3h**：Java 或 Python 消费者幂等键/唯一约束
- **D5 / 3h**：模拟消费者断开、重复/乱序消息及恢复
- **D6 / 3h**：检查任务与事件一致性，绘制失败路径和补偿表

**本周 DoD（完成条件）**：一条真实 Outbox→Broker→Consumer 运行路径+重复投递不重复副作用的测试；另一套 MQ 只做对比。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W20｜SQL/缓存/数据边界（18h；G21）

**先修验收**：W4 PG 双连接实验、W19 消息事件模型

- **D1 / 3h**：PG 索引/锁/EXPLAIN 与连接池复盘
- **D2 / 3h**：MySQL/InnoDB 事务/隔离/索引和 PG 差异
- **D3 / 3h**：同表查询分页：offset 与 keyset 的对照
- **D4 / 3h**：Redis TTL/更新/缓存一致性、失效压力
- **D5 / 3h**：模拟两个服务无边界修改表导致竞争，并设计禁止共享写权
- **D6 / 3h**：给出容量估算、DB/缓存/消息失败时一致性取舍

**本周 DoD（完成条件）**：真实查询计划和 MySQL/PG 方言对比；服务表所有权和错误重试规则明确。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W21｜OAuth2/OIDC / AuthZ / API 安全（18h；G22）

**先修验收**：W5 Cookie/Session/CSRF、W13 Spring Security

- **D1 / 3h**：OAuth2/OIDC/PKCE/Refresh 的角色与流转图
- **D2 / 3h**：对合成用户/租户定义 RBAC/ABAC 与资源边界
- **D3 / 3h**：服务间身份与 Token 验证，拒绝未知观众
- **D4 / 3h**：API 错误暴露/XSS/CSRF/SSRF/依赖漏洞分析
- **D5 / 3h**：越权/伪造过期令牌/跨租户 API 负例与日志脱敏
- **D6 / 3h**：复测修复，留下威胁建模和安全验证清单

**本周 DoD（完成条件）**：用现成可信 IdP 或 Mock OIDC 进行受控测试，不自己设计 OAuth 协议；越权、过期 token 无法通过。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W22｜Linux、部署/CI/恢复（18h；G23）

**先修验收**：W7 Compose 的部署/恢复最小演练

- **D1 / 3h**：Linux 进程/网络/权限/systemd/服务排障
- **D2 / 3h**：Compose profiles 为 Java 服务按需启动、健康检查
- **D3 / 3h**：Nginx HTTPS/TLS、Secrets、镜像标签与 SBOM 概念
- **D4 / 3h**：GitHub Actions Java+Python+前端多栈矩阵与版本固定
- **D5 / 3h**：一次带备份的失败部署/数据恢复/回滚
- **D6 / 3h**：写单机→云架构图、成本与故障风险，不强制 K8s 真机

**本周 DoD（完成条件）**：可重复的多栈部署/回滚/恢复证据；未取得域名/证书须注明本地 TLS 验证范围。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W23｜前后端性能/可观测性（18h；G23）

**先修验收**：W8 OTel 最小 Span、W11 JFR 基础、W16 React Profiler

- **D1 / 3h**：明确 SLO、基线负载、机器/数据规模
- **D2 / 3h**：Web Vitals LCP/INP/CLS 与性能瀑布/组件 Profiler
- **D3 / 3h**：JVM JFR/GC/线程池和 Java 数据库调用
- **D4 / 3h**：PG/Redis/API tracing、Python/Java 上下文传播
- **D5 / 3h**：注入 3 个慢点（前端/Java I/O/SQL），归因
- **D6 / 3h**：优化前后重复压测、写 P50/P95/P99 与资源图

**本周 DoD（完成条件）**：可观察 Trace/原始指标/环境记录，性能改善有重复试验依据而非无条件 QPS 宣传。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

### W24｜跨语言纵切/毕业答辩（18h；G24）

**先修验收**：G01–G23 各必要模块已运行；本周是集成收口，非从零写全部服务

- **D1 / 3h**：冻结版本/API/事件 Schema，制定端到端场景
- **D2 / 3h**：React→FastAPI→Java 专属职责→DB→UI E2E
- **D3 / 3h**：注入服务挂掉/重复事件/身份失败/Schema 改动
- **D4 / 3h**：综合运行 G01–G23 高风险回归与部署恢复
- **D5 / 3h**：生成架构/ERD/API/安全/性能报告与 ADR
- **D6 / 3h**：关 AI 对陌生业务变更独立修复，完成答辩

**本周 DoD（完成条件）**：真正跨进程可运行并能复现故障；任何既有 Gate 不达标标 PARTIAL，不能仅因 W24 到期毕业。

**证据**：提交 `repo@full_sha`、命令与工具版本、原始输出/截图、预期与实际、至少一个失败→修复记录、AI 辅助与本人独立部分。

## 课程范围清单

- **仅限自选旧全量覆盖挑战的内部必做专题**：Java Core/JVM/Spring Data/Security；HTML/CSS/a11y、TS/React、Next SSR/SPA 原理、Node 最小 BFF、消息一致性、OAuth/OIDC、Linux/性能/安全/跨语言纵切。
- **按需选修**：把主 SPA 整体替换 Next、Vue3/Nuxt 深度、NestJS 全套、WebFlux/Spring Cloud 复杂微服务、K8s 生产级集群、Kafka/RabbitMQ 两种全套、Mongo/ES。除非目标岗位明确需要。
- **现实能力层级**：此计划旨在建立可证明的实战能力，不承诺 432h 就具备多年大型企业分布式系统经验。
