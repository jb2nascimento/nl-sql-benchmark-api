from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_query_should_return_benchmark_for_known_input() -> None:
    payload = {"question": "What is the compensation range for Senior Backend Engineer in London?"}

    response = client.post("/query", json=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["insufficient_data"] is False
    assert body["parsed_role_title"] == "Backend Engineer"
    assert body["parsed_seniority_level"] == "Senior"
    assert body["parsed_location"] == "London"
    assert body["benchmark"] is not None
    assert body["benchmark"]["currency"] == "GBP"
