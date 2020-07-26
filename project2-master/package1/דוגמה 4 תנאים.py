grade =int(input("enter number: "))

if grade<0 or grade>100:
    print("the grade is between 0 and 100")

if grade>=0 and grade<=100:  # דרך נוספת
    if 90<=grade<=100:
        print("very good")
    if grade<90 and grade>=80:
        print("good")
    if grade<80 and grade>=70:
        print("ok")
    if grade<70
        print("failed")
else:
        print("invaild grade")





if grade>=0 and grade<=100:
    if grade>=90:
        print("very good")
    else:
        if grade>=80:
            print("good")
        else:
            if grade>=70:
                print("ok")
            else:
                print("failed")
else:
print("invaild grade")




if grade>=0 and grade<=100:
    if grade>=90:
        print("very good")
    elif grade>=80:
            print("good")
    elif grade>=70:
                print("ok")
    else:
                print("failed")
else:
print("invaild grade")