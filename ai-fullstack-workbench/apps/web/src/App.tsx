import { useEffect, useState } from "react";
import { loadDemo, preview } from "./api";
import { amount, labels } from "./domain";
import type { Dataset, Report } from "./types";
import "./styles.css";

export default function App() {
  const [dataset, setDataset] = useState<Dataset | null>(null);
  const [report, setReport] = useState<Report | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    const controller = new AbortController();
    setBusy(true);
    loadDemo(controller.signal)
      .then(async data => {
        const result = await preview(data, controller.signal);
        if (!controller.signal.aborted) {
          setDataset(data);
          setReport(result);
        }
      })
      .catch(err => {
        if (!controller.signal.aborted) setError(String(err));
      })
      .finally(() => {
        if (!controller.signal.aborted) setBusy(false);
      });
    return () => controller.abort();
  }, []);

  async function toggleMismatch() {
    if (!dataset || busy) return;
    const changed: Dataset = {
      orders: dataset.orders,
      payouts: dataset.payouts.map(p =>
        p.order_id === "DEMO-102"
          ? { ...p, paid: p.paid === "74.00" ? "76.00" : "74.00" }
          : p
      ),
    };
    setBusy(true);
    setError(null);
    try {
      const next = await preview(changed);
      setDataset(changed);
      setReport(next);
    } catch (e) {
      setError(String(e));
    } finally {
      setBusy(false);
    }
  }

  const summary = report?.summary;
  return (
    <main className="app">
      <header className="top">
        <div>
          <span className="eyebrow">X-SUPERPLAY · FULLSTACK LEARNING OS</span>
          <h1>ReconLab <span>结算核对学习沙箱</span></h1>
          <p>订单、平台费用与打款记录 — 从真实业务问题理解全栈工程。</p>
        </div>
        <span className="flag">SYNTHETIC ONLY</span>
      </header>
      <section className="notice" role="note">
        所有样本均为合成数据，不接真实电商平台、不保存真实订单、不执行付款。
        示意毛利不包含广告、运费、税费、跨币种和其他复杂结算项目。
      </section>
      {error && <p className="error" role="alert">API 错误：{error}</p>}
      <section className="actions">
        <h2>核对结果预览</h2>
        <button disabled={!dataset || busy} onClick={toggleMismatch} type="button">
          {busy ? "正在计算…" : "切换 DEMO-102 打款金额并重新核对"}
        </button>
      </section>
      {!report && <p aria-live="polite">{busy ? "正在连接 FastAPI…" : "暂无结果"}</p>}
      {summary && <>
        <section className="stats">
          <div><span>订单数</span><strong>{summary.order_count}</strong></div>
          <div><span>预计结算金额</span><strong>¥ {summary.expected_payout_total}</strong></div>
          <div><span>已识别订单的实际打款</span><strong>¥ {summary.known_order_paid_total}</strong></div>
          <div><span>示意毛利</span><strong>¥ {summary.indicative_margin_before_other_costs}</strong></div>
        </section>
        <section className="panel">
          <p className="hint">缺失打款和未知订单不会默默丢失，也不会被当成零元结算。</p>
          <div className="tableWrap">
            <table>
              <thead><tr><th>订单</th><th>状态</th><th>应结算</th><th>实际打款</th><th>差额</th></tr></thead>
              <tbody>{report?.rows.map(row => <tr key={row.order_id}>
                <td className="mono">{row.order_id}</td>
                <td><span className={"status " + row.status.toLowerCase()}>{labels[row.status]}</span></td>
                <td>{amount(row.expected_payout)}</td>
                <td>{amount(row.paid_amount)}</td>
                <td>{amount(row.difference)}</td>
              </tr>)}</tbody>
            </table>
          </div>
        </section>
      </>}
      <footer>阶段 S0：React ↔ FastAPI ↔ Decimal 核对规则。后续学习数据库、CSV 导入、权限、契约生成、消息可靠性与部署。</footer>
    </main>
  );
}
