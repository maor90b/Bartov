def rand_k_num(l, u, k):
    'this function will get k random numbers between l and u'
    from random import randint

    if type(l)!=int:
        l=0
    if l>u:
        l,u=u,l
    list1 = []

    for i in range(k):
        num = randint(l, u)
        while (num in list1):
            num = randint(l, u)
        list1.append(num)

    return list1                          #אם אנחנו רוצים מסםר ערכים זה יהפוך לטאפל  list1, ...


# is the current module running?
if __name__=='__main__':

    l = int(input("enter lower num:"))
    u = int(input("enter higher num:"))
    k = int(input("enter num of numbers:"))

# print(rand_k_num.__doc__)
# help(rand_k_num)
    print(rand_k_num(l, u, k))

# list1=rand_k_num(l,u,k)
# list2=rand_k_num(20,8,10)
# print(list1)
# print(list2)
