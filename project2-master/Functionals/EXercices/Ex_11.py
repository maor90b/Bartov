
def List(a):
    for i in range(2,40):
        if i%2==0:
            num=i
            a.append(num)
    print(a)


list1=[]
List(list1)