num1=int(input("enter number one: "))
num2=int(input("enter number two: "))
if num1>num2:
    for i in range (num2+1,num1):
        if i%2==0:
            print(i)
elif num1<num2:
    for i in range(num1+1, num2):
        if i%2==0:
            print(i)
else:
    print("the numbers equals")



