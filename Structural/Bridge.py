from __future__ import annotations
from abc import ABC, abstractmethod

class RemoteControl(ABC):


    def __init__(self, device: Device):
        self._device = device
        
    def downVolume(self, amt: int = 1):
        self._device.setVolume(self._device.getVolume() - amt)
    def upVolume(self, amt: int = 1):
        self._device.setVolume(self._device.getVolume() + amt)
    def upChannel(self,amt: int = 1):
        self._device.setChannel(self._device.getChannel() + amt)
    
    def downChannel(self,amt: int = 1):
        self._device.setChannel(self._device.getChannel() - amt)
    

class AdvancedRemoteControl(RemoteControl):
    def select_channel(self, channel: int) -> None:
        self._device.setChannel(channel)
        
    def mute(self):
        self.downVolume(self._device.getVolume())
    


class Device(ABC):
    @abstractmethod
    def getVolume(self) -> int:
        pass
    @abstractmethod
    def setVolume(self, up: int) -> None:
        pass
    @abstractmethod
    def getChannel(self):
        pass
    @abstractmethod
    def setChannel(self, up: int) -> None:
        pass

class TV(Device):

    def __init__(self):
        self._volume = 4
        self._channel = 101
    def getVolume(self) -> int:
        return self._volume

    def setVolume(self, volume: int) -> None:
        self._volume = volume

    def getChannel(self):
        return self._channel

    def setChannel(self, channel: int) -> None:
        self._channel = channel

    def showStats(self):
        print(f'Volume is {self._volume} and Channel is {self._channel}')


if __name__ == '__main__':

    tv = TV()
    tv_adv = TV()
    tvRemote = RemoteControl(tv)
    tvRemoteAdvanced = AdvancedRemoteControl(tv_adv)
    tv.showStats()
    tv_adv.showStats()

    tvRemote.upVolume()
    tvRemote.downChannel()
    tvRemoteAdvanced.mute()

    tv.showStats()
    tv_adv.showStats()
