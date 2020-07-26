grade= int(input("enter grade: "))
count=0
sum=0
max=0
while 0<=grade<=100:
    count+=1
    sum+=grade
    if max<grade and 0<=grade<=100:
        max=grade
    grade = int(input("enter grade: "))
print("the max grade is,",max)
print("the average is",sum/count)
print("max grade - average=",max-sum/count)


