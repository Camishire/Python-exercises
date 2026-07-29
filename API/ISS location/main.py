import requests
from datetime import datetime

MY_LAT = 51.500000
MY_LONG= -0.123456

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# longitude=response.json()["iss_position"]["longitude"]
# latitude=response.json()["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/v2", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["sunrise"]
sunset = data["sunset"]

time_now = datetime.now()

sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]

print(sunrise, sunset)
print(time_now.hour, time_now.minute, time_now.second)