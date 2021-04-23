from tkinter import *

class ShopScreen(Tk):
  def __init__(self):
    super().__init__()
    self.title('Wang Bikes')
    self.resizable(0,0)

    self.kidsBikeButton = Button(self,text='Kid\'s bike',bg='green',fg='white')

    self.mountainBikeButton = Button(self, text='Mountain Bikes',bg='brown',fg='white')

    
    self.kidsBikeButton.grid(row=1,column=1)
    self.mountainBikeButton.grid(row=1,column=3)




  #have fun ;)
  