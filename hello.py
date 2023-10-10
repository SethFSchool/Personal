from tkinter import *
from tkinter import messagebox

scr=Tk()
scr.geometry("500x500")
scr.title("Login")

label=Label(scr,text="Login",font=("",40))
label.pack(anchor="center")

lb2=Label(scr,text="Email:",font=("",30))
lb2.place(x=10,y-90)

in1=Entry(scr)
in1.place(x=200,y=100)

lb3=Label(window,text="Password:",font=("",30))
lb3.place(x=10,y=170)

in2=Entry(scr)
in2.place(x=200,y=100)

bn=Button(scr,text="Apply",font=("",25))
bn.place(x=150,y=300)

scr.mainloop()
