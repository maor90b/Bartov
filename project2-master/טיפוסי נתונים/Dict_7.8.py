keys=[]
val=[]
dict1={}
list1=[]
for i in range(5):
    name=input("enter name: ")
    grade=int(input("enter grade: "))
    keys.append(name)
    val.append(grade)
    dict1[name]=grade
print(dict1)
averege=(sum(dict1.values())/(len(dict1)))
print(averege)

for i in dict1:
    if dict1[i]>averege:
        list1.append(dict1[i])
print(list1)