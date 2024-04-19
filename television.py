class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        self._status = not self._status

    def mute(self):
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._previous_volume = self._volume
                self._volume = 0
            else:
                self._volume = self._previous_volume

    def channel_up(self):
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        if self._status:
            self._channel = (self._channel - 1) if self._channel > self.MIN_CHANNEL else self.MAX_CHANNEL

    def volume_up(self):
        if self._status:
            if not self._muted:
                if self._volume < self.MAX_VOLUME:
                    self._volume += 1
            else:
                self._muted = False
                self._volume = min(self._previous_volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        if self._status:
            if not self._muted:
                if self._volume > self.MIN_VOLUME:
                    self._volume -= 1
            else:
                self._muted = False
                if self._previous_volume > self.MIN_VOLUME:
                    self._volume = self._previous_volume - 1
                else:
                    self._volume = self._previous_volume

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
