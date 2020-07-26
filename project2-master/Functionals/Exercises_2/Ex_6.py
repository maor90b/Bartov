def Discount(age, city):
    if age <= 10:
        return 100
    if 18 >= age > 10 and city == 'jerusalem':
        return 35
    if 18 >= age > 10:
        return 25
    if 60 >= age > 18 and city == 'jerusalem':
        return 10
    if age > 60:
        return 50


def Pr(ds, price):
    e = (1 + (ds / 100)) * price
    return e


price = int(input("enter price: "))
age = int(input("enter age: "))
city = input("enter city: ")

ds = Discount(age, city)

print(Pr(ds, price))
