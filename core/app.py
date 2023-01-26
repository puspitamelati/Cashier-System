import pandas as pd
from termcolor import colored

class App :
    '''
    mengkonstruksi setiap nilai inputan dari kelas Menu() dan Main() sesuai dengan perintah yang dipilih

    atributes
    ----------
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

    methods
    -------
        add_item(nama_item, jumlah_item, harga_item) :
            menyimpan nilai masukan dari input di class Menu() ke tiap variabel
        update_item_name(nama_item, update_nama) :
            mengganti/mengupdate nama_item yang sudah tersimpan dengan nama yang baru
        update_item_harga(nama_item, update_harga) :
            mengganti atau mengupdate harga dari item tertentu
        cetak () :
            mencetak semua transaksi yang sudah dibuat
    '''

    def __init__(self) :
       '''
       menyimpan nilai transaksi dari dictionary di method add_item()

       local variables
       ---------------
            transactions : list
                menimpan nilai dari variabel transaksi dari method add_item
       '''

       self.transactions = []
        
    def add_item(self, nama_item, jumlah_item, harga_item) :
        '''
        menyimpan nilai masukan dari input di class Menu() ke tiap variabel
        menggabungkan masukan nilai tersebut dalam dictionary

        parameters
        ----------
            nama_item : str
                nama item belanja dari input nama_item di fungsi get_menu() kelas Menu()
            jumlah_item : int
                jumlah item belanja dari input jumlah_item di fungsi get_menu() kelas Menu()
            harga_item : int
                harga item belanja dari input harga_item di fungsi get_menu kelas Menu()
        
        local variables
        ---------------
            transaction : dict
                menampung nilai nama_item, jumlah_item, dan harga_item

        '''

        self.transaction = {}
        self.nama_item = nama_item
        self.jumlah_item = int(jumlah_item)
        self.harga_item = int(harga_item)
        
        self.transaction['item'] = self.nama_item
        self.transaction['jumlah'] = self.jumlah_item
        self.transaction['harga'] = self.harga_item
        
        self.transactions.append(self.transaction)
    
    def update_item_name(self, nama_item, update_nama) :
        '''
        mengganti/mengupdate nama_item yang sudah tersimpan dengan nama yang baru

        parameters
        ----------
            nama_item : str
                nama item yang sudah dimasukkan
            update_nama : str
                nama item baru
        '''

        for i in self.transactions :
            if i['item'] == nama_item :
                i['item'] = update_nama
        
    def update_item_qty(self, nama_item, update_qty) :
        '''
        mengganti atau mengupdate jumlah dari item tertentu

        parameters
        ----------
            nama_item : str
                nama item yang sudah dimasukkan
            update_qty : int
                jumlah item yang baru
        '''

        for i in self.transactions :
            if i['item'] == nama_item :
                i['jumlah'] = int(update_qty)
    
    def update_item_harga(self, nama_item, update_harga) :
        '''
        mengganti atau mengupdate harga dari item tertentu

        parameters
        ----------
            nama_item : str
                nama item yang sudah dimasukkan
            update_harga : int
                harga item yang baru
        '''

        for i in self.transactions :
            if i['item'] == nama_item :
                i['harga'] = int(update_harga)
    
    def cetak (self) :
        '''
        mencetak semua transaksi yang sudah dibuat
        mencetak nilai total belanja
        mencetak nilai yang harus dibayar

        local variables 
        ---------------
            df : data frame
                tabel data dari transactions 
            total : int
                total dari belanjaan
            total belanja : int
                total harga yang harus dibayar
        '''
        df = pd.DataFrame(self.transactions)
        df['total harga'] = df['jumlah'] * df['harga']
        
        total = sum(df["total harga"])
        total_belanja = sum(df["total harga"])
        
        if total_belanja > 200000 :
            total_belanja = total_belanja*0.95
        elif total_belanja > 300000 :
            total_belanja = total_belanja*0.92
        elif total_belanja > 500000 :
            total_belanja = total_belanja*0.9
        else :
            pass
        
        print(df)
        print(colored(f'\ntotal belanjaan anda : {total}',attrs=['bold']))
        print(colored(f'total yang harus dibayar : {total_belanja}',attrs=['bold']))
