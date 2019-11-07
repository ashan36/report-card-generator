import data
import os
import argparse

tester = data.DataParser()
tester.loadAll(data.DataParser.defaultLoc)

for id in tester.tests:
    tester.tests[id].print()

for id in tester.students:
    tester.students[id].computeGrades()
    tester.students[id].print()
    print(str(tester.students[id].computeAverage()))

for id in tester.courses:
    tester.courses[id].print()
    