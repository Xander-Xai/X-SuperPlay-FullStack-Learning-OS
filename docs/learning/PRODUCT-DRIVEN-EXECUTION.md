# ReconLab可选实战案例：旧W1–W24知识如何用于一个产品

> 状态：**EXECUTION_SPEC + SYNTHETIC_SLICE_IMPLEMENTED / LEARNER_NOT_ASSESSED / PRODUCT_NOT_AUTHORIZED**。
>
> **这只是ReconLab合成核对业务的一个可选案例，不是本仓唯一项目、默认学习入口或强制W1–W24日历。** 通用入口：[需求路由](DEMAND-ROUTER.md) · [知识图](KNOWLEDGE-GRAPH.md) · [下游覆盖](REQUIREMENTS-COVERAGE.md)。下方旧W→ReconLab映射保留以供需要这一案例时参考。
>
> 产品案例参考 [Utility-Sites](https://github.com/Xander-Xai/X-SuperPlay-Utility-Sites) 公开说明的 **ReconCheck（中小电商多平台结算与利润核对）**，但该产品仓目前 `DEVELOPMENT_ON_HOLD` 且没有产品代码/商业验证。所有代码只在学习仓 `ai-fullstack-workbench`，只用合成数据，不属于其商业应用开发或生产部署授权。

## 0. 执行策略：不再“先学 24 周，最后才做产品”

- 每个真实需求从用户问题或故障倒推知识；**不要求每周选择ReconLab**。只有当该案例与实际Gap相关时才使用其代码，独立完成变化需求和失败路径。
- **课程三层**：理论 L1（能解释机制）→ 独立修改 L2（有 commit 与测试）→ 故障排查 L3（复现、归因、修复、复测）。每周必须产生可运行产物；下游真实上线还必须经过单独的产品/安全/运营验收。
- **代码基座与学习结果分开**：目前 S0 基座是 AI 辅助生成，GitHub CI 通过仅证明该版本的测试/构建，不证明学习者已掌握，也不证明商业产品可上线。
- **用户需求原则**：平台结算语义、退款/分账/手续费、实际利润计算等不能凭开发者猜；没有官方账单样本、买家访谈、商户授权就只做合成模型，不将 demo 金额当真实利润。
- **真实工程参照**：[Dev-Workbench](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench) 有运行代码、Node 工具与 CI；要按其 [SaaS/企业/静态工具开发 Gate](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench/blob/main/docs/learning/PRODUCT-GUIDES.md) 做 Spec→AC→实现→验证→发布/回滚。Workbench 的 11 阶段才是工程方法权威。
- **每次相关实战所需证据**：`project_repo@commit`、运行命令、实际输入输出、错误测试、本人不看答案的修复、结果截图/日志和学习反思。全部登记唯一 [PROGRESS](PROGRESS.md)，不凭计划内容给 PASS。

## 1. 真实项目里不断扩大的产品能力切片

| 里程碑 | 业务用户可以做什么 | 应用/运行状态 | 不可偷换的 Gate |
|---|---|---|---|
| **S0 合成核对预览** | 在 React 页面查看 3 个合成订单与 3 条合成打款，对照应结算金额，切换一个金额差异 | **已有源码、Python 与前端 CI 通过**；尚未上线/未独立学习验收 | 精确 Decimal、重复记录/异常拒绝、API HTTP 测试 |
| **S1 结构化数据与权限** | 安全地导入受控 CSV、创建核对批次、分页筛选、保存/撤销记录，仅能查看自己的数据 | 计划中 | CSV 编码/大小/公式注入，PostgreSQL 迁移、资源级 AuthZ、幂等 |
| **S2 可靠异步处理** | 大批次提交后台任务、跟踪进度、断线重连，查看可恢复结果 | 计划中 | Celery 重投递/幂等、SSE 分块与资源清理、真实故障注入 |
| **S3 多语言模块与观测** | Java 独立保存审计/规则事件，Python 核算域保持数据所有权；跨服务可追溯 | 计划中 | Spring/PG Testcontainers、事件契约、Outbox、OTel/权限 |
| **S4 上线候选** | 多租户、高并发、安全备份、灰度与回滚，有真实产品验证与明确授权才可能公开发布 | **BLOCKED（商业验证、授权及真实平台规则缺失）** | [真实上线门禁](../project/DOWNSTREAM-RELEASE-GATES.md) |

## 2. 如果选择ReconLab，该案例的24知识坐标实战参考（可跳）

| 周 | 要学懂的原理 | 直接改动的 ReconLab / 工程功能 | 必测故障或独立变化题 | 对应 Gate |
|---|---|---|---|---|
| W1 | HTTP/JS Event Loop/TS/Fetch | 在现有页面请求层加入超时、取消、`X-Request-ID` 和异常分类 | 连续切换查询 + 断网，旧响应不得覆盖新结果 | G01 |
| W2 | React 状态/生命周期/Query | 改造差异表格、筛选、排序、错误/空态、表单与键盘交互 | 破坏数据加载/慢响应，恢复正确状态 | G01 |
| W3 | FastAPI/Pydantic/OpenAPI/Orval | 将当前手写 `types.ts` / `api.ts` 替换为生成的客户端类型；契约 CI | 改订单字段并复现 TS 编译或契约测试失败 | G02/G03 |
| W4 | PostgreSQL/事务/MVCC/Redis | 将合成核对批次保存到 PG，唯一约束、迁移，加入受控缓存 | 并发写同一批次、过期热点缓存回源 | G04/G05 |
| W5 | AuthN/AuthZ/上传/Request ID | 加入登录、租户/项目级授权与限制 CSV 文件的导入接口 | 用户 B 获取用户 A 批次，CSV 恶意内容/过大文件 | G02/G08 |
| W6 | Celery/幂等/SSE | 大批次核对入队、持久化结果、前端进度/恢复 | Kill Worker、重复提交/重连、SSE 任意分块 | G06/G07 |
| W7 | Docker/Nginx/CI/CD/安全 | 单机 Compose 部署 React/API/DB/Redis/Worker，预演 TLS、回滚 | 干净环境部署、数据库丢失/恢复、凭据扫描 | G09/G10/G11 |
| W8 | P95/日志/Trace/系统设计 | 合成大批次压测、Request ID/最小 OTel Trace、整理 ERD/API/运行手册 | 定位慢 SQL/慢核对任务，真实复测 | G08/G12 |
| W09 | Java/面向对象/泛型 | 在 Java Lab 定义核对事件、金额类型与审计值对象 | 非法状态/金额输入与编译边界 | G13 |
| W10 | 集合/Stream/算法 | Java 对核对异常分组、去重、排序、汇总 | 错误 hashCode、重复事件不能静默吞掉 | G13 |
| W11 | Java 并发/JMM/JVM | 对审计事件/批次规则运行并发负载与 JFR | 数据竞争、错误线程池容量、JVM 线程阻塞 | G14 |
| W12 | Spring IoC/MVC/Boot | 新增 Java 审计/通知 API（和 Python 核算域**分离**） | 无效 Bean、参数/接口错误、服务异常 | G15 |
| W13 | Spring Data/Security | 仅审计域 Java 写其独立 PG schema，Testcontainers + 资源权限 | @Transactional 自调用、N+1、越权审计记录 | G16 |
| W14 | HTML/CSS/可访问性 | 优化导入流程/核对结果响应式、错误提示/焦点管理 | 390px 溢出、键盘不能上传/查看错误 | G17 |
| W15 | TS/ESM/Vite Toolchain | 代码拆分、构建优化、严格类型、分支/锁文件管理 | TS 契约漂移/Chunk 懒加载异常 | G18 |
| W16 | React 高级架构与 Profiler | 批次搜索/大列表虚拟化、Mutation 回滚、复杂表单验证 | 旧筛选结果覆盖新状态、回滚失败 | G19 |
| W17 | CSR/SSR/SSG/Next | 用公开**合成说明页**比较 SPA 与 SSR 的 SEO/缓存/成本 | Hydration/缓存过期，不迁移后台主 SPA | G20 |
| W18 | Node Streams/BFF | 在 Node Lab 用合成 CSV 做背压与流式处理对比 | 大文件和客户端取消，内存不持续增长 | G20 |
| W19 | MQ/Outbox/幂等事件 | 核对完成→Outbox→审计 Java 消费链（RabbitMQ 或 Kafka 选一） | DB 成功但事件暂不可送、重复/乱序消息 | G21 |
| W20 | PG/MySQL/Redis 一致性 | 设计部分打款/多条流水的可验证规则；对照分页/索引 | 重复流水、分账金额不守恒、缓存陈旧 | G21 |
| W21 | OAuth2/OIDC/多租户 | 授权模拟、租户 A/B 隔离，服务到服务认证 | 不同租户枚举订单/批次、过期 Token | G22 |
| W22 | Linux/生产工程 | 可恢复 staging 部署/迁移/备份/回滚/密钥管理 | 数据库不可用、镜像回滚/恢复 | G23 |
| W23 | Web Vitals/JFR/OTel/SLO | 大数据报表性能优化、跨 Python/Java Trace、告警 | 压测瓶颈、Java I/O 堵塞、慢 SQL | G23 |
| W24 | 系统设计/发布验收 | 完整“导入→批次→核对→审计→展示”纵切、架构答辩 | 陌生账单规则变化、回滚/权限故障 | G24 + 下游 Gate |

**W1/W2 优先学 HTML/CSS 的最小必要部分**，W14 再深入；不会先等十几周才允许做真实页面。W09–W24 的每日 96 项执行安排仍由 [执行手册](W09-W24-EXECUTION-PLAYBOOK.md) 负责，这份映射只是把课程应用到同一产品需求。

## 3. 每一课必须包含五段证据

1. **理论卡**：为什么需要该技术？核心机制/边界/可替换方案是什么？
2. **先自己改代码**：不是复制 AI 回答，而是从已经 CI 成功的基线做陌生的变化题，生成前后 Git Diff。
3. **故障卡**：明确坏输入、并发/断网/跨租户、预期失效与实际输出。
4. **验收回执**：真实运行的终端命令、测试名称与断言、GitHub CI 链接、独立口述结果。
5. **下游可采用性**：用 [Release Gates](../project/DOWNSTREAM-RELEASE-GATES.md) 判定 `TRAINING_ONLY`、`STAGING_CANDIDATE` 或 `AUTHORIZED_RELEASE`；**课程 PASS 不自动允许商业生产发布**。

## 4. Dev-Workbench 实际工程 Dogfood（不重做它的现有产品）

- **阅读与复现**：从现有代码的 `package.json`、`src/catalog.mjs`、`src/route-packs.mjs`、`test/`、`docs/learning/PRODUCT-GUIDES.md` 追踪 CLI/11 阶段路线及 Gate。
- **W1–W8**：先在学习仓验证 JS/TS/React/API/测试/部署；在 Dev-Workbench 的**工作分支**复现一个可验证的小型学习缺口（例如接口文档与 CLI 行为不一致），避免直接修改 main。
- **W15/W18**：用 Workbench 现有 Node ESM/Test 系统练习模块、打包、脚本和故障定位，必须保持其实际 CI 通过；不得把 Workbench 仅当概念资料。
- **W22–W24**：对照真实 Workbench Release/Verification Skills 生成“业务上线前 Gate”，验证计划中的备份、灰度、回滚、监控是否实际有证据。
- **跨仓变更边界**：只有确定的下游 Bug、明确范围、独立测试与正常 PR/Review 才对 Dev-Workbench 提交代码；当前不因创建学习实验而擅自改下游运行时。

## 5. 当前第一段练习：由已生成代码反向拆解

[运行说明](../../ai-fullstack-workbench/README.md) · [合成核对规则与验收](../project/RECON-LAB-CASE.md)

- 打开前端切换 DEMO-102 金额 → 观察 POST API / JSON 与金额差异由 -2.00 变为 0.00。
- 先解释为什么金额用 Python `Decimal`、为何未知打款不能丢、为何“预计毛利”不是实际利润。
- **独立改动题 A**：加入测试证明订单列表按 order_id 的稳定排序（需要真正处理匹配/未知订单的排序规则）。
- **独立改动题 B**：新增一种非法输入（重复或无效金额/超范围），让 API 明确拒绝并添加前端错误态。
- **独立改动题 C**：模拟 200ms/2s 请求、触发两次点击，修复任何可能出现的陈旧数据覆盖。
- 本次已有源码与 CI 是 **AI-assisted baseline**，**不代替你自己完成上面三题**。只有提供新 commit + 实测故障日志才能把 W1/W2 的状态从 `NOT_RUN` 改为真实学习进展。

## 6. ReconLab S0–S4 可选教学案例 Issues（非默认待办）

- [#1 S0 独立修改与故障复现](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/1)（仅选择该案例时领取；不能因基线CI成功自动关闭）
- [#2 S1 CSV + PostgreSQL + AuthZ](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/2)
- [#3 S2 Celery + SSE 可靠核对](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/3)
- [#4 S3 Java/Spring + Outbox](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/4)
- [#5 S4 真实业务与发布授权 Gate](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/5)

当前基线 [已验证的前后端 CI](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/actions/runs/43475808749) 包含 npm lockfile 的 `npm ci`、前端测试/构建与后端测试，**不等于浏览器 E2E 或独立人类学习验收**。
