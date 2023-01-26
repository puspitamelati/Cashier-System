from core.app import App
from core.menu import Menu

class Transaction :
    '''
    Kelas yang menunjukkan tampilan atau interface dari sistm kasir

    class
    -----
        App() : 
            mengkonstruksi setiap nilai inputan dari kelas Menu() dan Main() sesuai dengan perintah yang dipilih
        Menu() :
            kelas menu terdiri dari beberapa fitur yang akan dijalankan sesuai dengan input dari user

    methods
    -------
    interface()
        print pilihan menu pada sistem kasir
    '''

    def __init__(self) :
        '''
        mendefinisikan dan memanggil kelas yang digunakan
        class
        -----
            App() :
            Menu() :
        '''

        self.app = App()
        self.menu = Menu()
    
    def interface (self) :
        '''
        mencetak pilihan menu dari sistem kasir
        
        local variables 
        ---------
        user : str
            input nilai pengguna
        
        functions
        ---------
        get_menu() : 
            fungsi dari kelas Menu()
             

        '''

        print('\n1.Add Item\n2. Update Item Name\n3. Update Item Quantity\n4. Update Item Harga\n5.pesanan')
        user = input('Choose your transaction :')
        print('////////////////////////////////')
        self.menu.get_menu(user)


m = Transaction()

while True :
    m.interface()