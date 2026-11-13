# X-SuperPlay-FullStack-Learning-OS

> **全栈工程学习执行仓** · 8 周 / 144 小时参考预算 · 唯一学习主线 · 初始状态：`PLAN / NOT_RUN`

从已有 Python/FastAPI/RAG/Agent 项目经验出发，系统补齐 React/TypeScript、Web 原理、API 契约、SQL 并发、异步可靠性、测试、部署与排障，围绕一个可验证的 `ai-fullstack-workbench` 完成端到端学习。

## 从这里开始

| 入口 | 作用 | 事实状态 |
|---|---|---|
| [ROADMAP.md](ROADMAP.md) | 唯一 W1–W8 学习计划、专项实验和完成门槛 | PLAN |
| [学习进度](docs/learning/PROGRESS.md) | 当前周、Gap、证据与复盘 | NOT_RUN |
| [前端专项字典](docs/learning/references/frontend.md) | JS/TS、React、请求状态、SSE 按需深挖 | REFERENCE |
| [后端专项字典](docs/learning/references/backend.md) | FastAPI、SQL、锁、Celery、缓存按需深挖 | REFERENCE |
| [实验模板](docs/learning/EXPERIMENT-TEMPLATE.md) | 复现、证据、失败与修复记录 | TEMPLATE |
| [仓库关系索引](docs/REPOSITORY-INDEX.md) | 上游/下游的职责与权威边界 | INDEX |
| [架构与选型决策](docs/decisions/ADR-0001-stack-and-boundaries.md) | 主栈、Next.js/Java 取舍 | PROPOSED |

## 唯一执行规则

1. 按 [ROADMAP](ROADMAP.md) 推进**一个**项目，不另外执行独立前端 8 周 + 后端 8 周路线；缺什么查专项字典并做最小故障实验。
2. W1 Web/TS → W2 React → W3 API + Orval → W4 SQL/Redis → W5 联调 → W6 Celery/SSE → W7 部署/测试 → W8 观测/验收。
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
- 未开展/未验证：八周实验、主项目编码、持续集成、生产部署、个人闭卷考核与跨仓产品交付。
- 所有 `NOT_RUN` 应在实际发生并保存证据后更新，不把文档创建等同于任务完成。
