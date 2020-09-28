
import sqlite3


conn = sqlite3.connect('practise1.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS numbers(number INTEGER)')

def insert():
    with conn:
        c.execute('INSERT INTO numbers VALUES(20)')
# print("He is a cool video edditor")
# print("This will be always runed")
# def nesh_cool():
#     print("First file name :{}".format(__name__))



if __name__ == "__main__":
    create_table()
    insert()

#     nesh_cool()
#     print("Nesh is awsome")
#     print("Nesh is cool")