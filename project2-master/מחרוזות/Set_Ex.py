set1=set()      #if i dont want double things in the list

set1.add(1)
set1.add(2)
set1.add(3)

print(set1)

set1.add(3)
print(set1)


list1=[1,2,3,4,2]
# print(set(list1))
# print(list(set1))
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
print(set(list1))