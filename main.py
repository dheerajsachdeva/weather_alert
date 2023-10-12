import requests

API_ID = "69f04e4613056b159c2761a9d9e664d2"
URL = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 29.678524,
    "lon": 77.001018,
    "appid": API_ID,
    "exclude": "current,minutely,daily",
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)
will_rain = False
for hour_data in weather_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    print("it will rain")
# if weather_data["hourly"]
