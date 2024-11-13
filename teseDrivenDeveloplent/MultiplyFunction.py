from unittest import TestCase
import multiply

class MultiplyFunction(TestCase):
	def test_that_multiply_function_exists(self):
		multiply.multiple(3,4)

	def test_that_multiply_function_returns_correct_value(self):
		actual = multiply.multiple(3,4)
		expected = 12
		actual = multiply.multiple(2,3)
		expected = 6
	
	def test_that_multiply_function_raise_exception_with_invald_input(self):
		self.assertRaises(TypeError, multiply.multiple, "moses")

	def test_that_multiply_function_returns_correct_value_with_float(self):
		actual = multiply.multiple(2.3,2.5)
		expected = 5.75

	def test_that_multiply_function_returns_correct_value_with_float(self):
		actual = multiply.multiple(2.3,2.5)
		expected = 5.75
	
	
	
 	
