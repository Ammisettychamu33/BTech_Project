import json
from app import app

class FakeModel:
    def predict(self, inputs):
        # Return values shaped so app extracts [0][0][0]
        return [
            [[[10.0]]],  # distance
            [[[4.2]]],   # magnitude
            [[[180.0]]], # azimuth
            [[[12.5]]]   # depth
        ]


def test_model_prediction_with_stub(monkeypatch):
    # Stub the loader to return a fake model
    import app as app_module

    monkeypatch.setattr(app_module, "_load_model", lambda path, compile=False: FakeModel())
    # Ensure model is reloaded on request
    app_module.model = None

    client = app.test_client()
    payload = {"features": [0.0]*900}
    rv = client.post('/predict', json=payload)
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["distance"] == 10.0
    assert data["magnitude"] == 4.2
    assert data["azimuth"] == 180.0
    assert data["depth"] == 12.5
