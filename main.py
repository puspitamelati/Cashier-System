from core.app import App
from core.menu import Menu

class Transaction :
  def __init__(self) :
    self.app = App()
    self.menu = Menu()
    
  def interface (self) :
    print('\n1.Add Item\n2. Update Item Name\n3. Update Item Quantity\n4. Update Item Harga\n')
    user = input('Choose your transaction :')
    print('////////////////////////////////')
    self.menu.get_menu(user)


m = Transaction()

while True :
    m.interface()