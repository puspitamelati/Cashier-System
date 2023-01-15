from core.app import App
from termcolor import colored

class Menu :
    def __init__(self) :
        self.app = App()
    
    def get_menu (self, user) :
        if user == '1' :
            nama_item = input('nama item :\n')
            jumlah_item = input('jumlah item:\n')
            harga_item = input('harga item:\n')
            self.validation(nama_item, jumlah_item, harga_item)
        elif user == '2' :
            nama_item = input('nama item :\n')
            update_nama = input('update nama item:\n')
            self.app.update_item_name(nama_item, update_nama)
        elif user == '3' :
            nama_item = input('nama item :\n')
            update_jumlah = input('update jumlah item:\n')
            self.app.update_item_qty(nama_item, update_jumlah)
        elif user == '4' :
            nama_item = input('nama item :\n')
            update_harga = input('update harga item:\n')
            self.app.update_item_harga(nama_item, update_harga)
        elif user == '5' :
            self.app.cetak()
        else :
            pass

    def validation(self, nama_item, jumlah_item, harga_item) :
        try :
            self.app.add_item(nama_item, jumlah_item, harga_item)
            print(colored("pesanan sudah benar\n", attrs=['bold']))
        except ValueError :
            print(colored("Data masukan salah\n", 'red', attrs=['bold']))