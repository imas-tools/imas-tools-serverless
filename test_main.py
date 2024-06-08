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

story_txt = r"""[backgroundgroup backgrounds=[background id=schoolroom-00 src=env_3d_adv_schoolroom-00-00-noon]]"""

def test_gakuen_parser():
    client = TestClient(app)
    res = client.post(f"/story/gakuen_parser", json={
        "story_txt": story_txt
    })
    assert res.status_code == 200
    print(res.json())
    assert res.json()[0]["__tag__"] == "backgroundgroup"
