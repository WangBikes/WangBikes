from tkinter import * # import the tkinter module for gui

class login_screen(Tk):
  def __init__(self):
    super().__init__()
    self.geometry('400x400')
    self.title('log in')
    self.resizable(0,0)

    
    self.lblUsername = Label(self, text='Username', font='arial 15 bold') 
    self.lblPassword = Label(self, text='Password', font='arial 15 bold') #create a label for passwords
    self.lblUsername.place(x=20,y=40) #place the username and password labels
    self.lblPassword.place(x=20,y=100)

    self.entUsername = Label(self, text='', font='arial 15 bold') #create a label for username
    self.entPassword = Label(self, text='', font='arial 15 bold') #create a label for passwords
    self.entUsername.place(x=120,y=40) #place the username and password labels
    self.entPassword.place(x=120,y=100)
#login screen
#login function
#register
if __name__ == '__main__': #when main.py is ran do the following
  myWindow = login_screen()
  myWindow.mainloop()
  
