# 下游 ReconCheck 真实上线 Gate（学习→产品迁移）

> **RECONCHECK_PRODUCT = SELECTED_FOR_VALIDATION / DEVELOPMENT_ON_HOLD**。本文件约束**学习实验如何转成真实上线候选**，不构成直接授权或产品已上线声明。
>
> 事实来源：[Utility-Sites README](https://github.com/Xander-Xai/X-SuperPlay-Utility-Sites#readme)。其当前只有 README/.gitignore，没有产品源码，尚无真实付款验证证据。AI-Learning-OS 是上游知识来源；[Dev-Workbench SaaS/企业开发路线](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench/blob/main/docs/learning/PRODUCT-GUIDES.md) 是交付流程参考。

## 0. 状态的严格含义

| 状态 | 客观证据 | 可以做什么 | 不得宣称 |
|---|---|---|---|
| `TRAINING_DEMO` | 本仓有合成数据代码 + 部分测试通过 | 学习、独立实验、演示 UI/API | 能对接真实平台/财务正确/可上线 |
| `DOMAIN_SPEC_REVIEWED` | 目标用户采访、账单样本授权、平台规则/异常口径确认 | 在授权范围内完善业务规则 | 商业验证成功 |
| `PRODUCT_DEVELOPMENT_AUTHORIZED` | 业主/Owner 明确改变开发冻结状态并记录批准、范围、费用预算 | 才能开始正式 Utility-Sites 产品开发 | 已经生产发布 |
| `STAGING_CANDIDATE` | 环境/安全/隐私/接口/账单金标/数据迁移/负例通过 | 在受控授权测试环境试用 | 已获真实客户/支付 |
| `AUTHORIZED_RELEASE` | UAT 签收、资质/隐私/运行监控、备份恢复、回滚、Owner 发布批准、实际部署回执 | 允许在授权环境发布并监测 | 自动保证收入/商业成功 |

## 1. 上线前的不可省略条件

- [ ] **市场/买家证据**：明确目标平台/店铺类型、真实问题、愿付费或可验证的需求强度；产品范围、非目标、成功指标、商业验证结论。
- [ ] **官方平台账单口径**：来自有权使用的真实/脱敏样本和官方规则，确认订单/退款/促销/平台佣金/打款周期、分次打款、跨币种/时区、税务/物流/广告口径。**当前学习公式绝不可称真实利润。**
- [ ] **数据安全**：授权获取、租户隔离、最小权限、文件处理、数据保留/删除、敏感日志脱敏、导出 CSV 注入防护、隐私文本与司法辖区要求。
- [ ] **可靠性**：精确金额与币种、尾差/舍入策略、唯一流水/幂等、事务、批次版本、补偿/审计、异步 Worker/消息恢复。
- [ ] **产品交付**：可用交互与无障碍、异常态、版本化 API/CSV、基础监控、告警、人工复核/纠错入口、客服与回滚 SOP。
- [ ] **工程验收**：真实数据库集成测试、Playwright、API 契约、并发负例、备份恢复/灾难演练、依赖锁和安全扫描；第三方凭据和供应链检查。
- [ ] **安全部署**：HTTPS、服务端授权、Secrets 管理、可信主机/CORS、最小暴露端口、反代/限流/日志/基础告警。
- [ ] **发布授权**：产品 Owner 明确记录 `DEVELOPMENT_ON_HOLD` 状态已解除并批准发布；保留真实发布回执和时间、回滚责任人。
- [ ] **运营反馈**：真实用户任务成功率、问题修复时长、差错率、反馈/付费指标、运行成本、回归后的数据质量。

## 2. 迁移原则

- 不直接把学习演示代码复制为正式产品；先以实际账单语义写可审查的 **Domain Contract**，逐条金标验证，再转移经过测试的基础组件。
- 金额算法先有事实口径后编码，不能根据演示公式反推出支付方账单定义。
- 学习应用中 Java 审计服务仅用于技术训练，未来是否需要独立部署服务，应由真实系统边界和运营成本决定；不应因学过 Java 就强制微服务化。
- **不把课程 W24 的通过写作产品的商业验证成功**。即使 24 Gate 全通过，缺真实用户/合规/Owner 发布批准仍须保持 `RELEASE_BLOCKED`。

## 3. Dev-Workbench 交付复用

正式产品开发时采用 Dev-Workbench 11 阶段（discovery→spec→architecture→planning→implementation→verification→review→release→operation 等），按其 SaaS/企业/静态 Web 类型与业务模型选择检查项；必须有真实测试、审批、日志/恢复证据，而不是复用“通过”的文档勾选。
