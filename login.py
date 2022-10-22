from cProfile import label
from cgitb import text
from ipaddress import ip_address
from logging import root
from tkinter import*
from turtle import bgcolor, left, right, width
import tkinter as tk
import json
from tkinter import messagebox
from nbformat import write
import hashlib
import random 
import ReqExptoNFAGUI
import ReqExptoDFAGUI
import nfaTOdfaGUI


#mainpage you can select either send or recieve
class mainpage(Tk):
    def __init__(self):

        #create screen layout
        super().__init__()
        
        self.geometry("1200x800")
        self.title('Main page')
        self.config(bg='#669BBC')
        self.resizable(True,True)
        frame = Frame(self,bg='#669BBC')
        frame.place(x=120,y=50,width=950,height=600)

        #create buttones
        headline = Label(frame, text='Please select option.', fg='white',bg='#669BBC',font=('Courier',30,'bold'),pady=0).place(x=220,y=20)

        btn_reqtodfa = Button(self,text='Reqular Expression to DFA',bg='#F3A712',bd=0,font=('Courier',10),command=self.todfa).place(x=350,y=200,width=500,height=50)
        btn_reqtonfa = Button(self,text='Reqular Expression to NFA',bg='#F3A712',bd=0,font=('Courier',10),command=self.tonfa).place(x=350,y=300,width=500,height=50)
        btn_nfatodfa = Button(self,text='NFA to DFA',bg='#F3A712',bd=0,font=('Courier',10),command=self.nfatodfa).place(x=350,y=400,width=500,height=50)


    def tonfa(self):
        self.destroy()
        ReqExptoNFAGUI.ReqtoNFA()
    def todfa(self):
        self.destroy()
        ReqExptoDFAGUI.ReqtoDFA()
    def nfatodfa(self):
        self.destroy()
        nfaTOdfaGUI.NFAtoDFA()
        
if __name__ == "__main__":
    obj = mainpage()
    # obj = mainpage("ss")s
    obj.mainloop()

