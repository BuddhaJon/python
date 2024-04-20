class Television:
    """A simple model of a television, including power, volume, and channel controls."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializes the Television with all settings in the default state."""
        self.__status: bool = False  # True if the TV is on, False if off
        self.__muted: bool = False  # True if the TV is muted, False otherwise
        self.__volume: int = self.MIN_VOLUME  # Current volume level
        self.__channel: int = self.MIN_CHANNEL  # Current channel

    def power(self) -> None:
        """Toggles the power state of the TV."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggles the mute state. Muting also remembers the last volume before muting."""
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__previous_volume = self.__volume
                self.__volume = 0
            else:
                self.__volume = self.__previous_volume

    def channel_up(self) -> None:
        """Increases the channel number, wrapping around to MIN_CHANNEL after reaching MAX_CHANNEL."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decreases the channel number, wrapping around to MAX_CHANNEL if going below MIN_CHANNEL."""
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > self.MIN_CHANNEL else self.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increases the volume level by one step, not exceeding MAX_VOLUME. Automatically unmutes if muted."""
        if self.__status:
            if not self.__muted:
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1
            else:
                self.__muted = False  # Unmute the TV if it was muted
                self.__volume = min(self.__previous_volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decreases the volume level by one step, not falling below MIN_VOLUME. Automatically unmutes if muted."""
        if self.__status:
            if not self.__muted:
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1
            else:
                self.__muted = False  # Unmute the TV if it was muted
                if self.__previous_volume > self.MIN_VOLUME:
                    self.__volume = self.__previous_volume - 1
                else:
                    self.__volume = self.__previous_volume

    def __str__(self) -> str:
        """Returns a string representation of the current state of the TV. This includes the power, channel, and volume."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
