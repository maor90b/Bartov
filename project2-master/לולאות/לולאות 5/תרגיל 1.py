length = int(input("enter length: "))
width = int(input("enter width: "))
print(width*"*")
for i in range(length-2):
    print("*"+(width-2)*" "+"*")
print(width*"*")

num = int(input("enter number: "))
for i in range (num+1):
    print("*"*i)

for i in range(num+1):
    print(i*" "+"*"*(num-i))


