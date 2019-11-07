import csv
import io

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = {}#k: courseId, v: grade = (mark * weight)/100

    def computeGrades(self):
        for test in DataStore.tests:
            if self.id in DataStore.tests[test].marks: #if student took this test
                if DataStore.tests[test].courseId in self.grades: #if already stored in grades dict, accumulate
                    self.grades[DataStore.tests[test].courseId] += float(DataStore.tests[test].marks[self.id]) * float(DataStore.tests[test].weight) /100
                else: #otherwise initialize to 0 and add
                    self.grades[DataStore.tests[test].courseId] = 0
                    self.grades[DataStore.tests[test].courseId] += float(DataStore.tests[test].marks[self.id]) * float(DataStore.tests[test].weight) /100
            
    def computeAverage(self):
        average = 0.0
        for grade in self.grades:
            average += self.grades[grade]

        average /= len(self.grades)
        self.average = average

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

class DataStore: #stores and manipulates data objects on a class level
    students = {} #dict of student objects where the student ID is the key
    courses = {} #dict of course objects where the course ID is the key
    tests = {} #dict of test objects combining marks and tests data, test id is the key

    @classmethod
    def clearData(cls):
        cls.students.clear()
        cls.courses.clear()
        cls.tests.clear()

    @classmethod
    def computeAll(cls):
        for student in cls.students:
            cls.students[student].computeGrades()
            cls.students[student].computeAverage()

    @classmethod
    def bulidReport(cls):
        outputString = ""
        for student in cls.students.values():
            outputString += "".join(("Student Id: {}, name: {}\n".format(student.id, student.name),
            "Total Average:\t{:4.2f}%\n".format(student.average)))

            for course in student.grades:
                outputString += "".join(("\n\t\tCourse: {}, Teacher: {}\n".format(cls.courses[course].name, cls.courses[course].teacher),
                "\t\tFinal Grade:\t{:4.2f}%\n".format(student.grades[course])))
        
            outputString += "\n\n"
        
        return outputString


class DataParser: #Used to load data from CSV files into the DataStore
    inputPath = './resources'

    @classmethod
    def loadAll(cls):
            
        try:
            with open(cls.inputPath + '/students.csv', newline='') as studentsFile:
                studentsReader = csv.reader(studentsFile)
                for row in studentsReader:
                    if studentsReader.line_num == 1: #throw away header
                        continue
                    else:
                        DataStore.students[row[0]] = Student(row[0], row[1])
        except:
            print("error opening {}/students.csv".format(cls.inputPath))
            quit()
            
        try:
            with open(cls.inputPath + '/courses.csv', newline='') as coursesFile:
                coursesReader = csv.reader(coursesFile)
                for row in coursesReader:
                    if coursesReader.line_num == 1: #throw away header
                        continue
                    else:
                        DataStore.courses[row[0]] = Course(row[0], row[1], row[2])
        except:
            print("error opening {}/courses.csv".format(cls.inputPath))
            quit()

        try:
            with open(cls.inputPath + '/tests.csv', newline='') as testsFile:
                testsReader = csv.reader(testsFile)
                for row in testsReader:
                    if testsReader.line_num == 1: #throw away header
                        continue
                    else:
                        DataStore.tests[row[0]] = Test(row[0], row[1], row[2])
        except:
            print("error opening {}/tests.csv".format(cls.inputPath))
            quit()

        try:
            with open(cls.inputPath + '/marks.csv', newline='') as marksFile:
                marksReader = csv.reader(marksFile)
                for row in marksReader:
                    if marksReader.line_num == 1: #throw away header
                        continue
                    else:
                        DataStore.tests[row[0]].addMark(row[1], row[2])
        except:
            print("error opening {}/marks.csv".format(cls.inputPath))
            quit()
