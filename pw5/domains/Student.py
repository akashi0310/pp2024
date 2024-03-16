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

