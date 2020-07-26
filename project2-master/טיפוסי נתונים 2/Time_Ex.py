from datetime import  datetime
#
# print(datetime.now())
#
#
# d=datetime.now()
#
# print(d.year)
#

from datetime import  datetime


d = datetime.now()
new_d=datetime(days=-2)

print(new_d)
print(d.strftime("%d/%m/%y"))

str1='20 mar 2009'

print(datetime.strftime(str1,'%d %b %y'))