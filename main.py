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
    b Find a rooom
    c Go to the swimming pool
    d Cinema
    e Confrence 
    f Sports
    g Spa
    h Salon and Barber shop
    i Find your total bill
    ''')
activities()

if activity == "a" or activity == "Eat food" or activity == "eat food" or activity == "Eat Food" or activity == "eat food" or activity == "A":
    print("The resturant is at the ground floor")
    what_meal = input("Do you want Breakfast, Lunch, Dinner or Desert:  ")
    if what_meal == "Breakfast" or what_meal == "breakfast":
        global breakfast_meal
        breakfast_meal = 0
        c.execute('SELECT * FROM breakfast')
        print(c.fetchall())
        print("The breakfast was 50")
        breakfast_meal += 50
        d.execute('INSERT INTO breakfast_bill VALUES(?)',(breakfast_meal,))
        donn.commit()   
        activities()
    elif what_meal == "Lunch" or what_meal == "lunch":
        global lunch_meal
        lunch_meal = 0
        donn.commit()
        print("The lunch was 50")
        c.execute('SELECT * FROM lunch')
        lunch_meal += 50
        print(c.fetchall())
        d.execute('INSERT INTO lunch_bill VALUES(?)',(lunch_meal,))
        donn.commit()
        activities()
    elif what_meal == "Dinner" or what_meal == "dinner":
        global diner_meal
        diner_meal = 0
        c.execute('SELECT * FROM dinner')
        print(c.fetchall())
        diner_meal += 50
        print("Dinner is 50")
        d.execute('INSERT INTO supper_bill VALUES(?)',(diner_meal,))
        donn.commit()
        activities()
    elif what_meal == "Desert" or what_meal == "desert":
        c.execute('SELECT * FROM desert')
        print(c.fetchall())
        print("Desert is free")
        activities()
    else:
        print("I did not understand you. Please try again.")
        activities()

elif activity == "c" or activity == "swimming pool":
    print("The swimming pool is at the top floor")
    activities()







elif activity == "b" or activity == "hotel room" or activity == "Hotel room":
    global hotel_bill
    hotel_bill = 0
    print("You gan go to your hotel room")

    c.execute('SELECT * FROM hotel_rooms')
    print(c.fetchall())


    print("These are all the rooms available")
    which_room = input("Which room do you want:  ")
    print("The hotel rooms are 1000")
    hotel_bill += 1000
    c.execute('DELETE FROM hotel_rooms WHERE hotelnumber = ?',(which_room,))
    d.execute('INSERT INTO room_bill(price) VALUES(1000)')

    donn.commit()
    activities()    

















    
elif activity == "d" or activity == "cinema" or activity == "Cinema":
    print("These are the movies available ")
    c.execute('SELECT * FROM movilunch_billes')
    print(c.fetchall())
    activities()
elif activity == "e" or activity == "confrence" or activity == "Confrence":
    print("You can do confrences in the third floor")
    activities()
elif activity == "f" or activity == "Sports" or activity == "sport":
    c.execute('SELECT * FROM sports')
    print(c.fetchall())
    activities()
elif activity == "g" or activity == "spa" or activity == "Spa":
    print("The spa is on the 4 floor ")
    activities()
elif activity == "h" or activity == "Salon and Barber shop" or activity == "salon and barber shop" or activity == "Salon and barber shop":
    print("There are in the 3 floor")
    activities()
elif activity == "i" or activity == "total bill":
    def total_amount():
        # d.execute('SELECT * FROM 0fast_bill')
        # dub1 = d.fetchall()
        # print(dub1)

        print("Your total price is ")
        global bill_total
        bill_total = 0

        list1 = [a for dub in d.execute('SELECT * FROM breakfast_bill') for a in dub]
        list2 = [a for dub in d.execute('SELECT * FROM lunch_bill') for a in dub]
        list3 = [a for dub in d.execute('SELECT * FROM supper_bill') for a in dub]
        list4 = [a for dub in d.execute('SELECT * FROM room_bill') for a in dub]
        # c.execute('SELECT * FROM room_bill')
        # print(c.fetchall())
        comal = sum(list1)
        comal2 = sum(list2)
        comal3 = sum(list3)
        comal4 = sum(list4)

        bill_total += comal
        bill_total += comal2
        bill_total += comal3
        bill_total += comal4
        
        print(bill_total)
        
       
        
        amount_cash = int(input("Enter amount paying here:  "))

        if amount_cash < bill_total:
            print("Please pay more or the equal amount")
            total_amount()
        elif amount_cash > bill_total:
            balance = amount_cash - bill_total
            print("Your change is " + str(balance))
            print("Good bye.:D")
        elif amount_cash == bill_total:
            print("Thankyou. Good bye:)")
        elif amount_cash < 0:
            print("You can not pay less than zero")
            total_amount()
        else:
            print("I did not understand you.:/")
            total_amount()
            
    total_amount()
else:
    print("I did not understand you")
    activities()