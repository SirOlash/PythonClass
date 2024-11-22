import unittest
import listsum

class NumberSum(unittest.TestCase):
	"""def test_that_function_exists(self):
		num = [2,6,8]
		listsum.get_sum(num)

	def test_that_sum_of_numbers_return_correct_result(self):
		num = [1,2,3,4]
		actual = listsum.get_sum(num)
		expected = 10
		self.assertEqual(actual,expected)"""
	
	
	def test_that_remove_function_exists(self):
		numb = [2,6,8]
		listsum.remove_function(numb)

	def test_that_remove_function_return_correct_result(self):
		numb = [1,4,9,3,5,7]
		numb.pop()
		actual = listsum.remove_function(numb)
		expected = [1,4,9,3,5]
		self.assertEqual(actual,expected)




	