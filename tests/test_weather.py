import requests_mock
from fastapi.testclient import TestClient
from app.main import app

API_KEY = "ccae9a131b963aa38d95131277b6b428"
client = TestClient(app)


def test_weather_endpoint_success():
    mock_response = {
        "name": "Fortaleza",
        "main": {"temp": 30.5},
        "weather": [{"description": "céu limpo"}]
    }

    with requests_mock.Mocker() as m:
        m.get(f"http://api.openweathermap.org/data/2.5/weather?q=Fortaleza,BR&appid={API_KEY}&units=metric&lang=pt_br",
              json=mock_response, status_code=200)

        response = client.get("/weather/Fortaleza")

    assert response.status_code == 200
    assert response.json() == {
        "cidade": "Fortaleza",
        "temperatura": 30.5,
        "clima": "céu limpo"
    }


def test_weather_endpoint_failure():
    with requests_mock.Mocker() as m:
        m.get(f"http://api.openweathermap.org/data/2.5/weather?q=Fortaleza,BR&appid={API_KEY}&units=metric&lang=pt_br",
              status_code=401, text="Invalid API key")

        response = client.get("/weather/Fortaleza")

    assert response.status_code == 200
    assert response.json() == {"error": "Não foi possível obter os dados do clima"}
