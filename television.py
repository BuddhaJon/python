class Television:
    """A simple model of a television, including power, volume, and channel controls."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializes the Television with all settings in the default state."""
        self._status: bool = False  # True if the TV is on, False if off
        self._muted: bool = False  # True if the TV is muted, False otherwise
        self._volume: int = self.MIN_VOLUME  # Current volume level
        self._channel: int = self.MIN_CHANNEL  # Current channel

    def power(self) -> None:
        """Toggles the power state of the TV."""
        self._status = not self._status

    def mute(self) -> None:
        """Toggles the mute state. Muting also remembers the last volume before muting."""
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._previous_volume = self._volume
                self._volume = 0
            else:
                self._volume = self._previous_volume

    def channel_up(self) -> None:
        """Increases the channel number, wrapping around to MIN_CHANNEL after reaching MAX_CHANNEL."""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decreases the channel number, wrapping around to MAX_CHANNEL if going below MIN_CHANNEL."""
        if self._status:
            self._channel = (self._channel - 1) if self._channel > self.MIN_CHANNEL else self.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increases the volume level by one step, not exceeding MAX_VOLUME. Automatically unmutes if muted."""
        if self._status:
            if not self._muted:
                if self._volume < self.MAX_VOLUME:
                    self._volume += 1
            else:
                self._muted = False  # Unmute the TV if it was muted
                self._volume = min(self._previous_volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decreases the volume level by one step, not falling below MIN_VOLUME. Automatically unmutes if muted."""
        if self._status:
            if not self._muted:
                if self._volume > self.MIN_VOLUME:
                    self._volume -= 1
            else:
                self._muted = False  # Unmute the TV if it was muted
                if self._previous_volume > self.MIN_VOLUME:
                    self._volume = self._previous_volume - 1
                else:
                    self._volume = self._previous_volume

    def __str__(self) -> str:
        """Returns a string representation of the current state of the TV."""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
