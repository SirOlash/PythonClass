import os
import unittest

from coursemanagement.courseregistration import CourseRegistration


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self):
        self.test_filename = "test_registered_courses.txt"

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_that_initialize_file_creates_file_with_header_successfully(self):
        CourseRegistration(filename = self.test_filename)
        self.assertTrue(os.path.exists(self.test_filename))

        with open(self.test_filename, "r") as file:
            content = file.read()
        expected_header = "student_email,course_name,facilitator_email,facilitator_name,grade\n"
        self.assertEqual(content, expected_header)





if __name__ == '__main__':
    unittest.main()
