def age(n):
    if  0<=n<=18:
        return "child"
    if 19<=n<=60:
        return "adult"
    if 61<=n<=120:
        return "senior"


a = int(input("enter age:"))

while a > 120 or a < 0:
    print("eror. enter again.")
    a = int(input("enter age:"))
print(age(a))
