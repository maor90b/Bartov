from random import randint
num= randint(1,9)
num2= int(input("enter number: "))
while num2 !=num:
    if num2 > num:
        print("the number is smaller ")
        num2 = int(input("enter number: "))
    else:
        print("the number is bigger")
        num2 = int(input("enter number: "))
print("num = num2 \ngreat")

