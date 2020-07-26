password=input("enter pssword: ")
password2=input("enter pssword 2: ")
count=0
while password2!=password:
    count+=1
    if count==5:
        print("failed")
        break
    password2 = input("failed. enter pssword 2: ")
else:
    print("good")