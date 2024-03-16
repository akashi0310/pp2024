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
