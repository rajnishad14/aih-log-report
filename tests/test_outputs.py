import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    return json.loads(REPORT.read_text())


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and is a single valid JSON object."""
    assert REPORT.exists(), "no /app/report.json found"
    data = _load()
    assert isinstance(data, dict), "report.json must be a single JSON object"


def test_total_requests():
    """Criterion 2: total_requests equals the number of request lines (6)."""
    assert _load()["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs (3)."""
    assert _load()["unique_ips"] == 3


def test_top_path():
    """Criterion 4: top_path is the most-requested path (/index.html)."""
    assert _load()["top_path"] == "/index.html"
