from tkinter import * # import the tkinter module for gui
from GUI.shopPage import ShopScreen
from GUI.signupPage import SignUpScreen
from GUI.adminPage import adminPage

class LoginScreen(Tk):
  def __init__(self):
    super().__init__()
    self.title('log in')
    self.resizable(0,0)

    
    self.lblUsername = Label(self, text='Username', font='arial 15 bold') 
    self.lblPassword = Label(self, text='Password', font='arial 15 bold') 

    self.entryUsername = Entry(self)
    self.entryPassword = Entry(self,show='*')

    self.buttonLogin = Button(self,text='Login',bg='blue',fg='white',command=self.checkLogin)
    self.buttonSignup = Button(self,text='Sign up',bg='blue',fg='white',command=self.signup)

    self.lblUsername.place(x=20,y=50) 
    self.lblPassword.place(x=20,y=100)

    self.entryUsername.place(x=140,y=50)
    self.entryPassword.place(x=140,y=100)

    self.buttonLogin.place(x=100,y=150)
    self.buttonSignup.place(x=200,y=150)

  def checkLogin(self):
    username= self.entryUsername.get()
    password = self.entryPassword.get()
    print(username,password)
    
  def signup(self):
    gui = SignUpScreen()
    gui.geometry('500x500')
    gui.mainLoop()
    

  def showShopPage(self):
    gui = ShopScreen()
    gui.geometry('1000x1000')
    gui.mainloop()

  def showAdminPage(self):
    gui =  adminPage()
    gui.geometry('500x500')
    gui.mainloop()
    

  def showSignupPage(self):
    gui = SignUpScreen()
    gui.geometry('500x500')
    gui.mainloop()
    
     
    

if __name__ == '__main__':
  myWindow =LoginScreen()
  myWindow.mainloop()