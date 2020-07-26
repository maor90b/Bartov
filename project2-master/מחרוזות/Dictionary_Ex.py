d1={1:10,2:200,3:'a',4:'b',150:60} #there is no index !!!

print(d1[2])

d1[2]=250    #change value of 2
#
# print(d1)
#
# d1[5]=500
# print(d1)

print(list(d1.keys()))
print(list(d1.values()))


for i in d1:
    print(i,d1)              #print key and his value besides him

