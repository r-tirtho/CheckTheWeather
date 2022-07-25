import requests
API_KEY = "3620e7c26a453f75c03f008f72f53675"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("City: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    print(f"Weather Information of {city.capitalize()}:")
    print(f"Current Weather: {str(weather).capitalize()}")
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(f"Current Temperature: {temperature}°c")
else:
    print("An error occured")


