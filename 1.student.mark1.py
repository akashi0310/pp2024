student = int(input('Enter the number of students: '))
students = {}
def student_info():
    for i in range(student):
        id = input('Enter id of student: ')
        name = input('Enter the name of student: ')
        DoB = input('Enter the date of birth: ')
        students[id] = {'name':name,'DoB':DoB} 
student_info()

course = int(input('Enter the number of courses: '))
courses = {}
#course info
def course_info():
    for i in range(course):
        course_id = input('Enter the id for course: ')
        course_name = input('Enter the name of the course: ')
        courses[course_id] = {'name':course_name,'bangdiem':{}}
course_info()

def mark_info():
    for course_id in courses.keys():
        for student_id in students.keys():
            courses[course_id]['bangdiem'][student_id] = int(input(f"Enter the mark for {courses[course_id]['name']} of student {students[student_id]['name']}: "))

mark_info()

def printmark():
    for course_id in courses.keys():
        for student_id in students.keys():
            print('mark of student',students[student_id]['name'],'in the course',courses[course_id]['name'],'is ',courses[course_id]['bangdiem'][student_id])

printmark()


           
    