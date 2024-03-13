from API_Key import API_Key
import requests

import tkinter as tk
import customtkinter

resultList = []

#creating a function to send get requests to the API and display results
def getWeather(list, font):

    try:
        print (len(list))
        for i in range(0, len(list)):
            list[0].destroy()
            list.pop(0)
    except:
        pass
        
    #get request
    CITY = inputEntry.get()
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&APPID={API_Key}"
    response = requests.get(BASE_URL).json()

    #display the response

    searchResultCity = customtkinter.CTkLabel(app, text = f"City: {response['name']}", font = font)
    list.append(searchResultCity)

    searchResultWeather = customtkinter.CTkLabel(app, text = f"Weather: {response['weather'][0]['main']}")
    list.append(searchResultWeather)

    searchResultTemperature = customtkinter.CTkLabel(app, text = f"Temperature: {response['main']['temp']}°C")
    list.append(searchResultTemperature)

    for label in list:
        label.pack()

#system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#frame 
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Weather App")

#UI
text_font2 = ("", 18)
bigger_font = ("", 18)

CitySearchLabel = customtkinter.CTkLabel(app, text="weather search by city:", font=text_font2)
CitySearchLabel.pack(pady = "20")

City = tk.StringVar()
inputEntry = customtkinter.CTkEntry(app, width = 400, height = 40, textvariable = City)
inputEntry.pack()

SearchButton = customtkinter.CTkButton(app, text = "Search!", command = lambda : getWeather(resultList, bigger_font))
SearchButton.pack(pady = 20)

app.mainloop()