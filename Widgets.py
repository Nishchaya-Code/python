from tkinter import *
window=Tk()
window.title("Widgets for Starters")
window.geometry("200x201")


label=Label(text="Enter your Name",bg='cyan',fg='yellow')
label.pack()


entry=Entry()
entry.pack()

def fun():
    c=entry.get()
    txt.insert(END,"Welcome to codingal dear ")
    txt.insert(END,c)

b=Button(text='click me for the result',command=fun)
b.pack()

txt=Text()
txt.pack()

window.mainloop()