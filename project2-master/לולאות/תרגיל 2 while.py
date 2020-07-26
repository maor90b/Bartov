age=int(input("enter age: "))
while age<0 or age>120:
    age=int(input("age invalid! \nenter new age: "))
if age>=0 and age<=18:
    print("child",age,"years old")
if age>=19 and age<=60:
    print("adult",age,"years old")
if 61 <= age <= 120:
    print("senior",age,"years old")