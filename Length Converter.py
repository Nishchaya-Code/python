from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
l1=Label(text="enter number in inches : ")
l1.pack()
e1=Entry()
e1.pack()
def converter():
    n1=int(e1.get())
    x=n1*int(2.54)
    messagebox.showinfo("product",x)
b=Button(text="click me",command=converter)
b.pack()
window.mainloop()