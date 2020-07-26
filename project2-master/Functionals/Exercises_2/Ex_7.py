from random import randint
def rand(l,h,k):
    if l>h:
        l,h=h,l

    list1=[]
    for i in range(k):
        num=randint(l,h)
        while (num in list1):
            num=randint(l,h)
        list1.append(num)
    print(list1)
    print(sum(list1)/len(list1))



l=int(input("enter low range: "))
h=int(input("enter high range: "))
k=int(input("enter num of numbers: "))
rand(l,h,k)


