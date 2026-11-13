# V4.2 全栈能力坐标对照表

> 本表是旧W坐标/知识/验收编号的对照；优先从[需求路由](DEMAND-ROUTER.md)→[知识依赖图](KNOWLEDGE-GRAPH.md)→[权威资料](OFFICIAL-RESOURCES.md)进入。W1–W24不是时间轴或固定完成顺序，证据只在[PROGRESS](PROGRESS.md)登记。

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

## 正式学习卡入口

- [42个知识点的专业/大白话卡片](NODE-STUDY-CARDS.md)：每个含机制、边界、官方具体章节、上游来源性质及可复现负例；不是另建进度表。
- [实际可运行的部分实验](labs/README.md)：Node请求竞态是机制级已纳入CI，其他实验按真实环境执行后才可记录本人结果。

## 新增分支与知识关系

- 旧W坐标对照表仍用于已有课程的归档，不用它来判断Vue/Nuxt/桌面等新增选修节点不存在；实际完整知识节点在[42节点机器图](knowledge-map.json)与[人类关系图](KNOWLEDGE-GRAPH.md)。
- 补充：**F08 Vue3、F09 Nuxt、F10 PWA、F11 WebSocket；B07 Nest、B08 Go、B09 Rust/C++；D05存储/检索；E05跨语言构建；M03桌面、M04 uni-app、M05原生；A02 MCP。**
- 旧G01–G24可按当前需求归档对应证据，不要求所有技术在一个项目里实作。
- 多来源资料见[上游汇合索引](UPSTREAM-ASSET-INDEX.md)；专业与大白话贯通见[全景图](FULLSTACK-MENTAL-MODEL.md)。

## 能力证据由 Gate 决定，而不是勾选技术名词

- **L1**：不看资料解释语言/框架执行机制；**L2**：独立实现和测试；**L3**：故障注入、归因、修复、取舍和新场景复测。
- **P0/P1/P2 是旧全量学习覆盖深度**，不代表任何下游产品必须同时使用Java、Python、Next、Redis和消息系统；当前项目依照[能力覆盖矩阵](REQUIREMENTS-COVERAGE.md)选用。
- **项目不唯一**：当前有权限的业务项目优先，其次独立最小Lab；`ai-fullstack-workbench`只是可选合成示例。
