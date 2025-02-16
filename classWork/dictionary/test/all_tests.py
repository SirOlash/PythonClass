import unittest

import grading_program


class MyTestCase(unittest.TestCase):
    def test_that_grading_function_returns_correct_value(self):
        student_scores = {"Gloria": 88, "Divine": 78, "Esther": 65, "Mercy": 75, "Uzo": 71}
        expected_score = 88
        actual = grading_program.student_score(student_scores)
        self.assertEqual(expected_score, actual)


if __name__ == '__main__':
    unittest.main()
