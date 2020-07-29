from Ex_course.Student import Student
from Ex_course.Course import Course

qa1=Course(1,'QA')
for i in range(3):
    topic=input('enter topic: ')
    teacher=input('enter teacher: ')
    qa1.Topics[topic]= teacher

num=int(input('enter id: '))
n=input('enter name: ')
while num !=0 or len(qa1.Students) == qa1.max_students:
    student= Student(num, n)
    n=student
    topic=input('enter topic: ')
    grade = int(input('enter grade: '))
    student.add_grade(topic, grade)

    qa1.add_student(student.name)
    num = int(input('enter id: '))
    n = input('enter name: ')


print(qa1)




