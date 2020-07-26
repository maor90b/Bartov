class Person:
    '''the class shows persons name,age,num of childs'''

    def __str__(self):
         return f'name={self.name}, age={self.age},childrens={self.childs}'


    def hasChildrens(self):
        if self.childs>0:
            return True
        elif self.childs<0:
            return False
        else:
            return None

    def ageGroup(self):
        if 0<=self.age<=18:
            return 'Child'
        if 19<=self.age<=60:
            return 'Adult'
        if 61<=self.age<=120:
            return 'Senior'

M=Person()

M.name= 'mike'
M.age= 25
M.childs= 3

print(M)

print(M.hasChildrens())

print(M.ageGroup())