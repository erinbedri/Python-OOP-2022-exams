#from abc import ABC, abstractmethod


class Hardware:
    _INSTALLATION_EXCEPTION_MESSAGE = "Software cannot be installed"

    #@abstractmethod
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        needed_capacity = software.capacity_consumption
        needed_memory = software.memory_consumption

        if needed_memory > self.memory or needed_capacity > self.capacity:
            raise Exception(self._INSTALLATION_EXCEPTION_MESSAGE)

        self.software_components.append(software)

    def uninstall(self, software):
        self.software_components.remove(software)

