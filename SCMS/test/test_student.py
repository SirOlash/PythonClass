import unittest
from multiprocessing.resource_tracker import register

from models.facilitator import Facilitator
from models.student import Student
from services.course_manager import CourseManager


class MyTestCase(unittest.TestCase):
    def setUp(self):
        CourseManager.all_courses = []

        self.facilitator = Facilitator("Bruno", "Fernandez", "bruno@gmail.com", "password")
        self.student = Student("Martin", "Odegaard", "average@gmail.com", "password")

    def test_that_right_message_is_returned_if_courses_list_is_empty(self):
        result = self.student.view_available_courses()
        self.assertEqual(result, "No courses available yet!! Chill")

    def test_that_you_can_view_the_created_courses(self):
        self.facilitator.create_course("python 101")
        self.facilitator.create_course("python 102")

        expected_lines = ["python 101 (Facilitator: Bruno Fernandez)", "python 102 (Facilitator: Bruno Fernandez)"]
        expected_result = "\n".join(expected_lines)

        result = self.student.view_available_courses()
        self.assertEqual(result, expected_result)

    def test_that_you_can_register_a_course(self):
        self.facilitator.create_course("python 101")
        registration_object = self.student.register_for_course("python 101")
        self.assertEqual(registration_object.course.course_name, "python 101")
        self.assertEqual(len(self.student.registered_courses), 1)

    def test_that_you_can_view_your_registered_courses(self):
        self.facilitator.create_course("python 102")
        self.student.register_for_course("python 102")

        expected_output = (f"python 102 (Facilitator: {self.facilitator.first_name} {self.facilitator.last_name}) "
                           f"- Grade: unassigned")
        result = self.student.view_registered_courses()
        self.assertEqual(result, expected_output)

    def test_that_student_can_view_the_updated_grades(self):
        self.facilitator.create_course("Python 101")
        self.student.register_for_course("Python 101")
        self.facilitator.assign_grade("Python 101", "average@gmail.com", 75)
        self.assertIn("Grade: A", self.student.view_registered_courses())

if __name__ == '__main__':
    unittest.main()
