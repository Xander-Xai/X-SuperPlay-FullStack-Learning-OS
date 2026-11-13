from decimal import Decimal
import pytest
from app.domain import Order, Payout, reconcile


def sample():
    orders = [
        Order("a", Decimal("120.00"), Decimal("0"), Decimal("6"), Decimal("70")),
        Order("b", Decimal("80.00"), Decimal("0"), Decimal("4"), Decimal("40")),
        Order("c", Decimal("50.00"), Decimal("0"), Decimal("2.50"), Decimal("20")),
    ]
    payouts = [Payout("a", Decimal("114")), Payout("b", Decimal("74")), Payout("x", Decimal("9"))]
    return orders, payouts


def test_four_statuses_and_money_exact():
    orders, payouts = sample()
    report = reconcile(orders, payouts)
    assert report["summary"]["expected_payout_total"] == "237.50"
    assert report["summary"]["known_order_paid_total"] == "188.00"
    assert report["summary"]["indicative_margin_before_other_costs"] == "107.50"
    assert report["summary"]["status_counts"] == {
        "MATCHED": 1, "AMOUNT_MISMATCH": 1, "MISSING_PAYOUT": 1, "UNKNOWN_ORDER": 1
    }
    rows = {row["order_id"]: row for row in report["rows"]}
    assert rows["b"]["difference"] == "-2.00"
    assert rows["c"]["paid_amount"] is None
    assert rows["x"]["expected_payout"] is None


def test_duplicate_order_fails():
    orders, payouts = sample()
    with pytest.raises(ValueError, match="duplicate"):
        reconcile(orders + [orders[0]], payouts)


def test_duplicate_payout_not_silently_aggregated():
    orders, payouts = sample()
    with pytest.raises(ValueError, match="duplicate"):
        reconcile(orders, payouts + [payouts[0]])


@pytest.mark.parametrize("bad", ["-1", "NaN", "Infinity", "1.001"])
def test_bad_money_fails(bad):
    orders, payouts = sample()
    orders[0] = Order("a", Decimal(bad), Decimal("0"), Decimal("6"), Decimal("70"))
    with pytest.raises(ValueError):
        reconcile(orders, payouts)


def test_refund_plus_fee_exceeds_gross_is_unsupported():
    orders, payouts = sample()
    orders[0] = Order("a", Decimal("1"), Decimal("2"), Decimal("0"), Decimal("0"))
    with pytest.raises(ValueError, match="unsupported"):
        reconcile(orders, payouts)
