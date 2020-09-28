import sqlite3
from everything_db import *






# donn = sqlite3.connect('bill.db')
# d = donn.cursor()
# conn = sqlite3.connect('everything.db')
# c = conn.cursor()

print("Hi. Welcome to Nero Nesh hotel")

def activities():
    global activity
    activity = input('''
    These are what you can do.
    a Eat food
    b Go to your hotel room
    c Go to the swimming pool
    d Cinema
    e Confrence 
    f Sports
    g Spa
    h Salon and Barber shop
    i Find your total bill
    ''')
activities()

if activity == "a":
    print("The resturant is at the ground floor")
    what_meal = input("Do you want Breakfast, Lunch, Dinner or Disert:  ")
    if what_meal == "Breakfast":
        global breakfast_meal
        breakfast_meal = 0
        c.execute('SELECT * FROM breakfast')
        print(c.fetchall())
        print("The breakfast was 50")
        breakfast_meal += 50
        d.execute('INSERT INTO breakfast_bill VALUES(?)',(breakfast_meal,))
        donn.commit()
    elif what_meal == "Lunch":
        global lunch_meal
        lunch_meal = 0
        donn.commit()
        print("The lunch was 50")
        c.execute('SELECT * FROM lunch')
        lunch_meal += 50
        print(c.fetchall())
        d.execute('INSERT INTO lunch_bill VALUES(?)',(lunch_meal,))
    elif what_meal == "Dinner":
        global diner_meal
        diner_meal = 0
        c.execute('SELECT * FROM dinner')
        print(c.fetchall())
        diner_meal += 50
        print("Dinner is 50")
        d.execute('INSERT INTO supper_bill VALUES(?)',(diner_meal,))

    elif what_meal == "Desert":
        c.execute('SELECT * FROM desert')
        print(c.fetchall())
        print("Desert is free")

elif activity == "c":
    print("The swimming pool is at the top floor")







elif activity == "b":
    global hotel_bill
    hotel_bill = 0
    print("You gan go to your hotel room")

    c.execute('SELECT * FROM hotel_rooms')
    print(c.fetchall())


    print("These are all the rooms available")
    which_room = input("Which room do you want:  ")
    print("The hotel rooms are 1000")
    hotel_bill += 1000
    c.execute('DELETE FROM hotel_rooms WHERE hotelnumber = ?',which_room)
    d.execute('INSERT INTO hotel_rooms VALUES(?)',(hotel_bill,))

    conn.commit()
    

















    
elif activity == "d":
    print("These are the movies available ")
    c.execute('SELECT * FROM movie')
    print(c.fetchall())
elif activity == "e":
    print("You can do confrences in the third floor")
elif activity == "f":
    c.execute('SELECT * FROM sports')
    print(c.fetchall())
    print("")
elif activity == "g":
    print("The spa is on the 4 floor ")
elif activity == "h":
    print("There are in the 3 floor")
elif activity == "i":
    def total_amount():
                    
        print("Your total price is ")
        global bill_total
        bill_total = 0

        for dub in d.execute('SELECT * FROM breakfast_bill'):
            bill_total += dub[0]
            print(bill_total)
            break
        for dub in d.execute('SELECT * FROM lunch_bill'):
            bill_total += dub[0]
            print(bill_total)

            break
        for dub in d.execute('SELECT * FROM supper_bill'):
            bill_total += dub[0]
            print(bill_total)

            break
        for dub in d.execute('SELECT * FROM room_bill'):
            bill_total += dub[0]
            print(bill_total)

            break
        
        amount_cash = int(input("Enter amount paying here:  "))

        if amount_cash < bill_total:
            print("Please pay more or the equal amount")
            total_amount()
        elif amount_cash > bill_total:
            balance = amount_cash - bill_total
            print("Your change is " + str(balance))
            print("Good bye.:D")
        elif amount_cash == dub:
            print("Thankyou. Good bye:)")
        else:
            print("I did not understand you.:/")
            total_amount()
            
    total_amount()