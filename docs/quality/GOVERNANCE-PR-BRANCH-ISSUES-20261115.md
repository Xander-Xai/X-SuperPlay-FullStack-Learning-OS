# 2026-11-15：PR / Branch / Issue 遗留任务治理与真实验收

> **作用：一次性治理记录，不是第二套学习进度表。** 学员技能状态只写 [PROGRESS](../learning/PROGRESS.md)，产品授权以 [发布门禁](../project/DOWNSTREAM-RELEASE-GATES.md) 和下游仓真实 Owner 审批为准。仓库任务不因行政清理而被标记完成。

## 1. PR：清零待合并，保留审计历史

| PR | 内容 | GitHub 实际状态 | 结论 |
|---|---|---|---|
| [#6](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/pull/6) | 42 节点深度与路由机制 | 已合并，merge commit `4a7918f` | **CLOSED / MERGED** |
| [#7](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/pull/7) | 2026 全栈学习增量 | 已合并，merge commit `375989e` | **CLOSED / MERGED** |
| [#8](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/pull/8) | 17 项横向基础及单一治理 | 已合并，merge commit `84ddaa7` | **CLOSED / MERGED** |

复核日：现存 **OPEN PR=0**。当前 `main@84ddaa75f41ceb32dbf0603f1df3084efc95b6d6` 的 [Actions #43587661317](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/actions/runs/43587661317) 结论 **SUCCESS**。历史已失败的 CI run 仍作为调试记录保留，但对应的已合并最终提交和主分支都通过；不以旧失败判定当前 HEAD 失败。

## 2. Branch：已核实可清理的三个旧分支

| 分支 | 对应已合并 PR | 最后审计 Head SHA | 与 `main` 的内容关系 |
|---|---|---|---|
| `audit/v4.2-knowledge-depth-20261114` | #6 | `5cb7dec8abccdd7fff12a506735715d149dcf8a1` | 主分支包含全部原文件；22 个路径被后续提交修改，旧 branch 不再是权威版本 |
| `docs/integrate-2026-fullstack-execution-20261114` | #7 | `eed94b70a68739c75ecc6aa155488649c077a0a8` | 主分支包含全部原文件；22 个路径被后续提交修改 |
| `audit/complete-fullstack-basics-20261114` | #8 | `f545402f505fbceaef757e823e8a1668decd26fc` | 该分支全部 74 个文件与当前主分支同名文件的 blob SHA 一致 |

**注意**：Squash Merge 后 GitHub `compare main...old_branch` 常显示 `diverged`，这不意味着需要重新合并旧分支。必须核对对应 PR `merged=true`、所有旧分支文件在 main 可找到、PR head 与分支当前 HEAD 未变化，绝不能对旧分支做强制合并或覆盖 `main`。

使用一次性 [安全清理脚本](cleanup_merged_pr_branches.py) 与 [CI 工作流](../../.github/workflows/cleanup-merged-pr-branches.yml)：写死 PR 6/7/8 和已核对 SHA，且可按相同要求清理本次治理 PR 的工作分支。**只有 main 上真实 push 事件的 Actions token 允许 --apply**；PR 上只运行离线安全测试。若 GitHub 阻止删除、PR 未合并、SHA 漂移或缺权限，则保留分支并报告，不能直接标记已删除。工作流日志才是最终删除证据。

## 3. Issue：清理的是假完成与模糊状态，不是强行关单

| Issue | 真实状态 | 已存在的工程事实 | 未通过的不可省略门槛 | 当前处置 |
|---|---|---|---|---|
| [#1 S0](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/1) | **OPEN / HUMAN_LEARNING_NOT_RUN** | 合成 FastAPI/React 代码、pytest/Vitest/build CI 已通过 | 用户本人关 AI 独立做排序、非法输入、请求竞态和故障复现，记录 commit、原始 CI 与解释 | 保留；仅用户选这个可选练习时领取 |
| [#2 S1](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/2) | **OPEN / NOT_IMPLEMENTED** | S0 合成 API 可作实验起点 | 受限 CSV、PG/Alembic、FastAPI→Orval、真实多租户 AuthZ 与越权负例 | 保留；如选择 ReconLab 教材再设计/执行 |
| [#3 S2](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/3) | **OPEN / NOT_IMPLEMENTED** | 有同步预览代码 | PostgreSQL 状态机、幂等重试、Celery/SSE 实验、Worker kill/恢复、Compose/Trace | 保留；未取得真实测试不得关闭 |
| [#4 S3](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/4) | **OPEN / OPTIONAL_NOT_IMPLEMENTED** | Java/Spring 学习资料有入口 | 独立 Java audit 域、Spring Security、PG Testcontainers、Outbox/重复消息、JFR/并发实验 | 保留；仅岗位/当前需求确实需要时做 |
| [#5 S4](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/issues/5) | **OPEN / BLOCKED_EXTERNAL_AUTHORIZATION** | 本仓只包含合成学习环境 | 真实买家验证、平台授权账单金标、产品开发 Owner 批准、隐私安全/UAT/回滚与部署证据 | 保留；不得绕过 `DEVELOPMENT_ON_HOLD` |

**完成定义（DoD）**：
- #1 需要“本人独立变化题 + 原始测试证据 + 新场景解释”，AI 帮其完成代码不自动构成本人验收。
- #2–#4 需要可运行集成及负例，不能凭本仓知识图、文档清单、计划 PR 或纯 Mock 判定完成。
- #5 需要来自真实用户与 Owner 的授权，学习仓维护者不能代替商业决策或伪造证据。
- Close 之前在对应 Issue 留下 `commit_SHA / run_URL / tested_environment / failed_case / reviewer / artifact / human_gate`；必要时明确标 `not_planned`，仅当真实范围取消且解释充分。**保留任务 OPEN 是正确的治理结果，不应为了统计归零而关闭。**

## 4. 遗留任务执行顺序（仅在用户选择本案例时）

- **先做 S0 人类学习证据**（Issue #1），记录到唯一 [PROGRESS](../learning/PROGRESS.md)。
- 需要持久化与租户隔离时选择 S1（#2）；需要批任务可靠性时选择 S2（#3），可以按当前实际需求拆单，不强制所有仓使用完整架构。
- 需要 Java 岗练习或审计服务时选择 S3（#4）；Java 微服务不是所有应用的默认架构。
- 产品正式开发/上线走 S4（#5）的商业证据与授权门禁，独立于前述任何学习 Gate。

按需学习规则由 [ADR-0004](../decisions/ADR-0004-fullstack-foundations-and-authority.md) 优先，不能因这份治理报告恢复历史“必须先 W1→W24”或要求每个学习项目都变成 ReconCheck。

## 5. 后续 PR/Branch/Issue 固定治理 SOP

1. **PR**：明确关联 Issue/GAP、目的范围、排除项、实际执行命令、正负测试与证据；所有必需 CI 成功且 diff 已审阅才能 merge。Squash 后保留 PR 与运行记录。
2. **Branch**：feature 分支用于单一变化；仅在对应 PR 合并后、确认没有未合并文件且分支未继续新增提交时删除；禁止批量按日期删除。
3. **Issue**：标清 `LEARN / BUILD / RELEASE_GATE`、具体 DoD、前置依赖和真实状态；记录 BLOCKED 的客观原因，不随便标 DONE。
4. **单一权威**：本报告只存治理事实；学习进度以 PROGRESS 为唯一台账，真实业务产品授权归下游，CI 只能证明其真正执行的步骤。
5. **回归**：合并后检查 `main` 对应 Actions 的实际结论；若清理工作流失败，记录原因并只重试安全的核对步骤，不强制覆盖 refs。

## 6. 复核标准

- [x] 三个历史 PR 的 `merged=true` 与合并 SHA 已核对。
- [x] 三条旧分支的文件路径在当前 `main` 全部存在，且 #8 分支全部对应 blob 一致。
- [x] 五个 Issue 的实际门槛和权威状态已核对，不冒充完成。
- [x] 写出仅针对已合并 PR 的精确 branch SHA 删除保护与离线单测。
- [ ] 合并治理 PR 后，确认 GitHub 实际删掉分支的 workflow 结果。
- [ ] 确认合并后 `main` CI 无回归。
- [ ] #1–#5 真正完成（保留 OPEN，直到对应实际学习/集成/授权证据齐全）。
