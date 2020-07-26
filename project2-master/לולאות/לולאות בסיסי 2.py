i=0
sum=0
while i<6:
    num=int(input("enter number: "))
    i+=1
    if num%2==0:
        sum=+num
print("the sum of even numbers is",sum)
print("and the average of the even numbers is",sum/6)