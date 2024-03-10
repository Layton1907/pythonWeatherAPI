from API_Key import API_Key
import datetime as dt
import requests

#Creating a URL to send requests
CITY = "Brighton"
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=imperial&APPID={API_Key}"



response = requests.get(BASE_URL).json()

print (response)