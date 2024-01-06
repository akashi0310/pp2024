def number_student(): 
    return int(input("Enter the number of students: "))

num_student = number_student()

def student_information():
    students = {}
    for _ in range(num_student):
        # Student information
        student_id = input("Enter the student ID: ")
        student_name = input("Enter student name: ")
        DoB = input("Enter DoB: ")
        students[student_id] = {'student_name': student_name, 'Date of birth': DoB}
    return students
    
# Course information
def number_of_course():
    return int(input("Enter number of courses: "))

num_course = number_of_course()

def course_information():
    courses = {}
    for _ in range(num_course):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = course_name
    return courses

# Student marks
def student_marks(students, courses):
    marks = {}
    for course_id in courses:
        marks[course_id] = {}
        print(f'Enter the marks for {courses[course_id]}')
        for student_id in students:
            mark = float(input(f"Enter mark for {students[student_id]['student_name']} (ID: {student_id}): "))
            marks[course_id][student_id] = mark
    return marks

students = student_information()
courses = course_information()
marks = student_marks(students, courses)

# Print all values
print("Student Information:")
for student_id, student_info in students.items():
    print("Student ID:", student_id)
    for key, value in student_info.items():
        print(key + ":", value)
    print()

print("Course Information:")
for course_id, course_name in courses.items():
    print("Course ID:", course_id)
    print("Course Name:", course_name)
    print()

print("Student Marks:")
for course_id, course_marks in marks.items():
    print("Course ID:", course_id)
    for student_id, mark in course_marks.items():
        print(f"Student ID: {student_id}, Mark: {mark}")
    print()