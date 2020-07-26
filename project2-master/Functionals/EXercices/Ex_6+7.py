def func(a, b):
    for i in range(a, b+1):
        print(i,end=" ")


def high(a,b):
    if a>b:
        return a
    return b

def low(a,b):
    if a>b:
        return b
    return a



num1 = int(input("enter num 1 : "))
num2 = int(input("enter num 2 : "))

print('the hig num is',high(num1,num2))
print('the low num is',low(num1,num2))

func(low(num1,num2),high(num1,num2))