from fastapi.testclient import TestClient  # ou pode usar starlette.testclient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de Integração - Projeto N703"}
