def Str(a):
    a=a[-1::-1]
    return a


str1=input("enter str: ")
print(3*(Str(str1)+' '))
print(3*Str(str1))