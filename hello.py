from tkinter import *
import os
import pickle

scr=Tk()
scr.geometry("400x400")
scr.title("Logger")

label=Label(scr,text="Entry Logger",font=("",40))
label.pack(anchor="center")

lb2=Label(scr,text="Name:",font=("",30))
lb2.place(x=10,y=90)

in1=Entry(scr)
in1.place(x=150,y=107)

lb3=Label(scr,text="Email:",font=("",30))
lb3.place(x=10,y=170)

in2=Entry(scr)
in2.place(x=150,y=187)

bn=Button(scr,text="Access Robot Controls",font=("",25))
bn.place(x=0,y=300)

scr.mainloop()
