import csv
import io
import exceptions
import traceback

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = {}#k: courseId, v: grade = (mark * weight)/100

    def computeGrades(self): #requires a filled DataStore
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


class Course:
    def __init__(self, id, name, teacher):
        self.id = id
        self.name = name
        self.teacher = teacher

class Test:
    def __init__(self, testId, courseId, weight):
        self.testId = testId
        self.courseId = courseId
        self.weight = weight
        self.marks = {}#k: studentId, v: mark
    
    def addMark(self, student, mark):
        self.marks[student] = mark

class DataStore: #stores and manipulates data objects on a class level
    students = {} #dict of student objects where the student ID is the key
    courses = {} #dict of course objects where the course ID is the key
    tests = {} #dict of test objects combining marks and tests data, test id is the key

    @classmethod
    def validateTestWeights(cls):
        weightsDict = {} #k: course id, v: accumulated weight
        for key in cls.tests: #accumulate weights per courseId in dictionary.
            if cls.tests[key].courseId in weightsDict:
                tempInt = int(cls.tests[key].weight)
                weightsDict[cls.tests[key].courseId] += tempInt
            else:
                tempInt = int(cls.tests[key].weight)
                weightsDict[cls.tests[key].courseId] = tempInt
        
        for course in weightsDict: #test each course to see if the weights added up to 100
            if int(weightsDict[course]) != 100:
                raise exceptions.InvalidCourseWeightError("Error, test weights for courseId {} does not equal 100, check tests.csv file".format(course))

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
                    elif len(row) != 2:
                        raise exceptions.IncompleteRowError("Error in students file, data must consist of 2 columns (id, name)", studentsReader.line_num)
                    elif row[0].isdecimal() != True or row[1].isalpha() != True:
                        raise exceptions.InvalidDataTypeError("Error in students file, id must be a number and names must be composed of characters", studentsReader.line_num)
                    else:
                        if row[0] not in DataStore.students: #Add row to the dictionary if it doesn't already exist
                            DataStore.students[row[0]] = Student(row[0], row[1])
                        else:
                            raise exceptions.NonUniqueFieldIdError("Error in students file, id field must be unique", studentsReader.line_num)

            with open(cls.inputPath + '/courses.csv', newline='') as coursesFile:
                coursesReader = csv.reader(coursesFile)
                for row in coursesReader:
                    if coursesReader.line_num == 1: #throw away header
                        continue
                    elif len(row) != 3:
                        raise exceptions.IncompleteRowError("Error in courses file, data must consist of 3 columns (id, name, teacher)", coursesReader.line_num)
                    elif row[0].isdecimal() != True or row[1].isalpha() != True:
                        raise exceptions.InvalidDataTypeError("Error in courses file, id must be a number and names must be composed of characters", coursesReader.line_num)
                    else:
                        if row[0] not in DataStore.courses: #Add row to the dictionary if it doesn't already exist
                            DataStore.courses[row[0]] = Course(row[0], row[1], row[2])
                        else:
                            raise exceptions.NonUniqueFieldIdError("Error in courses file, id field must be unique", coursesReader.line_num)

            with open(cls.inputPath + '/tests.csv', newline='') as testsFile:
                testsReader = csv.reader(testsFile)
                for row in testsReader:
                    if testsReader.line_num == 1: #throw away header
                        continue
                    elif len(row) != 3:
                        raise exceptions.IncompleteRowError("Error in tests file, data must consist of 3 columns (id, course_id, weight)", testsReader.line_num)
                    elif row[0].isdecimal() != True or row[1].isdecimal() != True or row[2].isdecimal() != True:
                        raise exceptions.InvalidDataTypeError("Error in tests file, id, course_id, and weights must be numbers", testsReader.line_num)
                    elif row[1] not in DataStore.courses:
                        raise exceptions.CrossTableReferenceError("Error in tests file, course id does not match an existing course record", testsReader.line_num)
                    else:
                        if row[0] not in DataStore.tests: #Add row to the dictionary if it doesn't already exist
                            DataStore.tests[row[0]] = Test(row[0], row[1], row[2])
                        else:
                            raise exceptions.NonUniqueFieldIdError("Error in tests file, id field must be unique", testsReader.line_num)

            with open(cls.inputPath + '/marks.csv', newline='') as marksFile:
                marksReader = csv.reader(marksFile)
                for row in marksReader:
                    if marksReader.line_num == 1: #throw away header
                        continue
                    elif len(row) != 3:
                        raise exceptions.IncompleteRowError("Error in marks file, data must consist of 3 columns (test_id, student_id, mark)", marksReader.line_num)
                    elif row[0].isdecimal() != True or row[1].isdecimal() != True or row[2].isdecimal() != True:
                        raise exceptions.InvalidDataTypeError("Error in marks file, test_id, student_id, and mark must be numbers", marksReader.line_num)
                    elif int(row[2]) < 0 or int(row[2]) > 100:
                        raise exceptions.InvalidMarkValueError("Error in marks file, marks must be between 0 and 100", marksReader.line_num)
                    elif row[1] not in DataStore.students:
                        raise exceptions.CrossTableReferenceError("Error in marks file, student id does not match an existing student record", marksReader.line_num)
                    else:
                        if row[0] in DataStore.tests: #Add row to the dictionary if it doesn't already exist
                            DataStore.tests[row[0]].addMark(row[1], row[2])
                        else:
                            raise exceptions.CrossTableReferenceError("Error in marks file, test id does not match an existing test record", marksReader.line_num)

        except exceptions.ParsingException as e: #Catch all types of ParsingExceptions as the underlying behavior is the same.
            print(e.message)
            print("error occurred on line number {}".format(e.lineNum))
            quit()

        except: #Catch any other error that arises and print the exception
            print("Unknown error occured while parsing data")
            traceback.print_exc()
            quit()