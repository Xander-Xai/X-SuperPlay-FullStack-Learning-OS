"""Run from the j01-web-request directory: python -m pytest -q."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home_serves_html():
    response = client.get("/")
    assert response.status_code == 200
    assert "学校查询系统" in response.text


def test_all_synthetic_schools_when_query_empty():
    response = client.get("/api/schools")
    assert response.status_code == 200
    assert response.json()["total"] == 3


def test_keyword_filters_schools():
    response = client.get("/api/schools", params={"q": "广东"})
    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 1
    assert body["items"][0]["province"] == "广东"


def test_whitespace_is_removed():
    response = client.get("/api/schools", params={"q": "  广西  "})
    assert response.status_code == 200
    assert response.json()["items"][0]["name"] == "广西示例学院"


def test_no_match_returns_empty_result_not_error():
    response = client.get("/api/schools", params={"q": "不存在的学校"})
    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_too_long_query_rejected():
    response = client.get("/api/schools", params={"q": "a" * 65})
    assert response.status_code == 422
