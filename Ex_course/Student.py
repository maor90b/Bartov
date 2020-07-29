class Student:
    def __init__(self, id, name):
        self.id=id
        self.name= name
        self.grades={}

    def add_grade(self,topic,grade):
        self.grades[topic]=grade

    def __str__(self):
        return f'id: {self.id}, name: {self.name},grades: {self.grades}'

    def calc_factor(self,topic,percent):
        if self.grades[topic]*((percent+100)/100)<=100:
            self.grades[topic]*=((percent+100)/100)
        else:
            self.grades[topic]=100


    def average(self):
        Sum=sum(self.grades.values())
        return Sum/len(self.grades)




