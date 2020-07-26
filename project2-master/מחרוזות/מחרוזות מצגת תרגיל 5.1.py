num=input("enter numbers for list(do space between them): ").split()

for i in range(len(num)):
    num[i]=int(num[i])
print(max(num),min(num),sum(num)/len(num))