import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWN_ENDPOINT = "https://api.openaweathermap.org/data/2.5/forecast"

# api_key = "<API_KEY>"
api_key = os.getenv("OWM_API_KEY")

weather_params = {
    "lat": 35.6895,  # Latitude for Tokyo
    "lon": 139.6917,  # Longitude for Tokyo
    "appid": api_key,
}

response = requests.get(
    OWN_ENDPOINT,
    params=weather_params
)

response.raise_for_status()  # Raise an error for bad responses

weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("It's going to rain today.")

# print(weather_data["list"][0]["main"]["temp"])  # Print the temperature of the first forecast
# print(weather_data["list"][0]["weather"][0]["description"])  # Print the weather description of the first forecast

account_sid = "<TWILIO_ACCOUNT_SID>"
auth_token = "<TWILIO_AUTH_TOKEN>"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="It's going to rain today. Don't forget your umbrella!",
    from_="<TWILIO_PHONE_NUMBER>",
    to="<YOUR_PHONE_NUMBER>"
)

print(message.sid)  # Print the status of the message
print(message.status)  # Print the status of the message
print("Message sent successfully!")  # Confirmation message
