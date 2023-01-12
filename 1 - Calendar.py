from tkinter import *
import calendar

text=calendar.calendar(2023)
root=Tk()
root.geometry("700x650")
root.title("Calendar - 2023")

l1=Label(root,text="Calendar for the Year 2023",bg='light blue', font=("arial",28,'bold'))
l1.grid(row=1,column=1)
root.config(bg="gray")
l2=Label(root, text=text,bg='pink',font="Consolas 10")
l2.grid(row=2,column=1, padx=20)

root.mainloop()