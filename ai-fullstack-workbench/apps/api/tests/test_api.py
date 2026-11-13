from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_and_demo_are_training_only():
    assert client.get("/healthz").json() == {"status": "ok", "environment": "training"}
    data = client.get("/api/demo").json()
    assert data["orders"][0]["order_id"].startswith("DEMO-")


def test_real_preview():
    data = client.get("/api/demo").json()
    response = client.post("/api/reconcile/preview", json=data)
    assert response.status_code == 200
    report = response.json()
    assert report["summary"]["expected_payout_total"] == "237.50"
    assert report["summary"]["status_counts"]["AMOUNT_MISMATCH"] == 1


def test_duplicate_payout_is_422():
    data = client.get("/api/demo").json()
    data["payouts"].append(data["payouts"][0])
    response = client.post("/api/reconcile/preview", json=data)
    assert response.status_code == 422
    assert "duplicate payout" in response.json()["detail"]


def test_float_money_is_422():
    data = client.get("/api/demo").json()
    data["orders"][0]["gross"] = 120.001
    assert client.post("/api/reconcile/preview", json=data).status_code == 422


def test_extra_field_is_422():
    data = client.get("/api/demo").json()
    data["untrusted"] = "no"
    assert client.post("/api/reconcile/preview", json=data).status_code == 422
