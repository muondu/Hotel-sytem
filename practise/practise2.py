from practise1 import *
def read():
    c.execute('SELECT * FROM numbers')
    print(c.fetchall())

read()

def delete():
    num = 20
    with conn:
        c.execute('DELETE FROM numbers WHERE number = ?',(num,))
delete()