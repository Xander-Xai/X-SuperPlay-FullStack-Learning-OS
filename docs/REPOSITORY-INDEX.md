# 仓库索引与上游/下游关系

> 索引建立：2026-11-13；本页登记**职责与链接**，不是自动依赖/代码引用/跨仓同步或发布授权。

| 方向 | 仓库 | 角色 | 权威信息 | 本仓如何使用 |
|---|---|---|---|---|
| 上游 | [X-SuperPlay-AI-Learning-OS](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS) | AI/工程知识、市场驱动学习研究、独立评分 | 全栈研究、原六周按岗位 Gap Track（仅研究/参考，不单独执行）、0–4 评分量表 | 参考并按 Gap 深挖；不同时执行第二套进度；部分内容可能仅授权账户可读 |
| 当前 | [X-SuperPlay-FullStack-Learning-OS](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS) | 需求驱动全栈能力地图、权威资料、真实Gap实验 | **KNOWLEDGE-GRAPH + ROADMAP + PROGRESS** | 多下游能力底座，不绑定单一产品 |
| 下游（工程方法） | [X-SuperPlay-Dev-Workbench](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench) | 工程生命周期、Profiles、Skills、交付与验证范式 | `src/catalog.mjs` 的 11 阶段 + `docs/learning/START-HERE.md` | 按需复用方法；不在本仓再发明另一套工程状态机 |
| 下游（产品候选） | [X-SuperPlay-Utility-Sites](https://github.com/Xander-Xai/X-SuperPlay-Utility-Sites) | 可能用于未来产品实战的业务项目 | 本项目 README 中的产品定位与**开发授权状态** | 目前 `SELECTED_FOR_VALIDATION / DEVELOPMENT_ON_HOLD`；未经授权不得当作本学习项目的生产交付对象 |

## 权威冲突时的优先级

- **学习路线/实际优先级**：本仓[按需路由](learning/DEMAND-ROUTER.md)+[知识图](learning/KNOWLEDGE-GRAPH.md)负责定位当前需要的知识；W1–W24只是完整知识覆盖坐标（24周/432h旧参考预算），[PROGRESS](learning/PROGRESS.md)是唯一实际学习会话/证据台账。
- **岗位需求和课程取舍**：上游 AI-Learning-OS 记录资料与 rubric；只有真实有效岗位/授权业务信号才调整 P0 优先级。
- **工程生命周期**：Dev-Workbench 的权威 11 阶段；本仓“需求→部署→复盘”是学习视图，并非新的 Workbench 状态源。
- **具体产品方向和授权**：Utility-Sites 当前仓的产品和许可边界最高；学习仓不得宣称启动 ReconCheck 或获得真实客户验证。
- **学习表现 vs 运行系统**：教学笔记、模拟案例、CI 结果与个人独立评分严格分离，不把设计中的验收写作已通过。

## 索引更新约定

1. 跨仓只放稳定链接、职责和引用来源；不复制上游私有项目内容到公共仓。
2. 每次上游 Roadmap/评分尺度、下游开发状态或仓库迁移发生实质变更时，更新本页与 README 对应入口。
3. 新实验的代码、命令、失败证据放本仓（或有权的项目仓）并在 `PROGRESS.md` 附稳定 commit 链接；敏感/真实客户数据不得公开。
4. 若需要对其它仓库实际修改，请遵循对应仓库权限、PR 与 Gate；此索引本身仅建立知识联系。

## 相关导航

- [主 Roadmap](../ROADMAP.md)
- [学习状态](learning/PROGRESS.md)
- [上游全栈专项 Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md)
- [上游独立考核](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/assessments/ai-native-fullstack-rubric.md)
- [Dev-Workbench 11 阶段指南](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench/blob/main/docs/learning/FULLSTACK-LIFECYCLE-GUIDE.md)
