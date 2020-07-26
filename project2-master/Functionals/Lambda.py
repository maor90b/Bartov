# num=5
# func1=lambda num:num*2

def func1(num):
    return num*2

# print(func1(20))

list1=[1,2,3,4,5,6]


# list2=map(func1,list1)
list2=map(lambda num:num*2,list1)
print(list(list2))



