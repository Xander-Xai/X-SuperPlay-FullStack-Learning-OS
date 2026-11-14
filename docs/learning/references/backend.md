# 后端专项深挖字典 V4.2：Java/JVM/Spring + Python + 数据/架构

> **2026新增可查入口**：[后端/数据/部署高频细节](../DETAIL-GAP-INDEX-2026.md)、[20道工程面试题](../INTERVIEW-ENGINEERING-DRILLS.md)、[按需求到交付的完整链路](../DELIVERY-LIFECYCLE.md)。这些补充是既有知识卡的专题索引，非第二学习进度。

> **REFERENCE / NOT_RUN / NEED_FIRST**。本字典仅作深挖资料，优先从[需求路由](../DEMAND-ROUTER.md)与[知识依赖图](../KNOWLEDGE-GRAPH.md)定位问题。W序号是旧课程坐标，不要求按顺序学习。本页按[知识地图](../../../ROADMAP.md)检索；Java Core/JVM/Spring属于全面覆盖的重要专题，但只有当前需求/岗位使用Java时才需优先学，不是每个下游产品的强制栈。语言熟悉程度不由历史项目自动推断。

## 容易漏掉的后端/交付横向基础

[横向基础专题](../CROSS-CUTTING-FOUNDATIONS.md)：X02算法/复杂度、X08 API分页/版本/事件回调、X09契约/集成测试、X10威胁建模、X11依赖安全、X12数据生命周期、X13运维SLO、X14容量成本、X15 DNS/TLS、X16配置密钥、X17序列化与精度。主线仍按需求进入B01/B02/B04/B07，不强制所有技术栈。

## 本次上游补充：多后端语言与跨端协作

- [上游语言与框架全景](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)：Python、Node、Java、Go、Rust/C++是语言/运行时/工程路线，FastAPI、Spring、NestJS是后端框架，不必同一服务全部使用。
- [企业AI 18项可选LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md)：按当前问题直接看[LAB02 API/SSE](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md)、[LAB08 SQL缓存](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB08.md)、[LAB09多租户](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB09.md)、[LAB11部署](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB11.md)、[LAB14 Java](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB14.md)。
- **新增节点**：B07 Node/NestJS、B08 Go、B09 Rust/C++/CUDA、D05对象存储/全文/向量检索、E05构建/打包、A02 MCP工具协议。入口：[知识图](../KNOWLEDGE-GRAPH.md)→[权威学习资料](../OFFICIAL-RESOURCES.md)。
- **关系辨析**：语言不是框架，SQL不是PostgreSQL，MCP不是REST替代品，SSE/WebSocket不是可靠消息队列；技术选型依据团队、协议、错误风险、实际交付要求。详见[专业+大白话全景图](../FULLSTACK-MENTAL-MODEL.md)。

## 一、Java 语言与 JVM（W09–W11）

| 知识 | 最低必须掌握 | 实验 |
|---|---|---|
| Java 核心 | primitive/reference、OOP/接口/抽象、多态、泛型/类型擦除、异常、record/enum、日期、IO/NIO、Maven/Gradle | 纯 Java 任务领域模型+JUnit |
| 集合/Stream | List/Set/Map/HashMap、equals/hashCode、Comparator、Lambda、Stream/Optional、复杂度、不可变对象 | 去重/排序、重复键/空值负例 |
| 并发/JMM | Thread/Executor、Future/CompletableFuture、volatile、synchronized、Lock、Atomic、ThreadLocal 风险 | 共享计数竞态与锁修复 |
| JVM | 类加载、内存、堆/栈、GC、jcmd/JFR、线程 dump、OOM 排查、基础性能分析 | GC/JFR 证据和故障根因 |
| 虚拟线程 | Platform vs Virtual Thread、I/O 适合而非 CPU 适合、Pinning、连接池限制 | 虚拟线程/平台线程 I/O 对照 |

官方：[Dev.java](https://dev.java/learn/)、[Java Virtual Threads](https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html)。实际项目选择与 Spring 兼容的受支持 JDK LTS 并固定版本，不盲用旧 JDK8 教程当现代最佳实践。

## 二、Spring / Spring Boot（W12–W13）

| 模块 | 必学内容 | 反例与验收 |
|---|---|---|
| IoC/DI/AOP | Bean Scope/生命周期、自动配置/Conditional、代理、循环依赖、配置 Profiles | 能解释 Spring 从注解到运行时 Bean 的路径 |
| MVC | DispatcherServlet、Filter/Interceptor、Controller→Service→Repository、校验/异常映射 | 400/401/403/500 与错误结构 |
| 数据访问 | JDBC/JdbcTemplate、Spring Data JPA/Hibernate、MyBatis 原理/比较、连接池、N+1 | JPA 或 MyBatis 主路径一条深入，不重复实现全部 ORM |
| 事务 | @Transactional 传播/隔离、代理自调用失效、锁与死锁、失败回滚 | 可复现自调用与回滚实验 |
| 安全 | Spring Security FilterChain、Session、JWT/OIDC、资源级 AuthZ | 用户 A/B/租户权限负例 |
| 测试 | JUnit 5、Mockito、MockMvc/REST Assured、Testcontainers PostgreSQL | 不用单纯 H2 代替实际数据库隔离/锁行为 |
| 运维 | Actuator/Micrometer、健康检查、配置外置、优雅退出、JVM/JFR/Trace | 可观察 Java 服务调用链 |
| 选修 | WebFlux、Spring Cloud、复杂微服务框架 | JD 或真实业务需要时再学 |

官方：[Spring Boot](https://docs.spring.io/spring-boot/reference/)、[Spring Framework](https://docs.spring.io/spring-framework/reference/)、[Spring Security](https://docs.spring.io/spring-security/reference/)、[Spring Data](https://docs.spring.io/spring-data/jpa/reference/)、[Testcontainers](https://testcontainers.com/guides/testing-spring-boot-rest-api-using-testcontainers/)。

## 三、Python API 与统一契约（阶段 A）

- FastAPI/Pydantic/Depends、Router→Service→Repository、async vs sync、SQLAlchemy/Alembic、Pytest；
- Session/Cookie/Refresh Token、RBAC/资源级授权、文件上传安全、REST/OpenAPI/Orval 一致性；
- Redis/Celery ACK/Retry/Worker Kill、业务幂等与 PostgreSQL 权威状态；
- SSE chunk/event 边界、EventSource vs fetch-stream、取消及任务解耦。

官方：[FastAPI](https://fastapi.tiangolo.com/tutorial/)、[Orval](https://orval.dev/docs/)、[Celery](https://docs.celeryq.dev/en/stable/userguide/tasks.html)。

## 四、数据库、消息和最终一致性（W4、W19–W20）

| 方向 | 核心能力 | 失败实验 |
|---|---|---|
| PostgreSQL | SQL/CTE/Window、MVCC/隔离/锁、联合索引、EXPLAIN、连接池、迁移 | 双连接丢失更新和死锁 |
| MySQL/InnoDB | 常见 SQL/索引、隔离和 PG 差异，对比数据类型/事务语义 | W20 SQL/索引选择和迁移差异 |
| Redis | String/Hash/Set/ZSet、TTL/淘汰、Cache Aside、击穿/穿透/雪崩、缓存一致性 | 集中过期/并发回源测量 |
| 消息队列 | RabbitMQ 或 Kafka 二选一深入；ACK/Offset、重投递、重试、DLQ、版本契约 | 断线/重复/乱序后不破坏业务 |
| 事件一致性 | Transactional Outbox、幂等消费者、服务所有权、最终一致性与补偿 | DB 成功/消息发送失败、重放 |
| P2 | MongoDB、ES/OpenSearch、复杂分库分表与多区域复制 | 真实业务触发 |

资料：[PostgreSQL](https://www.postgresql.org/docs/current/)、[MySQL](https://dev.mysql.com/doc/)、[Redis](https://redis.io/docs/latest/)、[RabbitMQ](https://www.rabbitmq.com/docs)、[Kafka](https://kafka.apache.org/documentation/)。

## 五、安全、系统设计与生产交付（W21–W24）

- **认证鉴权**：OAuth2/OIDC/Authorization Code+PKCE、Session/Token、CSRF/XSS/SSRF、RBAC/ABAC、租户隔离、服务间身份与密钥轮换。
- **运维**：Linux/进程/端口/权限、Nginx、Docker/Compose/Profiles、CI/CD、HTTPS、备份/恢复/回滚；K8s 核心对象可认知，真机集群 P2。
- **观测**：日志、Metrics、Trace、SLI/SLO、JVM JFR/GC、SQL/Redis/HTTP P95/P99、前端 LCP/INP/CLS。涉及追踪与上线可靠性时需要最小OTel验证；W8/W23只是其旧知识坐标。
- **系统设计**：单体分层、领域边界、API/事件契约、消息幂等、缓存一致性、容量/成本、微服务拆分触发条件、威胁建模、ADR。
- **同项目集成**：React+FastAPI 主业务不变，Java Spring 拥有独立审计/通知业务域；不得两个服务无所有权边界写同一业务表。

官方：[OWASP API Top10](https://owasp.org/API-Security/)、[Spring Observability](https://docs.spring.io/spring-boot/reference/actuator/observability.html)、[OpenTelemetry](https://opentelemetry.io/docs/)。

## 六、执行原则

本字典不设独立进度；遇到后端缺口 → 找到 W9–W24 对应任务与 G13–G24 → 阅读官方知识 → **本人先实现** → 注入故障与复测 → 记录到 [PROGRESS](../PROGRESS.md)。任何静态文档、Mock 或 AI 自动执行都不能当个人 L3。
