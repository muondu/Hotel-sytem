import sqlite3


donn = sqlite3.connect('bill.db')
d = donn.cursor()
conn = sqlite3.connect('everything.db')
c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS hotel_rooms(hotelnumber INTEGER)')
c.execute('INSERT INTO hotel_rooms VALUES(15)')
c.execute('INSERT INTO hotel_rooms VALUES(13)')
c.execute('INSERT INTO hotel_rooms VALUES(10)')


d.execute('CREATE TABLE IF NOT EXISTS breakfast_bill(price INTEGER)')
d.execute('CREATE TABLE IF NOT EXISTS lunch_bill(price INTEGER)')
d.execute('CREATE TABLE IF NOT EXISTS supper_bill(price INTEGER)')
d.execute('CREATE TABLE IF NOT EXISTS room_bill(price INTEGER)')
c.execute('CREATE TABLE IF NOT EXISTS breakfast(name TEXT)')
c.execute('INSERT INTO breakfast VALUES("Eggs")')
c.execute('INSERT INTO breakfast VALUES("Bread")')


c.execute('CREATE TABLE IF NOT EXISTS lunch(name TEXT)')
c.execute('INSERT INTO lunch VALUES("Chips")')
c.execute('INSERT INTO lunch VALUES("Fish")')

c.execute('CREATE TABLE IF NOT EXISTS dinner(name TEXT)')
c.execute('INSERT INTO dinner VALUES("Rice")')
c.execute('INSERT INTO dinner VALUES("Ugali")')

c.execute('CREATE TABLE IF NOT EXISTS desert(name TEXT)')
c.execute('INSERT INTO desert VALUES("Ice cream")')
c.execute('INSERT INTO desert VALUES("Cake")')


c.execute('CREATE TABLE IF NOT EXISTS movies(name TEXT)')
c.execute('INSERT INTO movies VALUES("Megamind")')
c.execute('INSERT INTO movies VALUES("Nesh movie")')

c.execute('CREATE TABLE IF NOT EXISTS sport(name TEXT)')
c.execute('INSERT INTO sport VALUES("Tennis")')
c.execute('INSERT INTO sport VALUES("Golf")')

