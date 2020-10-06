
import sqlite3


conn = sqlite3.connect('practise1.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS numbers(number INTEGER)')

def insert():
    with conn:
￼ Use your coins in the shop or just gamble them (dice, slots, cups, etc)
￼ Get MORE COINS with daily, weekly and vote
￼ Get items with chop and fish to craft equipment with craft!
HOW DOES THE DUNGEON WORK?
￼ When you feel ready, buy a dungeon key and enter with dungeon! If you kill the boss, you will unlock the next area!
￼ New areas means new items, recipes, commands, enemies, boosts and a harder dungeon

Check all commands with help!
Make sure to read the "rules" command too!
￼
djdennis33Today at 9:21 AM
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