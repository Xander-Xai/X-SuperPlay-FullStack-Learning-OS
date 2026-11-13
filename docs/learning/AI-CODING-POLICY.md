# AI Coding 协作边界与个人独立能力

> 此文件是 [ROADMAP](../../ROADMAP.md) 的方法附件，不是第二份时间计划。AI 生成 ≠ AI 运行通过 ≠ 本人独立掌握 ≠ 生产交付。

## 最小学习闭环

原理学习 → 本人先写最小版本 → 故障注入 → 实际测试/修复 → 关闭 AI 独立讲解 → 1–7 日变化约束复测。可使用 AI 提问、审核、解释、搭建重复代码，但不要让它直接生成正在考核的核心答案。

| 本人优先实现与验收 | AI 可加速初稿 |
|---|---|
| React 状态快照、Effect 清理、跨请求竞态 | 后台 UI、表格/分页组件 |
| AbortController 超时/取消、身份刷新并发 | 基础 CRUD 接口 |
| OpenAPI 生成→前端类型检查与契约差异定位 | Pydantic/TS 类型草案 |
| SQL 锁、事务、乐观版本/幂等键 | 样例数据和测试骨架 |
| SSE 流块缓冲/事件解析/取消/重连 | UI 进度组件 |
| Celery ACK/Worker 失败/任务状态恢复 | Compose/Dockerfile/CI 初稿 |
| 高延迟/错误率根因排障与 ADR | 日志整理、文档排版 |

**所有生成内容都需审查与执行**；要保留原始测试命令与日志、变化前后、关 AI 独立修复的证据。没有证据不得预设 PASS。

## 能力等级与其他仓库的区别

- 本仓 **L1 理解**：关文档能解释机制与输入/输出/故障。
- 本仓 **L2 独立应用**：自己编码并测试关键实现。
- 本仓 **L3 工程掌握**：自己复现、定位、修复故障，说明安全/成本/可靠性/性能取舍。
- 上游 AI-Learning-OS 有独立 0–4 评分；Dev-Workbench 工程成熟度是另外的运行状态。不得把这些数值互换。

记录模板：[EXPERIMENT-TEMPLATE](EXPERIMENT-TEMPLATE.md)。

## V3.0：Java、Spring 与前端深入的 AI Coding 边界

- **优先自己写 Java**：集合/泛型业务规则、竞态/Atomic/Lock、JMM/JFR 根因、Spring Bean/`@Transactional` 代理、自调用事务失效、资源级 Spring Security。
- **优先自己写前端**：HTML/表单语义/键盘焦点、CSS 布局 bug、TS 边界、React 请求竞态/Query 回滚、SSR/Client Secret 与缓存、Node Stream 背压。
- **必须亲自串联**：Java 与 Python 服务间身份、事件/请求幂等、数据所有权、OpenAPI/事件版本、Trace Context、恢复演练。
- **AI 可协助生成初稿**：重复 CRUD、UI 组件、Spring 脚手架、数据样本、Maven 配置、Dockerfile/CI/测试框架，但不得用“AI 生成了”代表实际运行成功。
- **评判**：每次提交 commit/版本/运行命令/失败注入/原始日志与闭卷独立解释；新 G13–G24 的个人状态同样全部从 NOT_RUN 开始。
