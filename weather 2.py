import requests
import tkinter as tk

def city_temp():
    city = entry.get()
    link1 = 'http://api.openweathermap.org/data/2.5/weather?q=%20' 
    link2 = '&units=metric&APPID=6bab4d6713adbf3a428b1f2a7454395d'
    link = link1 + city + link2

    data = requests.get(link) 
    jdata = data.json() 
    temperature = "Temperature:", jdata['main']['temp']
    feelslike = "Feels", "like:", jdata["main"]["feels_like"]
    weather = "Weather:", jdata['weather'][0]['main']
    wind = "Wind", "Speed:", jdata["wind"]["speed"]

    label['text'] = temperature
    label2['text'] = feelslike
    label3['text'] = weather
    label4['text'] = wind
    
wn=tk.Tk()
wn.title("Weather")
wn.geometry("300x330+600+300")
wn["bg"] = "#00ebff"


entry = tk.Entry(wn, justify=tk.CENTER, font = ("Arial", 15))
entry.pack(anchor="center", padx=8, pady=10)

button = tk.Button(text = "Watch City", command = city_temp, font = ("Arial", 15))
button.pack(anchor = "center", padx = 1, pady = 10)

label = tk.Label(wn, font = ("Arial", 15), background = "#00ebff")
label.pack(anchor = "center", padx = 1, pady = 10)

label2 = tk.Label(wn, font = ("Arial", 15), background = "#00ebff")
label2.pack(anchor = "center", padx = 1, pady = 1)

label3 = tk.Label(wn, font = ("Arial", 15), background = "#00ebff")
label3.pack(anchor = "center", padx = 1, pady = 10)

label4 = tk.Label(wn, font = ("Arial", 15), background = "#00ebff")
label4.pack(anchor = "center", padx = 1, pady = 6)

wn.mainloop()
    


