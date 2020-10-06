from everything_db import *
def read():
    d.execute('SELECT * FROM room_bill')
    print(d.fetchall())
read()