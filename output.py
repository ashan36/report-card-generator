import data

class ReportOutput:
    outputPath = './report-card.txt'

    @classmethod
    def saveReport(cls):
        f = open(cls.outputPath, "w")
        f.write(data.DataStore.bulidReport())
        f.close()


    