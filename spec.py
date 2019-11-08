import unittest
import data
import output

class DataTest(unittest.TestCase):

    def setUp(self):
        self.student1 = data.Student("1", "A")
        self.test1 = data.Test("1", "1", "10")
        self.test1.marks['1'] = "78"
        self.test2 = data.Test("2", "1", "40")
        self.test2.marks['1'] = "87"
        self.test3 = data.Test("3", "1", "50")
        self.test3.marks['1'] = "95"       
        data.DataStore.tests['1'] = self.test1
        data.DataStore.tests['2'] = self.test2
        data.DataStore.tests['3'] = self.test3

        self.student2 = data.Student("2", "B")
        self.test1.marks["2"] = "78"
        self.test2.marks["2"] = "87"
        self.test3.marks["2"] = "15"

    def test_computeGrades(self):
        self.student1.computeGrades()
        self.assertEqual(round(self.student1.grades['1'], 2), 90.1)
        self.student2.computeGrades()
        self.assertEqual(round(self.student2.grades['1'], 2), 50.1)

    def test_computeAverage(self):
        self.student1.grades = {"1": 90.1, "2": 51.8, "3": 74.2}
        self.student1.computeAverage()
        self.assertEqual(round(self.student1.average, 2), 72.03)

if __name__ == '__main__':
    unittest.main()