import data

tester = data.DataParser()
tester.loadAll(data.DataParser.defaultLoc)

for student in tester.studentsList:
    student.print()

for course in tester.coursesList:
    course.print()

    