import csv
import io

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courses = []
        self.marks = {}

    def addMarks(self):
        pass

    def computeAverage(self):
        pass

    def addCourse(self):
        pass

    def computeGrade(self):
        pass

    def print(self):
        print("StudentID:", self.id, "StudentName:", self.name)

class Course:
    def __init__(self, id, name, teacher):
        self.id = id
        self.name = name
        self.teacher = teacher
        self.tests = {}

    def addTest(self):
        pass

    def print(self):
        print("CourseID:", self.id, "CourseName:", self.name, "CourseTeacher:", self.teacher)

class DataParser:
    defaultLoc = './resources'
    
    def __init__(self):
        self.studentsList = []
        self.coursesList = []

    def loadAll(self, pathString):
        with open(pathString + '/students.csv', newline='') as studentsFile:
            studentsReader = csv.reader(studentsFile)
            for row in studentsReader:
                if studentsReader.line_num == 1:
                    continue
                else:
                    self.studentsList.append(Student(row[0], row[1]))

        with open(pathString + '/courses.csv', newline='') as coursesFile:
            coursesReader = csv.reader(coursesFile)
            for row in coursesReader:
                if coursesReader.line_num == 1:
                    continue
                else:
                    self.coursesList.append(Course(row[0], row[1], row[2]))



    


