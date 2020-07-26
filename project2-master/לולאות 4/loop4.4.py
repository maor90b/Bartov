num = int(input('enter number: '))    #קולט מספר שאורכו לא ידוע. הופך את המספר ומדפיס את המספר ההפוך וגם כפול 2
new_num = 0

while num//10 != 0:
    new_num += num%10
    new_num *= 10
    num //= 10

new_num += num
print(new_num)
print(new_num*2)