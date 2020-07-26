num=int(input("enter number: "))
num2=0
while num//10!=0:
    num2=num2+num%10
    num2=num2*10
    num=num//10
num2=num2+num
print(num2)

