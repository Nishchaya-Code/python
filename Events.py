from tkinter import *
window=Tk()
window.title("Events")
window.geometry("200x200")

def Key_Press(event):
    print(event.char)
window.bind("<Key>",Key_Press)

def Button_Click(event):
    print("The button has been clicked")
button=Button(text="Click me")
button.pack()
button.bind("<Button-1>",Button_Click)

window.mainloop()