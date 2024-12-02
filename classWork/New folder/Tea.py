import unittest
 
import eventot
#import my_dict

class Tea(unittest.TestCase):
	"""def test_that_function_exists(self):
		number = [2,7,9,17,19,2,8,10]
		sum.is_even(number)

	def test_is_even_returns_correct_result(self):
		number = [2,7,9,17,19,2,8,10,10]
		actual = sum.is_even(number)
		expected = 32
		self.assertEqual(actual,expected)

	def test_is_prime_returns_correct_result(self):
		number = 20
		actual = sum.is_prime(number)
		expected = [2,3,5,7,11,13,17,19]
		self.assertEqual(actual,expected)"""

	def test_that_even_total_function_exists(self):
		number = [1,5,7,3,2,9,8,10]
		eventot.even_total(number)

	def test_even_total_returns_correct_result(self):
		number = [1,5,7,3,2,9,8,10]
		actual = eventot.even_total(number)
		expected = 3
		self.assertEqual(actual,expected)

	def test_that_even_odd_total_function_exists(self):
		number = [10,3,7,1,9,4,2,8,5,6]
		eventot.even_odd(number)

	def test_even_total_returns_correct_result(self):
		number = [10,3,7,1,9,4,2,8,5,6]
		actual = eventot.even_odd(number)
		expected = [True,False,False,False,False,True,True,True,False,True]
		self.assertEqual(actual,expected)

	def test_capitalized_returns_correct_result(self):
		words = ["red","orange","yellow"]
		actual = eventot.get_capitalized(words)
		expected = ["Red","Orange","Yellow"]
		self.assertEqual(actual,expected)
	
	def test_multiple_total_returns_correct_result(self):
		first = 3
		second = 31
		actual = eventot.three_multiple(first,second)
		expected = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
		self.assertEqual(actual,expected)

	"""def test_multiple_total_returns_correct_result(self):
		number = [10,3,7,1,9,4,2,8,5,6]
		actual = eventot.odd_square(list(filter(is_odd,numbers))
		expected = [9,49,1,81,25]
		self.assertEqual(actual,expected)"""

	def test_number_square_returns_correct_result(self):
		number = 4
		actual = eventot.numbers_square(number)
		expected = [1,4,9,16]
		self.assertEqual(actual,expected)

	def test_greater_ten_returns_correct_result(self):
		number = [1,5,12,15,8]
		actual = eventot.greater_ten(number)
		expected = [12,15]
		self.assertEqual(actual,expected)

	def test_palindrome_list_returns_correct_result(self):
		words= ['madam','apple','racecar']
		actual = eventot.palindrome_list(words)
		expected = [True,False,True]
		self.assertEqual(actual,expected)

	def test_string_int_returns_correct_result(self):
		sentence= 'abc123defef456'
		actual = eventot.string_int(sentence)
		expected = [1,2,3,4,5,6]
		self.assertEqual(actual,expected)

	def test_double_returns_correct_result(self):
		number= [1,2,3]
		actual = eventot.double(number)
		expected = [2,4,6]
		self.assertEqual(actual,expected)

	def test_longwords_correct_result(self):
		sentence= ["Apple","Fish","Orange","ice","Lime"]
		actual = eventot.longwords(sentence)
		expected = ["Apple","Orange"]
		self.assertEqual(actual,expected)

	def test_sum_numb_returns_correct_result(self):
		number= 192374
		actual = eventot.sum_numb(number)
		expected = 26
		self.assertEqual(actual,expected)
	
	"""def test_remove_vowel_correct_result(self):
		sentence= ["Orange","Apple","ice","Beans","Rice"]
		actual = eventot.remove_vowel(sentence)
		expected = ["rng","ppl"]
		self.assertEqual(actual,expected)"""

	def test_even_numb_returns_correct_result(self):
		number= 10
		actual = eventot.even_numb(number)
		expected = {2: 4, 4: 16, 6: 36, 8: 64}
		self.assertEqual(actual,expected)

	def test_zip_list_returns_correct_result(self):
		keys = ["name","age","city"]
		values = ["Alice",25,"New York"]
		actual = eventot.zip_list(keys,values)
		expected = {"name":"Alice","age":25,"city":"New York"}
		self.assertEqual(actual,expected)

	def test_return_value_returns_correct_result(self):
		number= {"name":"Alice","age":25,"city":"New York"}
		actual = eventot.return_value(number)
		expected = {2: 4, 4: 16, 6: 36, 8: 64}
		self.assertEqual(actual,expected)










