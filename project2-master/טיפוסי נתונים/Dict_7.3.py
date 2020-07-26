dic1={1:10,2:20,3:30}
dic1=dic1.items()
dic2={}
for i in dic1:
    dic2[i[1]]=i[0]
print(dic2)