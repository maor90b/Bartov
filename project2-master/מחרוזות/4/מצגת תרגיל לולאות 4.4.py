num=int(input("enter number: "))
count=0
from random import randint
num2=randint(1,100)
while num2!=num:
    count+=1
    num2 = randint(1, 100)
print("the system did",count,"chances to find your number")



