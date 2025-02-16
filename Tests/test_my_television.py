import unittest
from classWork.television.mytelevision import MyTelevision


class TestTelevision(unittest.TestCase):
    def test_that_my_television_default_is_off(self):
        television = MyTelevision()
        self.assertFalse(television.status())

    def test_that_my_television_can_be_turned_on(self):
        television = MyTelevision()
        self.assertFalse(television.status())
        television.turn_on()
        self.assertTrue(television.status())

    def test_that_my_television_can_be_turned_off(self):
        television = MyTelevision()
        self.assertFalse(television.status())
        television.turn_on()
        self.assertTrue(television.status())
        television.turn_off()
        self.assertFalse(television.status())

    def test_that_you_can_increase_volume(self):
        television = MyTelevision()
        television.turn_on()
        initial_volume = television.get_volume
        television.increase_volume()
        self.assertEqual(initial_volume + 1, television.get_volume)

    def test_that_you_can_decrease_volume(self):
        television = MyTelevision()
        television.turn_on()
        television.increase_volume()
        initial_volume = television.get_volume
        television.decrease_volume()
        self.assertEqual(initial_volume - 1, television.get_volume)

    def test_that_you_cant_increase_or_decrease_volume_when_tv_is_off(self):
        television = MyTelevision()
        self.assertEqual(0, television.get_volume)
        television.increase_volume()
        self.assertEqual(0, television.get_volume)
        television.turn_on()
        television.increase_volume()
        self.assertEqual(1, television.get_volume)
        television.turn_off()
        television.decrease_volume()
        self.assertEqual(1, television.get_volume)

    def test_that_you_can_raise_channel_number(self):
        television = MyTelevision()
        television.turn_on()
        initial_channel = television.channel
        television.raise_channel()
        self.assertEqual(initial_channel + 1, television.channel)

    def test_that_you_can_decrease_channel_number(self):
        television = MyTelevision()
        television.turn_on()
        initial_channel = television.channel
        television.reduce_channel()
        self.assertEqual(initial_channel - 1, television.channel)

    def test_that_you_cant_increase_or_decrease_channel_when_tv_is_off(self):
        television = MyTelevision()
        self.assertEqual(1, television.channel)
        television.raise_channel()
        self.assertEqual(1, television.channel)
        television.turn_on()
        television.raise_channel()
        self.assertEqual(2, television.channel)
        television.turn_off()
        television.reduce_channel()
        self.assertEqual(2, television.channel)

    def test_that_you_can_set_channel(self):
        television = MyTelevision()
        television.turn_on()
        television.channel = 45
        self.assertEqual(45, television.channel)



    def test_that_you_can_mute_volume(self):
        television = MyTelevision()
        television.turn_on()
        for index in range(10):
            television.increase_volume()
        self.assertEqual(10, television.get_volume)
        television.mute()
        self.assertEqual(0, television.get_volume)

    def test_that_you_can_Unmute_volume(self):
        television = MyTelevision()
        self.assertFalse(television.status())
        television.turn_on()
        for index in range(10):
            television.increase_volume()
        self.assertEqual(10, television.get_volume)
        television.mute()
        self.assertEqual(0, television.get_volume)
        television.un_mute()
        self.assertEqual(10, television.get_volume)



if __name__ == '__main__':
    unittest.main()
