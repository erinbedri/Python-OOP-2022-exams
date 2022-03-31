from math import floor

from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    _TYPE = "Heavy"
    _CAPACITY_FACTOR = 2
    _MEMORY_FACTOR = 0.75

    def __init__(self, name, capacity, memory):
        super().__init__(name,
                         self._TYPE,
                         (capacity * self._CAPACITY_FACTOR),
                         floor(memory * self._MEMORY_FACTOR))