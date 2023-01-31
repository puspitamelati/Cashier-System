from core.app import App
from termcolor import colored

class Menu :
    '''
    kelas menu terdiri dari beberapa fitur yang akan dijalankan sesuai dengan input dari user

    attributes
    ----------
        nama_item : str
                nama item belanja dari input nama_item di fungsi get_menu() kelas Menu()
        jumlah_item : int
                jumlah item belanja dari input jumlah_item di fungsi get_menu() kelas Menu()
        harga_item : int
                harga item belanja dari input harga_item di fungsi get_menu kelas Menu()

    methods
    -------
        get_menu(user)
            pilihan fitur yang disesuaikan dengan input dari user

        validation (nama_item, jumlah_item, harga_item)
            memvalidasi input yang dimasukkan user

    '''
    def __init__(self) :
        '''
        mendefinisikan dan memanggil class yang digunakan
        
        class
        -----
            App() : class
                mengkonstruksi setiap nilai inputan dari kelas Menu() dan Main() sesuai dengan perintah yang dipilih
        '''

        self.app = App()
    
    def get_menu (self, user) :
        '''
        pilihan fitur yang disesuaikan dengan input dari user
        
        parameters
        ----------
            user : str
                inuput nilai dari user
        
        local variable
        --------------
            nama_item : str
                nama item belanja dari input nama_item di fungsi get_menu() kelas Menu()
            jumlah_item : int
                jumlah item belanja dari input jumlah_item di fungsi get_menu() kelas Menu()
            harga_item : int
                harga item belanja dari input harga_item di fungsi get_menu kelas Menu()
            update_nama : str
                nama item baru
            update_qty : int
                jumlah item yang baru
            update_harga : int
                harga item yang baru
        '''
        
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
            nama_item = input('nama item :\n')
            self.app.del_item(nama_item)
        elif user == '6' :
            self.app.reset_item()
        elif user == '7' :
            self.app.cetak()
        else :
            pass
        
    def validation(self, nama_item, jumlah_item, harga_item) :
        '''
        memvalidasi input yang dimasukkan user

        parameters
        ----------
            nama_item : str
                nama item belanja dari input nama_item di fungsi get_menu() kelas Menu()
            jumlah_item : int
                jumlah item belanja dari input jumlah_item di fungsi get_menu() kelas Menu()
            harga_item : int
                harga item belanja dari input harga_item di fungsi get_menu kelas Menu()
        '''
        
        try :
            self.app.add_item(nama_item, jumlah_item, harga_item)
            print(colored("pesanan sudah benar\n", attrs=['bold']))
        except ValueError :
            print(colored("Data masukan salah\n", 'red', attrs=['bold']))