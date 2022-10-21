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


#mainpage you can select either send or recieve
class mainpage(Tk):
    def __init__(self):

        #create screen layout
        super().__init__()
        
        self.geometry("650x600")
        self.title('Main page')
        self.config(bg='#669BBC')
        self.resizable(True,True)
        frame = Frame(self,bg='#669BBC')
        frame.place(x=120,y=50,width=950,height=600)

        #create buttones
        headline = Label(frame, text='Please select option.', fg='white',bg='#669BBC',font=('Courier',30,'bold'),pady=0).place(x=220,y=20)

        btn_back = Button(self,text='Back',bg='#F3A712',bd=0,font=('Courier',10),command=self.back_btn).place(x=20,y=20,width=100,height=50)
        btn_reqtodfa = Button(self,text='Reqular Expression to DFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=200,width=500,height=50)
        btn_reqtonfa = Button(self,text='Reqular Expression to NFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=300,width=500,height=50)
        btn_nfatodfa = Button(self,text='NFA to DFA',bg='#F3A712',bd=0,font=('Courier',10),).place(x=350,y=400,width=500,height=50)

        #back to previous page
    def back_btn(self):
        login()
        self.destroy()






class signinpage(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("650x600")
        self.title('Sign Up')
        self.config(bg='#669BBC')
        self.resizable(False,False)

        self.frame2 = Frame(self,bg='#669BBC')
        self.frame2.place(x=120,y=50,width=550,height=500)

        self.headline2 = Label(self.frame2, text='Sign Up', fg='white',bg='#669BBC',font=('Courier',55,'bold'),pady=20).place(x=100)

        self.txt_email2 = Label(self.frame2,text='Username',fg='white',bg='#669BBC',font=('Courier',18),pady=20).place(x=30,y=120)
        self.email2 = Entry(self.frame2,font=('Courier',18,'bold'))
        self.email2.place(x=30,y=185,width=350,height=45)

        self.txt_pass2 = Label(self.frame2,text='Password',fg='white',bg='#669BBC',font=('Courier',18),pady=20).place(x=30,y=240)
        self.password2 = Entry(self.frame2,font=('Courier',18,'bold'))
        self.password2.place(x=30,y=300,width=350,height=45)

        self.btn_login = Button(self.frame2,text='Register',bg='#F3A712',bd=0,font=('Courier',18),command=self.register).place(x=30,y=380,width=350,height=50)

    #this function will create new user
    def register(self):

        #create random number as a salt with the password
        self.ran = random.randint(0,100)

        #get the user name
        self.email_in = str(self.email2.get().lower())

        #get the password and add the salt
        self.pass_in = str(self.password2.get()+str(self.ran))

        #hashing the password
        self.hash_obj = hashlib.md5(self.pass_in.encode())
        self.md5_hash = self.hash_obj.hexdigest()

        # python object to be appended
        self.data = [ {  "password": self.md5_hash, "salt": self.ran  } ]

        #call write_json function to store the data
        self.write_json(self.data,str(self.email_in),'users_data.json')

        #call function to create private and public key for the user
        self.destroy()
        login()

    # function to add to JSON
    def write_json(self,new_data,email, filename):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data[email]=(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

        


    
class login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("650x600")
        self.title('login')
        self.config(bg='#669BBC')
        self.resizable(False,False)

        frame = Frame(self,bg='#669BBC')
        frame.place(x=120,y=50,width=550,height=500)

        headline = Label(frame, text='Login', fg='white',bg='#669BBC',font=('Courier',55,'bold'),pady=20).place(x=100)

        txt_email = Label(frame,text="Username",fg='white',bg='#669BBC',font=('Courier',18),pady=20).place(x=30,y=120)
        self.email = Entry(frame,font=('Courier',18,'bold'))
        self.email.place(x=30,y=185,width=350,height=45)

        txt_pass = Label(frame,text='Password',fg='white',bg='#669BBC',font=('Courier',18),pady=20).place(x=30,y=240)
        self.password = Entry(frame,show = '*',font=('Courier',18,'bold'))
        self.password.place(x=30,y=300,width=350,height=45)

        btn_login = Button(frame,text='Login',bg='#F3A712',bd=0,font=('Courier',18),command=self.login).place(x=30,y=380,width=350,height=50)
        btn_signin = Button(frame,text='Sign Up',bg='#F3A712',bd=0,font=('Courier',10),command=self.signin).place(x=160,y=450,width=100,height=40)

    def signin(self):
        signinpage()
        self.destroy()

    # this function will check if the user registered or not if it is register it will login into home page
    def login(self):
        try:
            json_file = json.load(open("users_data.json"))      
            pass_list = [ x["password"] for x in json_file[str(self.email.get().lower())] ]
            salt_list = [ x["salt"] for x in json_file[str(self.email.get().lower())] ]
            for i in salt_list:   
                self.currpass=self.password.get()+str(i)
                hash_obj = hashlib.md5(self.currpass.encode())
                md5_hash = hash_obj.hexdigest()

                if (md5_hash) in pass_list :
                    self.user=self.email.get()
                    self.destroy()
                    mainpage()
                    
                else:
                    messagebox.showerror("Error", "Incorrect Email or Password, Please Try Again.")
        except:
                    messagebox.showerror("Error", "Incorrect Email or Password, Please Try Again.")           


if __name__ == "__main__":
    obj = login()
    # obj = mainpage("ss")
    obj.mainloop()

