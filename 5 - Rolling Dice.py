from tkinter import *
import random

win=Tk()
win.geometry("700x450")
win.configure(bg='light blue')

l1=Label(win,font=("arial",200),bg='light blue')

def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1=Button(win,text="Roll the die",font=('arial',15,'bold'), command=roll, width=12,height=2)
b1.place(x=300,y=0)

win.mainloop()