# ADR-0004：全栈基础补全、单一知识治理与历史内容优先级

- 日期：2026-11-14
- 状态：**ACCEPTED / DOCUMENTATION_AND_ROUTING_SCOPE_ONLY**
- 继承：[ADR-0003需求驱动](ADR-0003-demand-driven-learning.md)；覆盖[ADR-0001](ADR-0001-stack-and-boundaries.md)/[ADR-0002](ADR-0002-v3-multistack-expansion.md)中过时的“当前V3”“Java/Spring所有项目必修”“只能在Workbench实战”“必须按周验收”等通用执行表述；历史版本保留以供决策追溯。

## 决策：哪份文件说了算

| 事实与权限 | 当前权威来源 | 不可从其他材料推断什么 |
|---|---|---|
| 完整知识地图与历史覆盖坐标 | [ROADMAP](../../ROADMAP.md)及42节点 [knowledge-map.json](../learning/knowledge-map.json) | W1–W24不代表真实时间安排与强制先修 |
| 17项横向基础、实操/资料及检索 | [cross-cutting-topics.json](../learning/cross-cutting-topics.json) + [专题卡](../learning/CROSS-CUTTING-FOUNDATIONS.md) | X01–X17不是新Gate；42核心节点仍是主图 |
| 每次先学什么 | [DEMAND-ROUTER](../learning/DEMAND-ROUTER.md) / `route_need.py` | 关键词匹配只是候选，需要检查真实项目/JD/报错 |
| 学习证据与学员能力状态 | [PROGRESS](../learning/PROGRESS.md) | 读到文档/CI绿并不代表本人独立达标 |
| 独立能力评价门槛 | [ACCEPTANCE](../learning/ACCEPTANCE.md) G01–G24 | 旧V3 P0/P1/P2只表示自愿全量覆盖的教学深度，不强制每个项目 |
| 产品开发、部署授权与上线门禁 | 下游真实产品仓自身要求及[本仓Release Gates](../project/DOWNSTREAM-RELEASE-GATES.md) | 本学习仓不自动授权真实客户数据/生产发布 |
| 合成示例代码与可复现测试事实 | [ai-fullstack-workbench](../../ai-fullstack-workbench/README.md)及GitHub Actions日志 | S0合成React/FastAPI代码**已存在**，但完整蓝图未实现、非生产 |
| 14天/8周/24周计划 | [可选执行模式](../learning/OPTIONAL-EXECUTION-MODES.md)与历史ROADMAP章节 | 仅用于自己选择的教学安排，不能自动登记PASS |

## 术语统一

1. **知识覆盖/INDEXED**：有专业定义、关系、权威链接和可执行或可设计的反例，并不代表实际掌握。
2. **LAB_DESIGNED**：有操作方案但未执行，不能标已通过。**CI_VERIFIED**：GitHub自动化验证了具体代码/检查的子集。**INDEPENDENT_PASS**：本人关AI独立完成变化条件、真实负例和解释，并在唯一进度台账中附证据。**PRODUCTION_VERIFIED**：符合真实业务授权、环境与发布标准，不由学习仓CI替代。
3. **P0/P1/P2**：如果出现在旧V3表中，是**自愿进行全领域覆盖挑战**时的优先深度，不是Spring/Redis/MQ/Next对所有项目的强制要求。横向专题的`P0基础`指该方向常见、值得先认识；不同业务可跳过深度实作。
4. **P1最小OTel**：只有选择相关的W8/G08完整追踪验收或当前项目明确要求跨服务Trace时必须亲自实测；日志RequestID不等于Trace，单纯做静态网页不需要部署OTel服务。
5. **Java/Spring**：全栈知识地图必须涵盖，但是否需要深学由Java岗位、既有Java业务及具体需求触发。React/Vue、FastAPI/Spring/Nest是**条件分支**。
6. **示例项目**：`ai-fullstack-workbench` 是**部分实现的合成训练切片**。Blueprint完整目录仍是设计态；其他项目可作为学习实战来源，绝非唯一主线。

## 一致性自动化门禁

- [文档完整性](../quality/check_roadmap.py)验证历史W坐标、Gate、内部相对链接与合法状态。
- [知识图](../quality/check_knowledge_map.py)验证42核心节点、依赖图、官方资料和上游路径。
- [横向基础与治理校验](../quality/check_baseline_and_consistency.py)验证X01–X17、原节点归属、正文学习卡、路由入口、版本与关键当前事实；**允许明确标明是历史快照的旧文档保留原决策文字**。
- 文档验收通过只意味着静态资料和相应CI检查通过，不意味着某款产品已上线或全部17+42项已本人独立学会。

## 决策代价与变化条件

多了一个横向基础索引，但不会维护第二份`PROGRESS`或W进度表；新项目需要行业/平台专属知识时必须以GAP登记、追加官方资料与可重现实验。任何更改本条治理规则应通过新的ADR显式覆盖，不依赖散落在旧W表中的“必修”措辞。