import unittest
from classWork import morningtask


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_character_count_function(self):
        actual = morningtask.character_count("semicolon.")
        expected = {'s':1,'e':1,'m':1,'i':1,'c':1,'o':2,'l':1,'n':1,'.':1}
        self.assertEqual(actual, expected)

    def test_that_you_can_swap_character(self):
        actual = morningtask.swap_character("abc","xyz")
        expected = "abc xyz"
        self.assertEqual(actual, expected)

    def test_that_you_can_add(self):
        actual = morningtask.divide_word("hell")
        expected = "hecell"
        self.assertEqual(actual, expected)

    def test_that_upper_first_works(self):
        actual = morningtask.upper_first("sEmIColOn")
        expected = "EICOsmoln"
        self.assertEqual(actual, expected)

    def test_that_character_occurence_function_works(self):
        actual = morningtask.character_occurrences("semicolon","o")
        expected = ('o',2)
        self.assertEqual(actual, expected)

    def test_that_remove_special_character_function_works(self):
        actual = morningtask.remove_special_character("he,ll.o")
        expected = "hello"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
