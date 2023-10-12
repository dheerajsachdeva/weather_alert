import requests
from twilio.rest import Client
import os

account_sid = 'AC275ed69d1e89d2085e78cdb6b0c1351e'
auth_token = os.environ.get("AUTH_TOKEN")

api_id = os.environ.get("API_ID")
URL = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 29.678524,
    "lon": 77.001018,
    "appid": api_id,
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
    if int(condition) > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Today, it's going to Rain. bring an ☂️ Umbrella",
        from_='+12564826942',
        to='+919728883131'
    )
    print(message.status)
