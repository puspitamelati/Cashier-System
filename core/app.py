import pandas as pd
from termcolor import colored

class App :
    
    def __init__(self) :
       self.transactions = []
        
    def add_item(self, nama_item, jumlah_item, harga_item) :
        self.transaction = {}
        self.nama_item = nama_item
        self.jumlah_item = int(jumlah_item)
        self.harga_item = int(harga_item)
        
        self.transaction['item'] = self.nama_item
        self.transaction['jumlah'] = self.jumlah_item
        self.transaction['harga'] = self.harga_item
        
        self.transactions.append(self.transaction)
    
    def update_item_name(self, nama_item, update_nama) :
        for i in self.transactions :
            if i['item'] == nama_item :
                i['item'] = update_nama
        
    def update_item_qty(self, nama_item, update_qty) :
        for i in self.transactions :
            if i['item'] == nama_item :
                i['jumlah'] = int(update_qty)
    
    def update_item_harga(self, nama_item, update_harga) :
        for i in self.transactions :
            if i['item'] == nama_item :
                i['harga'] = int(update_harga)
    
    def cetak (self) :
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