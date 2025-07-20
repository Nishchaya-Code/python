from tkinter import *
from tkinter.filedialog import *
window=Tk()
window.title('NoteEditor')
window.geometry('100x100')
def openfile():
    text.insert(END,open(askopenfilename()).read())
def  sevef():
    open(asksaveasfilename(defaultextension='.txt'),'w').write(text.get(1.0,END))
Button(text="open file",command=openfile).pack()
Button(text="savefile",command=sevef).pack()
text=Text(window)
text.pack()
window.mainloop()