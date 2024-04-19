from main import app
from fastapi.testclient import TestClient

def test_metadata():
    client = TestClient(app)
    song_name = "Sunshine See May(M@STER VERSION)"
    res = client.get(f"/recochoku/metadata?song_name={song_name}")
    assert res.status_code == 200
    assert res.json()["title"] == song_name

def test_month_schedule():
    client = TestClient(app)
    res = client.get(f"/portal/schedule/month")
    assert res.status_code == 200
    assert len(res.json()["article_list"]) > 0


def test_today_schedule():
    client = TestClient(app)
    res = client.get(f"/portal/schedule/today")
    assert res.status_code == 200
    assert len(res.json()["article_list"]) > 0
