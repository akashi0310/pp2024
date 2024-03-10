import math
import numpy as np

student_number = int(input("Enter the number of students in class : "))
class Student:
    def __init__(self,id,name,DoB):
        self.id = id
        self.name = name
        self.DoB = DoB

course_number = int(input("Enter the number of course: "))
class Course:
    def __init__(self,cID,cname):
        self.cID = cID
        self.cname = cname
        self.mark = {}

studentList = []        
for i in range(student_number):
    id = input("Enter the id for student: ")
    name = input("Enter the name for student: ")
    DoB = input("Date of birth: ")

    student = Student(id,name,DoB)
    studentList.append(student)

courseList = []
for i in range(course_number):
    cID = input("Enter the id for course: ")
    cname = input("Enter the name for course: ")

    courseList.append(Course(cID,cname))

markList = []
creditList = []
for i in courseList:
    credits = int(input(f"Enter the number of credits for course {i.cname}: "))

    for j in studentList:
        creditList.append(credits)
        cre = np.array(creditList)
    
        mark = float(input(f"mark for student {j.name} in course {i.cname} is: "))
        result = math.floor(mark*10)/10
        i.mark[j.id] = result
        markList.append(i.mark[j.id])
        point = np.array(markList)

        j.gpa = (np.dot(cre,point))/np.sum(cre)


def Print():
    for i in studentList:
        print(i.name)
        for j in courseList:
            print(j.cname)
            print(f"mark for student {i.name} in course {j.cname} is {j.mark[i.id]} ")
        print(f"gpa of student {i.name} is {i.gpa} ")        

print("------------------------------")
Print()
