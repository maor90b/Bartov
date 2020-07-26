num1=int(input("enter number one: "))
num2=int(input("enter number two: "))
while num1%2==0 and num2%2==0:
    num3=num1+num2
    print(num3)
    num1 = int(input("enter number one: "))
    num2 = int(input("enter number two: "))
if num1%2!=0 or num2%2!=0:
    print(num1*num2)
