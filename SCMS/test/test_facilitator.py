import unittest

from models.facilitator import Facilitator
from models.student import Student
from services.course_manager import CourseManager


class MyTestCase(unittest.TestCase):
    def setUp(self):
        CourseManager.all_courses = []

        self.facilitator = Facilitator("Bruno","Fernandez",
                                        "Bruno@gmail.com","password")

        self.student1 = Student("Maino", "Kobie", "maino@gmail.com", "password")
        self.student2 = Student("Lisandro", "Martinez", "lisandro@gmail.com", "password")

    def test_that_you_can_create_courses(self):
        course = self.facilitator.create_course("Python 101")
        self.assertEqual(len(self.facilitator.created_courses), 1)
        self.assertEqual(course.course_name, "Python 101")
        course2 = self.facilitator.create_course("Python 102")
        self.assertEqual(len(self.facilitator.created_courses), 2)
        self.assertEqual(course2.course_name, "Python 102")

    def test_that_you_cannot_create_duplicate_course(self):
        self.facilitator.create_course("Python 101")
        with self.assertRaises(Exception) as context:
            self.facilitator.create_course("python 101")

        self.assertEqual(str(context.exception), "Course already exists")

    def test_that_a_facilitator_can_view_registered_students_for_each_created_course(self):
        self.course = self.facilitator.create_course("Python 101")
        self.student1.register_for_course("Python 101")
        self.student2.register_for_course("Python 101")

        expected = []
        expected.append("Course: Python 101")
        expected.append("  Student: Maino Kobie - Grade: unassigned")
        expected.append("  Student: Lisandro Martinez - Grade: unassigned")
        expected_output = "\n".join(expected)

        result = self.facilitator.view_registered_students()
        self.assertEqual(result, expected_output)

    def test_that_a_facilitator_can_assign_grades_to_students_registered_under_his_created_course(self):
        self.facilitator.create_course("Python 101")
        self.student1.register_for_course("Python 101")
        self.student2.register_for_course("Python 101")

        registration = self.facilitator.assign_grade("Python 101", "maino@gmail.com", 75)
        self.assertEqual(registration.get_grade(), "A")

        registration2 = self.facilitator.assign_grade("Python 101", "lisandro@gmail.com", 60)
        self.assertEqual(registration2.get_grade(), "B")

    def test_that_exception_is_thrown_if_invalid_course_is_provided(self):
        self.facilitator.create_course("Python 101")
        self.student1.register_for_course("Python 101")
        self.student2.register_for_course("Python 101")

        with self.assertRaises(Exception) as context:
            self.facilitator.assign_grade("python 102", "maino@gmail.com", 85)
        self.assertEqual(str(context.exception), "Course not found")

    def test_student_not_registered(self):
        self.facilitator.create_course("Python 101")
        self.student1.register_for_course("Python 101")
        self.student2.register_for_course("Python 101")

        with self.assertRaises(Exception) as context:
            self.facilitator.assign_grade("Python 101", "odegaard@gmail.com", 85)
        self.assertEqual(str(context.exception), "Student not registered in this course")

if __name__ == '__main__':
    unittest.main()
