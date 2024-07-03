from abc import ABC, abstractmethod

class Device:
    @abstractmethod
    def size(self):
        pass

class Laptop(Device):
    def size(self):
        return f'A size of ~14"'

class Phone(Device):
    def size(self):
        return f'A size of ~6.5"'
		
my_devices = [Laptop(), Phone()]
for device in my_devices:
	print(device.size())