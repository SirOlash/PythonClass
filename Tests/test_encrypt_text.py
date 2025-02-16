import unittest
from classWork import encrypttext, encrypt_try


class TestEncrypt(unittest.TestCase):
    def test_that_function_exists(self):
        encrypt_text.encrypt("HelloWorld")

    def test_that_encrypt_function_returns_correct_result(self):
        actual = encrypt_text.encrypt("Hello, World!")
        expected = "Uryyb, Jbeyq!"
        self.assertEqual(actual, expected)

    def test_that_encrypt_function_returns_a_number_in_its_actual_position(self):
        actual = encrypt_text.encrypt("1Hello, 1World!")
        expected = "1Uryyb, 1Jbeyq!"
        self.assertEqual(actual, expected)

    def test_that_encrpt_function_is_case_insensitive(self):
        actual = encrypt_text.encrypt("HELLO, WORLD!")
        expected = "URYYB, JBEYQ!"
        self.assertEqual(actual, expected)

    def test_that_encrypt_function_returns_correct_resu(self):
        actual = encrypt_text.encrypt("aaa")
        expected = "nnn"
        self.assertEqual(actual, expected)

   # def test_that_encrypt_second_function_returns_correct_result(self):
    #    actual = encrypt_try.encrypt("Hello, World!")
     #   expected = "Uryyb, Jbeyq!"
      #  self.assertEqual(actual,expected)

