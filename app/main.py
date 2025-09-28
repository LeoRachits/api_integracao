import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de Integração - Projeto N703"}

@app.get("/weather/{city}")
def get_weather(city: str):
    api_key = "ccae9a131b963aa38d95131277b6b428"
    url = url = f"http://api.openweathermap.org/data/2.5/weather?q={city},BR&appid={api_key}&units=metric&lang=pt_br"

    
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Não foi possível obter os dados do clima"}
    
    data = response.json()
    return {
        "cidade": data["name"],
        "temperatura": data["main"]["temp"],
        "clima": data["weather"][0]["description"],
    }
