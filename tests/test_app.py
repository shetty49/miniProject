from app import app

def test_index() -> None:
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
