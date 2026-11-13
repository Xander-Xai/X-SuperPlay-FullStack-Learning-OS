export type Order = { order_id: string; gross: string; refund: string; fee: string; cost: string };
export type Payout = { order_id: string; paid: string };
export type Dataset = { orders: Order[]; payouts: Payout[] };
export type Status = "MATCHED" | "AMOUNT_MISMATCH" | "MISSING_PAYOUT" | "UNKNOWN_ORDER";
export type Report = {
  summary: {
    order_count: number;
    payout_record_count: number;
    expected_payout_total: string;
    known_order_paid_total: string;
    indicative_margin_before_other_costs: string;
    status_counts: Record<Status, number>;
  };
  rows: Array<{
    order_id: string;
    status: Status;
    expected_payout: string | null;
    paid_amount: string | null;
    difference: string | null;
    indicative_margin_before_other_costs: string | null;
  }>;
  disclaimer: string;
};
