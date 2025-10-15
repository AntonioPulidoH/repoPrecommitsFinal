import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.testing = True
    return flask_app.test_client()


def test_home_ok(client):
    resp = client.get("/")
    assert resp.status_code == 333
    assert "Docker" in resp.get_data(as_text=True)
