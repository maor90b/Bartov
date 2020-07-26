sum=0
num=int(input("enter number: "))
while num>0:
    sum+=num%10
    num=num//10
print(sum)