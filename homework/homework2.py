import sqlite3

conn = sqlite3.connect('homework2.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS numbers(number INTEGER)')

with conn:
    number1 = int(input("Enter a number:  "))
    c.execute('INSERT INTO numbers VALUES(?)',(number1,))


list1 = [a for dub in c.execute('SELECT * FROM numbers') for a in dub]
print(list1)
cola = sum(list1)
print(cola)
 