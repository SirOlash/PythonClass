import unittest
from classWork.datastructures.array import Array


class TestArrayMethods(unittest.TestCase):
    def setUp(self):
        self.my_array = Array()

    def test_that_list_is_empty(self):
        self.assertTrue(Array().is_empty())
        #self.assertEqual(True, False)

    def test_that_add_function_works(self):
        self.my_array.add("Hello")
        self.assertFalse(self.my_array.is_empty())

    def test_that_size_function_works(self):
        self.my_array.add("Hello")
        self.my_array.add("World")
        actual = self.my_array.size()
        expected = 2
        self.assertEqual(actual, expected)

    def test_that_remove_function_works(self):
        self.my_array.add("Hello")
        self.my_array.add("World")
        self.my_array.add("Python")
        self.my_array.remove("World")
        self.assertEqual(self.my_array.size(), 2)

    def test_that_contain_function_works(self):
        self.my_array.add("Hello")
        self.my_array.add("World")
        self.my_array.add("Python")
        self.assertTrue(self.my_array.contains("World"))


if __name__ == '__main__':
    unittest.main()
