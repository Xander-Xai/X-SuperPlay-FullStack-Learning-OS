# X-SuperPlay-FullStack-Learning-OS

> **全栈工程学习执行仓** · 24 周 / 432 小时参考预算（原 8 周作为阶段 A） · 唯一学习主线 · 初始状态：`PLAN / NOT_RUN`

从已有 Python/FastAPI/RAG/Agent 项目经验出发，系统补齐**Java Core/JVM/Spring Boot**、完整 Web/前端工程（HTML/CSS/a11y/React/Next.js SSR/Node.js）、数据库与消息中间件、API 契约/安全、性能和生产交付，在唯一项目 `ai-fullstack-workbench` 中按阶段验证。**W1–W8 为基础，W9–W24 为深入；不是开三条平行路线。**

## 从真实下游产品倒推全栈技能

- **[可运行的 ReconLab 业务纵切源码](ai-fullstack-workbench/README.md)**：React/TypeScript + FastAPI/Decimal，合成账单核对；已有代码与 CI，但尚不是 ReconCheck 产品或完成学习。
- **[产品驱动 W1–W24 理论＋实战映射](docs/learning/PRODUCT-DRIVEN-EXECUTION.md)**：每周一个产品功能、一个故障实验和一个 Gate，不再只背知识清单。
- **[S0 合成用例与独立练习](docs/project/RECON-LAB-CASE.md)**：真实修改代码/运行测试；AI 生成基线不等于本人学会。
- **[下游正式上线门禁](docs/project/DOWNSTREAM-RELEASE-GATES.md)**：Utility-Sites 冻结、商业验证、隐私安全、授权部署的独立条件。

## 现在可领取的产品实战任务

| 里程碑 | GitHub Issue | 目标 |
|---|---|---|
| **S0 从现在开始** | [#1 独立改造合成核对](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/1) | 理论/代码修改/故障复现与本人考核 |
| S1 数据和权限 | [#2 CSV + PostgreSQL + AuthZ](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/2) | 受控数据导入和用户隔离 |
| S2 后台可靠性 | [#3 Celery + SSE](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/3) | 异步核对与恢复 |
| S3 Java 多栈 | [#4 Spring + Outbox](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/4) | 独立审计业务与最终一致性 |
| S4 真正上线 | [#5 产品开发与发布 Gate](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/5) | 需要真实市场验证、授权和发布验收 |

## 从这里开始

| 入口 | 作用 | 事实状态 |
|---|---|---|
| [ROADMAP.md](ROADMAP.md) | **V3.0 唯一 W1–W24 学习计划（含原 V2 基线）**：每周时间细分、重点实验、资料、门槛 | PLAN |
| [学习进度](docs/learning/PROGRESS.md) | W1–W24 状态、Gap、证据与复盘 | NOT_RUN |
| [能力地图](docs/learning/CAPABILITY-MATRIX.md) | Java/JVM/Spring/前端/系统设计的知识点→周次→Gate 索引 | REFERENCE |
| [W09–W24 执行手册](docs/learning/W09-W24-EXECUTION-PLAYBOOK.md) | 每周 D1–D6 任务、先修检查、故障实验与完成条件 | PLAN |
| [版本选择约束](docs/learning/STACK-VERSION-POLICY.md) | JDK/Boot/Node 稳定版本、兼容矩阵、许可证与锁定机制 | REFERENCE |
| [前端专项字典](docs/learning/references/frontend.md) | HTML/CSS/a11y、JS/TS、React、SSR/Next、Node、性能与测试 | REFERENCE |
| [后端专项字典](docs/learning/references/backend.md) | Java/JVM/Spring/安全、FastAPI、SQL、消息、缓存按需深挖 | REFERENCE |
| [实验模板](docs/learning/EXPERIMENT-TEMPLATE.md) | 复现、证据、失败与修复记录 | TEMPLATE |
| [项目蓝图](docs/project/PROJECT-BLUEPRINT.md) | 目标 Monorepo 目录、数据流、API 草案；**尚未生成应用代码** | DESIGN_ONLY |
| [12 项验收](docs/learning/ACCEPTANCE.md) | G01–G12 的负例、状态和独立证据 | NOT_RUN |
| [AI Coding 边界](docs/learning/AI-CODING-POLICY.md) | 本人先写与 AI 可辅助范围、L1–L3 标准 | REFERENCE |
| [落盘覆盖矩阵](docs/quality/ROADMAP-COVERAGE.md) | V3.0 八周基线与十六周拓展的一致性核验 | DOCUMENTED |
| [仓库关系索引](docs/REPOSITORY-INDEX.md) | 上游/下游的职责与权威边界 | INDEX |
| [架构与选型决策](docs/decisions/ADR-0002-v3-multistack-expansion.md) | V3.0 Java 必修、Next SSR 对比与架构边界 | ACCEPTED_FOR_PLAN |

## 文档结构自动验收

GitHub Actions 的 [Roadmap document integrity](.github/workflows/roadmap-integrity.yml) 在相关文档提交/PR 时检查 24 周、24 个 Gate、96 个 D1–D6 任务、初始进度与内部相对链接。**只保证文档结构自洽，不等于学员通过或应用测试通过。**

## 唯一执行规则

1. 按 [ROADMAP](ROADMAP.md) 推进**一个**项目，不另外执行独立前端 8 周 + 后端 8 周路线；缺什么查专项字典并做最小故障实验。
2. **阶段 A：** W1–W8 Web/TS/React/FastAPI/DB/Celery/部署；**阶段 B：** W9–W16 Java/JVM/Spring 与前端深度；**阶段 C：** W17–W24 SSR/Node/事件一致性/安全/性能/跨语言集成。
3. 每周的“完成”必须有**本人独立操作、可复现命令、测试证据、commit SHA 与失败路径**；本仓当前只是学习计划，不宣称已通过。
4. 有真实岗位/产品交付优先级冲突时按事实动态调度；不得因为八周时间盒耽误更重要的工作。
5. AI 可协助重复性代码，跨端状态/刷新、SQL 锁与幂等、Worker 故障及 SSE 解析必须先做本人最小实现和独立验收。

## 仓库定位

```text
X-SuperPlay-AI-Learning-OS       上游：知识研究、岗位需求、评分参考
              │
              ▼
X-SuperPlay-FullStack-Learning-OS（本仓：唯一学习路线与个人实验台账）
              │
              ├──► X-SuperPlay-Dev-Workbench  下游：工程方法/工具与交付证据标准
              └──► X-SuperPlay-Utility-Sites  下游：可选产品实践场景（开发仍受业务授权约束）
```

详见 [责任与索引](docs/REPOSITORY-INDEX.md)。**不自动同步、不自动授权对其他仓库做代码改动。**

## 当前已完成与未完成

- 已创建：路线、索引、学习模板及资料入口。
- 未开展/未验证：W1–W24 实验、主项目编码、持续集成、生产部署、个人闭卷考核与跨仓产品交付。
- 所有 `NOT_RUN` 应在实际发生并保存证据后更新，不把文档创建等同于任务完成。新扩展 G13–G24 同样默认 NOT_RUN。
