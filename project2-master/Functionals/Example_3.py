def f1(a,b,c=5,**kwargs):
    print(kwargs)
    print(a,b)
    return a+b+c



x=6
y=8
num=f1(x,y,11,name='david',age=30)
print(num)
