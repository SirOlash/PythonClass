import unittest

from classWork.datastructures.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.myQueue = Queue()

    def test_that_queue_is_empty(self):
        self.assertTrue(self.myQueue.is_empty())

    def test_that_you_can_add_item_to_the_queue(self):
        self.myQueue.add("bruno")
        self.assertFalse(self.myQueue.is_empty())

    def test_that_you_can_add_more_items_to_the_queue(self):
        self.myQueue.add("bruno")
        self.myQueue.add("amad")
        self.myQueue.add("martinez")
        self.myQueue.offer("fty")
        self.assertEqual(3, self.myQueue.size())

    def test_that_offer_function_works(self):
        self.myQueue.offer("bruno")
        self.myQueue.offer("amad")
        self.myQueue.offer("martinez")
        self.assertEqual(3, self.myQueue.size())
        self.assertFalse(self.myQueue.offer("ugarte"))

    def test_that_poll_function_works(self):
        self.myQueue.offer("bruno")
        self.myQueue.offer("amad")
        self.myQueue.offer("martinez")
        self.assertEqual(3, self.myQueue.size())
        self.myQueue.poll()
        self.assertEqual(2, self.myQueue.size())

    def test_that_poll_function_returns_null(self):
        self.assertIsNone(self.myQueue.poll())

    def test_that_peek_function_works(self):
        self.myQueue.offer("bruno")
        self.myQueue.offer("amad")
        self.myQueue.offer("martinez")
        self.myQueue.poll()
        self.myQueue.peek()
        self.assertEqual("amad", self.myQueue.peek())

if __name__ == '__main__':
    unittest.main()
