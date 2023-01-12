from tkinter import *
from tkinter import messagebox
import requests
from configparser import ConfigParser

url_api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file = 'weather.key'
file_a = ConfigParser()
file_a.read(api_file)
api_key = file_a['api_key']['key']

def weatherfind(city):
    final = requests.get(url_api.format(city,api_key))
    if final:
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        k_temperature = json_file['main']['temp']
        c_temperature = k_temperature - 273.15
        f_temperature = (k_temperature - 273.15)*9/5+32
        weather_display = json_file['weather'][0]['main']
        result = (city,country_name,c_temperature,f_temperature,weather_display)

        return result
    else:
        return None

def print_weather():
    city = search_city.get()
    weather = weatherfind(city)
    if weather:
        location['text'] = '{}, {}'.format(weather[0],weather[1])
        temperature_entry['text'] = '{:.2f}C,{:.2f}F'.format(weather[2],weather[3])
        weather_entry['text'] = weather[4]

    else:
        messagebox.showerror('Error', "Please enter a valid city.")




win = Tk()
win.title("Weather Look-Up")
win.configure(bg="light blue")
win.geometry("700x400")

search_city = StringVar()
enter_city = Entry(win,textvariable=search_city,fg="black", font=("Arial",30,'bold'),bg="thistle")
enter_city.pack()



search_button = Button(win,text="SEARCH CITY", width=15, font=("arial",25,'bold'),fg='white',bg='light salmon', command=print_weather)
search_button.pack()

location = Label(win,font=('Calibri',35,'bold'),bg='Cadet blue')
location.pack()

temperature_entry = Label(win, font=('Calibri',35,'bold'),bg='orchid')
temperature_entry.pack()

weather_entry = Label(win, font=('Calibri',35,'bold'),bg='orange')
weather_entry.pack()

win.mainloop()


