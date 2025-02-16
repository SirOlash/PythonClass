class MyTelevision:
    def __init__(self):
        self._volume_level = 0
        self._channel_number = 1
        self.is_on = False
        self.temp_volume = 0

    def status(self):
        return self.is_on

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    @property
    def get_volume(self):
        return self._volume_level

    def increase_volume(self):
        if self.is_on and self._volume_level < 100:
            self._volume_level += 1

    def decrease_volume(self):
        if self.is_on and self._volume_level > 0:
            self._volume_level -= 1

    @property
    def channel(self):
        return self._channel_number

    def raise_channel(self):
        if self.is_on and self._channel_number < 100:
            self._channel_number += 1

    def reduce_channel(self):
        if self.is_on and self._channel_number > 0:
            self._channel_number -= 1

    @channel.setter
    def channel(self, number):
        if self.is_on and 100 > number > 0:
            self._channel_number = number

    def mute(self):
        if self.is_on:
            self.temp_volume = self._volume_level
            self._volume_level = 0

    def un_mute(self):
        if self.is_on:
            self._volume_level = self.temp_volume






