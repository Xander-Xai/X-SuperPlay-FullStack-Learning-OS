# X-SuperPlay-FullStack-Learning-OS

> **V4.0 全栈能力操作系统** · 需求驱动学习 · 知识图谱与权威资料 · 实战及独立验收。
>
> **完整覆盖与执行顺序分离**：保留 W1–W24、G01–G24 的系统性知识地图，原432小时只是全部覆盖时的参考预算。**不要求从W1顺序学到W24**，也不要求所有下游应用同时采用Python、Java、React和Next.js。

## 第一入口：我当前要做什么？

1. **[按需求查学习模块](docs/learning/DEMAND-ROUTER.md)**：从当前业务功能、岗位JD或Bug切入，找到最小需要的技能与实战。
2. **[全栈知识关系图（29个节点）](docs/learning/KNOWLEDGE-GRAPH.md)**：看每个技术在哪一层、解决什么问题、如何与其他技术连接，以及最低先修依赖。
3. **[权威官方学习资料](docs/learning/OFFICIAL-RESOURCES.md)**：对应具体知识点和章节学习，不刷完整文档目录。
4. **[下游能力覆盖表](docs/learning/REQUIREMENTS-COVERAGE.md)**：静态工具/SaaS/企业Web/Java/CLI/微信小程序/移动App/AI应用等。
5. **[需求学习会话模板](docs/learning/GAP-SESSION-TEMPLATE.md)**：原理→亲手改代码→错误注入→独立验收→继续项目。
6. **[ROADMAP 全面知识地图](ROADMAP.md)**：W1–W24作为覆盖坐标和可选的系统性补全路径，不是强制日历。

**学习问题示例**：现在要写 Spring API → 先查 B04，补最低 Java B03 → 阅读官方 Spring MVC → 做接口+错误测试；遇到数据库问题才补 D01/B05。无须先把 React、Next、Celery 学完。

## 实战代码与下游仓的区别

- **学习实战可在任何有权限的当前项目进行**。本仓提供学习路线、官方资料、诊断和独立验收证据；业务方向反过来决定先学习的技能。
- [Dev-Workbench](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench)：现有 Node CLI / 测试 / CI 真实代码，可用于按需维护和交付工程训练。
- [Utility-Sites](https://github.com/Xander-Xai/X-SuperPlay-Utility-Sites)：下游产品候选；ReconCheck 仍未获正式产品开发/发布授权。
- [ReconLab 合成业务示例](ai-fullstack-workbench/README.md)：React + FastAPI 已有代码和 CI，是**可选教材**，不是本仓唯一主项目或你的默认学习任务。[S0–S4 实战案例索引](docs/learning/PRODUCT-DRIVEN-EXECUTION.md)仅供适合此业务时使用。

## 从这里开始

| 入口 | 作用 | 事实状态 |
|---|---|---|
| [ROADMAP.md](ROADMAP.md) | V4.0 全面知识覆盖坐标；原24周可选引导式学习，不强制先后顺序 | REFERENCE + OPTIONAL_PLAN |
| [学习进度](docs/learning/PROGRESS.md) | **以真实需求会话为先**；W坐标/Gate只做能力覆盖与证据索引 | NOT_RUN |
| [能力地图](docs/learning/CAPABILITY-MATRIX.md) | Java/JVM/Spring/前端/系统设计的知识点→周次→Gate 索引 | REFERENCE |
| [W09–W24 执行手册](docs/learning/W09-W24-EXECUTION-PLAYBOOK.md) | 可选系统补基础的D1–D6任务样例，非必修日历 | OPTIONAL_SPRINT_TEMPLATE |
| [版本选择约束](docs/learning/STACK-VERSION-POLICY.md) | JDK/Boot/Node 稳定版本、兼容矩阵、许可证与锁定机制 | REFERENCE |
| [前端专项字典](docs/learning/references/frontend.md) | HTML/CSS/a11y、JS/TS、React、SSR/Next、Node、性能与测试 | REFERENCE |
| [后端专项字典](docs/learning/references/backend.md) | Java/JVM/Spring/安全、FastAPI、SQL、消息、缓存按需深挖 | REFERENCE |
| [实验模板](docs/learning/EXPERIMENT-TEMPLATE.md) | 复现、证据、失败与修复记录 | TEMPLATE |
| [项目蓝图](docs/project/PROJECT-BLUEPRINT.md) | 已有 React/FastAPI S0 合成核对，数据库/异步/Java/上线仍为设计态 | PARTIALLY_IMPLEMENTED |
| [24 项验收](docs/learning/ACCEPTANCE.md) | G01–G24 的负例、状态和本人独立证据 | LEARNER_NOT_RUN |
| [AI Coding 边界](docs/learning/AI-CODING-POLICY.md) | 本人先写与 AI 可辅助范围、L1–L3 标准 | REFERENCE |
| [落盘覆盖矩阵](docs/quality/ROADMAP-COVERAGE.md) | V3.0 八周基线与十六周拓展的一致性核验 | DOCUMENTED |
| [仓库关系索引](docs/REPOSITORY-INDEX.md) | 上游/下游的职责与权威边界 | INDEX |
| [学习治理决策](docs/decisions/ADR-0003-demand-driven-learning.md) | V4.0需求驱动、知识依赖图、下游多场景覆盖 | ACCEPTED_FOR_PLAN |

## 文档结构自动验收

GitHub Actions 的 [Roadmap document integrity](.github/workflows/roadmap-integrity.yml) 在相关文档提交/PR 时检查24个知识坐标、24项Gate、96个可选D1–D6任务、可合法更新的学习状态、知识图先修无环、官方来源索引、路由器测试与内部相对链接。**只保证文档结构自洽，不等于学员通过或应用测试通过。**

## 唯一执行机制（不是唯一步骤顺序）

1. 当前需求决定需要补哪个知识节点；知识图说明最低先修和相邻原理，**不按W编号强制排序**。
2. 为具体任务选一份官方权威资料和真实可跑的实验；已掌握的技术直接应用，不反复教程。
3. 本人独立实现、负例测试和解释后记录证据；相关Gxx可以按需验收，不因其他Gxx未通过阻止当前合理需求。
4. 可选采用原W1–W24/432h作为全面查漏的参考课程；不是所有产品上线的强制条件。
5. 项目开发与发布由各目标仓真实授权、风险和工程验收控制，不以学习仓CI替代生产批准。

## 仓库定位

```text
X-SuperPlay-AI-Learning-OS       上游：知识研究、岗位需求、评分参考
              │
              ▼
X-SuperPlay-FullStack-Learning-OS（本仓：知识图谱、需求驱动学习、证据台账）
              │
              ├──► X-SuperPlay-Dev-Workbench  下游：工程方法/工具与交付证据标准
              └──► X-SuperPlay-Utility-Sites  下游：可选产品实践场景（开发仍受业务授权约束）
```

详见 [责任与索引](docs/REPOSITORY-INDEX.md)。**不自动同步、不自动授权对其他仓库做代码改动。**

## 当前已完成与未完成

- 已创建：路线、索引、学习模板和资料入口，以及合成核对 S0 API/React 代码和两套实际通过的 GitHub CI（文档与前后端测试/构建）。
- 未开展/未验证：个人独立需求会话与W1–W24能力验收、可选高级模块实验、生产部署、跨仓商业交付；S0只有合成样例的CI证据。
- 所有 `NOT_RUN` 应在实际发生并保存证据后更新，不把文档创建等同于任务完成。新扩展 G13–G24 同样默认 NOT_RUN。
