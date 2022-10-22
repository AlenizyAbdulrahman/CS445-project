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
import reqtonfa

class ReqtoNFA(Tk):
    def __init__(self):

        #create screen layout
        super().__init__()
        self.geometry("1200x800")
        self.title('Main page')
        self.config(bg='#669BBC')
        self.resizable(True,True)
        frame = Frame(self,bg='#669BBC')
        frame.place(x=120,y=50,width=1000,height=600)

        self.text = StringVar()
        #create buttones
        headline = Label(frame, text='Convert Reqular Expression to NFA.', fg='white',bg='#669BBC',font=('Courier',30,'bold'),pady=0).place(x=120,y=0)

        btn_back = Button(self,text='Back',bg='#F3A712',bd=0,font=('Courier',10),command=self.back_btn).place(x=20,y=20,width=100,height=50)


        txt_reqexp = Label(frame,text="Reqular Expression: ",fg='white',bg='#669BBC',font=('Courier',18),pady=20).place(x=20,y=120)
        self.reqexp = Entry(frame,font=('Courier',18,'bold'),textvariable=self.text)
        self.reqexp.place(x=300,y=130,width=500,height=45)
        btn_build = Button(frame,text='Build',bg='#F3A712',bd=0,font=('Courier',10),command=self.getresult).place(x=820,y=130,width=120,height=45)

        self.resarea = Text(frame,width=100,height=200,font=('Courier',18))
        self.resarea.pack()
        self.resarea.place(x=100,y=250)


        #back to previous page
    def back_btn(self):
        login.mainpage()
        self.destroy()
    def getresult(self):
        x = reqtonfa.reqtonfa().getresult(self.text.get())
        self.resarea.delete("1.0","end")
        self.resarea.insert(END,x)




if __name__ == "__main__":
    obj = ReqtoNFA()
    # obj = mainpage("ss")
    obj.mainloop()
