import requests

api_key = "4a214b0349794974fa4fa320a113abb9"


def api(lat, lon, typ):
    if typ == 'current':
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
    elif typ == "hourly":
        response = requests.get(
            f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}")
    elif typ == "daily":
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt=7&appid={api_key}")
    return response
