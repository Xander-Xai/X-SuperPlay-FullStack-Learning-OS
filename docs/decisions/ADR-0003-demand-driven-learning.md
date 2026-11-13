# ADR-0003：从按周通关改为需求驱动知识图谱

- 日期：2026-11-14
- 状态：**ACCEPTED_FOR_LEARNING_GOVERNANCE / PRACTICE_NOT_RUN**
- 继承：[ADR-0001](ADR-0001-stack-and-boundaries.md)、[ADR-0002](ADR-0002-v3-multistack-expansion.md) 的技术覆盖和工程质量边界。
- **覆盖部分历史约束**：ADR-0002 的「24周顺序学习」「一个Java/Python贯穿项目」「Spring必须在W9之后」作为通用执行规定已失效；但Java/Spring、前端进阶和24个Gate仍属于**全面知识地图**的一部分。

## 决策

1. **唯一知识总地图**：[ROADMAP](../../ROADMAP.md) 继续保留W1–W24及G01–G24，作为知识覆盖坐标，不代表用户必须每周按序学习。
2. **真正执行顺序**：由当前产品/岗位/故障需求和 [知识依赖图](../learning/KNOWLEDGE-GRAPH.md) 决定。`requires` 只指开始动手的最小先修，不能强制完成前置模块全部实验。
3. **统一入口**：[DEMAND-ROUTER](../learning/DEMAND-ROUTER.md)。每个学习会话：需求→Gap诊断→关键原理/关系→权威小节→最小代码/实验→失败注入→独立验收→回当前项目。
4. **覆盖范围**：静态工具、SaaS、企业Web、微信小程序、移动App、CLI/Node、AI应用与Java/Spring等。按 [REQUIREMENTS-COVERAGE](../learning/REQUIREMENTS-COVERAGE.md) 覆盖下游，而非只为某个产品服务。
5. **权威资料**：[OFFICIAL-RESOURCES](../learning/OFFICIAL-RESOURCES.md) 与节点关联，优先标准/官方文档；不收藏无来源大杂烩，不要求按完整目录从头到尾阅读。
6. **单一实际学习进度来源**：[PROGRESS](../learning/PROGRESS.md)（需求会话与Gate证据）；旧W时间表只是可选完整覆盖自学节奏。参考432h绝非必须投入的总时长。
7. **学习载体由需求选择**：授权的真实项目/下游代码、独立Lab、或者ReconLab。AI-assisted starter与本人成绩严格分离。任何真实产品仍遵循其开发/发布授权，不在本ADR解冻ReconCheck。

## 边界

- 不要“哪里不会学哪里”演变成碎片化：在学单一知识点前必须能说清它与上下层的联系、最低先修与替代方案，留下独立反例。
- 不要把宽广全栈地图误当所有应用都必须同时装 Java/Python/Next/Redis/Kafka。
- 需要全栈综合能力时可以选用旧W1–W24引导式路径；这是自愿选项，不是唯一进阶方式。
- 未来新增下游类别而地图不够覆盖时，公开标注GAP，补知识点、权威资料和最小实验。
