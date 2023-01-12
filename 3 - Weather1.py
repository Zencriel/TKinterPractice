import requests
from tkinter import *

def weather():
    city=city_listbox.get()
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=167bde252e49c692cc816fa05668ff48&units=metric".format(city)
    res=requests.get(url)
    output=res.json()

    weather_status=output['weather'][0]['description']
    temperature=output['main']['temp']
    humidity=output['main']['humidity']
    wind_speed=output['wind']['speed']

    weather_status_label.configure(text="Weather Status : " + weather_status)
    temperature_label.configure(text="Temperature : " + str(temperature))
    humidity_label.configure(text="Humidity : " + str(humidity))
    windspeed_label.configure(text="Wind Speed : " + str(wind_speed))

win=Tk()
win.geometry('400x300')

bg_image = PhotoImage(file=(r"C:\Users\Suhrid Dhakal\Downloads\2275.png"))

l4=Label(win, image=bg_image)
l4.place(x = 112, y = -12)

city_name_list=["London","Melbourne","Tokyo","Kathmandu"]
city_listbox=StringVar(win)
city_listbox.set("Select the City")
option=OptionMenu(win,city_listbox,*city_name_list)
option.grid(row=2,column=2,padx=150,pady=10)

b1=Button(win,text="O",width=15,command=weather)
b1.grid(row=5, column=2,padx=150)

weather_status_label=Label(win,font=("arial",10,'bold'))
weather_status_label.grid(row=10,column=2)

temperature_label=Label(win,font=("arial",10,'bold'))
temperature_label.grid(row=12,column=2)

humidity_label=Label(win,font=("arial",10,'bold'))
humidity_label.grid(row=14,column=2)

windspeed_label=Label(win,font=("arial",10,'bold'))
windspeed_label.grid(row=16,column=2)

win.mainloop()