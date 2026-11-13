# V3.0 全栈 Roadmap 覆盖与一致性核查

> **DOCUMENTED / SYNTHETIC_S0_CODE_AND_CI_VERIFIED / LEARNING_NOT_RUN**。当前已存在 S0 合成核对 API/React 代码和真实 CI；这不等于完成全部课程、上线产品或个人独立通过。

## 权威归属

- 学习唯一执行路线：[ROADMAP.md](../../ROADMAP.md)，W1–W24。
- 学习唯一状态台账：[PROGRESS.md](../learning/PROGRESS.md)，初始 24 周均 NOT_RUN。
- Java 必修与项目边界：[ADR-0002](../decisions/ADR-0002-v3-multistack-expansion.md)，覆盖历史 [ADR-0001](../decisions/ADR-0001-stack-and-boundaries.md) 对 Java 后置的决策。
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

1. **路线一条**：W1–W8 144h 保留；W09–W24 288h；总 24×18=**432h** 参考预算，非保证期限。
2. **Java/Spring 为必修**；Next.js SSR/Node 比较实验必修，**完整 Next 迁移**属于 P2；不能再把 Java 同时称为 P2。
3. **仅一个贯穿应用** `ai-fullstack-workbench`：S0 API/React 合成核对已实现并有 CI 证据，Java/DB/SSE/Next/Node 为后续扩展且仍需本人实验；Java 服务独立业务边界与 DB 所有权，Next/Node 仅 Labs。
4. G01–G12 不失效；G13–G24 新增，所有 Gate 不能因“计划编写”打 PASS。
5. Dev-Workbench 11 个工程阶段仍为过程权威，Utility-Sites 未授权业务不能被学习项目擅自开发。
6. 文档 CI 与 S0 API/React 单元/API/构建 CI 已真实执行成功；真实数据库、容器生产部署、性能/安全验收、Java 跨语言系统与本人独立答辩仍 `NOT_RUN`。
