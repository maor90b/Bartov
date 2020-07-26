d1={'abcdef':10,2:20,3:30,400:40,'a':30}

d2={}

for i in d1:
    d2[d1[i]]=i

print(d2)