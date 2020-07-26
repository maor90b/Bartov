class Course:
    def __init__(self):
        self.number=int(input("enter num course:"))
        self.name= input("enter course name: ")
        self.num_st=int(input("enter num of students: "))
        self.num_limit=int(input("enter limit:"))

    def details(self):
        return f'course num:  {self.number}, name:{self.name},st num:{self.num_st},limit st:{self.num_limit}'


    def place(self):
        return f'we have {self.num_limit-self.num_st} empty places.'


course_QA= Course()

print(course_QA.details())
print(course_QA.place())