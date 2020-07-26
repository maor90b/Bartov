def s(a):
    if a>0:
        return a+s(a-1)
    return 0

print(s(6))



def s(a):
    if a>1:
        return a*s(a-1)
    return 1