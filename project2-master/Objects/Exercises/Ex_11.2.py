class StudenInClass:
    def __init__(self):
        self.id = int(input("enter id: "))
        self.name =input("enter name: ")
        self.adress = input("enter adress: ")
        self.grade = int(input("enter grade: "))
        
    def P_or_F(self):
        if self.grade<70:
            return False
        return True

    def details(self):
        return f'id={self.id}, name={self.name}, adress={self.adress}, grade={self.grade}'
    
st_1 = StudenInClass()



st_1.details()
print(st_1.P_or_F())

