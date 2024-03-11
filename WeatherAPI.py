from API_Key import API_Key
import requests

import tkinter as tk
import customtkinter

resultList = []

#creating a function to send get requests to the API and display results
def getWeather(list):

    try:
        resultList[0].destroy()
        resultList.pop(0)
    except:
        pass
        
    #get request
    CITY = inputEntry.get()
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=imperial&APPID={API_Key}"
    response = requests.get(BASE_URL).json()

    #display the response
    #print (response)
    print(f"In {response['name']} there is {response['weather'][0]['main']}")
    searchResult = customtkinter.CTkLabel(app, text = f"In {response['name']} there is {response['weather'][0]['main']}")
    list.append(searchResult)
    searchResult.pack()

#system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#frame 
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Weather App")

#UI
text_font2 = ("", 18)

CitySearchLabel = customtkinter.CTkLabel(app, text="weather search by city:", font=text_font2)
CitySearchLabel.pack(pady = "20")

City = tk.StringVar()
inputEntry = customtkinter.CTkEntry(app, width = 400, height = 40, textvariable = City)
inputEntry.pack()

SearchButton = customtkinter.CTkButton(app, text = "Search!", command = lambda : getWeather(resultList))
SearchButton.pack(pady = 20)

app.mainloop()