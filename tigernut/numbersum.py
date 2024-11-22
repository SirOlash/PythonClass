import unittest
import sum

class NumberSum(unittest.TestCase):
	def test_that_function_exists(self):
		number = [2,6,8]
		sum.get_sum(number)

	def test_that_get_sum_function_return_correct_result(self):
		number = [1,2,3,4]
		actual = sum.get_sum(number)
		expected = 6
		self.assertEqual(actual,expected)
	
	def test_that_get_sum_function_return_correct_result_with_negative_numbers (self):
		number = [-1,-2,-3,-4]
		actual = sum.get_sum(number)
		expected = 6
		self.assertEqual(actual,expected)


	def test_that_vowel_return_correct_result(self):
		character = "python is sweet"
		actual = sum.get_vowel(character)
		expected = 4
		self.assertEqual(actual,expected)
	
	def test_that_anagram_return_correct_result(self):
		string_one = "listen"
		string_two = "silent"
		actual = sum.get_anagram(string_one,string_two)
		expected = True
		self.assertEqual(actual,expected)

	def test_that_prime_return_correct_result(self):
		actual = sum.get_prime(10)
		expected = False
		self.assertEqual(actual,expected)

	def test_that_palindrom_return_correct_result(self):
		actual = sum.get_palindrome("madam")
		expected = True
		self.assertEqual(actual,expected)

	def test_that_average_return_correct_result(self):
		number = [10,20,30,40]
		actual = sum.get_average(number)
		expected = 25
		self.assertEqual(actual,expected)

	def test_that_reversed_return_correct_result(self):
		actual = sum.get_reversed("hello")
		expected = "olleh"
		self.assertEqual(actual,expected)

	def test_that_capitalized_return_correct_result(self):
		list = ["apple","banana","cherry"]
		actual = sum.get_capitalized(list)
		expected = ["Apple","Banana","Cherry"]
		self.assertEqual(actual,expected)
	
	
	def test_that_duplicate_return_correct_result(self):
		number = [1,2,3,4,5,2]
		actual = sum.get_duplicate(number)
		expected = True
		self.assertEqual(actual,expected)

	def test_that_remove_spaces_return_correct_result(self):
		actual = sum.remove_spaces("hello world")
		expected = "helloworld"
		self.assertEqual(actual,expected)

	def test_that_sum_product_return_correct_result(self):
		number = [1,2,3,4]
		actual = sum.get_product_sum(number)
		expected = 30
		self.assertEqual(actual,expected)

	def test_that_sum_magic_number_return_correct_result(self):
		number = [1,2,3,4,5,6,7,8,9,10]
		actual = sum.magic_number(number)
		expected = 495
		self.assertEqual(actual,expected)

	def test_that_merge_return_correct_result(self):
		array_one = [3,4,9,10,90]
		array_two = [1,5,7,8,-7]
		actual = sum.merge_list(array_one,array_two)
		expected = [-7,1,3,4,5,7,8,9,10,90]
		self.assertEqual(actual,expected)
	
	def test_that_common_elements_return_correct_result(self):
		array_one = [1,2,3,4]
		array_two = [3,4,5,2,4]
		actual = sum.get_common_elements(array_one,array_two)
		expected = [2,3,4]
		self.assertEqual(actual,expected)

	def test_that_sorted_list_return_correct_result(self):
		list = ["apple","cashews","cherry"]
		actual = sum.get_sorted_list(list)
		expected = ["apple","cherry","cashews"]
		self.assertEqual(actual,expected)

	def test_that_factorial_return_correct_result(self):
		actual = sum.get_factorial(7)
		expected = 5040
		self.assertEqual(actual,expected)
	
	def test_that_digits_sum_return_correct_result(self):
		actual = sum.get_digits_sum(15324)
		expected = 15
		self.assertEqual(actual,expected)

	def test_that_interleave_lists_return_correct_result(self):
		list_one = [1,3,5]
		list_two = [2,4,6]
		actual = sum.interleave_lists(list_one,list_two)
		expected = [1,2,3,4,5,6]
		self.assertEqual(actual,expected)
	
	def test_that_acronym_return_correct_result(self):
		actual = sum.get_acronym("Portable Network Graphics")
		expected = "PNG"
		self.assertEqual(actual,expected)

	
	


	