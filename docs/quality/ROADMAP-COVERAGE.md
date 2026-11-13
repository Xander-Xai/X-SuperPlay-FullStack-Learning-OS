# V2.0 完整性与一致性对照（文档验收）

> **DOCUMENTED / LEARNING_NOT_RUN**。本矩阵只核对用户 V2.0 要求是否在仓库有明确、唯一的责任文件；不代表实验、测试、部署或本人独立能力已经完成。

| V2.0 要求 | 权威落实文件 | 核对点 |
|---|---|---|
| 一、六项纠偏、8周参考期、避免宣称30%精确重叠 | [ROADMAP](../../ROADMAP.md) `0–2 | 一条主线与现有 FastAPI/RAG Skip&Focus |
| 二、唯一主栈与选修后置 | ROADMAP `1–2；[ADR](../decisions/ADR-0001-stack-and-boundaries.md) | Vite/React/FastAPI，Next.js/Java 后置 |
| W1 5/6/5/2h | ROADMAP W1 补充 | TS request、竞态、Network |
| W2 7/4/4/3h | ROADMAP W2 补充 | React 状态/Query、Mock UI 负例 |
| W3 先6h+余12h | ROADMAP W3 补充 | OpenAPI→Orval→TS/CI、鉴权 |
| W4 5/8/3/2h | ROADMAP W4 补充 | 双连接、索引、缓存集中失效 |
| W5 Request ID vs Trace | ROADMAP W5 补充 | 浏览器/API/DB/Worker 的关联边界 |
| W6 6/6/4/2h | ROADMAP W6 补充 | Kill Worker/幂等/SSE 分块与回收 |
| W7 Docker/测试/安全/部署 | ROADMAP W7 补充 | 空环境启动、HTTPS、备份恢复 |
| W8 性能/OTel/答辩 | ROADMAP W8 补充 | P50/P95/P99、最小 Trace 必修 |
| 四、贯穿项目完整结构与 MVP/P1/P2 | [PROJECT-BLUEPRINT](../project/PROJECT-BLUEPRINT.md) + ROADMAP `4 | 单个 ai-fullstack-workbench，目录仅设计态 |
| 五、官方资料库 | ROADMAP `7、前后端 [专项字典](../learning/references/) | MDN/TS/React/FastAPI/Orval/PG/Redis/Celery/Docker/OTel |
| 六、每周3/9/4/2h、L1–L3、AI 协同 | ROADMAP `5；[AI-CODING-POLICY](../learning/AI-CODING-POLICY.md) | 人独立/AI 协助明确分离 |
| 七、12 项验收 | ROADMAP `6 + [ACCEPTANCE](../learning/ACCEPTANCE.md) | G01–G12 1:1、NOT_RUN |
| 上游/下游关联及授权 | [REPOSITORY-INDEX](../REPOSITORY-INDEX.md) | 上游研究/评分，Workbench 工程方法，Utility-Sites 产品授权 |

## 不变量

1. 只存在一个权威 `ROADMAP.md` 和一个 `docs/learning/PROGRESS.md`；专项字典不是独立第二套进度。
2. W1–W8 各 18h；每周明细合计 18h；总计 144h。学时是参考预算。
3. W8 最小 OTel Span/Trace 是 P1 必修；复杂观测平台才为 P2，不能在文档里互相矛盾。
4. G01–G12 完全对应，当前所有验收与个人能力均未运行，不伪造通过结果。
5. Monorepo 代码目录是未来目标设计，不能因为有蓝图而称应用已实现。
6. 外部仓库索引不代表自动数据同步、产品研发授权或真实交付。
