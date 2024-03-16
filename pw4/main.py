from domains import *
from Input import *

studentInput()
courseInput()
gradeInput()
i=0
for student in studentList:
    print()
    print(f"Name of the student {student.getName()}")
    for course in courseList:
        print(f"Name of course {course.getCname()}")
        print(f"the grade for {student.getName()} in course {course.getCname()} is {markList[i]}")
        i+=1
    print(f"gpa of student {student.getName()} is {student.getGpa()}")


          