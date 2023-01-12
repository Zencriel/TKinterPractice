from datetime import datetime
import pytz
from tkinter import *
import time

def times():
    home=pytz.timezone('Asia/Kathmandu')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    pais.config(text="Kathmandu")

    home = pytz.timezone('Australia/Queensland')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock2.config(text=current_time)
    pais2.config(text="Brisbane")

    home = pytz.timezone('America/New_York')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock3.config(text=current_time)
    pais3.config(text="New York")

    home = pytz.timezone('Europe/London')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock4.config(text=current_time)
    pais4.config(text="London")

    clock.after(200,times)


win=Tk()
win.geometry('500x250')

bg_image = PhotoImage(file=(r"C:\Users\Suhrid Dhakal\Downloads\Jojos-Bizarre-Adventure.png"))

l4=Label(win, image=bg_image)
l4.place(x = 0, y = 0)

pais=Label(win,font=("arial",20,"bold"))
pais.place(x=30,y=5)
clock=Label(win,font=("arial",25,'bold'))
clock.place(x=10,y=40)
nota=Label(win,text="Hours  Minutes  Seconds", font="arial 10 bold")
nota.place(x=10,y=80)

pais2=Label(win,font=("arial",20,"bold"))
pais2.place(x=30,y=105)
clock2=Label(win,font=("arial",25,'bold'))
clock2.place(x=10,y=140)
nota2=Label(win,text="Hours  Minutes  Seconds", font="arial 10 bold")
nota2.place(x=10,y=180)

pais3=Label(win,font=("arial",20,"bold"))
pais3.place(x=330,y=105)
clock3=Label(win,font=("arial",25,'bold'))
clock3.place(x=310,y=140)
nota3=Label(win,text="Hours  Minutes  Seconds", font="arial 10 bold")
nota3.place(x=310,y=180)

pais4=Label(win,font=("arial",20,"bold"))
pais4.place(x=330,y=5)
clock4=Label(win,font=("arial",25,'bold'))
clock4.place(x=310,y=40)
nota4=Label(win,text="Hours  Minutes  Seconds", font="arial 10 bold")
nota4.place(x=310,y=80)

times()
win.mainloop()