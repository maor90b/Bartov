d1={1:10,2:20,3:30,4:40,'b':20,'a':30}

d2={}

for i in d1:
    if d1[i] not in d2.values():
        d2[i]=d1[i]

print(d2)