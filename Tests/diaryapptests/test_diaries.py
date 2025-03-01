import unittest

from diaryapp.src.diaries import Diaries


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diaries = Diaries()


    def test_that_you_can_create_diary(self):
        self.diaries.create_diary("UserName","Password")
        self.diaries.create_diary("UserName2","Password")
        self.assertEqual(2,self.diaries._size())

    def test_that_you_can_find_diary_by_user_name(self):
        self.diaries.create_diary("UserName1","Password")
        self.assertIsNotNone(self.diaries.find_diary_by("UserName1"))

    def test_that_you_can_delete_diary_by_user_name(self):
        self.diaries.create_diary("UserName1","Password")
        self.diaries.create_diary("UserName3","Password")
        self.diaries.delete_diary("UserName3","Password")
        self.assertEqual(1,self.diaries._size())

if __name__ == '__main__':
    unittest.main()
