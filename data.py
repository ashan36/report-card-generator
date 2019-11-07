import csv
import io

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = {}#k: courseId, v: grade (mark * weight)/100

    def computeGrades(self):
        for test in DataParser.tests:
            if self.id in DataParser.tests[test].marks:
                self.grades[DataParser.tests[test].courseId] = 0
            
        for test in DataParser.tests:
            if self.id in DataParser.tests[test].marks:
                self.grades[DataParser.tests[test].courseId] += float(DataParser.tests[test].marks[self.id]) * float(DataParser.tests[test].weight) /100

    def computeAverage(self):
        average = 0.0
        for grade in self.grades:
            average += self.grades[grade]

        average /= len(self.grades)
        return average

    def print(self):
        print("StudentID:", self.id, "StudentName:", self.name, "\nGrades:", self.grades)


class Course:
    def __init__(self, id, name, teacher):
        self.id = id
        self.name = name
        self.teacher = teacher

    def print(self):
        print("CourseID:", self.id, "CourseName:", self.name, "CourseTeacher:", self.teacher)

class Test:
    def __init__(self, testId, courseId, weight):
        self.testId = testId
        self.courseId = courseId
        self.weight = weight
        self.marks = {}#k: studentId, v: mark
    
    def addMark(self, student, mark):
        self.marks[student] = mark

    def print(self):
        print("TestID:", self.testId, "CourseID:", self.courseId, "Weight:", self.weight, "\nMarks", self.marks)

class DataParser:
    defaultLoc = './resources'
    students = {} #dict of student objects where the student ID is the key
    courses = {} #dict of course objects where the course ID is the key
    tests = {} #dict of test objects combining marks and tests data, test id is the key

    def loadAll(self, pathString): #refactor this to multiple method calls
        with open(pathString + '/students.csv', newline='') as studentsFile:
            studentsReader = csv.reader(studentsFile)
            for row in studentsReader:
                if studentsReader.line_num == 1: #throw away header
                    continue
                else:
                    DataParser.students[row[0]] = Student(row[0], row[1])

        with open(pathString + '/courses.csv', newline='') as coursesFile:
            coursesReader = csv.reader(coursesFile)
            for row in coursesReader:
                if coursesReader.line_num == 1: #throw away header
                    continue
                else:
                    DataParser.courses[row[0]] = Course(row[0], row[1], row[2])

        with open(pathString + '/tests.csv', newline='') as testsFile:
            testsReader = csv.reader(testsFile)
            for row in testsReader:
                if testsReader.line_num == 1: #throw away header
                    continue
                else:
                    DataParser.tests[row[0]] = Test(row[0], row[1], row[2])

        with open(pathString + '/marks.csv', newline='') as marksFile:
            marksReader = csv.reader(marksFile)
            for row in marksReader:
                if marksReader.line_num == 1: #throw away header
                    continue
                else:
                    DataParser.tests[row[0]].addMark(row[1], row[2])

