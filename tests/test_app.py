import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c


def test_missing_features_returns_400(client):
    rv = client.post('/predict', json={})
    assert rv.status_code == 400


def test_incorrect_length_returns_400(client):
    rv = client.post('/predict', json={'features': [0]*899})
    assert rv.status_code == 400
