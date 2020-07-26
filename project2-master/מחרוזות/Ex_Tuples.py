# tup = (1,2,3,4,5)
# tup+=6,7,8
# print(tup)
#
# tup=(10,20,30)+tup
# print(tup)
#
#
# tup+='abc',
# print(tup)
#
# num1=int(input("enter number 1 : "))
# num2=int(input("enter number 2 : "))
# if num1>num2:
#     num1,num2 = num2,num1
# print(num1,num2)
#

a,b,c=10,20,'abc'
print(a,b,c)

tup=(1,2,3)

list1=list(tup)
print(list1)

tup=tuple(list1)
print(tup)


for i in tup:
    print(i)


tup=()
for i in range(5):
    num = int(input("enter number: "))
    tup+=num,
print(tup)

