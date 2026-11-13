# 下游能力覆盖矩阵：能做什么产品，就查什么知识

> 目标：**学习仓覆盖可能需要的全栈能力，而不是绑定一个下游产品的开发日程。** 核对时应问“这一类产品需要哪些能力、缺哪个 Gate/实验”，而不是“整个仓是不是ReconLab专属”。
>
> 基于 [Dev-Workbench 四条路线、静态Web、AI叠加层的产品指南](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench/blob/main/docs/learning/PRODUCT-GUIDES.md) 以及 [Utility-Sites 当前公开方向](https://github.com/Xander-Xai/X-SuperPlay-Utility-Sites)。这只是**学习能力覆盖检查**，不构成产品方向获市场验证或开发/发布授权。

## 1. 目前应支持的主要产品 / 工作流

| 场景 | 核心产品交付链 | 推荐能力节点 | 典型独立实验 / Release Gate | 不必要的强制项 |
|---|---|---|---|---|
| 静态工具站、海外SEO小工具 | 用户问题→前端页面→静态发布→使用分析 | P01 F02 F03 U01 E01 E02 P03；有SEO再F05 | 无障碍、弱网、XSS、静态托管部署与回滚 | DB/JVM/Redis/Kafka |
| SaaS / Micro-SaaS | 工作区/租户→API→DB→鉴权→测试→部署运营 | P01 P02 B01 D01 E03 E01 E02 P03；前端F04/F05二选；后端B02/B04按需求；支付再P04 | 租户A/B互斥、迁移/恢复、webhook重放、UAT | 强制同时写Python和Java |
| 企业内部Web/AI管理系统 | 岗位流程→审批/权限→接口集成→审计和UAT | P01 P02 F04 B01 E03 D01 E01 E04；B02/B04按现有生态 | 审批越权、企业IdP、重复回调、运维交接 | 默认SSR、K8s集群 |
| 微信小程序 | 页面/登录→合法域名/API→真机→平台审核 | M01 F03 F01 B01 E03 E01 P03；后端语言按现有系统 | 弱网、真机/合法域名、审核回执 | 先学完整React、Spring |
| 移动App | 设备/权限→API→离线→签名/测试分发 | M02 P01 B01 E03 E01 P03；RN或Flutter择一 | 离线恢复、权限拒绝、设备矩阵、商店签名/审核 | 同时学Flutter+RN、强制Next |
| AI/RAG/Agent/FDE应用 | 业务输入→工具/模型→状态/权限→评测→部署 | A01 B01 B02或B04 E03 E04 E01 P03；用到UI/异步/DB再接F04 B06 D01 | Tool权限、模型/检索评测、HITL、故障降级 | 每次重新预训练、强制Agent集群 |
| 开发者工具/CLI/Dev-Workbench | 需求/代码变更→Node/脚本→单测→PR→发布 | P01 P02 F03 F06 E01 E04；需要网站才F02/U01 | 模块/CLI契约、错误码、构建/CI回归、回滚 | 强行替换既有Node为Spring |
| 电商结算核对/ReconCheck示例 | 导入账单→规则核对→异常/审核→安全交付 | P01 B01 D01 E03 E01；UI选F04；异步用B06；事件用D03 | Decimal/币种口径、部分结算、重复流水、权限、恢复、官方账单金标 | Java审计服务不是此产品天然必需 |

## 2. 共同能力与按需扩展

**所有软件交付都需要**：明确需求/验收（P01）、适用范围的错误测试与版本管理（E01）、安全/部署相关门禁（P03）。

**条件触发**（不用为了“覆盖”而在每个项目安装）：

- 用户账号 / 多租户 → E03，存储需要D01；
- 长任务、浏览器刷新恢复 → B06（并根据后端栈选择任务框架）；
- 跨服务异步事件/最终一致性 → D03；
- 搜索流量、公开内容/SSR → F05或U01；
- Java岗位或现存Spring系统 → B03/B04/B05；
- 移动与小程序 → M02/M01特有平台能力；
- AI系统 → A01评测、安全/人工接管与相应API边界。

## 3. 如何验收“覆盖下游”而非“已经完成产品”

1. 某个下游出现新场景 → 更新本矩阵的一行，不迁就现有某个案例。
2. 逐项检查目标能力是否在 [知识图](KNOWLEDGE-GRAPH.md) 有节点、在 [官方资料](OFFICIAL-RESOURCES.md) 有权威原文、在 [ROADMAP](../../ROADMAP.md) 有解释/实验入口。
3. 用 [学习会话模板](GAP-SESSION-TEMPLATE.md) 对**真实缺口**建立实践证据，状态记入 [PROGRESS](PROGRESS.md)；没有用到的技术可以长期 NOT_RUN。
4. 对真实产品上线，遵循对应目标仓的 Spec/AC/安全/发布/授权，不能拿本学习仓“课程完成”代替发布审批。
5. 以后如果方向扩展为桌面应用、浏览器扩展、数据工程、游戏、实时音视频等**尚未覆盖充分**的领域，明确标 GAP 并补模块/官方资料/实验，而不是声称本图覆盖一切。

## 4. 当前仓库关系

- 上游 [AI-Learning-OS](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS)：AI研究/专项知识与评分；
- 本仓 FullStack-Learning-OS：**横向全栈能力底座 + 需求驱动学习路由**；
- [Dev-Workbench](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench)：11阶段工程方法与真实Node代码维护；
- [Utility-Sites](https://github.com/Xander-Xai/X-SuperPlay-Utility-Sites)：可能的下游产品场景，目前ReconCheck仍 DEVELOPMENT_ON_HOLD；
- [ReconLab](../../ai-fullstack-workbench/README.md)：**可选的合成教学样本**，不是上述仓库的产品开发替身。

**价值判断**：本仓能够覆盖这些产品类别的主要通用知识与关键质量门禁，但不意味着所有平台特殊规则、第三方SDK、支付合规、市场验证或生产发布都已实现；以当次需求为准增补。
