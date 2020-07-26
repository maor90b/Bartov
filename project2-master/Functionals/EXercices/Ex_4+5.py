def sum_num(n):
    list1=[]
    count=0
    for i in range (n):
        count+=1
        list1.append(count)
    Sum=sum(list1)
    return Sum

num=int(input("enter num: "))
# sum,list1 = sum_num(num)
# print(sum)
# print(list1)

print(sum_num(num))


for i in range(5):
    num = int(input("enter num: "))
    print(sum_num(num))


