import unittest
import kata_functions

class Kata(unittest.TestCase):
	def test_that_function_exists(self):
		number = 8
		kata_functions.is_even(number)

	def test_is_even_returns_correct_result(self):
		number = 6
		actual = functionlists.is_even(number)
		expected = True
		self.assertEqual(actual,expected)

	"""def test_that_is_even_returns_correct_result(self):
		number = [2,3,5,6,8]
		actual = functionlists.largest_number(number)
		expected = 8
		self.assertEqual(actual,expected)"""
