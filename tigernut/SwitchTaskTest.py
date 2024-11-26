import unittest
import switch

class SwitchTaskTest(unittest.TestCase):
	def test_that_function_exists(self):
		number_list = [1,2,3,4,5]
		number = 3
		switch.switchlist(number_list,number)
	
	def test_that_switch_function_returns_correct_result(self):
		number_list = [1,2,3,4,5]
		number = 1
		actual = switch.switchlist(number_list,number)
		expected = [2,3,4,5,1]
		self.assertEqual(actual,expected)

	def test_that_odd_even_function_returns_correct_result(self):
		number = [1,4,3,2,5,9,50]
		actual = switch.odd_even(number)
		expected = [False,True,False,True,False,False,True]
		self.assertEqual(actual,expected)
	
	def test_that_seperate_function_returns_correct_result(self):
		number = [1,2,3,4,5,6,7,8]
		actual = switch.seperate(number)
		expected = [[1,2,3,4],[5,6,7,8]]
		self.assertEqual(actual,expected)

