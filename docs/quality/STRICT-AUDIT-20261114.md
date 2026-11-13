# 历史V3.0对抗审查与修复记录（2026-11-14）

> **历史快照，不代表当前学习治理或CI要求。** 本文件的“Java必修/每周必达”等内容描述的是已由[ADR-0003](../decisions/ADR-0003-demand-driven-learning.md)废止的旧全量课表。当前有效审查与最新CI证据请以[V4.2严格验收报告](AUDIT-V4.2-20261114.md)为准，勿按本历史报告旧结论执行。

> 验收对象：FullStack-Learning-OS 的 main 文档与跨仓索引。状态：**DOCUMENTATION_AUDITED / TRAINING_NOT_RUN**。这不是对代码、CI 测试、实际部署和学员能力的验收报告。

## 审计结论与发现

| 严重程度 | 发现 | 审查结论与修复 |
|---|---|---|
| P0 | ADR-0001 仍声称 Spring 由岗位触发，但 V3.0 定为必修 | ADR-0001 标历史/部分废止，ADR-0002 明确覆盖；统一 Java/Spring W09–W13 |
| P1 | 扩展 16 周只列主题/一段实验，无法每天明确执行 | 新建 W09–W24 执行手册：每周 6×3h、先修、至少一个反例和 DoD |
| P1 | G13–G24 共 12 个 Gate 覆盖 16 周，单 Gate 不能替代每周实际验收 | 在执行手册和 PROGRESS 要求按周单独记录证据，Gate 用于汇总 |
| P1 | 缺少可复现依赖版本/兼容边界 | 新建 STACK-VERSION-POLICY；JDK21/25、Boot/Node LTS 等以启动时官方兼容核验为准 |
| P1 | W14 才深挖 HTML/CSS，容易误解为 W1/W2 可以完全跳过基础 | 在执行手册强调 W1/W2 最小必修 HTML/CSS，W14 只深化 |
| P1 | W24 18h 从零开发 Python+Java 服务不现实 | W12–W23 渐进集成，W24 只做回归/故障/答辩 |
| P2 | 主线残留“八周唯一执行”字句 | 修复为 W1–W24 |
| P2 | Java 工程可能污染 Git 仓库 | .gitignore 加 Maven/Gradle/Java 构建产物 |
| P2 | 全栈范围过宽，432h 不能保证所有技术都达到资深水平 | 标明预算是参考，可 Gap Jump；强制区分必修/对比实验/P2 选修 |

## 本轮不能冒称完成的事项

- 本仓没有真实 `ai-fullstack-workbench` 应用代码、Java/Spring/React CI 结果、真实数据库并发测试、JFR/Trace、部署/恢复或 24 周学员独立考核。
- 实际选定的 Java、Node、Spring 版本与锁文件尚未写入应用（应用还未启动），仅给版本选择原则与外部官方文档。
- 下游 Utility-Sites 仍不代表商业授权；本次不改其代码。
- 所有 W1–W24 / G01–G24 均应保持 `NOT_RUN / UNASSESSED`。

## 结构与后续验收

1. 确认唯一 ROADMAP + 唯一 PROGRESS，W1–W24 24 个周段、G01–G24 24 个 Gate。
2. 新增 W09–W24 执行手册每周 6 个 D1–D6 条目（合计 96 日任务），必须有先修和 DoD。
3. 校验 Markdown 相对链接与 ADR 覆盖规则，不能暗中新增 Java/Spring 选修结论。
4. 真正开学前优先 W1 基线；目标 Java/Spring 岗可按 JD 做 W09→W12→W13 先修可满足的部分，但仍不得跳过 W10/11 的已声明能力。
5. 已添加 GitHub Actions **Roadmap document integrity**（静态结构与内部链接检查）；仍需在实际 Run 执行后才能记录 CI PASS。项目代码的 Java/Python/前端测试尚未创建，绝不能让文档 CI 代替功能 CI。

## 技术资料核查

- Java LTS 21/25：[Oracle SE Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
- Spring Boot 当前兼容要求：[Spring Boot System Requirements](https://docs.spring.io/spring-boot/system-requirements.html)
- Node 支持线：[Node.js Release Schedule](https://nodejs.org/en/about/previous-releases)


## 真实 CI 验收与剩余缺口（最终复核）

- **通过记录**：[Roadmap document integrity run #43471143052](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/actions/runs/43471143052)；对提交 `8b2f0aaa48653630315f1b833c47c1c1c9608bd9` 的 `roadmap-docs` 作业结论为 **SUCCESS**。
- **原始 CI 摘要**：`ROADMAP DOCS PASS: 24 weeks; 24 gates; 16x6 daily tasks; 81 relative links checked; actual training remains NOT_RUN.`
- **两次真实失败与修复**：最初的断言错误地要求 ADR-0002 含固定短语、又要求 Java 必修文本精确包含特定 W09 字样；修复为核对明确语义，并改用 Node24 运行时的 actions/checkout@v5 与 actions/setup-python@v6。失败记录保留在 Actions 历史中，不宣称“第一次就通过”。
- **审计覆盖边界**：Python 静态检查核对相对链接**文件路径**，不核对 GitHub 生成的标题锚点、所有外部 URL 的存活，也不执行 Java/React/FastAPI 程序。
- **尚未完成的实际教学验收**：24 周全部 `NOT_RUN`、24 Gate 尚无独立人类证据；应用源码、自动化应用测试、部署/恢复和真实多语言集成均尚未执行。
- **仍需改进的非阻塞项**：432h 是参考预算，某些深层模块如 JVM/Spring/消息/架构可能需要延长，不能压缩负例；实际岗位优先时采用 Gap Jump 并记录遗漏；外部文档版本与链接需在开学时复核。
- **GitHub 仓库页面元数据**：Description 已更新为 24-week。Topics 仍缺 `java`、`spring-boot`、`jvm` 等搜索标签；这不影响学习路线与 CI，但建议在 GitHub About 中补充。

**本次结论**：文档完整性及可执行性模板 **PASS**；实际能力与工程系统运行 **NOT_RUN**。两者必须分别对外表述。

## 新阶段状态：学习仓已拥有真实合成业务代码

此前报告所记的“没有应用代码”是当时的事实；现已由 React/Vite + FastAPI 代码与真正的 GitHub Actions 单元/API/前端测试和 build 取代。见 [训练源码](../../ai-fullstack-workbench/README.md) 与 [产品驱动映射](../learning/PRODUCT-DRIVEN-EXECUTION.md)。**S0 合成程序可构建 ≠ 独立课程考核 PASS ≠ Utility-Sites 商业产品可上线**。仍须完成 OpenAPI 代码生成、PostgreSQL、权限、安全 CSV、幂等任务、SSE/Java/事件、真实部署及 [上线门禁](../project/DOWNSTREAM-RELEASE-GATES.md)。

## 实战代码阶段最终验收（2026-11-14）

- **真实代码**：学习仓 `ai-fullstack-workbench/apps/api`（FastAPI + Decimal）、`apps/web`（React/Vite/TypeScript）以及前后端测试/锁文件已经提交。
- **最新实战 CI**：[ReconLab synthetic slice #43476058819](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/actions/runs/43476058819) = SUCCESS。含 Python API/Unit Test、npm ci/React 测试、TS/Vite build。无 Browser E2E、真实 DB、安全/部署结论。
- **最新文档 CI**：[Roadmap document integrity #43476059220](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/actions/runs/43476059220) = SUCCESS。
- **可执行需求**：24 周产品驱动映射、S0–S4 五个 GitHub Issues、商业上线 Gate 已写入本仓；Utility-Sites README 索引学习代码但保持 `DEVELOPMENT_ON_HOLD`；Dev-Workbench [PR #43](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench/pull/43) verify 成功并合并。
- **状态分离**：S0 AI-assisted starter / CI_VERIFIED；学员独立学习验收 W1–W24 = NOT_RUN；ReconCheck 正式产品代码/授权/上市 = BLOCKED。旧版本历史记录中“没有应用代码”不再代表当前状态。


## V4.0 纠偏：下游多场景与需求自由跳学

- 用户明确否定“全仓围绕ReconLab/ReconCheck”和“强制W1→W24按周通关”。已以[ADR-0003](../decisions/ADR-0003-demand-driven-learning.md)替换旧执行规定；保留已有代码案例及历史演变记录。
- 目前可从[DEMAND-ROUTER](../learning/DEMAND-ROUTER.md)→[知识图](../learning/KNOWLEDGE-GRAPH.md)→[官方资料](../learning/OFFICIAL-RESOURCES.md)→真实业务/独立故障实验，知识坐标与学习顺序不再混用。
- [下游能力覆盖](../learning/REQUIREMENTS-COVERAGE.md)包含静态Web、SaaS、企业Web、微信小程序、移动App、AI/Agent、Node CLI、Java/Spring与电商结算案例；未覆盖全部平台特殊细节，应用边界仍以真实需求与授权为准。
- 新增`route_need.py`按NodeID或关键词打印作用、最低先修、官方资料；GitHub Actions静态验证知识图关系无环、覆盖W01–W24及G01–G24、资料索引，并运行CLI单测。**静态工具和文档CI通过不等于用户已经学会任何模块。**

## V4.1 上游资料合并与全栈心智模型（2026-11-14）

- 核对上游源代码目录/既有文档共840个仓库文件，重点阅读语言/框架关系图、Vue3/FastAPI实训、企业AI18Labs、多端路线、独立评分；汇合20个具体入口至[上游索引](../learning/UPSTREAM-ASSET-INDEX.md)，保留上游原文和固定提交快照。
- 新增[三张Mermaid图及专业定义/大白话类比](../learning/FULLSTACK-MENTAL-MODEL.md)，说明系统分层、语言框架分类、一次HTTP请求的完整旅程；避免将Vite/Node/Next、SQL/PostgreSQL、MCP/REST混淆。
- 新增13个按需分支，知识节点从29扩至42，最低先修40条；[官方资料](../learning/OFFICIAL-RESOURCES.md)与每一节点一一对应，课程仍不要求按周学习。
- 实际技术实验、各上游GitHub课程的安装与学员独立验收**没有因为文档合并而自动完成**。
