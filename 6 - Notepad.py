from tkinter import *
from tkinter import filedialog

win=Tk()
win.geometry("500x600")
win.configure(bg='orange')

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def Clear():
    entry.delete(1.0,END)

def Open_File():
    file=filedialog.askopenfile(mode='r',filetypes=[('Text Files','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)

b1=Button(win,text="Save File", command=save_file, font=('arial',10,'bold'),bg='light green')
b1.place(x=10,y=10)

b2=Button(win,text="Clear",command=Clear, font=('arial',10,'bold'),bg='red')
b2.place(x=440,y=10)

b3=Button(win,text="Open File",command=Open_File, font=('arial',10,'bold'),bg='cyan')
b3.place(x=100,y=10)

entry=Text(win,height=33,width=59,wrap=WORD)
entry.place(x=10,y=50)



win.mainloop()