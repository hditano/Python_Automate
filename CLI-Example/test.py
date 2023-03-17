import os
import time
from datetime import datetime
import sqlite3
from sqlite3 import Error

USER = os.getlogin()
TIME = datetime.now().strftime("%H:%M:%S")


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()        
            
def create_table(db_file):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    print(cur.fetchone)
    cur.execute("CREATE TABLE users(id integer PRIMARY KEY, user text, data text)")
    con.commit()
    print('Database created...')
    con.close()

def fetch_data(db_file):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.close()

def insert_data(db_file):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    my_name = input("Please type your name: ")
    my_data = input("Please type your text: ")
    temp_data = (my_name, my_data)
    cur.execute("INSERT INTO users (user, data) VALUES(? , ?)", temp_data)
    con.commit()
    con.close()
    
def users_profile(db_file):
    os.system('cls')
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute("SELECT user FROM users")
    rec_table = cur.fetchall()
    for row in rec_table:
        print(row[0])
    my_user = input("Please type your user: ")
    temp_data = (my_user,)
    cur.execute("SELECT * FROM users where user = ?", temp_data)
    record = cur.fetchall()
    for item in record:
        print(f'Username: {item[1]}')
        print(f'Data: {item[2]}')
    con.close()
 
def InitApp():
    print(f'Time: {TIME}'.ljust(0) + f'User: {USER}'.rjust(60))
    print('*** Welcome to All Around CLI ***'.center(75))
    print('***  Please choose an option  ***'.center(75))
    print('*** --------------------------***'.center(75))
    print('*** 1- View Entries           ***'.center(75))
    print('*** 2- View Users Profile     ***'.center(75))
    print('*** 3- Add Data               ***'.center(75))
    print('*** 4- Check Database         ***'.center(75))
    print('*** 5- Create Table           ***'.center(75))
    print('***  -- Choose an Option --   ***'.center(75))
    my_input = input()
    
    match my_input:
        case '1':
            p1 = Init('Hernan')
            p1.view_entries()
        case '2':
            users_profile('database.db')
        case '3':
            insert_data('database.db')
        case '4':
            fetch_data('database.db')
        case '5':
            create_table('database.db')


class Init():
    def __init__(self, user) -> None:
        self.user = user
        
    def view_entries(self) -> None:
        os.system('cls')
        print('*** Your entries are ***'.center(75))
        for k, v in ENTRIES.items():
            if v == self.user:
                for item in ENTRIES['data'].values():
                    print(item)
        time.sleep(2.0)
        os.system('cls')
        InitApp()
                
       
        
if __name__ == "__main__":
    create_connection('database.db')
    InitApp()
