import unittest
import find_number

class NumberSumTest(unittest.TestCase):
	def test_that_function_exists(self):
		number_list = [12,17,24,32,14]
		number = 24
		find_number.find_number(number_list,number)

	def test_that_find_number_return_correct_result(self):
		number_list = [12,17,24,32,14]
		number = 12
		actual = find_number.find_number(number_list,number)
		expected = 0
		self.assertEqual(actual,expected)