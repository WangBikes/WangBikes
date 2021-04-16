from tkinter import * # import the tkinter module for gui

class login_screen(Tk):
  def __init__(self):
    super().__init__()
    self.geometry('400x400')
    self.title('log in')
    self.resizable(0,0)

    
    self.lblUsername = Label(self, text='Username', font='arial 15 bold') 
    self.lblPassword = Label(self, text='Password', font='arial 15 bold') 

    self.entryUsername = Entry(self)
    self.entryPassword = Entry(self,show='*')

    self.buttonLogin = Button(self,text='Login')
    self.buttonSignup = Button(self,text='Sign up')

    self.lblUsername.place(x=20,y=50) 
    self.lblPassword.place(x=20,y=100)

    self.entryUsername.place(x=140,y=50)
    self.entryPassword.place(x=140,y=100)

    self.buttonLogin.place(x=100,y=150)
    self.buttonSignup.place(x=200,y=150)


if __name__ == '__main__':
  myWindow = login_screen()
  myWindow.mainloop()