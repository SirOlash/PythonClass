from models.courses import Course
from models.student import Student


class CourseRegistration:
    def __init__(self, course:Course,student:Student):
        self.course = course
        self.student = student
        self.__grade = "unassigned"

    def set_grade(self, grade:float):
        if 0 <= grade < 40:
            self.__grade = "F"
        elif 40 <= grade < 45:
            self.__grade = "E"
        elif 45 <= grade < 50:
            self.__grade = "D"
        elif 50 <= grade < 60:
            self.__grade = "C"
        elif 60 <= grade < 70:
            self.__grade = "B"
        elif 70 <= grade <= 100:
            self.__grade = "A"
        else:
            raise ValueError("Grade must be between 0 and 100")


    def get_grade(self):
        return self.__grade


