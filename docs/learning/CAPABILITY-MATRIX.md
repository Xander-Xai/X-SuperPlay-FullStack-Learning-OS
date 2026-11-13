# V3.0 全栈能力地图与检索入口

> 这是知识索引，**不是第二套进度表**。唯一时间轴为 [ROADMAP W1–W24](../../ROADMAP.md)，唯一实际状态台账为 [PROGRESS](PROGRESS.md)。所有能力目前 **UNASSESSED / NOT_RUN**。

| 能力层 | 必备技能 | 周次 | 验收 Gate | 详情 |
|---|---|---|---|---|
| Web/计算机基础 | DNS/TCP/TLS/HTTP、浏览器渲染、Cookie、Linux 进程/内存/网络 | W1/W14/W22 | G01/G17/G23 | [Frontend](references/frontend.md) |
| HTML/CSS/a11y | 表单语义、Flex/Grid/定位/层叠、响应式、键盘无障碍 | W2/W14 | G17 | [Frontend](references/frontend.md) |
| JavaScript/TS/构建 | JS Event Loop/闭包/this/原型；TS 泛型/映射类型；ESM/Vite/pnpm | W1/W15 | G01/G18 | [Frontend](references/frontend.md) |
| React 与前端架构 | Hooks/Query/表单/状态、性能、组件/E2E 测试 | W2/W16 | G19 | [Frontend](references/frontend.md) |
| SSR/Node | Next RSC/SSR/SSG/ISR、缓存/Secret 边界；Node Streams/事件循环 | W17/W18 | G20 | [Frontend](references/frontend.md) |
| Python API | FastAPI/Pydantic、分层、SQLAlchemy、Celery/SSE、OpenAPI | W3–W6 | G02/G03/G06/G07 | [Backend](references/backend.md) |
| **Java/JVM** | JDK/构建、集合/泛型/Streams、线程/JMM/虚拟线程/GC/JFR | W09–W11 | G13/G14 | [Backend](references/backend.md) |
| **Spring** | IoC/AOP、Spring MVC/Boot/Security/Data、事务、Testcontainers | W12/W13 | G15/G16 | [Backend](references/backend.md) |
| 数据/可靠性 | PostgreSQL/MySQL 差异、Redis、RabbitMQ/Kafka 选一、Outbox、幂等 | W4/W19/W20 | G04/G05/G21 | [Backend](references/backend.md) |
| 鉴权/安全 | Session/OAuth2/OIDC/PKCE、RBAC/ABAC、多租户、OWASP API | W3/W13/W21 | G02/G16/G22 | [Backend](references/backend.md) |
| 交付与观测 | Docker/Nginx/Linux/CI/E2E、JVM/JFR、Web Vitals、OTel、SLO | W7/W8/W22/W23 | G08–G11/G23 | 双字典 |
| 多语言架构 | 单一领域归属、服务间接口/事件契约、跨语言鉴权/Trace、故障恢复 | W24 | G24 | [蓝图](../project/PROJECT-BLUEPRINT.md) |

## 能力证据由 Gate 决定，而不是勾选技术名词

- **L1**：不看资料解释语言/框架执行机制；**L2**：独立实现和测试；**L3**：故障注入、归因、修复、取舍和新场景复测。
- **P0**：基础全栈与 Java/JVM/Spring 必修；**P1**：前端进阶/SSR/Node 最小实验/消息安全与系统设计；**P2**：完整 Next 迁移、NestJS/Vue/微服务/K8s 集群等由有效需求驱动。
- **唯一项目**：`ai-fullstack-workbench`；Java 是其中新增独立业务边界，不因学 Java 自动拆成复杂微服务。
