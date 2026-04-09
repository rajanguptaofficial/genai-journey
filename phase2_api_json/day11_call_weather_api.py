import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true"

response = requests.get(url)

data = response.json()

print(data["current_weather_units"]["temperature"])
print(data["current_weather_units"]["windspeed"])