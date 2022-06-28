from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests, json
from .models import City


def index(request):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    url_latlon = "http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}"
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&units=metric&lon={}&appid={}"

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res_latlon = requests.get(url_latlon.format(city.name, API_KEY)).json()

        lat = res_latlon[0]["lat"]
        lon = res_latlon[0]["lon"]

        response = requests.get(url.format(lat, lon, API_KEY)).json()

        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities
    }

    return render(request, 'weather/index.html', context)


def about(request):
    return render(request, 'weather/index.html')
