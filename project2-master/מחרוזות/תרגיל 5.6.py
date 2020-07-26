list1 = [i for i in range(1, 11)]
print(list1)
# list2 = list1[len(list1):len(list1)-4:-1]
# print(list2)
# print(list1[::-1])
# print(list1[0::2])
# list3=list1[0::2]
# print(list3)
#
# num1=int(input("enter num 1: "))
# num2=int(input("enter num 2: "))
# num3=int(input("enter num 3: "))
# list1[4:6]=[num1,num2,num3]
# list1.append(num3)
# print(list1)
# for i in range(len(list1)):
#     list1[i]*=2
# print(list1)
new_list=[]
new_list.append(list1[0]);new_list.append(list1[-1])
print(new_list)

