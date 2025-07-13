from tkinter import *

window=Tk()
window.title("Number Pad")
window.geometry('300x430')

Nums=[[9,8,7],[6,5,4],[3,2,1],["*",0,"#"]]

for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=75)
    for j in range(3):
        frame=Frame(window,relief=RAISED,borderwidth=2)
        frame.grid(row=i,column=j)
        label=Label(frame,text=Nums[i][j])
        label.pack()

window.mainloop()