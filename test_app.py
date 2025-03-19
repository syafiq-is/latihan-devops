import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert (
        b"Selamat datang di dunia monitoring dengan Prometheus & Grafana!"
        in response.data
    )


def test_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"http_requests_total" in response.data  # Check if Prometheus metric exists
