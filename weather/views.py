from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

# Create your views here.

load_dotenv()


def main():
    pass


def get_weather(request):
    api_key = os.getenv("WEATHER_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=" + api_key
    response = requests.get(url)
    response = response.json()
    print(response)
    return render(request, "base.html", {"weather": response})
