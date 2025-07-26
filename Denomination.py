from tkinter import *
root=Tk()
root.title('Money Calculator')
entry=Entry()
entry.pack()

def calculator():
    try:
        amount=int(entry.get())
        notes=[1000,500,100,50,20,10,5,1]
        result=" "
        for n in notes:
            count=amount//n
            if count:
                result += f"₹{n} x {count}\n"
            amount%=n
        output.delete('1.0',END)
        output.insert(END,result)
    except:
        output.delete('1.0',END)
        output.insert(END,'invalid input')

a=Button(text="click me",command=calculator)
a.pack()
output=Text()
output.pack()

root.mainloop()