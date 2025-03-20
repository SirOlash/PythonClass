import json



class CourseManager:
    all_courses = []


    @classmethod
    def get_all_courses(cls):
        return cls.all_courses

    @classmethod
    def add_course(cls,course):
        cls.all_courses.append(course)

