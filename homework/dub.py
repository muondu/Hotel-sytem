import sqlite3
conn = sqlite3.connect('homework.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS name_age(name TEXT, age INTEGER)')
create_table()
def insert():
    with conn:
        c.execute('INSERT INTO name_age VALUES("Nesh",20)')
insert()
def read():
    c.execute('SELECT * FROM name_age')
    print(c.fetchall())
read()
