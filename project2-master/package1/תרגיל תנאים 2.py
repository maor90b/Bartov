num=int(input("enter number: "))
if 100<=num<1000:
    print((num%10)+(num//10%10)+(num//100))
else:
    print("Eror")