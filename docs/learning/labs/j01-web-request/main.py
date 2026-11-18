"""J01 L00: synthetic, training-only FastAPI school search.

Run from this directory:
    python -m uvicorn main:app --reload --port 8000
"""

from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse

app = FastAPI(title="J01 L00 学校查询教学实验")

# Synthetic data only. Do not use for real admissions decisions.
SCHOOLS = [
    {"id": 1, "name": "广东示例大学", "province": "广东"},
    {"id": 2, "name": "广西示例学院", "province": "广西"},
    {"id": 3, "name": "北京示例大学", "province": "北京"},
]


@app.get("/")
def home() -> FileResponse:
    """Serve the HTML from this file's folder, regardless of working directory."""
    return FileResponse(Path(__file__).with_name("index.html"))


@app.get("/api/schools")
def get_schools(q: str = Query(default="", max_length=64)) -> dict:
    """Keyword search: teaching demo, not a database query."""
    keyword = q.strip().lower()
    matches = [
        school for school in SCHOOLS
        if keyword in school["name"].lower()
    ]
    return {"items": matches, "total": len(matches)}
