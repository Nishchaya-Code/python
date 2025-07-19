from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("245x3000")
window.title("MamamiaApp(definitely not virus)")

def showmsg():
    messagebox.showwarning("Allert","Virus has been found")

button=Button(text="Clek Me",command=showmsg)
button.pack()

window.mainloop()