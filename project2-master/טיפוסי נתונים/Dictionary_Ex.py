d1={1:10,2:20,3:30,4:40,5:5}

keys=d1.keys()
keys=list(keys)
print(type(keys))

print(max(d1.values()))
val=d1.values()
val=list(val)
print(val)

print()


d={1:10,2:20,3:30}

print(d.items())
for i in d.items():
    print(i)