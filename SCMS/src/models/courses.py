from models.facilitator import Facilitator


class Course:
    def __init__(self, course_name:str, facilitator_object:Facilitator):
        self.__course_name = course_name
        self.facilitator = facilitator_object
        self.registrations = []

    @property
    def course_name(self):
        return self.__course_name



