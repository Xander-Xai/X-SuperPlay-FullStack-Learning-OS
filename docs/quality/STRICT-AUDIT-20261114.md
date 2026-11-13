# V3.0 对抗审查与修复记录（2026-11-14）

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

