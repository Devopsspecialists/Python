import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "0719871e29da1197735e25b94824c22c"
account_sid = "AC4f2c7e2a1ee49923bbfe4f09646a0c01"
auth_token = "cac7ec7d84f127cec26dbbee65707112"


weather_params = {
    "lat": 59.332790,
    "lon": 18.064489,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+19362825572",
        to="+46737364476"
    )
    print(message.status)
