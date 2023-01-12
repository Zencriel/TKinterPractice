import sys
from tkinter import *
import time

def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)

win=Tk()
win.geometry("500x300")

bg_image = PhotoImage(file=(r"C:\Users\Suhrid Dhakal\Downloads\Jojos-Bizarre-Adventure.png"))

l4=Label(win, image=bg_image)
l4.place(x = 0, y = 0)

clock=Label(win,font=("Arial",50,'bold'),bg="cyan")
clock.grid(row=2,column=2,pady=25,padx=100)
times()


digital=Label(win, text="DIGITAL CLOCK", bg='Light blue', font=("Times",25,'bold'))
digital.grid(row=0,column=2)

nota=Label(win, text="Hours    Minutes   Seconds", font=("Arial",15,'bold'),bg='light green')
nota.grid(row=3,column=2)

win.mainloop()

