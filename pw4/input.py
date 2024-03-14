from domains import Course
from domains import Student
from domains import Grade

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