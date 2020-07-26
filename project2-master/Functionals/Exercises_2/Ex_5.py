def N(a):
    b=float(a)
    c=int(a)
    if b-c>=0.5:
        c+=1
        return c
    if b-c<0.5:
        return c


num1=float(input("enter float num 1: "))
num2=float(input("enter float num 2: "))

print(N(num1)+N(num2))