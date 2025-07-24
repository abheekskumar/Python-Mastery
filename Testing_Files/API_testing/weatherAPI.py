import requests

API_KEY = "653c996a2506c811d681838c25d05498"
city = "Houston"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)
data = response.json()
print(data)
print(data["weather"][0]["description"])
