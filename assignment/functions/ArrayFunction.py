import unittest
import functionlists

class ArrayFunction(unittest.TestCase):
	def test_that_function_exists(self):
		number = [4,5,7]
		functionlists.largest_number(number)

	def test_that_largest_returns_correct_result(self):
		number = [2,3,5,6,8]
		actual = functionlists.largest_number(number)
		expected = 8
		self.assertEqual(actual,expected)

	
	def test_that_reversed_function_returns_correct_result(self):
		number = [2,3,5,6,8]
		actual = functionlists.reversed_number(number)
		expected = [8,6,5,3,2]
		self.assertEqual(actual,expected)

	def test_that_occurance_function_returns_correct_result(self):
		element = 6
		number = [2,3,5,6,8]
		actual = functionlists.element_occurance(element,number)
		expected = True
		self.assertEqual(actual,expected)

	def test_that_odd_function_returns_correct_result(self):
		number = [2,3,5,6,8]
		actual = functionlists.odd_elements(number)
		expected = [3,6]
		self.assertEqual(actual,expected)

	def test_that_even_function_returns_correct_result(self):
		number = [2,3,5,6,8]
		actual = functionlists.even_elements(number)
		expected = [5,8]
		self.assertEqual(actual,expected)

	def test_that_running_function_returns_correct_result(self):
		numbers = [1,2,3,4]
		actual = functionlists.running_total(numbers)
		expected = [1,3,6,10]
		self.assertEqual(actual,expected)

	def test_that_palindrome_function_returns_correct_result(self):
		word = "madam"
		actual = functionlists.string_palindrome(word)
		expected = True
		self.assertEqual(actual,expected)

	def test_that_sum_for_function_returns_correct_result(self):
		number = [1,2,3,4]
		actual = functionlists.number_sum_for(number)
		expected = 10
		self.assertEqual(actual,expected)

	def test_that_sum_while_function_returns_correct_result(self):
		number = [1,2,3,4]
		actual = functionlists.number_sum_while(number)
		expected = 10
		self.assertEqual(actual,expected)
	def test_that_concatenate_function_returns_correct_result(self):
		word = ["a","b","c"]
		number = [1,2,3]
		actual = functionlists.concatenates_list(word,number)
		expected = ["a","b","c",1,2,3]
		self.assertEqual(actual,expected)

	def test_that_alternate_function_returns_correct_result(self):
		list_one = ["a","b","c"]
		list_two = [1,2,3]
		actual = functionlists.alternate_merge(list_one,list_two)
		expected = ["a",1,"b",2,"c",3]
		self.assertEqual(actual,expected)

	def test_that_digits_function_returns_correct_result(self):
		number = 2342
		actual = functionlists.digits_of_number(number)
		expected = [2,3,4,2]
		self.assertEqual(actual,expected)


	







