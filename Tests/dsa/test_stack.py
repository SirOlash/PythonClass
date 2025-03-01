import unittest

from classWork.datastructures.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.myStack = Stack()

    def test_that_stack_is_empty(self):
        self.assertTrue(self.myStack.is_empty())

    def test_that_push_method_works(self):
        self.myStack.push("bruno")
        self.assertFalse(self.myStack.is_empty())

    def test_that_peek_method_works(self):
        self.myStack.push("bruno")
        self.assertTrue(self.myStack.peek() == "bruno")

    def test_that_push_method_adds_element_to_the_top_of_stack(self):
        self.myStack.push("onana")
        self.myStack.push("martinez")
        self.myStack.push("amad")
        self.myStack.push("bruno")
        self.assertEqual(4, self.myStack.size())
        self.assertEqual("bruno", self.myStack.peek())

    def test_that_pop_method_works(self):
        self.myStack.push("bruno")
        self.myStack.push("martinez")
        self.myStack.push("amad")
        self.myStack.pop()
        self.assertEqual("martinez", self.myStack.peek())

    def test_that_search_method_works(self):
        self.myStack.push("bruno")
        self.myStack.push("martinez")
        self.myStack.push("amad")
        self.assertEqual(2, self.myStack.search("martinez"))

if __name__ == '__main__':
    unittest.main()
