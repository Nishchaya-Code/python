from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
l1=Label(text="Input anything 1 : ")
l1.pack()
e1=Entry()
e1.pack()
l2=Label(text="enter number 2 : ")
l2.pack()
e2=Entry()
e2.pack()
def product():
    n1=int(e1.get())
    n2=int(e1.get())
    x=n1*n2
    messagebox.showinfo("product",x)
b=Button(text="click me",command=product)
b.pack()
window.mainloop()