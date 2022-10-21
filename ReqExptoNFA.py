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


class ReqtoNFA(Tk):
    def __init__(self):

        #create screen layout
        super().__init__()
        self.geometry("650x600")
        self.title('Main page')
        self.config(bg='#669BBC')
        self.resizable(True,True)
        frame = Frame(self,bg='#669BBC')
        frame.place(x=120,y=50,width=1000,height=600)

        #create buttones
        headline = Label(frame, text='Convert Reqular Expression to NFA.', fg='white',bg='#669BBC',font=('Courier',30,'bold'),pady=0).place(x=120,y=0)

        btn_back = Button(self,text='Back',bg='#F3A712',bd=0,font=('Courier',10),command=self.back_btn).place(x=20,y=20,width=100,height=50)
        # btn_reqtodfa = Button(self,text='Reqular Expression to DFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=200,width=500,height=50)
        # btn_reqtonfa = Button(self,text='Reqular Expression to NFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=300,width=500,height=50)
        # btn_nfatodfa = Button(self,text='NFA to DFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=400,width=500,height=50)


        txt_reqexp = Label(frame,text="Reqular Expression: ",fg='white',bg='#669BBC',font=('Courier',18),pady=20).place(x=20,y=120)
        self.reqexp = Entry(frame,font=('Courier',18,'bold'))
        self.reqexp.place(x=300,y=130,width=500,height=45)
        btn_build = Button(frame,text='Build',bg='#F3A712',bd=0,font=('Courier',10),).place(x=820,y=130,width=120,height=45)


        #back to previous page
    def back_btn(self):
        login.mainpage("")
        self.destroy()


if __name__ == "__main__":
    obj = ReqtoNFA()
    # obj = mainpage("ss")
    obj.mainloop()
