# 全栈项目最终 12 项 Gate（G01–G12）

> 初始状态：全部 **NOT_RUN / UNASSESSED**。文档通过、CI 通过与本人独立通过是不同概念。对应 [唯一 ROADMAP](../../ROADMAP.md) 的 G01–G12，不另建进度表。

| Gate | 要求 | 应保留的独立实验证据 | 必测反例 |
|---|---|---|---|
| G01 | React 登录/列表/表单/分页/路由、异步状态 | 浏览器/E2E、Query 状态、本人实现 | 断网、空值、快速切换、重复点击 |
| G02 | API 校验、异常、认证及资源级权限 | Pytest/响应/数据库状态 | 400/401/403、用户 B 越权 A |
| G03 | OpenAPI→Orval→Typecheck/CI 漂移 | 导出文件与生成命令、失败再修复日志 | 改响应字段后 TS 校验或契约测试暴露 |
| G04 | PostgreSQL 事务/并发/索引 | 双连接命令、无超扣断言、EXPLAIN 报告 | 丢失更新、锁等待/死锁、回滚 |
| G05 | Redis 热点失效保护 | 回源并发、QPS/延迟数据对照 | Key 集中到期后请求放大 |
| G06 | Celery 状态/幂等/Worker 恢复 | Worker 终止/重试和 DB 状态 | 重投递、重复副作用、悬挂状态 |
| G07 | SSE 分块/重连/取消/资源清理 | 任意 chunk 拆分、网络断连测试 | chunk≠event、代理缓冲、资源泄漏 |
| G08 | X-Request-ID 与最小 OTel Trace | Network→API/Worker 日志、traceparent/Span 导出 | UUID 存在但 Trace 没有跨度 |
| G09 | Compose 干净环境启动和持久化 | 环境/命令、Healthcheck、重启数据 | 缺失环境、容器重启丢数据 |
| G10 | CI/单测/集成/E2E/权限负例 | GitHub Actions 运行及 Playwright/Pytest | 仅 Mock 通过、服务端越权未测 |
| G11 | HTTPS/密钥/备份恢复/回滚 | TLS 与配置证据、恢复后的完整性 | Secret 泄漏、备份不可恢复 |
| G12 | 架构/ERD/API/部署/答辩 | 图文资料、问题回答、独立陌生约束复测 | 讲不清根因或 AI 代写含糊 |

## 状态与硬门槛

- `NOT_RUN` 未执行；`IN_PROGRESS` 正在做；`PARTIAL` 有缺失；`FAIL` 测试失败；`BLOCKED` 外部前提不足；`PASS_WITH_EVIDENCE` 真实命令、负例、解释和复测完整。
- 证据字段：测试日期、环境版本、`project_repo@full_commit`、命令/断言/原始日志路径、失败与修复、AI_ASSISTED/INDEPENDENT 范围、后续迁移复测日期。
- 任意未授权跨用户泄露、泄密、未批准外部写操作，或把 Mock/教程/CI 讲成真实生产交付，均不可判 PASS。
- W7/W8 的 HTTPS/生产就绪演练如缺域名或授权环境应标 BLOCKED，不可伪造已经上线的事实。

## 独立能力标准

L1=关文档能解释；L2=独立编码测试；L3=故障注入/定位/修复与取舍说明。与上游 AI-Learning-OS 的 0–4 独立量表，以及 Dev-Workbench 的工程成熟度等级各自独立。

每次记录可复制 [实验模板](EXPERIMENT-TEMPLATE.md)；学习状态只更新 [PROGRESS.md](PROGRESS.md)。
