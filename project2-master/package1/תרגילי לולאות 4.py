num=int(input("enter number: "))
min=0
while num!=0:
    if num>0 and (num<min or min==0):   #min==0 או
        min=num
    num = int(input("enter number: "))
print(min)