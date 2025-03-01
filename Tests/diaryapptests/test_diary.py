import unittest

from diaryapp.src.diary import Diary

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("olash","correctpin")

    def test_that_diary_is_unlocked_by_default(self):
        self.assertFalse(self.diary.is_locked())

    def test_that_you_can_lock_diary(self):
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_you_can_unlock_diary(self):
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary()
        self.assertFalse(self.diary.is_locked())

    def test_that_you_can_create_entry(self):
        self.diary.create_entry("title","content")
        self.assertEqual(1, self.diary._size)

    def test_you_can_find_entry_by_id(self):
        self.diary.create_entry("title1","content1")
        self.diary.create_entry("title2","content2")
        entry = self.diary.find_entry_by(1)
        self.assertEqual("title1", entry.title)

    def test_that_you_can_delete_entry(self):
        self.diary.create_entry("title","content")
        self.diary.create_entry("title","content")
        self.assertEqual(2, self.diary._size)
        self.diary.delete_entry(1)
        self.assertEqual(1, self.diary._size)

    def test_that_you_can_update_title(self):
        self.diary.create_entry("title1","content1")
        self.assertEqual("title1",self.diary.find_entry_by(1).title)
        self.diary.update_title(1,"newtitle")
        self.assertEqual("newtitle",self.diary.find_entry_by(1).title)


if __name__ == '__main__':
    unittest.main()
