from tkinter import *
window=Tk()
window.title('Hotel Management')
a=Label(text='Enter the quantities')
a.pack(pady=10)
b=Label(text='pizza 189')
b.pack()
c=Entry()
c.pack()
d=Label(text='MoMo 120')
d.pack()
e=Entry()
e.pack()
f=Label(text='Fry 75')
f.pack()
g=Entry()
g.pack()
h=Label(text='Burger 150')
h.pack()
i=Entry()
i.pack()
j=Label(text='Spagetti 169')
j.pack()
k=Entry()
k.pack()

output=Label(text='total 0')
output.pack(pady=10)

def mammamia():
    try :
        l=int(c.get() or 0)
        m=int(e.get() or 0)
        n=int(g.get() or 0)
        o=int(i.get() or 0)
        p=int(k.get() or 0)
        total=l*189+m*120+n*75+o*150+p*169
        output.config(text=f"total {total}")
    except:
        output.config(text="invalid input")
q=Button(text= " Place your order",command=mammamia)
q.pack()

window.mainloop()