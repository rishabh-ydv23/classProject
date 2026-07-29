from app import app

client = app.test_client()


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add():
    response = client.get("/add/10/5")
    assert response.data.decode() == "15"


def test_subtract():
    response = client.get("/subtract/10/5")
    assert response.data.decode() == "5"