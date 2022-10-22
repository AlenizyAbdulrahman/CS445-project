from cProfile import label
from cgitb import text
from ipaddress import ip_address
from logging import root
from tkinter import*
from turtle import bgcolor, left, right, width
import tkinter as tk
from tkinter import messagebox
from nbformat import write
import login
import NfaToDfa

class NFAtoDFA(Tk):
    def __init__(self):

        #create screen layout
        super().__init__()
        self.geometry("1200x800")
        self.title('Main page')
        self.config(bg='#669BBC')
        self.resizable(True,True)
        frame = Frame(self,bg='#669BBC')
        frame.place(x=120,y=50,width=1000,height=1000)

        #create buttones
        headline = Label(frame, text='Convert NFA to DFA.', fg='white',bg='#669BBC',font=('Courier',30,'bold'),pady=0).place(x=400,y=0)

        btn_back = Button(self,text='Back',bg='#F3A712',bd=0,font=('Courier',10),command=self.back_btn).place(x=20,y=20,width=100,height=50)
        # btn_reqtodfa = Button(self,text='Reqular Expression to DFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=200,width=500,height=50)
        # btn_reqtonfa = Button(self,text='Reqular Expression to NFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=300,width=500,height=50)
        # btn_nfatodfa = Button(self,text='NFA to DFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=400,width=500,height=50)

        self.text = StringVar()
        self.text2 = StringVar()
        txt_reqexp = Label(frame,text="NFA: ",fg='white',bg='#669BBC',font=('Courier',18),pady=20).place(x=20,y=120)
        self.reqexp = Entry(frame,font=('Courier',18,'bold'),textvariable=self.text)
        self.reqexp.place(x=300,y=130,width=700,height=45)

        txt_fsta = Label(frame,text="final State: ",fg='white',bg='#669BBC',font=('Courier',18),pady=20).place(x=20,y=180)
        self.fsta = Entry(frame,font=('Courier',18,'bold'),textvariable=self.text2)
        self.fsta.place(x=300,y=190,width=700,height=45)
        btn_build = Button(frame,text='Build',bg='#F3A712',bd=0,font=('Courier',10),command=self.getresult).place(x=590,y=260,width=120,height=45)

        self.resarea = Text(frame,width=600,height=20,font=('Courier',15))
        self.resarea.pack()
        self.resarea.place(x=100,y=330)


        #back to previous page
    def back_btn(self):
        login.mainpage()
        self.destroy()
    def getresult(self):
        x = NfaToDfa.nfatodfa().result(self.text.get(),self.text2.get())
        self.resarea.delete("1.0","end")
        self.resarea.insert(END,x)


if __name__ == "__main__":
    obj = NFAtoDFA()
    obj.mainloop()
