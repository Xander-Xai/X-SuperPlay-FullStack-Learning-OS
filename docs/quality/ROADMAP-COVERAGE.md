# V4.0 全栈知识地图与按需学习一致性核查

> **KNOWLEDGE_GRAPH_VERIFIED / OPTIONAL_S0_DEMO_CI_VERIFIED / LEARNER_NOT_RUN**。本仓覆盖下游多种产品，不再要求按W1–W24日历或只做ReconLab。静态知识图验证与学生技能、商业产品上线仍严格分离。

## 权威归属

- 学习方式：[DEMAND-ROUTER](../learning/DEMAND-ROUTER.md)优先，按[KNOWLEDGE-GRAPH](../learning/KNOWLEDGE-GRAPH.md)最低先修跳转；[ROADMAP](../../ROADMAP.md)是完整知识覆盖坐标，不是固定学习先后。
- 学习唯一状态台账：[PROGRESS.md](../learning/PROGRESS.md)，初始 24 周均 NOT_RUN。
- 当前学习治理：[ADR-0003](../decisions/ADR-0003-demand-driven-learning.md)覆盖原单项目/按周限制；[ADR-0002](../decisions/ADR-0002-v3-multistack-expansion.md)保留Java/Spring与前端专项覆盖范围。
- 专题索引：[CAPABILITY-MATRIX](../learning/CAPABILITY-MATRIX.md)、[frontend](../learning/references/frontend.md)、[backend](../learning/references/backend.md)。
- 最终考核：[ACCEPTANCE](../learning/ACCEPTANCE.md)，G01–G24。
- 技术蓝图：[PROJECT-BLUEPRINT](../project/PROJECT-BLUEPRINT.md)，新目录属于设计态，非已实现业务代码。

## 用户提出的关键缺口 → 明确落盘与门槛

| 需要补的能力 | 周次 | 必修机制/实验 | Gate |
|---|---|---|---|
| Java 基础、泛型/集合、Maven/JUnit、异常/Stream | W09–W10 | Java 领域模块和数据结构负例 | G13 |
| Java 并发/JVM/GC/JFR/虚拟线程 | W11 | JMM 竞态/线程/IO 测试 | G14 |
| Spring IoC/DI/AOP/MVC/Boot | W12 | 独立业务 Service、Bean/错误响应测试 | G15 |
| Spring Data/JPA/MyBatis、事务/Security/Testcontainers | W13 | DB 事务、代理自调用、资源级授权负例 | G16 |
| HTML/CSS/浏览器渲染/a11y/响应式 | W14 | DOM/键盘/移动布局负例 | G17 |
| JS/TS 深层/前端构建工具 | W15 | 类型与打包/Code Splitting/ESM | G18 |
| React 架构/状态/测试/性能 | W16 | Profiler、Mutation 回滚、RTL/E2E | G19 |
| SPA vs SSR/Next、Node Runtime | W17–W18 | 最小独立对照实验，不替换主项目 | G20 |
| 消息系统/Outbox 与 DB+缓存一致性 | W19–W20 | 重放/DLQ/SQL 差异与容量对照 | G21 |
| OAuth2/OIDC/PKCE/多租户/OWASP | W21 | 服务端鉴权、跨用户/租户越权负例 | G22 |
| Linux/Cloud/CI/性能/JFR/OTel | W22–W23 | 部署/恢复、Profile/Tracer/Web Vitals | G23 |
| 跨 Java/Python 前后端系统设计与答辩 | W24 | 全链路实测+独立变化条件复测 | G24 |

## 不可违反的一致性规则

1. **一份完整能力地图**：W1–W8及W09–W24总24个覆盖坐标；432h是自愿全面补课的历史参考预算，不是强制期限。
2. **Java/Spring/Next/Node全部覆盖在知识目录**；选择Java岗位时实际必学相应节点，纯静态工具站则不需要强行Java或Next。
3. **不限定一个项目**：已有 `ai-fullstack-workbench` S0合成核对案例与CI，只是可选实战；有授权的下游真实项目、最小Lab亦可学习。按[REQUIREMENTS-COVERAGE](../learning/REQUIREMENTS-COVERAGE.md)检查多场景覆盖。
4. G01–G24全部保留为独立能力证据类别，按当前需求选取相关Gate；不因计划编写或前置无关Gate未通过就自动失败。
5. Dev-Workbench 11 个工程阶段仍为过程权威，Utility-Sites 未授权业务不能被学习项目擅自开发。
6. 文档 CI 与 S0 API/React 单元/API/构建 CI 已真实执行成功；真实数据库、容器生产部署、性能/安全验收、Java 跨语言系统与本人独立答辩仍 `NOT_RUN`。


## V4.0 新增硬验收

- [知识图 JSON](../learning/knowledge-map.json) 29个独立知识节点、25条最小先修边、24坐标/24Gate覆盖，不允许先修环路或悬空节点。
- [官方原始资料库](../learning/OFFICIAL-RESOURCES.md) 每个节点可追溯到标准/官方文档及专题学习内容；外部网页存活与具体版本仍需使用时复核。
- [需求路由器](../learning/route_need.py) 支持自然语言关键词和NodeID直接查最小先修/资料；不把关键词匹配当全部业务理解。
- [场景覆盖](../learning/REQUIREMENTS-COVERAGE.md) 对静态站/SaaS/企业Web/小程序/移动App/AI工具/Java/Node/结算案例进行取舍；不宣布所有产品同时可以直接上线。
- 旧24模块状态校验必须允许 `IN_PROGRESS`/`PARTIAL`/`PASS_WITH_EVIDENCE`，通过要有证据；不能强制所有学习状态永久NOT_RUN。
