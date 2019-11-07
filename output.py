import data

class ReportOutput:
    outputPath = '.'

    @classmethod
    def saveReport(cls):
        try:
            f = open(cls.outputPath + "/report-card.txt", "w")
            f.write(data.DataStore.bulidReport())
            f.close()
            print("Output successful")
        except:
            print("error writing output file")
            quit()