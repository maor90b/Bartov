day=int(input("enter day: "))
month=int(input("enter month: "))
year=int(input("enter year: "))
if 31>=day>=1 and 12>=month>=1 and 2020>=year>=1950:
    print(day,"/",month,"/",int(year//10%10),int(year%10),sep="")  # another option ("%d/%d/%d%d"%(d,m,y//10%10,y%10))
else:
    if day<1 or day>31:
        print("invalid day")
    if month>12 or month<1:
        print("invalid month")
    if year>2020 or year<1950:
        print("invalid year")