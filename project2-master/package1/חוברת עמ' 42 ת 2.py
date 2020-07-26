num1=int(input("enter number one: "))
num2=int(input("enter number two: "))
num3=int(input("enter number three: "))
print(max(num1,num2,num3))

num1=int(input("enter number one: "))
num2=int(input("enter number two: "))
num3=int(input("enter number three: "))
if num1>num2 and num1>num3:
    print("the biggest number is number one =",num1)
elif num2>num1 and num2>num3:
    print("the biggest numer is number two =",num2)
elif num3>num1 and num3>num2:
    print("the biggest number is number three =",num3)


