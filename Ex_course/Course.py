from Ex_course.Student import Student



class Course:
    def __init__(self,num_c,Name_c):
        self.num_c=num_c
        self.Name_c=Name_c
        self.Topics={}
        self.Students=[]
        self.max_students=5

    def __str__(self):
        return f'num course: {self.num_c}, name course: {self.Name_c}, Topics: {self.Topics}, students: {self.Students}, max: {self.max_students}'

    def add_student(self,student):
        if len(self.Students)<=self.max_students:
            self.Students.append(student)
            return True
        else:
            return False




    def add_factor(self,Topic,percent):
        for i in range(len(self.Students)):
            self.Students[i].calc_factor(Topic,percent)

    def del_student(self,id):
        for i in range(len(self.Students)):
            if self.Students[i].id==id:
                self.Students.remove(i)
                break

    def calc_avg(self):
        for i in range(len(self.Students)):
            Sum=0
            Sum+=self.Students[i].average()
            Sum/len(self.Students)














