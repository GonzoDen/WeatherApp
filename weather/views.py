from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests, json


def index(request):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    # LONDON
    # TODO API for city-> lat, lon
    lat = 51.5085
    lon = -0.1257
    CITY = "London"
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&units=metric&lon={}&appid={}"

    response = requests.get(url.format(lat, lon, API_KEY)).json()

    city_info = {
        'city': CITY,
        'temp': response['main']['temp'],
        'icon': response["weather"][0]["icon"]
    }

    context = {
        'info': city_info
    }

    return render(request, 'weather/index.html', context)


def about(request):
    return render(request, 'weather/index.html')
