import pytest
import requests

url = "http://localhost:6016/api/v1/"


@pytest.fixture
def headers():
    return {
        'Content-Type': 'application/json'
    }


def test_search(headers):
    payload = {
        "input_query": "What the AI maturity themes are?"
    }
    response = requests.post(f"{url}search", headers=headers, json=payload)
    assert response.status_code == 200
    print(response.json())
