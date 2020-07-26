grade=int(input("enter grade: "))

while grade<0 or grade>100:
    grade = int(input("invalid grade! \nenter new grade: "))

if grade>=70:
    print("passed")
else:
    print("failed")
