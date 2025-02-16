import unittest

from classWork import earlymorning
from classWork.earlymorning import morning_task

class MyTestCase(unittest.TestCase):
    def test_that_one_adds(self):
        number_list = [8,9,9,9]
        actual = earlyMorning.morning_task(number_list)
        expected = [9,0,0,0]
        self.assertEqual(actual, expected)





