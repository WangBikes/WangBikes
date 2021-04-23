from tkinter import *

class SignUpScreen(Tk):
  def __init__(self):
      super().__init__()
      self.title('sign up')
      self.resizable(0,0)
      
      self.lblNew_Username = Label(self, text='Enter New Username', font='arial 15 bold')

      self.lblNew_Password = Label(self, text='Enter New Password', font='arial 15 bold')

      self.entryUsername = Entry(self)
      self.entryPassword = Entry(self)
      
      self.buttonSignup = Button(self, text='Create', bg='blue', fg='white', command=self.checkCreate) 

      self.buttonLogin = Button(self, text='Log in', bg='blue', fg='white', command=self.login)

      self.lblNew_Username.place(x=20,y=50) 
      self.lblNew_Password.place(x=20,y=100)

      self.entryUsername.place(x=140,y=50)
      self.entryPassword.place(x=140,y=100)

      self.buttonLogin.place(x=100,y=150)
      self.buttonSignup.place(x=200,y=150)
      
  def login():
    pass

  def checkCreate():
    pass
    #have fun ;)