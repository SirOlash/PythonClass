import unittest
import dividesquare

class DivisionSquare(unittest.TestCase):
	def test_that_function_exists(self):
		dividesquare.get_division_or_square(20)

	def test_that_number_is_divisible_by_5(self):
		actual = dividesquare.get_division_or_square(10)
		expected = 3.16
		self.assertEqual(actual,expected)
		actual = dividesquare.get_division_or_square(25)
		expected = 5
		self.assertEqual(actual,expected)
	
	def test_that_number_returns_remainder(self):
		actual = dividesquare.get_division_or_square(21)
		expected = 1
		self.assertEqual(actual,expected)
		actual = dividesquare.get_division_or_square(12)
		expected = 2
		self.assertEqual(actual,expected)
	
	def test_that_function_raise_exception_with_negative_value(self):
		self.assertRaises(TypeError,dividesquare.get_division_or_square(-1))

	def test_that_function_correct_value_with_float(self):
		actual = dividesquare.get_division_or_square(20.12)
		expected = 0.12
		self.assertEqual(actual,expected)

	def test_that_product_function_raise_exception_with_invald_input(self):
		self.assertRaises(TypeError, dividesquare.get_division_or_square,"tola")

	def test_that_function_raise_exception_with_zero(self):
		self.assertRaises(TypeError,dividesquare.get_division_or_square,"0")

	#Question 2
	def test_that_future_investment_function_exists(self):
		dividesquare.get_future_investment(10000,5,2)

	def test_that_future_investment_function_returns_correct_result(self):
		actual = dividesquare.get_future_investment(1000,1,12)
		expected = 1126.83
		self.assertEqual(actual,expected)
	
	"""def test_that_function_raise_exception_with_negative_value(self):
		self.assertRaises(TypeError,dividesquare.get_division_or_square(-1))"""

	
	
		