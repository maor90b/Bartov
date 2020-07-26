class Student:
    def __init__(self):
        self.name=input("enter name: ")
        self.adress=input("enter adress: ")
        self.age=int(input("enter age: "))
        self.grade=int(input("enter grade: "))


    def derails(self):
        print(f'name={self.name}, adress={self.adress}, age={self.age} ,grade={self.grade}')



st = Student()
st.derails()

