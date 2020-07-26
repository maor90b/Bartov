def grades(grade):
    if 70<=grade and grade<=100:
        return (True)
    return (False)



for i in range(5):
    grade = int(input("enter grade again: "))
    while grade>100 or grade<0:
        print("eror. invalid grade!")
        grade = int(input("enter grade again: "))
    print(grades(grade))

