from everything_db import *

def insert():
    pass
    # c.execute('INSERT INTO hotel_rooms VALUES(30)')
   

def delete():
    num = 15 
    with conn:
        c.execute('DELETE FROM hotel_rooms WHERE hotelnumber = ?',(num,))
        c.execute('SELECT * FROM hotel_rooms')
        print(c.fetchall())

delete()