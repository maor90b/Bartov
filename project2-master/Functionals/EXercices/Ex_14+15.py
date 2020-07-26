def L(a):
    list1=[]
    for i in range(a):
        grade=int(input("enter grade: "))
        list1.append(grade)
    return list1

def A(b):
    return sum(b)/len(b)

num=int(input("enter number of students: "))

grades=L(num)
print(grades)
print(A(grades))