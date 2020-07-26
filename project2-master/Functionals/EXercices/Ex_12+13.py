from random import randint
def l(a):
    for i in range(20):
        n=randint(1,100)
        a.append(n)
    return a

def N(a,b):
    count =a.count(b)
    return count

def M(a):
    return max(a)



list1=[]
print(l(list1))

num=int(input("enter number: "))

print(N(list1,num))
print(M(list1))