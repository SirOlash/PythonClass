import unittest

from classWork.datastructures.set import Set


class TestMySet(unittest.TestCase):
    def setUp(self):
        self.my_set = Set()

    def test_that_set_is_empty(self):
        self.assertTrue(self.my_set.is_empty())

    def test_that_you_can_add_element(self):
        self.my_set.add("bruno")
        self.my_set.add("amad")
        self.assertEqual(self.my_set.size(), 2)

    def test_that_you_cant_add_similar_elements(self):
        self.my_set.add("bruno")
        self.my_set.add("amad")
        self.my_set.add("bruno")
        self.assertEqual(self.my_set.size(), 2)

    def test_that_you_can_remove_element(self):
        self.my_set.add("bruno")
        self.my_set.add("amad")
        self.my_set.add("casemiro")
        self.assertEqual(self.my_set.size(), 3)
        self.my_set.remove("bruno")
        self.assertEqual(self.my_set.size(), 2)
        self.assertEqual(self.my_set.get_element_by_index(0), "amad")

    def test_that_set_contains_a_particular_element(self):
        self.my_set.add("bruno")
        self.my_set.add("amad")
        self.assertTrue(self.my_set.contains("bruno"))

    def test_that_clear_function_works(self):
        self.my_set.add("bruno")
        self.my_set.add("amad")
        self.my_set.add("u")
        self.assertEqual(self.my_set.size(), 3)
        self.my_set.clear()
        self.assertEqual(self.my_set.size(), 0)
        self.my_set.add("w")
        self.assertEqual(self.my_set.size(), 1)

if __name__ == "__main__":
        unittest.main()

