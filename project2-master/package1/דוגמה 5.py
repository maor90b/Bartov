grade =int(input("enter number: "))
name= input("enter name: ")

if grade>=70 and (name=="Michael" or name=="George"): # להוסיף סוגריים כדי לעשות שני תנאים
    print("passsed")
else:
    print("failed")