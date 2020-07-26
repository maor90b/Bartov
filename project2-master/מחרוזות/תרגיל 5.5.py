want = "yes"
passed = []
failed = []
while want == "yes":
    grade = int(input("enter grade: "))
    if grade > 100 or grade < 0:
        continue
    elif grade >= 60:
        passed.append(grade)
    else:
        failed.append(grade)
    want = input("want_more_grades(answer yes or no.)?")
    if want == "no":
        break
print("numbers of failed is", len(failed))
print("numbers of passed is", len(passed))

