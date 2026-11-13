# ReconLab S0 合成核对纵切：实际代码与验收

> **CODE_EXISTS / CI_VERIFIED / SYNTHETIC_ONLY / NOT_PRODUCTION_READY / LEARNER_NOT_ASSESSED**
>
> 代码：[ai-fullstack-workbench](../../ai-fullstack-workbench/README.md)；GitHub Actions：[ReconLab synthetic slice](https://github.com/Xander-Xai/X-SuperPlay-FullStack-Learning-OS/actions/workflows/reconlab-slice.yml)。

## 业务演示约束

- 输入：`orders[]` 中 `order_id/gross/refund/fee/cost`；`payouts[]` 中 `order_id/paid`。金额**以十进制字符串**传输，后端用 Python `Decimal` 处理，不采用 JS 浮点数直接核算。
- 试验公式：`expected_payout = gross - refund - platform_fee`；`indicative_margin = expected_payout - cost`。
- **明确非目标**：这不是最终利润，缺广告、物流、税费、账期、冻结款、手续费组合、平台促销/补贴、分批结算、坏账、汇兑和多币种。
- 识别四种状态：`MATCHED`、`AMOUNT_MISMATCH`、`MISSING_PAYOUT`、`UNKNOWN_ORDER`。
- 预览接口**无数据库写操作**，不存储真实用户财务数据。重复订单/重复打款直接 422 拒绝，不进行不受控聚合。
- 仅限**本地学习**。没有登录、认证/资源权限、限流、文件上传安全、数据库、多租户或生产安全控制，不得公开暴露为互联网服务。

## 合成输入和明确预期

| 订单/打款 | 业务情况 | 预期 |
|---|---|---|
| DEMO-101 gross=120 fee=6 payout=114 | 金额一致 | MATCHED |
| DEMO-102 gross=80 fee=4 payout=74 | 应打款 76，实打 74 | AMOUNT_MISMATCH，差额 -2.00 |
| DEMO-103 gross=50 fee=2.50；无打款 | 缺失打款 | MISSING_PAYOUT，不能显示为 0.00 |
| DEMO-404 payout=9；订单不存在 | 未知打款 | UNKNOWN_ORDER，不得忽略 |
| 重复 order_id/payout | 非唯一 | API 422 / 领域异常 |
| 负数/NaN/超两位小数/JSON float | 无效金额 | 领域异常或 API 422 |

固定合成预览指标：`expected_payout_total=237.50`，`known_order_paid_total=188.00`，`indicative_margin_before_other_costs=107.50`。指标用于**演示规则**，不是客户或平台财务事实。

## 今日实际代码能做什么

- FastAPI 具有 `GET /healthz`、`GET /api/demo`、`POST /api/reconcile/preview`。
- Python 单元测试和 API 测试拒绝重复/非法输入；前端有 React 页面、合成差异切换与状态标签。
- CI 验收证明安装依赖后测试和 build 成功；**没有完成浏览器 Playwright E2E、正式数据权限、外部用户验收或发布**。
- 前端 `types.ts` / `api.ts` 仍是手写的 **W1/W2 学习阶段**；必须在 W3 换成 OpenAPI→Orval 并增加契约 CI。
- 当前前端没有提交 npm lockfile；正式发布前必须补 lockfile 并将 CI 从 `npm install` 切为 `npm ci`，否则可复现性不足。

## 本人应该亲手完成的三题

1. **S0-EX01**：给模拟输入增加排序规则并写失败测试（改动前/后）；解释为什么不能丢未知打款。
2. **S0-EX02**：新增故障/非法输入，确保 API 返回 422 而不是丢数据或 500，保存真实 HTTP 测试日志。
3. **S0-EX03**：连续操作打款切换、增加模拟响应延迟，修复前端可能的竞态，保存 UI 网络证据。

**通过前提**：本人自行写代码/断言、能独立讲出逻辑和根因，并在唯一 [PROGRESS](../learning/PROGRESS.md) 附 commit 和测试结果；本次 AI 辅助建立的基线不计作独立通过。

## 扩展业务的严谨顺序

S1 受控 CSV、字段映射/金标→PostgreSQL 迁移/唯一性/tenant 权限→S2 Celery/SSE 可靠异步→S3 Java 独立审计域与事件/Outbox→S4 产品审核/授权部署。没有平台账单原始语义时不得将自动化业务核算宣称精确。
