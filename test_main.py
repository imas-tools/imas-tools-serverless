from main import app
from fastapi.testclient import TestClient

def test_metadata():
    client = TestClient(app)
    song_name = "Sunshine See May(M@STER VERSION)"
    res = client.get(f"/recochoku/metadata?song_name={song_name}")
    assert res.status_code == 200
    assert res.json()["title"] == song_name
