def f1(tup1, list1, d1, s1):
    list1.append(5)
    print('in f1 before change: ',id(tup1))
    tup1+=5,
    print('in ft2',tup1)
    print('in f1 after chenge',id(tup1))
    d1[5]=50
    s1.add(5)


l=[1,2,3,4]
t=(1,2,3,4)
# print('in main',id(t))
d={1:10,2:20,3:30,4:40}
s={1,2,3,4}
# t2=f1(t,l,d)
f1(t,l,d,s)
print(l,t,d,s)