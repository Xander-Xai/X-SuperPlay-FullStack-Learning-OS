"""SYNTHETIC TRAINING RECONCILIATION. Not accounting or production software."""
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

CENT = Decimal("0.01")


@dataclass(frozen=True)
class Order:
    order_id: str
    gross: Decimal
    refund: Decimal
    fee: Decimal
    cost: Decimal


@dataclass(frozen=True)
class Payout:
    order_id: str
    paid: Decimal


def money(value: Decimal, name: str) -> Decimal:
    try:
        result = Decimal(value)
        if not result.is_finite() or result < 0 or result != result.quantize(CENT):
            raise ValueError(f"{name} must be a finite nonnegative amount with at most 2 decimals")
        return result.quantize(CENT)
    except (InvalidOperation, TypeError) as exc:
        raise ValueError(f"{name} is not a valid decimal amount") from exc


def identifier(value: str) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 64:
        raise ValueError("order_id must be a nonblank string of at most 64 chars")
    return value.strip()


def display(value: Decimal | None) -> str | None:
    return f"{value:.2f}" if value is not None else None


def reconcile(orders: list[Order], payouts: list[Payout]) -> dict:
    """Pure preview: no writes, side effects, platform claims or actual payments."""
    order_map: dict[str, Order] = {}
    payout_map: dict[str, Decimal] = {}
    for o in orders:
        oid = identifier(o.order_id)
        if oid in order_map:
            raise ValueError(f"duplicate order_id: {oid}")
        gross, refund, fee, cost = (
            money(o.gross, "gross"),
            money(o.refund, "refund"),
            money(o.fee, "fee"),
            money(o.cost, "cost"),
        )
        if refund + fee > gross:
            raise ValueError(f"refund+fee exceeds gross for {oid}: unsupported training case")
        order_map[oid] = Order(oid, gross, refund, fee, cost)

    for p in payouts:
        oid = identifier(p.order_id)
        if oid in payout_map:
            raise ValueError(f"duplicate payout for order_id: {oid}")
        payout_map[oid] = money(p.paid, "paid")

    counts = dict.fromkeys(("MATCHED", "AMOUNT_MISMATCH", "MISSING_PAYOUT", "UNKNOWN_ORDER"), 0)
    rows = []
    expected_total = Decimal("0.00")
    paid_total = Decimal("0.00")
    indicative_margin = Decimal("0.00")

    for oid, o in order_map.items():
        expected = o.gross - o.refund - o.fee
        expected_total += expected
        indicative_margin += expected - o.cost
        paid = payout_map.pop(oid, None)
        difference = paid - expected if paid is not None else None
        status = ("MISSING_PAYOUT" if paid is None else
                  "MATCHED" if difference == 0 else "AMOUNT_MISMATCH")
        if paid is not None:
            paid_total += paid
        counts[status] += 1
        rows.append({
            "order_id": oid,
            "status": status,
            "expected_payout": display(expected),
            "paid_amount": display(paid),
            "difference": display(difference),
            "indicative_margin_before_other_costs": display(expected - o.cost),
        })

    for oid, paid in payout_map.items():
        counts["UNKNOWN_ORDER"] += 1
        rows.append({
            "order_id": oid,
            "status": "UNKNOWN_ORDER",
            "expected_payout": None,
            "paid_amount": display(paid),
            "difference": None,
            "indicative_margin_before_other_costs": None,
        })

    return {
        "summary": {
            "order_count": len(order_map),
            "payout_record_count": len(payouts),
            "expected_payout_total": display(expected_total),
            "known_order_paid_total": display(paid_total),
            "indicative_margin_before_other_costs": display(indicative_margin),
            "status_counts": counts,
        },
        "rows": rows,
        "disclaimer": "SYNTHETIC TRAINING ONLY. Margin excludes shipping, ads, tax and other real costs.",
    }
