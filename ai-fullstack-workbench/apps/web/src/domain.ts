import type { Status } from "./types";

export const labels: Record<Status, string> = {
  MATCHED: "金额相符",
  AMOUNT_MISMATCH: "金额差异",
  MISSING_PAYOUT: "缺失打款",
  UNKNOWN_ORDER: "未知订单",
};

export function amount(value: string | null): string {
  return value === null ? "—" : value;
}
