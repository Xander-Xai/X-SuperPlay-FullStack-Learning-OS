"""Local-only test API; production security/data controls are NOT implemented."""
from decimal import Decimal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field, field_validator
from .domain import Order, Payout, reconcile


class OrderIn(BaseModel):
    model_config = ConfigDict(extra="forbid")
    order_id: str = Field(min_length=1, max_length=64)
    gross: Decimal
    refund: Decimal
    fee: Decimal
    cost: Decimal

    @field_validator("gross", "refund", "fee", "cost", mode="before")
    @classmethod
    def decimal_strings_only(cls, v: object) -> object:
        if isinstance(v, (float, bool)):
            raise ValueError("use a decimal string for financial amounts, never JSON float")
        return v


class PayoutIn(BaseModel):
    model_config = ConfigDict(extra="forbid")
    order_id: str = Field(min_length=1, max_length=64)
    paid: Decimal

    @field_validator("paid", mode="before")
    @classmethod
    def decimal_strings_only(cls, v: object) -> object:
        if isinstance(v, (float, bool)):
            raise ValueError("use a decimal string for financial amounts, never JSON float")
        return v


class PreviewIn(BaseModel):
    model_config = ConfigDict(extra="forbid")
    orders: list[OrderIn] = Field(min_length=1, max_length=100)
    payouts: list[PayoutIn] = Field(max_length=100)


DEMO = {
    "orders": [
        {"order_id": "DEMO-101", "gross": "120.00", "refund": "0.00", "fee": "6.00", "cost": "70.00"},
        {"order_id": "DEMO-102", "gross": "80.00", "refund": "0.00", "fee": "4.00", "cost": "40.00"},
        {"order_id": "DEMO-103", "gross": "50.00", "refund": "0.00", "fee": "2.50", "cost": "20.00"},
    ],
    "payouts": [
        {"order_id": "DEMO-101", "paid": "114.00"},
        {"order_id": "DEMO-102", "paid": "74.00"},
        {"order_id": "DEMO-404", "paid": "9.00"},
    ],
}

app = FastAPI(title="ReconLab Synthetic Training API", version="0.1.0")


@app.get("/healthz")
def health() -> dict:
    return {"status": "ok", "environment": "training"}


@app.get("/api/demo")
def demo() -> dict:
    return DEMO


@app.post("/api/reconcile/preview")
def preview(data: PreviewIn) -> dict:
    try:
        return reconcile(
            [Order(**o.model_dump()) for o in data.orders],
            [Payout(**p.model_dump()) for p in data.payouts],
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
