# ai-fullstack-workbench · ReconLab 学习产品切片

> **SYNTHETIC TRAINING ONLY · CODE EXISTS / TESTED IN CI · NO PRODUCTION AUTHORIZATION**

这是 FullStack-Learning-OS 的首个可运行、可测试的**业务纵切示例**。业务方向参考 Utility-Sites 公共 README 的结算核对需求，但不等于正式 ReconCheck，也不处理任何真实商户数据。

## 已实现的能力

- **后端**：FastAPI + Python `Decimal` 结算预览算法，检查精确金额、重复订单、无对应打款和参数异常。
- **前端**：React + TypeScript + Vite 页面，展示核对结果，点击按钮切换 `DEMO-102` 金额并重新请求后端。
- **自动化 CI**：pytest 单元/API 测试、Vitest 前端测试、TypeScript 类型检查和 Vite 构建；已提交 npm lockfile 并由 `npm ci` 验证。见 [工作流](../.github/workflows/reconlab-slice.yml)。
- **不存在**：真实平台接入、商户账户/真实 CSV、数据库、身份认证、正式分账算法、Docker 部署和生产级安全策略。

## 本地启动（两个终端）

后端（Python 3.12+，在 API 目录执行）：

```bash
cd ai-fullstack-workbench/apps/api
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

后端接口：`http://127.0.0.1:8000/docs`

前端（Node 22+，在 Web 目录执行）：

```bash
cd ai-fullstack-workbench/apps/web
npm ci
npm run dev
```

浏览器：`http://127.0.0.1:5173`。Vite 本地代理将 `/api` 转发到 127.0.0.1:8000。**不要将这个无鉴权教学 API 绑定到公网。**

## 测试与故障实验

```bash
cd ai-fullstack-workbench/apps/api
python -m pytest -q

cd ../web
npm ci
npm run test
npm run build
```

实际测试中，合成样本包含金额相符、差异 -2.00、缺失打款和未知订单；重复/不合法金额应拒绝，不能静默汇总。

**正式学习不以 AI 已生成的代码为 PASS**。请按 [S0 核对规则/独立变化题](../docs/project/RECON-LAB-CASE.md) 自己改代码、做负例、提交证据。后续每周的真实产品任务在 [产品驱动学习映射](../docs/learning/PRODUCT-DRIVEN-EXECUTION.md)。

## 正式产品/上线边界

这段代码仅适合**学习环境演示**。实际 ReconCheck 仍在下游 Utility-Sites 的 `DEVELOPMENT_ON_HOLD` 状态。需要商业验证、正式授权、真实平台账单规则、安全/隐私、产品验收、部署回滚与运营责任后，才可能成为下游上线候选，见 [Release Gates](../docs/project/DOWNSTREAM-RELEASE-GATES.md)。
