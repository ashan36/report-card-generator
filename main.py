from data import DataParser
from data import DataStore
from output import ReportOutput
import os
import argparse
import exceptions
import traceback
  
def valid_path(path): 
    # validate file path 
    return os.path.exists(path)

def main():
    argparser = argparse.ArgumentParser(description = "Student Text Report Card Generator")

    argparser.add_argument("--input", type=str, nargs=1, metavar="inputPath", default=None, help="Define path for CSV files. Default is ./resources")
    argparser.add_argument("--output", type=str, nargs=1, metavar="outputPath", default=None, help="Define path for output txt file. Default is the current directory")
    
    args = argparser.parse_args()
    run(args)

def run(args):

    if args.input != None:
        if valid_path(args.input[0]):
            DataParser.inputPath = args.input[0]
        else:
            print("Input path not found")
            quit()
    if args.output != None:       
        if valid_path(args.output[0]):
            ReportOutput.outputPath = args.output[0]
        else:
            print("Output path not found")
            quit()

    DataParser.loadAll()

    try: 
        DataStore.validateTestWeights()
        DataStore.computeAll()
    except exceptions.InvalidCourseWeightError as e:
        print(e.message)
        quit()
    except: #Catch any other error that arises and print the exception
        print("Unknown error occured while parsing data")
        traceback.print_exc()
        quit()

    ReportOutput.saveReport()

if __name__ == "__main__":
    main()