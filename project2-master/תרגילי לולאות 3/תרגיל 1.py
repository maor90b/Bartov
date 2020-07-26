sum=0
count=0
sum2=0
percent=int(input("enter factor percent: "))
for i in range(5):
    grade = int(input("enter grade: "))
    new_grade=grade + (grade * percent / 100)
    sum+=new_grade
    count+=1
    sum2+=grade
    average1=sum/count
    average2=sum2/count
    print("the new grade is",new_grade)
print("the average of the new grades is",sum/count)
print("the average of the first grades is",sum2/count)
print("the remainder between the averages is",average1-average2)
