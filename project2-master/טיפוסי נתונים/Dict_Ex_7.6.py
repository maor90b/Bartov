dic1={1:10,2:20,3:30}
key=int(input("enter number: "))
if key in dic1:
    del dic1[key]
print(dic1)