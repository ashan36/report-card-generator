import data
import output
import os
import argparse

tester = data.DataStore()
parser = data.DataParser()
parser.loadAll(data.DataParser.defaultLoc)
tester.computeAll()

print(tester.bulidReport())

output.ReportOutput.saveReport()