import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0", "Incorrect initial state"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0", "Power on state incorrect"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0", "Power off state incorrect"

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0", "Mute on incorrect"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1", "Mute off incorrect"
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1", "Mute while off incorrect"

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0", "Channel up incorrect"
    for _ in range(3):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0", "Channel wrap around incorrect"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0", "Channel down wrap around incorrect"
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0", "Channel down incorrect"

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1", "Volume up incorrect"
    for _ in range(2):
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2", "Max volume incorrect"

def test_volume_down():
    tv = Television()
    tv.power()
    for _ in range(3):
        tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1", "Volume down incorrect"
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0", "Volume down while muted incorrect"
