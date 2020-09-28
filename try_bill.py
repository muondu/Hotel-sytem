from everything_db import *

def price():
    d.execute('SELECT * FROM breakfast_bill')
    dub1 = d.fetchall()
    print(dub1)

    d.execute('SELECT * FROM lunch_bill')
    dub2 = d.fetchall()
    print(dub2)
    
    d.execute('SELECT * FROM supper_bill')
    dub3 = d.fetchall()
    print(dub3)

    d.execute('SELECT * FROM room_bill')
    dub4 = d.fetchall()
    print(dub4)
price()

def insert():
    pass
    # d.execute('INSERT INTO room_bill VALUES(70)')
    # price()
# insert()