import math
import numpy as np
def numberStudent():
    return 

class Student:
    def __init__(self,name,id,DoB):
        self._name = name
        self._id = id
        self._DOB = DoB
        self._gpa = 0

    def getName(self):
        return self._name
    def getId(self):
        return self._id
    def getDob(self):
        return self._DOB
    def getGpa(self):
        return self._gpa
    
    def setGpa(self,gpa):
        self._gpa = gpa
    
    def studentInfo(self):
        print(f"The name of student:{self._name} ")
        print(f"The student id: {self._id}")
        print(f"The date of birth:{self._DOB} ")
    
class Course:
    def __init__(self,cname,cid):
        self._cname = cname
        self._cid = cid

    def getCname(self):
        return self._cname
    def getCid(self):
        return self._cid
    
    def courseInfo(self):
        print(f"The name of the course: {self._cname}")
        print(f"The course id: {self._cid}")

class Grade:
    def __init__(self,studentId,course,mark):
        self._studentID = studentId
        self._course = course
        self._mark = mark

    def getId(self):
        return self._studentID
    def getCourse(self):
        return self._course
    def getMark(self):
        return self._mark
    
    def gradeInfo(self):
        print(f"mark for student with id {self._studentID} in course {self._course} is {self._mark}")

studentList = []
numbstu = int(input("Enter the number of student: "))
def studentInput():
    for i in range(numbstu):
        name = input("Enter the name of student: ")
        id = input("Enter the student's id: ")
        dob = input("Enter the date of birth: ")
        student = Student(name,id,dob)
        studentList.append(student)
    return studentList

courseList = []
creditList = []
def courseInput():
    numbcourse = int(input("Enter the number of courses: "))
    for i in range(numbcourse):
        coursename = input("Enter the course name: ")
        courseId = input("Enter the course id: ")
        credit = int(input("Enter the number of credit: "))
        course = Course(coursename,courseId)
        courseList.append(course)
        for i in range(numbstu):
            creditList.append(credit)
    return courseList

markList = []
def gradeInput():
    for i in studentList:
        for j in courseList:
            cre = np.array(creditList)
            
            mark = float(input(f"Enter the grade for {i.getName()} in course {j.getCname()}: "))
            result = math.floor(mark*10)/10
            markList.append(result)
            point = np.array(markList)
            
        gpa = (np.dot(cre,point))/np.sum(cre)
        i.setGpa(gpa)
    return markList

def Print():
    studentInput()
    courseInput()
    gradeInput()
    i=0
    for student in studentList:
        print(f"Name of the student {student.getName()}")
        for course in courseList:
            print(f"Name of course {course.getCname()}")
            print(f"the grade for {student.getName()} in course {course.getCname()} is {markList[i]}")
            i+=1
        print(f"gpa of student {student.getName()} is {student.getGpa()}")
          
Print()
       
