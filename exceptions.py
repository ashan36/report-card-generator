class ParsingException(Exception):
    def __init__(self, message, lineNum):
        self.message = message
        self.lineNum = lineNum

class IncompleteRowError(ParsingException):
    def __init__(self, message, lineNum):
        self.message = message
        self.lineNum = lineNum

class InvalidDataTypeError(ParsingException):
    def __init__(self, message, lineNum):
        self.message = message
        self.lineNum = lineNum

class InvalidMarkValueError(ParsingException):
    def __init__(self, message, lineNum):
        self.message = message
        self.lineNum = lineNum

class NonUniqueFieldIdError(ParsingException):
    def __init__(self, message, lineNum):
        self.message = message
        self.lineNum = lineNum
    
class CrossTableReferenceError(ParsingException):
    def __init__(self, message, lineNum):
        self.message = message
        self.lineNum = lineNum

class InvalidCourseWeightError(Exception):
    def __init__(self, message):
        self.message = message

