from dub import *
def update():
    name = input("Enter your old name:  ")
    age = int(input("Enter your old age:  "))
    input1 = input("Enter your new name:  ")
    input2 = int(input("Enter your age:  "))

    with conn:  
        c.execute('UPDATE name_age SET name = ? WHERE name = ?',(input1,name))
        c.execute('UPDATE name_age SET age = ? WHERE age = ?',(input2,age))
        read()
update()


print("We are now deleting")
input3 = input("Enter your name:  ")
def delete():
    
    c.execute('DELETE FROM name_age WHERE name = ?',(input3,))
    conn.commit()
    read()
delete()
