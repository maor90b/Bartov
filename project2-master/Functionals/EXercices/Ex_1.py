def sum_num(a):
    print((a%10)+(a//100)+(a//10%10))

num = int(input("enter number: "))
while num <100 or num>999:
    print('number must be with three characters!')
    num = int(input("enter number: "))


sum_num(num)