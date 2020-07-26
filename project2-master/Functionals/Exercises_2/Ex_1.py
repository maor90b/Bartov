def Del(b):
    if 'a' or 'A' in b:
        b=b.replace('a','')
        b=b.replace('A','')
    return b

str1=input("enter str: ")
print(Del(str1))