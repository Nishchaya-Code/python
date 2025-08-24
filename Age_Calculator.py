from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("500x500")
l1=Label(text="enter your year of birth : ")
l1.pack()
e1=Entry()
e1.pack()
def calculator():
    age=int(e1.get())
    cage=2025-age
    messagebox.showinfo("age calculator","your age is : "+str(cage))
b=Button(text="click me",command=calculator)
b.pack()
window.mainloop()
