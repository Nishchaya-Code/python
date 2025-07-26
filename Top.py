from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("root window")

def TopWindow():
    Top=Toplevel()
    Top.geometry('200x200')
    Top.title('Top level Window')
    Top.mainloop()

d=Button(root,text='click me',command=TopWindow)
d.pack()

root.mainloop()