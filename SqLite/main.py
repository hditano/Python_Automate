import sqlite3
from sqlite3 import Error


def user_data():
    first_name = input('Please type your name: ')
    last_name = input('Please type your last name: ')
    my_data = [
        (first_name, last_name)
    ]
    return my_data


con = sqlite3.connect("sm_app.sqlite")

with con:
    cur = con.cursor()

    cur.execute("create table if not exists users (id integer primary key , first_name, last_name)")

    cur.execute("insert into users(first_name, last_name) values (?, ?)", ('Hernan', 'Di Tano'))

    cur.executemany("insert into users(first_name, last_name) values (?, ?)", user_data())

    cur.execute("select * from users")

    data = cur.fetchall()

    for item in data:
        print(item)
