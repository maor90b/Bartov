def n(x,y):
    if y>x:
        x,y=y,x


    count=0
    while x>=0:
        x-=y
        count+=1
    count-=1
    x*=-1
    if x*0.1>=0.5:
        x=1
    else:
        x=0
    return count,x


print(n(11,2))


    x*=(0.1*y)
