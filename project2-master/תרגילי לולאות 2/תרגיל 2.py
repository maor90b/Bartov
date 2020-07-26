password=input("enter pssword: ")
password2=input("enter pssword 2: ")
for i in range(4):
    if password == password2:
        print('good')
        break
    else:
        password2 = input('not good, enter again: ')
else:
    print('falied')
