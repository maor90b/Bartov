num=int(input("enter number: "))
while num<100 or num>999:
    num=int(input("number must be between 100-999. \nenter new number: "))
if 100<=num<=999:
    num2=num%10+num//10%10+num//100
    print(num%10,"+",num//10%10,"+",num//100,"=",num2,sep="")