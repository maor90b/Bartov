dic1={1:10,2:20,3:30,5:30,6:10}
dic2={}
for i in dic1.items():
    dic2[i[1]]=i[0]
print(dic2)
dic1.clear()
for i in dic2.items():
    dic1[i[1]]=i[0]
print(dic1)



