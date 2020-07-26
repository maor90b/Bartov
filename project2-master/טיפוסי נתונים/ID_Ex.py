#
list1=[1,2,3,4]
# list2=list1
list2=list1.copy()
print(id(list2))
list2.append(5)
print(list1)                 #מצביע על אותו שטח בזיכרון


print(list1==list2)


# tup1=(1,2,3)
# print(id(tup1))
# tup1+=4
# print(id(tup1))               #בלתי ניתן לשינוי, אבל כשמוסיפים לו ערך הוא מקצה זיכרון אחר
#




