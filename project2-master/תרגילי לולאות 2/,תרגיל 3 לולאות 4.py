count = 1
num = int(input("enter a number: "))
max = num
count_max=1

for i in range (6):
    num = int(input("enter a number: "))
    count+=1
    if num>max:
        max=num
        count_max=count

print (count_max)