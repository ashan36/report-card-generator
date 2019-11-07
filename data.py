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

class Course:
    def __init__(self, id, name, teacher):
        self.id = id
        self.name = name
        self.teacher = teacher
        self.tests = {}

    def addTest(self):
        pass

class DataParser:
    defaultLoc = './resources'
    studentsFileName = '/students.csv'
    coursesFileName = '/courses.csv'
    marksFileName = '/marks.csv'
    testsFileName = '/tests.csv'

    studentsList = []

    def __init__(self):
        pass

    def loadAll(self):
        with open(defaultLoc + '/students.csv', newLine='') as studentsFile:
            studentsReader = csv.reader(studentsFile)
            for row in studentsReader:
                    print("row")

    


