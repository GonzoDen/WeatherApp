from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests, json


def index(request):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    lat = 51.5085
    lon = -0.1257
    url = f'https://api.openweathermap.org/data/2.5/weather?units=metrics&&lat={lat}&lon={lon}&appid={API_KEY}'

    city = 'London'
    respon = requests.get(url.format(lat, lon)).json()
    rest = requests.get(url.format(city))
    print(rest.text)

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res["weather"][0]["icon"]
    }

    context = {
        'info': city_info
    }
    return render(request, 'weather/index.html')


def about(request):
    return render(request, 'weather/index.html')