import sqlite3
from sqlite3 import Error

class MyData():
    def __init__(self) -> None:
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
    
    # Lo usamos para confirmar el Context Manager - Mirar ultimo metodo  
    def __enter__(self):
        return self
   
    def create_table(self):
        self.cur.execute("CREATE TABLE users(id integer PRIMARY KEY, user text, data text)")
        self.con.commit()
        print("Database Created")
    
    def fetch_data(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
    
    def insert_data(self):
        my_name = input("Please type your name: ")
        my_data = input("Please type your text: ")
        temp_data = (my_name, my_data)
        self.cur.execute("INSERT INTO users (user, data) VALUES(?, ?)", temp_data)
        self.con.commit()
        
    def users_profile(self):
        self.cur.execute("SELECT user FROM users")
        rec_table = self.cur.fetchall()
        for row in rec_table:
            print(row[0])
        my_user = input("Please type your user: ")
        temp_data = (my_user,)
        self.cur.execute("SELECT * FROM users where user = ?", temp_data)
        record = self.cur.fetchall()
        for item in record:
            print(f'Username: {item[1]}')
            print(f'Data: {item[2]}')
    
    # Context Manager que nos cierra todo lo que esta abierto
    # Va en conjunto con el with MyData() en el archivo test.py
    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()
        self.con.close()